import re


class PhoneNumber:
    def __init__(self, phone_number: str):
        if not re.match(r'\d{11}', phone_number):
            raise ValueError(phone_number)
        self.value = phone_number

    def __str__(self) -> str:
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
