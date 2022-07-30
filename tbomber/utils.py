from httpx import AsyncClient
import re
import random

client = AsyncClient()


class PhoneNumber:
    def __init__(self, phone_number: str):
        if not re.match(r'\d{11}', phone_number):
            raise ValueError(phone_number)
        self.value = phone_number

    def __repr__(self) -> str:
        return self.value

    def format(self, mask: str, mask_char='*') -> str:
        formatted = ''
        i = 0
        for c in mask:
            if c == mask_char:
                formatted += self.value[i]
                i += 1
            else:
                formatted += c
        return formatted


def __unicode_range(l, r):
    return [chr(i) for i in range(ord(l), ord(r) + 1)]


def __random_str(sources):
    length = random.randint(7, 12)
    return ''.join(random.choices(sources, k=length))


def random_russian_word() -> str:
    return __random_str(__unicode_range('А', 'я'))


def random_english_word() -> str:
    return __random_str([*__unicode_range('a', 'z'),
                         *__unicode_range('A', 'Z')])


def random_email() -> str:
    random_domain = random.choice(['gmail.com', 'mail.ru', 'yandex.ru'])
    return '{}@{}'.format(random_english_word(), random_domain)
