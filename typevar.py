from typing import TypeVar

T = TypeVar('T')  

def halo(items: T) -> T:
    return items

def test2(items: list[T]) -> T:
    return items

result = halo(5)

print(result)  # Output: 1
# test = test2([2,4,6,7,8,98][int])
# print(test) # Output: