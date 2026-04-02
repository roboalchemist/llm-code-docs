Source: https://docs.slack.dev/tools/bolt-python/reference/request

# Module slack_bolt.request

Incoming request from Slack through either HTTP request or Socket Mode connection.

Refer to [https://docs.slack.dev/apis/events-api/](https://docs.slack.dev/apis/events-api/) for the two types of connections. This interface encapsulates the difference between the two.

## Sub-modules

`[slack_bolt.request.async_internals](async_internals.html "slack_bolt.request.async_internals")`

`[slack_bolt.request.async_request](async_request.html "slack_bolt.request.async_request")`

`[slack_bolt.request.internals](internals.html "slack_bolt.request.internals")`

`[slack_bolt.request.payload_utils](payload_utils.html "slack_bolt.request.payload_utils")`

`[slack_bolt.request.request](request.html "slack_bolt.request.request")`

## Classes

`class BoltRequest (*,   body: str | dict,   query: str | Dict[str, str] | Dict[str, Sequence[str]] | None = None,   headers: Dict[str, str | Sequence[str]] | None = None,   context: Dict[str, Any] | None = None,   mode: str = 'http')`

Expand source code

```python
class BoltRequest:
    raw_body: str
    query: Dict[str, Sequence[str]]
    headers: Dict[str, Sequence[str]]
    content_type: Optional[str]
    body: Dict[str, Any]
    context: BoltContext
    lazy_only: bool
    lazy_function_name: Optional[str]
    mode: str  # either "http" or "socket_mode"

    def __init__(
        self,
        *,
        body: Union[str, dict],
        query: Optional[Union[str, Dict[str, str], Dict[str, Sequence[str]]]] = None,
        headers: Optional[Dict[str, Union[str, Sequence[str]]]] = None,
        context: Optional[Dict[str, Any]] = None,
        mode: str = "http",  # either "http" or "socket_mode"
    ):
        """Request to a Bolt app.

        Args:
            body: The raw request body (only plain text is supported for "http" mode)
            query: The query string data in any data format.
            headers: The request headers.
            context: The context in this request.
            mode: The mode used for this request. (either "http" or "socket_mode")
        """
        if mode == "http":
            # HTTP Mode
            if body is not None and not isinstance(body, str):
                raise BoltError(error_message_raw_body_required_in_http_mode())
            self.raw_body = body if body is not None else ""
        else:
            # Socket Mode
            if body is not None and isinstance(body, str):
                self.raw_body = body
            else:
                # We don't convert the dict value to str
                # as doing so does not guarantee to keep the original structure/format.
                self.raw_body = ""

        self.query = parse_query(query)
        self.headers = build_normalized_headers(headers)
        self.content_type = extract_content_type(self.headers)

        if isinstance(body, str):
            self.body = parse_body(self.raw_body, self.content_type)
        elif isinstance(body, dict):
            self.body = body
        else:
            self.body = {}

        self.context = build_context(BoltContext(context if context else {}), self.body)
        self.lazy_only = bool(self.headers.get("x-slack-bolt-lazy-only", [False])[0])
        self.lazy_function_name = self.headers.get("x-slack-bolt-lazy-function-name", [None])[0]
        self.mode = mode

    def to_copyable(self) -> "BoltRequest":
        body: Union[str, dict] = self.raw_body if self.mode == "http" else self.body
        return BoltRequest(
            body=body,
            query=self.query,
            headers=self.headers,
            context=self.context.to_copyable(),
            mode=self.mode,
        )
```

Request to a Bolt app.

## Args

## `body`

The raw request body (only plain text is supported for "http" mode)

## `query`

The query string data in any data format.

## `headers`

The request headers.

## `context`

The context in this request.

## `mode`

The mode used for this request. (either "http" or "socket\_mode")

### Class variables

`var body : Dict[str, Any]`

The type of the None singleton.

`var content_type : str | None`

The type of the None singleton.

`var context : [BoltContext](../context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext")`

The type of the None singleton.

`var headers : Dict[str, Sequence[str]]`

The type of the None singleton.

`var lazy_function_name : str | None`

The type of the None singleton.

`var lazy_only : bool`

The type of the None singleton.

`var mode : str`

The type of the None singleton.

`var query : Dict[str, Sequence[str]]`

The type of the None singleton.

`var raw_body : str`

The type of the None singleton.

### Methods

`def to_copyable(self) ‑> [BoltRequest](request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")`

Expand source code

```python
def to_copyable(self) -> "BoltRequest":
    body: Union[str, dict] = self.raw_body if self.mode == "http" else self.body
    return BoltRequest(
        body=body,
        query=self.query,
        headers=self.headers,
        context=self.context.to_copyable(),
        mode=self.mode,
    )
```
