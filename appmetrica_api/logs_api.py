import time
import random
import datetime as dt
from typing import List, Dict, Union

from requests import Response

from appmetrica_api.utils import get_min_dt, get_max_dt
from appmetrica_api.http_utils import make_request


class AppMetricaLogs:
    def __init__(self, token: str):
        self._token = token
        self._base_url = 'https://api.appmetrica.yandex.ru/logs/v1/export/'

    @property
    def headers(self):
        return {'Authorization': f'OAuth {self._token}', 'Accept-Encoding': 'gzip'}

    def _load(self, url: str, params: dict) -> Response:
        status_code = None
        while status_code != 200:
            response = make_request(url, self.headers, params)
            status_code = response.status_code
            time.sleep(random.randint(5, 10))
        return response

    def _prepare_params(
        self,
        date_since: Union[str, dt.date],
        date_until: Union[str, dt.date],
        fields: List[str],
        filters: Dict[str, str],
    ):
        if isinstance(date_since, dt.date):
            date_since = get_min_dt(date_since)
        if isinstance(date_until, dt.date):
            date_until = get_max_dt(date_until)
        params = {
            'date_since': date_since,
            'date_until': date_until,
            'fields': ','.join(fields),
        }
        params.update(**filters)
        return params

    def export(
        self,
        entity: str,
        date_since: Union[str, dt.date],
        date_until: Union[str, dt.date],
        fields: List[str],
        filters: Dict[str, str],
        output_format: str = 'csv',
    ):
        entities = {
            'clicks': 'clicks',
            'installs': 'installations',
            'events': 'events',
            'sessions': 'sessions_starts',
        }

        if entity not in entities:
            raise KeyError(f'Unknown entity {entity}')

        url = f'{self._base_url}{entities[entity]}.{output_format}'
        params = self._prepare_params(date_since, date_until, fields, filters)
        response = self._load(url, params)
        return response.content
