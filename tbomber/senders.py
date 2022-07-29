from httpx import Response
from typing import Optional, Callable


def sender(country_code: Optional[str] = None,
           success_resp: Optional[str] = None):
    def decorator(func: Callable[[PhoneNumber], Response]):
        ...
    return decorator
