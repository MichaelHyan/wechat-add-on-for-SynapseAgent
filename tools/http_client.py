import json
import requests
DEFAULT_URL = "http://127.0.0.1:56700/cnmd"

DEFAULT_HEADERS = {
    "Content-Type": "application/json; charset=utf-8",
}

DEFAULT_METHOD = "ask"
DEFAULT_TIMEOUT = 15

def post(
    url: str = DEFAULT_URL,
    timeout: int = DEFAULT_TIMEOUT,
    body = {}
):
    resp = requests.post(
        url,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers=DEFAULT_HEADERS,
        timeout=timeout,
    )
    resp.raise_for_status()

    try:
        return resp.json()
    except ValueError:
        return resp.text