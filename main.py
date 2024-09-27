import asyncio
import time
from data_fetcher import DataFetcher
from scraper import Scraper
from database.list_to_json import recipes_to_json
from database.mongo_queries import RecipeQueries


url = """https://kulinaria.ge/receptebi/cat/karTuli-samzareulo/"""
start = time.perf_counter()


async def main():
    fetcher = DataFetcher()

    # inicialize database
    my_db = RecipeQueries()

    html = fetcher.fetch_data(url)
    scraper = Scraper(html, fetcher)
    await scraper.get_recipe_info()

    # insert data in database
    my_db.insert_many("recipies", scraper.get_recipes())

    # average ingredients for all recipies
    print(f"\n Average ingredients for recipes - {my_db.avg_ingredients()} \n ")
    print(
        "######################################################################################################"
    )
    # Average stages of cooking
    print(f"\n Average stages of cooking - {my_db.avg_stages()} \n ")
    print(
        "######################################################################################################"
    )
    # most beneficial recipe
    print(f" \n recipe with most portions - {my_db.most_beneficial_recipe()} \n ")
    print(
        "######################################################################################################"
    )
    # author who have most recipies
    print(f" \n Author with most recipies - {my_db.top_author()} \n ")
    print(
        "######################################################################################################"
    )


if __name__ == "__main__":
    asyncio.run(main())
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
