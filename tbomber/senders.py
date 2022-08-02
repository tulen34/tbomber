import sys
from collections import namedtuple
from inspect import getmembers
from typing import Optional, Callable, Awaitable, Set

from httpx import AsyncClient, Response

from .utils import PhoneNumber
from .utils.predicates import PredicateType, status_code_is_ok

__all__ = ['SenderFuncType', 'Sender', 'gather', 'sender']

SenderFuncType = Callable[[AsyncClient, PhoneNumber], Awaitable[Response]]
Sender = namedtuple("Sender", ["func", "timeout", "predicate"])


def gather() -> Set[Sender]:
    return {
        m[1] for m in getmembers(sys.modules[__name__], lambda m: isinstance(m, Sender))
    }


def sender(
    timeout: Optional[int] = None,
    predicate: Optional[PredicateType] = status_code_is_ok,
):
    def wrapper(func: SenderFuncType):
        return Sender(func, timeout, predicate)

    return wrapper


@sender()
async def ok_ru(client, phone_number):
    return await client.post(
        "https://ok.ru/dk",
        params={
            "cmd": "AnonymRegistrationEnterPhone",
            "st.cmd": "anonymRegistrationEnterPhone",
        },
        data={"st.r.phone": phone_number.with_plus()},
    )


@sender()
async def youla_ru(client, phone_number):
    return await client.post(
        "https://youla.ru/web-api/auth/request_code", data={"phone": phone_number}
    )
