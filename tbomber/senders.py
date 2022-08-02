from collections import namedtuple
from typing import Optional, Callable, Awaitable

from httpx import AsyncClient, Response

from .utils import PhoneNumber
from .utils.predicates import PredicateType, status_code_is_ok

SenderFuncType = Callable[[AsyncClient, PhoneNumber], Awaitable[Response]]

Sender = namedtuple('Sender', ['func', 'timeout', 'predicate'])


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
