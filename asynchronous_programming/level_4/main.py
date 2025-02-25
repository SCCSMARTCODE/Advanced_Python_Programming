import asyncio
import random
from time import perf_counter

NUM_WORKERS = 5
QUEUE_SIZE = 10

order_queue = asyncio.Queue(maxsize=QUEUE_SIZE)

async def producer(order_id):
    """Simulate producing orders."""
    await asyncio.sleep(random.uniform(0.1, 0.5))
    await order_queue.put(order_id)
    print(f"Produced order: {order_id}")

async def worker(worker_id):
    """Process orders from the queue."""
    while True:
        order_id = await order_queue.get()
        try:
            print(f"Worker {worker_id} processing order: {order_id}")
            await asyncio.sleep(random.uniform(0.5, 1.5))
        finally:
            order_queue.task_done()
            print(f"Worker {worker_id} finished order: {order_id}")

async def main():
    workers = [asyncio.create_task(worker(i)) for i in range(NUM_WORKERS)]

    for order_id in range(1, 21):  # Produce 20 orders
        await producer(order_id)

    await order_queue.join()
    for w in workers:
        w.cancel()

    await asyncio.gather(*workers, return_exceptions=True)

if __name__ == "__main__":
    begin_time = perf_counter()
    asyncio.run(main())
    print(f"Execution time is === [{perf_counter() - begin_time}] ===..")