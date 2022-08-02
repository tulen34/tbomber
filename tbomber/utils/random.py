import random

__all__ = ['russian_word', 'english_word', 'email']


def __unicode_range(a, b):
    return [chr(i) for i in range(ord(a), ord(b) + 1)]


def __random_str(sources):
    length = random.randint(7, 12)
    return ''.join(random.choices(sources, k=length))


def russian_word() -> str:
    return __random_str(__unicode_range('А', 'я'))


def english_word() -> str:
    return __random_str([*__unicode_range('a', 'z'),
                         *__unicode_range('A', 'Z')])


def email() -> str:
    random_domain = random.choice(['gmail.com', 'mail.ru', 'yandex.ru'])
    return '{}@{}'.format(english_word(), random_domain)
