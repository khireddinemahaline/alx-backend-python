#!/usr/bin/env python3
"""
meusure the run time / n
return total_time / n
"""

from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return time of excution / n"""
    start = time()
    asyncio.run(wait_n(n, max_delay))

    end = time()
    return (end - start) / n
