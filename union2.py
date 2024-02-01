from typing import Union


def example1(value: Union[int, str]) -> None:
    print(value)


def example2(value: int | str) -> None:
    print(value)
    
example1("holaa")
example2("hallo")