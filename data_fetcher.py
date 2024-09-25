import aiohttp
import requests
import asyncio
from typing import List


class DataFetcher:
    """
    Handles fetching data from the website using requests and
    aiohttp. It uses a semaphore to limit the number of concurrent
    requests to the website.
    """
    def __init__(self) -> None:
        self.urls: List[str] = []
        self.semaphore: asyncio.Semaphore = asyncio.Semaphore(5)

    @staticmethod
    def fetch_data(url: str) -> str:
        """
        Fetches data from the website using requests.

        :param url: str: URL of the website to fetch data from
        :return: str: response from the website
        """
        response = requests.get(url).text
        return response

    @staticmethod
    async def fetch_async(session: aiohttp.ClientSession, url: str) -> str:
        """
        Fetches data from the website using aiohttp.

        :param session: aiohttp.ClientSession: aiohttp session object
        :param url: str: URL of the website to fetch data from
        :return: str: response from the website
        """
        async with session.get(url) as response:
            return await response.text()

    async def fetch_async_all(self, urls: List[str]) -> List[str]:
        """
        Fetches data from multiple websites concurrently using aiohttp.

        :param urls: List[str]: List of URLs of the websites to fetch data from
        :return: List[str]: List of responses from the websites
        """
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                tasks = [self.fetch_async(session, url) for url in urls]
                return await asyncio.gather(*tasks)
