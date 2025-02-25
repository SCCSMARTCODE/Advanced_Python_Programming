import random

google_images_url = "https://www.google.com/search?q={}&sca_esv=5d5dc4b0a4716fb1&sxsrf=AHTn8zobu26SgCIuqGRuqQlHEPm9JJrJjQ:1740439761263&source=hp&biw=1286&bih=825&ei=0QC9Z9yCDo2akdUPiNa8iAY&iflsig=ACkRmUkAAAAAZ70O4S12XuIJuRgew2pehxvOLqBiFnep&ved=0ahUKEwicr-Ktu92LAxUNTaQEHQgrD2EQ4dUDCBc&uact=5&oq=dog&gs_lp=EgNpbWciA2RvZzILEAAYgAQYsQMYgwEyBRAAGIAEMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMg4QABiABBixAxiDARiKBTILEAAYgAQYsQMYgwFIxxJQuwxYvg9wAXgAkAEAmAHtA6AB8gWqAQcyLTEuMC4xuAEDyAEA-AEBigILZ3dzLXdpei1pbWeYAgOgApoGqAIKwgIKECMYJxjJAhjqAsICCxAAGIAEGLEDGIoFmAMTkgcJMS4wLjEuMC4xoAecCg&sclient=img&udm=2"


import aiohttp
import asyncio
from time import perf_counter

SEM_LIMIT = 10
semaphore = asyncio.Semaphore(SEM_LIMIT)

animals = [
    "dog", "cat", "goat", "sheep", "bird", "car",
    "lion", "tiger", "elephant", "giraffe", "zebra",
    "kangaroo", "panda", "koala", "rabbit", "hamster",
    "chicken", "duck", "penguin", "eagle", "sparrow",
    "whale", "dolphin", "shark", "octopus", "seal",
    "snake", "lizard", "frog", "tortoise", "goldfish",
    "mouse", "rat", "ferret", "squirrel", "raccoon",
    "bat", "moose", "antelope", "lynx", "bison",
    "peacock", "flamingo", "hawk", "owl", "rooster",
    "donkey", "alpaca", "llama", "badger", "otter"
]

async def fetch_page(session, animal):
    async with semaphore:
        try:
            await asyncio.sleep(random.choice([0, 1]))
            url = google_images_url.format(animal)
            async with session.get(url) as response:
                print(f"Fetched {animal}: Status {response.status}")
                return animal, response.status
        except aiohttp.ClientError as e:
            print(f"Request failed for {animal}: {e}")
            return animal, None

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.wait_for(fetch_page(session, animal), 1) for animal in animals]
        try:
            result = await asyncio.gather(*tasks)
            print(result)
        except TimeoutError:
            print("Request timed out")

if __name__ == "__main__":
    begin_time = perf_counter()
    asyncio.run(main())
    print(f"Execution time is === [{perf_counter() - begin_time}] ===..")