#!/usr/bin/env python3
"""complex multiply"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    def pow(value: float):
        """return fuction"""
        return multiplier * value
    return pow
