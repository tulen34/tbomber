from typing import Callable
from httpx import AsyncClient

client = AsyncClient()


def hook(cycles_amount: int):
    def decorator(func: Callable):
        ...
    return decorator
