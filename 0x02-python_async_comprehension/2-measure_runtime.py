#!/usr/bin/env python3
"""use gathe to run a coroutine multiple timr"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """calculate the run time"""
    start = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time()

    return end - start
