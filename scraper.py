from bs4 import BeautifulSoup
from typing import List, Optional
from data_fetcher import DataFetcher
from recipe import Recipe


class Scraper:
    """
    Scraper class is responsible for scraping the recipe links from
    the georgian cuisine category page and then scraping the information
    from each recipe link.
    """

    def __init__(self, html: str, fetcher: DataFetcher) -> None:
        """
        Initialize the Scraper class with the HTML content and
        a DataFetcher instance.

        :param html: str: html content of the page
        :param fetcher: DataFetcher: instance of a DataFetcher
        """
        self.html: str = html
        self.soup: BeautifulSoup = BeautifulSoup(self.html, 'html.parser')
        self.soup_recipe: Optional[BeautifulSoup] = None
        self._titles: List = []
        self.urls: List = []
        self.recipes: List = []
        self.fetcher: DataFetcher = fetcher
        self.get_recipe_links()

    @staticmethod
    def full_link_display(link: str) -> str:
        """
        Helper function to build the full URL by combining the
        base URL with the link part.

        :param link: str: link part
        :return: str: full link
        """
        return f'https://kulinaria.ge{link}'

    def get_recipe_links(self) -> None:
        """
        Scrapes the recipe links from the category page and stores
        them in the `self.urls` list.
        """
        self._titles = self.soup.find_all('a', {'class': 'box__title'})
        for title in self._titles:
            recipe_url_link = title.get('href')
            recipe_url = self.full_link_display(recipe_url_link)
            self.urls.append(recipe_url)

    @staticmethod
    def extract_text(element, default: str = '') -> str:
        """
        Extracts and strips the text content from an HTML element.
        If the element has no text, returns the default value.

        :param element: HTML element to extract text from
        :param default: str: Default text to return if the element has no text
        :return: str: Extracted and cleaned text
        """
        if len(element.text.strip()) != 0:
            return element.text.strip()
        else:
            return default

    def extract_category(self, element) -> dict:
        """
        Extracts the category title and URL from a category element.

        :param element: HTML element representing the category
        :return: dict: Dictionary containing the category title and URL
        """
        title = self.extract_text(element)
        link_part = element.get('href')
        link = self.full_link_display(link_part)
        return {title: link}

    def extract_image(self, soup) -> str:
        """
        Extracts the image URL from the recipe page.

        :param soup: Parsed HTML of the recipe page
        :return: str: Full URL of the recipe image
        """
        image = soup.find('div', {'class': 'post__img'})
        image_url_part = image.find('img').get('src')
        return self.full_link_display(image_url_part)

    def extract_description(self, soup) -> str:
        """
        Extracts the recipe description from the recipe page.
        Returns a default text if no description is available.

        :param soup: Parsed HTML of the recipe page
        :return: str: Description of the recipe
        """
        description = soup.find('div', {'class': 'post__description'})
        return self.extract_text(description, 'აღწერის გარეშე')

    def extract_author(self, soup) -> str:
        """
        Extracts the author of the recipe from the recipe page.

        :param soup: Parsed HTML of the recipe page
        :return: str: Author name (cleaned)
        """
        author = soup.find('div', {'class': 'post__author'})
        return self.extract_text(author).replace('ავტორი:  ', '')

    def extract_portion(self, soup) -> int:
        """
        Extracts the portion size from the recipe page
        and converts it to an integer.
        If the value cannot be converted to an integer, returns 1.

        :param soup: Parsed HTML of the recipe page
        :return: int: Number of portions (default is 1 if not available)
        """
        portion = self.extract_text(
            soup.find('div', {'class': 'lineDesc'})
            .findChild('div', {'class': 'lineDesc__item'})
            .find_next_sibling()
        )
        try:
            return int(portion.split()[0])
        except ValueError:
            return 1

    @staticmethod
    def extract_ingredients(soup) -> List:
        """
        Extracts the list of ingredients from the recipe page.

        :param soup: Parsed HTML of the recipe page
        :return: list: List of cleaned ingredient strings
        """
        ingredient_elements = soup.findAll('div', {'class': 'list__item'})
        ingredients = []

        for ingredient in ingredient_elements:
            text = (
                ingredient.text.replace('\xa0', '')
                .replace('\n', '').strip()
            )
            cleaned_text = ' '.join(text.split())
            ingredients.append(cleaned_text)

        return ingredients

    def extract_preparation(self, soup) -> dict:
        """
        Extracts the preparation steps from the recipe page.
        Each preparation step is stored with a step number.

        :param soup: Parsed HTML of the recipe page
        :return: dict: Dictionary where keys are step numbers
        and values are step descriptions
        """
        preparation_steps = {}
        preparation = soup.find('div', {'class': 'lineList'})
        preparation_elements = (
            preparation.findAll('div', {'class': 'lineList__item'})
        )

        for preparation_element in preparation_elements:
            preparation_step_count = self.extract_text(
                preparation_element.find('div', {'class': 'count'})
            )
            preparation_element_text = (
                self.extract_text(preparation_element.find("p"))
                .replace("\n", " ")
                .replace("\r", "")
            )
            preparation_steps[preparation_step_count] = (
                preparation_element_text
            )

        return preparation_steps

    async def get_recipe_info(self) -> None:
        """
        Asynchronously scrapes the recipe information from each recipe link.
        """
        responses = await self.fetcher.fetch_async_all(self.urls)
        for i, response in enumerate(responses):
            self.soup_recipe = BeautifulSoup(response, 'html.parser')

            title = self.extract_text(self.soup_recipe.find('h1'))
            recipe_url = self.urls[i]
            category = self.soup_recipe.select_one(
                "body > div.container > div.pagination > div > "
                "div > a:nth-child(3)"
            )
            category_dict = self.extract_category(category)
            sub_category = category.find_next_sibling() if category else None
            subcategory_dict = self.extract_category(sub_category)

            image_link = self.extract_image(self.soup_recipe)
            description_result = self.extract_description(self.soup_recipe)
            author_result = self.extract_author(self.soup_recipe)
            int_portion = self.extract_portion(self.soup_recipe)
            ingredients = self.extract_ingredients(self.soup_recipe)
            preparation_steps = self.extract_preparation(self.soup_recipe)

            recipe = Recipe(
                title,
                recipe_url,
                category_dict,
                subcategory_dict,
                image_link,
                description_result,
                author_result,
                int_portion,
                ingredients,
                preparation_steps
            )

            self.recipes.append(recipe.to_dict())
            print(recipe)

    def get_recipes(self) -> List:
        """
        This method is responsible for displaying the recipes
        """
        # for recipe in self.recipes:
        #     print(recipe)
        return self.recipes
