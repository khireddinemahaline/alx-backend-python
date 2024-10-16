#!/usr/bin/env python3
"""
async / await
- use asyncio library : could manage create tasks
"""

import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a List of float delat float values"""
    float_list = []
    for iter in range(n):
        iter = await asyncio.create_task(wait_random(max_delay))
        float_list.append(iter)
    return float_list
