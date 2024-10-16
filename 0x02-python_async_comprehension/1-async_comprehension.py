#!/usr/bin/env python3
"""run an async async_comprehension"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """use async in []"""
    result = [i async for i in async_generator()]
    return result
