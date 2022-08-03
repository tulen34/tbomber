from httpx import Response, codes

__all__ = ['status_code_is_ok']


def status_code_is_ok(resp: Response) -> bool:
    return resp.status_code == codes.OK
