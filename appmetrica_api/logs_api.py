from typing import List

import requests

from appmetrica_api.constants import Installs, Events, Sessions, Clicks


class AppMetricaLogs:
    def __init__(self, token: str):
        self._token = token

    def get_installs(self, fields: List[Installs.Field]):
        pass

    def get_events(self, fields: List[Events.Field]):
        pass

    def get_sessions(self, fields: List[Sessions.Field]):
        pass

    def get_clicks(self, fields: List[Clicks.Field]):
        pass
