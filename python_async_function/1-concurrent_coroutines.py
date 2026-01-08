#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    
    # asyncio.as_completed yields tasks as they complete (ascending order of duration)
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
        
    return delays
