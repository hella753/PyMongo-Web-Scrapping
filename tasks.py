from bs4 import BeautifulSoup
from data_fetcher import DataFetcher
from recipe import Recipe
from typing import List

class Tasks:
    def __init__(self, html):
        self.soup_recipe = None
        self.html = html
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self._titles = None
        self.recipes = []
        self.urls = []
        self.get_recipe_links()

    @staticmethod
    def full_link_display(link):
        return f"https://kulinaria.ge{link}"

    def get_recipe_links(self) -> None:
        self._titles = self.soup.find_all('a', {'class': 'box__title'})
        for title in self._titles:
            recipe_url_link = title.get('href')
            recipe_url = self.full_link_display(recipe_url_link)
            self.urls.append(recipe_url)

    async def get_recipe_info(self) -> None:
        responses = await DataFetcher().fetch_all(self.urls)
        for i, response in enumerate(responses):
            self.soup_recipe = BeautifulSoup(response, 'html.parser')
            title = self.soup_recipe.find('h1').text.strip()
            recipe_url = self.urls[i]
            category = self.soup_recipe.select("body > div.container > div.pagination > div > div > a:nth-child(3)")[0]
            category_title = category.text.strip()
            category_link_part = category.get('href')
            category_link = self.full_link_display(category_link_part)
            category_dict = {category_title: category_link}

            sub_category = category.find_next_sibling()
            sub_category_title = sub_category.text.strip()
            sub_category_link_part = sub_category.get('href')
            sub_category_link = self.full_link_display(sub_category_link_part)
            subcategory_dict = {sub_category_title: sub_category_link}

            image = self.soup_recipe.find('div', {'class': 'post__img'})
            image_url_part = image.find('img').get('src')
            image_url = self.full_link_display(image_url_part)

            image_link = image_url
            recipe = Recipe(title, recipe_url, category_dict, subcategory_dict, image_link)
            self.recipes.append(recipe)


    def get_recipes(self) -> None:
        for recipe in self.recipes:
            print(recipe)





