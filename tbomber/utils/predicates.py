from httpx import Response, codes
from typing import Callable

__all__ = ['PredicateType', 'status_code_is_ok']

PredicateType = Callable[[Response], bool]


def status_code_is_ok(resp: Response) -> bool:
    return resp.status_code == codes.OK
