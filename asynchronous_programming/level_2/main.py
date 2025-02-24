import aiohttp
import asyncio
from time import perf_counter

async def get_session(session):
    try:
        async with session.get('http://python.org', timeout=5) as response:
            print("Status:", response.status)
            return response.status
    except aiohttp.ClientError as e:
        print(f"Request failed: {e}")
        return None

async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[get_session(session) for _ in range(100)])
        print(result)

if __name__ == "__main__":
    begin_time = perf_counter()
    asyncio.run(main())
    print(f"Execution time is === [{perf_counter() - begin_time}] ===..")