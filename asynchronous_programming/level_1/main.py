import asyncio


async def simulate_download(simulated_download_count: int, latency_duration: float) -> None:
    print(f"Download func {simulated_download_count} begins...")
    await asyncio.sleep(latency_duration)
    print(f"Download func {simulated_download_count} ends...")



async def main():
    await asyncio.gather(
        simulate_download(1, 2),
        simulate_download(2, 3),
        simulate_download(3, 4),
    )



if __name__ == "__main__":
    asyncio.run(main())