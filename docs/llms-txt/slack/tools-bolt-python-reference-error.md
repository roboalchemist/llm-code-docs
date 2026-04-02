Source: https://docs.slack.dev/tools/bolt-python/reference/error

# Module slack_bolt.error

Bolt specific error types.

## Classes

`class BoltError (*args, **kwargs)`

Expand source code

```python
class BoltError(Exception):
    """General class in a Bolt app"""
```

General class in a Bolt app

### Ancestors

* builtins.Exception
* builtins.BaseException

### Subclasses

* [BoltUnhandledRequestError](#slack_bolt.error.BoltUnhandledRequestError "slack_bolt.error.BoltUnhandledRequestError")

`class BoltUnhandledRequestError (*,   request: BoltRequest | AsyncBoltRequest,   current_response: BoltResponse | None,   last_global_middleware_name: str | None = None)`

Expand source code

```python
class BoltUnhandledRequestError(BoltError):
    request: "BoltRequest"  # type: ignore[name-defined]
    body: dict
    current_response: Optional["BoltResponse"]  # type: ignore[name-defined]
    last_global_middleware_name: Optional[str]

    def __init__(
        self,
        *,
        request: Union["BoltRequest", "AsyncBoltRequest"],  # type: ignore[name-defined]
        current_response: Optional["BoltResponse"],  # type: ignore[name-defined]
        last_global_middleware_name: Optional[str] = None,
    ):
        self.request = request
        self.body = request.body if request is not None else {}
        self.current_response = current_response
        self.last_global_middleware_name = last_global_middleware_name

    def __str__(self) -> str:
        return "unhandled request error"
```

General class in a Bolt app

### Ancestors

* [BoltError](#slack_bolt.error.BoltError "slack_bolt.error.BoltError")
* builtins.Exception
* builtins.BaseException

### Class variables

`var body : dict`

The type of the None singleton.

`var current_response : BoltResponse | None`

The type of the None singleton.

`var last_global_middleware_name : str | None`

The type of the None singleton.

`var request : BoltRequest`

The type of the None singleton.
