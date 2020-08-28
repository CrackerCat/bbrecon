from typing import Any, Dict, Optional, Union, cast

import httpx

from ..client import Client
from ..errors import ApiResponseError
from ..models.alerts import Alerts
from ..models.alert import Alert


def get_alerts(*, client: Client, page: Optional[int] = None,) -> Union[Alerts]:
    url = "{}/v0b/alerts".format(client.base_url)

    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page

    response = httpx.get(url=url, headers=client.get_headers(), params=params)

    if response.status_code == 200:
        return Alerts.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())


def get_alert(*, client: Client, id: str) -> Union[Alert]:
    url = "{}/v0b/alerts/{id}".format(client.base_url, id=id)
    response = httpx.get(url=url, headers=client.get_headers())

    if response.status_code == 200:
        return Alert.from_dict(cast(Dict[str, Any], response.json()))
    raise ApiResponseError(code=response.status_code, detail=response.json())
