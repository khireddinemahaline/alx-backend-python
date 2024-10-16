#!/usr/bin/env python3
"""
create a generateur async
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """10 ele after 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)

        yield random.uniform(0, 10)
