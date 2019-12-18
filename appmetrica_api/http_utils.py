import logging

import requests


logger = logging.getLogger(__name__)


class APIError(Exception):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        self.request = kwargs.pop('request', None)


def make_request(
    url: str, headers: dict, params: dict, timeout: tuple = (15, 60)
) -> requests.Response:
    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        raise APIError(
            'Request exception occurred', response=e.response, requests=e.request
        ) from e
    else:
        return response
