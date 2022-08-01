import string
from typing import AnyStr

__all__ = ['PhoneNumber']

class PhoneNumber:
    def __init__(self, phone_number: AnyStr):
        self.__value = ''.join(c for c in phone_number if c in string.digits)
        if len(self.__value) != 11:
            raise ValueError(phone_number)

    def __str__(self) -> str:
        return self.__value

    def __mod__(self, mask: str) -> str:
        return self.format(mask)

    def format(self, mask: str, mask_char='*') -> str:
        formatted = ''
        i = 0
        for c in mask:
            if c == mask_char:
                formatted += self.__value[i]
                i += 1
            else:
                formatted += c
        return formatted

    def with_plus(self) -> str:
        return '+' + str(self)