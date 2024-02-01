from typing import List, Tuple, Type

# Day la type alias
IntList = List[int]


def test(numbers: IntList) -> int:
    return sum(numbers)

