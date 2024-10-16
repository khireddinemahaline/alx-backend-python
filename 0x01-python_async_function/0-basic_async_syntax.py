#!/usr/bin/env python3
"""
a function that wait for a delay random to excute
return the dely random value between <max_delay, 0>
"""


import random
import asyncio


async def wait_random(max_delay: int =10) -> float:
    """
        return a delay float of a function to excute
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
