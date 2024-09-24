import asyncio
from data_fetcher import DataFetcher
from tasks import Tasks


url = """https://kulinaria.ge/receptebi/cat/karTuli-samzareulo/"""

def main():
    fetcher = DataFetcher()

    tasks = Tasks(fetcher.fetch_data(url))

    asyncio.run(tasks.get_recipe_info())

    tasks.get_recipes()


if __name__ == "__main__":
    main()






