from numpy import inf, nan
from typing import Union

NaN = nan
Infinity = inf
Numeric = Union[int, float]


class Nil:
    def __init__(self):
        pass
