from typing import Optional, Callable, Awaitable, NamedTuple

from httpx import AsyncClient, Response

from .utils import PhoneNumber
from .utils.predicates import status_code_is_ok

__all__ = ['Sender']


class Sender(NamedTuple):
    func: Callable[[AsyncClient, PhoneNumber], Awaitable[Response]]
    predicate: Callable[[Response], bool]
    delay: Optional[float]


def sender(**kwargs):
    def wrapper(func):
        return Sender(
            func,
            kwargs.get('predicate', status_code_is_ok),
            kwargs.get('delay')
        )

    return wrapper


@sender()
async def ok_ru(client, phone_number):
    return await client.post(
        'https://ok.ru/dk',
        params={
            'cmd': 'AnonymRegistrationEnterPhone',
            'st.cmd': 'anonymRegistrationEnterPhone',
        },
        data={'st.r.phone': phone_number.with_plus()},
    )


@sender()
async def youla_ru(client, phone_number):
    return await client.post(
        'https://youla.ru/web-api/auth/request_code', data={'phone': phone_number}
    )
