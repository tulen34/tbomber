from typing import NamedTuple, Callable


def hook(cycles_amount: int):
    def decorator(func: Callable):
        ...
    return decorator
