Source: https://docs.slack.dev/tools/bolt-python/reference/listener

# Module slack_bolt.listener

Listeners process an incoming request from Slack if the request's type or data structure matches the predefined conditions of the listener. Typically, a listener acknowledge requests from Slack, process the request data, and may send response back to Slack.

## Sub-modules

`[slack_bolt.listener.async_builtins](async_builtins.html "slack_bolt.listener.async_builtins")`

`[slack_bolt.listener.async_listener](async_listener.html "slack_bolt.listener.async_listener")`

`[slack_bolt.listener.async_listener_completion_handler](async_listener_completion_handler.html "slack_bolt.listener.async_listener_completion_handler")`

`[slack_bolt.listener.async_listener_error_handler](async_listener_error_handler.html "slack_bolt.listener.async_listener_error_handler")`

`[slack_bolt.listener.async_listener_start_handler](async_listener_start_handler.html "slack_bolt.listener.async_listener_start_handler")`

`[slack_bolt.listener.asyncio_runner](asyncio_runner.html "slack_bolt.listener.asyncio_runner")`

`[slack_bolt.listener.builtins](builtins.html "slack_bolt.listener.builtins")`

`[slack_bolt.listener.custom_listener](custom_listener.html "slack_bolt.listener.custom_listener")`

`[slack_bolt.listener.listener](listener.html "slack_bolt.listener.listener")`

`[slack_bolt.listener.listener_completion_handler](listener_completion_handler.html "slack_bolt.listener.listener_completion_handler")`

`[slack_bolt.listener.listener_error_handler](listener_error_handler.html "slack_bolt.listener.listener_error_handler")`

`[slack_bolt.listener.listener_start_handler](listener_start_handler.html "slack_bolt.listener.listener_start_handler")`

`[slack_bolt.listener.thread_runner](thread_runner.html "slack_bolt.listener.thread_runner")`

## Classes

`class CustomListener (*,   app_name: str,   ack_function: Callable[..., [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None],   lazy_functions: Sequence[Callable[..., None]],   matchers: Sequence[[ListenerMatcher](../listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")],   middleware: Sequence[[Middleware](../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")],   auto_acknowledgement: bool = False,   ack_timeout: int = 3,   base_logger: logging.Logger | None = None)`

Expand source code

```python
class CustomListener(Listener):
    app_name: str
    ack_function: Callable[..., Optional[BoltResponse]]  # type: ignore[assignment]
    lazy_functions: Sequence[Callable[..., None]]
    matchers: Sequence[ListenerMatcher]
    middleware: Sequence[Middleware]
    auto_acknowledgement: bool
    ack_timeout: int = 3
    arg_names: MutableSequence[str]
    logger: Logger

    def __init__(
        self,
        *,
        app_name: str,
        ack_function: Callable[..., Optional[BoltResponse]],
        lazy_functions: Sequence[Callable[..., None]],
        matchers: Sequence[ListenerMatcher],
        middleware: Sequence[Middleware],
        auto_acknowledgement: bool = False,
        ack_timeout: int = 3,
        base_logger: Optional[Logger] = None,
    ):
        self.app_name = app_name
        self.ack_function = ack_function
        self.lazy_functions = lazy_functions
        self.matchers = matchers
        self.middleware = middleware
        self.auto_acknowledgement = auto_acknowledgement
        self.ack_timeout = ack_timeout
        self.arg_names = get_arg_names_of_callable(ack_function)
        self.logger = get_bolt_app_logger(app_name, self.ack_function, base_logger)

    def run_ack_function(
        self,
        *,
        request: BoltRequest,
        response: BoltResponse,
    ) -> Optional[BoltResponse]:
        return self.ack_function(
            **build_required_kwargs(
                logger=self.logger,
                required_arg_names=self.arg_names,
                request=request,
                response=response,
                this_func=self.ack_function,
            )
        )
```

### Ancestors

* [Listener](listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")

### Class variables

`var app_name : str`

The type of the None singleton.

`var arg_names : MutableSequence[str]`

The type of the None singleton.

`var logger : logging.Logger`

The type of the None singleton.

### Inherited members

* `**[Listener](listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")**`:
  * `[ack_function](listener.html#slack_bolt.listener.listener.Listener.ack_function "slack_bolt.listener.listener.Listener.ack_function")`
  * `[ack_timeout](listener.html#slack_bolt.listener.listener.Listener.ack_timeout "slack_bolt.listener.listener.Listener.ack_timeout")`
  * `[auto_acknowledgement](listener.html#slack_bolt.listener.listener.Listener.auto_acknowledgement "slack_bolt.listener.listener.Listener.auto_acknowledgement")`
  * `[lazy_functions](listener.html#slack_bolt.listener.listener.Listener.lazy_functions "slack_bolt.listener.listener.Listener.lazy_functions")`
  * `[matchers](listener.html#slack_bolt.listener.listener.Listener.matchers "slack_bolt.listener.listener.Listener.matchers")`
  * `[middleware](listener.html#slack_bolt.listener.listener.Listener.middleware "slack_bolt.listener.listener.Listener.middleware")`
  * `[run_ack_function](listener.html#slack_bolt.listener.listener.Listener.run_ack_function "slack_bolt.listener.listener.Listener.run_ack_function")`
  * `[run_middleware](listener.html#slack_bolt.listener.listener.Listener.run_middleware "slack_bolt.listener.listener.Listener.run_middleware")`

`class Listener`

Expand source code

```python
class Listener(metaclass=ABCMeta):
    matchers: Sequence[ListenerMatcher]
    middleware: Sequence[Middleware]
    ack_function: Callable[..., BoltResponse]
    lazy_functions: Sequence[Callable[..., None]]
    auto_acknowledgement: bool
    ack_timeout: int = 3

    def matches(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
    ) -> bool:
        is_matched: bool = False
        for matcher in self.matchers:
            is_matched = matcher.matches(req, resp)
            if not is_matched:
                return is_matched
        return is_matched

    def run_middleware(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
    ) -> Tuple[Optional[BoltResponse], bool]:
        """Runs a middleware.

        Args:
            req: The incoming request
            resp: The current response

        Returns:
            A tuple of the processed response and a flag indicating termination
        """
        for m in self.middleware:
            middleware_state = {"next_called": False}

            def next_():
                middleware_state["next_called"] = True

            resp = m.process(req=req, resp=resp, next=next_)  # type: ignore[assignment]
            if not middleware_state["next_called"]:
                # next() was not called in this middleware
                return (resp, True)
        return (resp, False)

    @abstractmethod
    def run_ack_function(self, *, request: BoltRequest, response: BoltResponse) -> Optional[BoltResponse]:
        """Runs all the registered middleware and then run the listener function.

        Args:
            request: The incoming request
            response: The current response

        Returns:
            The processed response
        """
        raise NotImplementedError()
```

### Subclasses

* [CustomListener](custom_listener.html#slack_bolt.listener.custom_listener.CustomListener "slack_bolt.listener.custom_listener.CustomListener")

### Class variables

`var ack_function : Callable[..., [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")]`

The type of the None singleton.

`var ack_timeout : int`

The type of the None singleton.

`var auto_acknowledgement : bool`

The type of the None singleton.

`var lazy_functions : Sequence[Callable[..., None]]`

The type of the None singleton.

`var matchers : Sequence[[ListenerMatcher](../listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")]`

The type of the None singleton.

`var middleware : Sequence[[Middleware](../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")]`

The type of the None singleton.

### Methods

`def matches(self,   *,   req: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> bool`

Expand source code

```python
def matches(
    self,
    *,
    req: BoltRequest,
    resp: BoltResponse,
) -> bool:
    is_matched: bool = False
    for matcher in self.matchers:
        is_matched = matcher.matches(req, resp)
        if not is_matched:
            return is_matched
    return is_matched
```

`def run_ack_function(self,   *,   request: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   response: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None`

Expand source code

```text
@abstractmethod
def run_ack_function(self, *, request: BoltRequest, response: BoltResponse) -> Optional[BoltResponse]:
    """Runs all the registered middleware and then run the listener function.

    Args:
        request: The incoming request
        response: The current response

    Returns:
        The processed response
    """
    raise NotImplementedError()
```

Runs all the registered middleware and then run the listener function.

## Args

## `request`

The incoming request

## `response`

The current response

## Returns

The processed response

`def run_middleware(self,   *,   req: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> Tuple[[BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None, bool]`

Expand source code

```python
def run_middleware(
    self,
    *,
    req: BoltRequest,
    resp: BoltResponse,
) -> Tuple[Optional[BoltResponse], bool]:
    """Runs a middleware.

    Args:
        req: The incoming request
        resp: The current response

    Returns:
        A tuple of the processed response and a flag indicating termination
    """
    for m in self.middleware:
        middleware_state = {"next_called": False}

        def next_():
            middleware_state["next_called"] = True

        resp = m.process(req=req, resp=resp, next=next_)  # type: ignore[assignment]
        if not middleware_state["next_called"]:
            # next() was not called in this middleware
            return (resp, True)
    return (resp, False)
```

Runs a middleware.

## Args

## `req`

The incoming request

## `resp`

The current response

## Returns

A tuple of the processed response and a flag indicating termination
