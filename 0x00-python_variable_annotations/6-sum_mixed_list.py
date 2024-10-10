#!/usr/bin/env python3
"""sum_mixed_list"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """miced value in list"""
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum
