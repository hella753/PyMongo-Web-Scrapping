from bs4 import BeautifulSoup
from data_fetcher import DataFetcher
from recipe import Recipe
from typing import List


class Scraper:
    """
    Scraper class is responsible for scraping the recipe links from
    the georgian cuisine category page and then scraping the information
    from each recipe link.
    """
    def __init__(self, html: str, fetcher: DataFetcher):
        """
        :param html: str: html content of the page
        :param fetcher: DataFetcher: instance of a DataFetcher
        """
        self.html: str = html
        self.soup: BeautifulSoup = BeautifulSoup(self.html, 'html.parser')
        self.soup_recipe = None
        self._titles = None
        self.urls: List = []
        self.recipes: List = []
        self.fetcher: DataFetcher = fetcher
        self.get_recipe_links()

    @staticmethod
    def full_link_display(link):
        """
        Helper function to display the full link

        :param link: str: link second part
        :return: str: full link
        """
        return f"https://kulinaria.ge{link}"

    def get_recipe_links(self) -> None:
        """
        This method is responsible for scraping the recipe links.
        """
        self._titles = self.soup.find_all('a', {'class': 'box__title'})
        for title in self._titles:
            recipe_url_link = title.get('href')
            recipe_url = self.full_link_display(recipe_url_link)
            self.urls.append(recipe_url)

    async def get_recipe_info(self) -> None:
        """
        This method is responsible for scraping the recipe information
        from each recipe link.
        """
        responses = await self.fetcher.fetch_async_all(self.urls)
        for i, response in enumerate(responses):
            self.soup_recipe = BeautifulSoup(response, 'html.parser')

            title = self.soup_recipe.find('h1').string.strip()

            recipe_url = self.urls[i]

            category = self.soup_recipe.select_one(
                "body > div.container > div.pagination > div > "
                "div > a:nth-child(3)"
            )
            category_title = category.string.strip()
            category_link_part = category.get('href')
            category_link = self.full_link_display(category_link_part)
            category_dict = {category_title: category_link}

            sub_category = category.find_next_sibling()
            sub_category_title = sub_category.string.strip()
            sub_category_link_part = sub_category.get('href')
            sub_category_link = self.full_link_display(sub_category_link_part)
            subcategory_dict = {sub_category_title: sub_category_link}

            image = self.soup_recipe.find('div', {'class': 'post__img'})
            image_url_part = image.find('img').get('src')
            image_url = self.full_link_display(image_url_part)
            image_link = image_url

            description = (
                self.soup_recipe
                .find(
                    'div', {'class': 'post__description'}
                )
            )
            description_result = description.text.strip()
            if len(description_result) == 0:
                description_result = "აღწერის გარეშე"

            author = self.soup_recipe.find('div', {'class': 'post__author'})
            author_result = author.text.strip()

            portion = (
                self.soup_recipe
                .find('div', {'class': 'lineDesc'})
                .findChild('div', {'class': 'lineDesc__item'})
                .find_next_sibling()
                .text.strip()
            )
            try:
                int_portion = int(portion.split()[0])
            except ValueError:
                int_portion = 1

            ingredient_elements = self.soup_recipe.findAll(
                'div', {'class': 'list__item'}
            )
            ingredients = []
            for ingredient in ingredient_elements:
                text = (
                    ingredient.text
                    .replace('\xa0', '')
                    .replace('\n', '')
                    .strip()
                )
                cleaned_text = " ".join(text.split())
                ingredients.append(cleaned_text)

            preparation = self.soup_recipe.find('div', {'class': 'lineList'})
            preparation_elements = (
                preparation
                .findAll(
                    'div', {'class': 'lineList__item'}
                )
            )
            preparation_steps = []
            for preparation_element in preparation_elements:
                preparation_step_count = (
                    preparation_element
                    .find(
                        'div', {'class': 'count'}
                    )
                    .text.strip()
                )
                preparation_element_text = (
                    f'ნაბიჯი {preparation_step_count} - '
                    f'{preparation_element.find("p").text.strip()}')
                preparation_steps.append(preparation_element_text)

            recipe = Recipe(
                title,
                recipe_url,
                category_dict,
                subcategory_dict,
                image_link,
                description_result,
                author_result,
                ingredients,
                int_portion,
                preparation_steps
            )

            self.recipes.append(recipe.to_dict())

    def get_recipes(self) -> None:
        """
        This method is responsible for displaying the recipes
        """
        for recipe in self.recipes:
            print(recipe)
