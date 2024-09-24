import aiohttp
import requests
import asyncio
from typing import List

class DataFetcher:
    def __init__(self) -> None:
        self.urls: List[str] = []
        self.semaphore: asyncio.Semaphore = asyncio.Semaphore(5)

    @staticmethod
    def fetch_data(url: str) -> str:
        response = requests.get(url).text
        return response

    @staticmethod
    async def fetch(session, url: str):
        async with session.get(url) as response:
            return await response.text()

    async def fetch_all(self, urls: List[str]):
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                tasks = [self.fetch(session, url) for url in urls]
                return await asyncio.gather(*tasks)
