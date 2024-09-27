import asyncio
import time
from data_fetcher import DataFetcher
from scraper import Scraper
from database.list_to_json import recipes_to_json
from database.database_config import MongoDB
from database.list_to_json import recipes_to_json


url = """https://kulinaria.ge/receptebi/cat/karTuli-samzareulo/"""
start = time.perf_counter()


async def main():
    fetcher = DataFetcher()
    my_db = MongoDB()

    html = fetcher.fetch_data(url)
    scraper = Scraper(html, fetcher)
    await scraper.get_recipe_info()

    my_db.insert_many("recipies", scraper.get_recipes())


if __name__ == "__main__":
    asyncio.run(main())
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
