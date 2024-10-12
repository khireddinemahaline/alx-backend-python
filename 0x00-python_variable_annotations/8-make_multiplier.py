#!/usr/bin/env python3
"""complex multiply"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    def pow(multiplier):
        """return fuction"""
        return multiplier ** 2
    return pow
