Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth/state_utils

# Module slack_sdk.oauth.state_utils

## Classes

`class OAuthStateUtils (*, cookie_name: str = 'slack-app-oauth-state', expiration_seconds: int = 600)`

Expand source code

```typescript
class OAuthStateUtils:
    cookie_name: str
    expiration_seconds: int

    default_cookie_name: str = "slack-app-oauth-state"
    default_expiration_seconds: int = 60 * 10  # 10 minutes

    def __init__(
        self,
        *,
        cookie_name: str = default_cookie_name,
        expiration_seconds: int = default_expiration_seconds,
    ):
        self.cookie_name = cookie_name
        self.expiration_seconds = expiration_seconds

    def build_set_cookie_for_new_state(self, state: str) -> str:
        return f"{self.cookie_name}={state}; " "Secure; " "HttpOnly; " "Path=/; " f"Max-Age={self.expiration_seconds}"

    def build_set_cookie_for_deletion(self) -> str:
        return f"{self.cookie_name}=deleted; " "Secure; " "HttpOnly; " "Path=/; " "Expires=Thu, 01 Jan 1970 00:00:00 GMT"

    def is_valid_browser(
        self,
        state: Optional[str],
        request_headers: Dict[str, Union[str, Sequence[str]]],
    ) -> bool:
        if state is None or request_headers is None or request_headers.get("cookie", None) is None:
            return False
        cookies = request_headers["cookie"]
        if isinstance(cookies, str):
            cookies = [cookies]
        for cookie in cookies:
            values = cookie.split(";")
            for value in values:
                # handle quoted cookie values (e.g. due to base64 encoding)
                if value.strip().replace('"', "").replace("'", "") == f"{self.cookie_name}={state}":
                    return True
        return False
```

### Class variables

`var cookie_name : str`

The type of the None singleton.

`var default_cookie_name : str`

The type of the None singleton.

`var default_expiration_seconds : int`

The type of the None singleton.

`var expiration_seconds : int`

The type of the None singleton.

### Methods

`def build_set_cookie_for_deletion(self) ‑> str`

Expand source code

```python
def build_set_cookie_for_deletion(self) -> str:
    return f"{self.cookie_name}=deleted; " "Secure; " "HttpOnly; " "Path=/; " "Expires=Thu, 01 Jan 1970 00:00:00 GMT"
```

`def build_set_cookie_for_new_state(self, state: str) ‑> str`

Expand source code

```python
def build_set_cookie_for_new_state(self, state: str) -> str:
    return f"{self.cookie_name}={state}; " "Secure; " "HttpOnly; " "Path=/; " f"Max-Age={self.expiration_seconds}"
```

`def is_valid_browser(self, state: str | None, request_headers: Dict[str, str | Sequence[str]]) ‑> bool`

Expand source code

```python
def is_valid_browser(
    self,
    state: Optional[str],
    request_headers: Dict[str, Union[str, Sequence[str]]],
) -> bool:
    if state is None or request_headers is None or request_headers.get("cookie", None) is None:
        return False
    cookies = request_headers["cookie"]
    if isinstance(cookies, str):
        cookies = [cookies]
    for cookie in cookies:
        values = cookie.split(";")
        for value in values:
            # handle quoted cookie values (e.g. due to base64 encoding)
            if value.strip().replace('"', "").replace("'", "") == f"{self.cookie_name}={state}":
                return True
    return False
```
