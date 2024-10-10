#!/usr/bin/env python3
"""sum_mixed_list"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, Union[str, float]]:
    """"""
    return (k, float(v ** 2))
