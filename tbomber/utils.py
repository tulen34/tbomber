from httpx import AsyncClient
from typing import Literal

client = AsyncClient()


class PhoneNumber:
    def __init__(self, phone_number: str):
        ...

    def format(self, mask: str) -> str:
        ...

    @property
    def country_code(self):
        raise NotImplemented()

    def __repr__(self) -> str:
        ...


def generate_info(category: Literal['russian_word',
                                    'user_name',
                                    'email']) -> str:
    ...

