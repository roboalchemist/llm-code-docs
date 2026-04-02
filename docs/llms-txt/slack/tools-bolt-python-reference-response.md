Source: https://docs.slack.dev/tools/bolt-python/reference/response

# Module slack_bolt.response

This interface represents Bolt's synchronous response to Slack.

In Socket Mode, the response data can be transformed to a WebSocket message. In the HTTP endpoint mode, the response data becomes an HTTP response data.

Refer to [https://docs.slack.dev/apis/events-api/](https://docs.slack.dev/apis/events-api/) for the two types of connections.

## Sub-modules

`[slack_bolt.response.response](response.html "slack_bolt.response.response")`

## Classes

`class BoltResponse (*,   status: int,   body: str | dict = '',   headers: Dict[str, str | Sequence[str]] | None = None)`

Expand source code

```python
class BoltResponse:
    status: int
    body: str
    headers: Dict[str, Sequence[str]]

    def __init__(
        self,
        *,
        status: int,
        body: Union[str, dict] = "",
        headers: Optional[Dict[str, Union[str, Sequence[str]]]] = None,
    ):
        """The response from a Bolt app.

        Args:
            status: HTTP status code
            body: The response body (dict and str are supported)
            headers: The response headers.
        """
        self.status: int = status
        self.body: str = json.dumps(body) if isinstance(body, dict) else body
        self.headers: Dict[str, Sequence[str]] = {}
        if headers is not None:
            for name, value in headers.items():
                if value is None:
                    continue
                if isinstance(value, list):
                    self.headers[name.lower()] = value
                elif isinstance(value, set):
                    self.headers[name.lower()] = list(value)
                else:
                    self.headers[name.lower()] = [str(value)]

        if "content-type" not in self.headers.keys():
            if self.body and self.body.startswith("{"):
                self.headers["content-type"] = ["application/json;charset=utf-8"]
            else:
                self.headers["content-type"] = ["text/plain;charset=utf-8"]

    def first_headers(self) -> Dict[str, str]:
        return {k: list(v)[0] for k, v in self.headers.items()}

    def first_headers_without_set_cookie(self) -> Dict[str, str]:
        return {k: list(v)[0] for k, v in self.headers.items() if k != "set-cookie"}

    def cookies(self) -> Sequence[SimpleCookie]:
        header_values = self.headers.get("set-cookie", [])
        return [self._to_simple_cookie(v) for v in header_values]

    @staticmethod
    def _to_simple_cookie(header_value: str) -> SimpleCookie:
        c = SimpleCookie()
        c.load(header_value)
        return c
```

The response from a Bolt app.

## Args

## `status`

HTTP status code

## `body`

The response body (dict and str are supported)

## `headers`

The response headers.

### Class variables

`var body : str`

The type of the None singleton.

`var headers : Dict[str, Sequence[str]]`

The type of the None singleton.

`var status : int`

The type of the None singleton.

### Methods

`def cookies(self) ‑> Sequence[http.cookies.SimpleCookie]`

Expand source code

```python
def cookies(self) -> Sequence[SimpleCookie]:
    header_values = self.headers.get("set-cookie", [])
    return [self._to_simple_cookie(v) for v in header_values]
```

`def first_headers(self) ‑> Dict[str, str]`

Expand source code

```python
def first_headers(self) -> Dict[str, str]:
    return {k: list(v)[0] for k, v in self.headers.items()}
```

`def first_headers_without_set_cookie(self) ‑> Dict[str, str]`

Expand source code

```python
def first_headers_without_set_cookie(self) -> Dict[str, str]:
    return {k: list(v)[0] for k, v in self.headers.items() if k != "set-cookie"}
```
