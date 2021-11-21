from functools import reduce
from typing import Union
from src.types import Vector


def mean(v: Vector) -> Union[float, int]:
    return sum(v) / len(v)
