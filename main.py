import asyncio
import time
from data_fetcher import DataFetcher
from scraper import Scraper

url = """https://kulinaria.ge/receptebi/cat/karTuli-samzareulo/"""
start = time.perf_counter()


async def main():
    fetcher = DataFetcher()
    html = fetcher.fetch_data(url)
    scraper = Scraper(html, fetcher)
    await scraper.get_recipe_info()
    scraper.get_recipes()


if __name__ == "__main__":
    asyncio.run(main())
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
