#!/usr/bin/env python3
"""
    create a task
"""

from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """create a new task with the func wait_random """
    task = create_task(wait_random(max_delay))
    return task
