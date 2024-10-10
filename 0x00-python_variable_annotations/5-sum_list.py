#!/usr/bin/env python3
"""sum of list as float"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """return float sum"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
