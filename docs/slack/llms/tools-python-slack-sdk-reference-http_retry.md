Source: https://docs.slack.dev/tools/python-slack-sdk/reference/http_retry

# Module slack_sdk.http_retry

## Sub-modules

`[slack_sdk.http_retry.async_handler](async_handler.html "slack_sdk.http_retry.async_handler")`

asyncio compatible RetryHandler interface. You can pass an array of handlers to customize retry logics in supported API clients.

`[slack_sdk.http_retry.builtin_async_handlers](builtin_async_handlers.html "slack_sdk.http_retry.builtin_async_handlers")`

`[slack_sdk.http_retry.builtin_handlers](builtin_handlers.html "slack_sdk.http_retry.builtin_handlers")`

`[slack_sdk.http_retry.builtin_interval_calculators](builtin_interval_calculators.html "slack_sdk.http_retry.builtin_interval_calculators")`

`[slack_sdk.http_retry.handler](handler.html "slack_sdk.http_retry.handler")`

RetryHandler interface. You can pass an array of handlers to customize retry logics in supported API clients.

`[slack_sdk.http_retry.interval_calculator](interval_calculator.html "slack_sdk.http_retry.interval_calculator")`

`[slack_sdk.http_retry.jitter](jitter.html "slack_sdk.http_retry.jitter")`

`[slack_sdk.http_retry.request](request.html "slack_sdk.http_retry.request")`

`[slack_sdk.http_retry.response](response.html "slack_sdk.http_retry.response")`

`[slack_sdk.http_retry.state](state.html "slack_sdk.http_retry.state")`

## Functions

`def all_builtin_retry_handlers() ‑> List[[RetryHandler](handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")]`

Expand source code

```python
def all_builtin_retry_handlers() -> List[RetryHandler]:
    return [
        connect_error_retry_handler,
        rate_limit_error_retry_handler,
    ]
```

`def default_retry_handlers() ‑> List[[RetryHandler](handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")]`

Expand source code

```python
def default_retry_handlers() -> List[RetryHandler]:
    return [connect_error_retry_handler]
```

## Classes

`class BackoffRetryIntervalCalculator (backoff_factor: float = 0.5,   jitter: [Jitter](jitter.html#slack_sdk.http_retry.jitter.Jitter "slack_sdk.http_retry.jitter.Jitter") | None = None)`

Expand source code

```typescript
class BackoffRetryIntervalCalculator(RetryIntervalCalculator):
    """Retry interval calculator that calculates in the manner of Exponential Backoff And Jitter
    see also: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
    """

    backoff_factor: float
    jitter: Jitter

    def __init__(self, backoff_factor: float = 0.5, jitter: Optional[Jitter] = None):
        """Retry interval calculator that calculates in the manner of Exponential Backoff And Jitter

        Args:
            backoff_factor: The factor for the backoff interval calculation
            jitter: The jitter logic implementation
        """
        self.backoff_factor = backoff_factor
        self.jitter = jitter if jitter is not None else RandomJitter()

    def calculate_sleep_duration(self, current_attempt: int) -> float:
        interval = self.backoff_factor * (2 ** (current_attempt))
        sleep_duration = self.jitter.recalculate(interval)
        return sleep_duration
```

Retry interval calculator that calculates in the manner of Exponential Backoff And Jitter see also: [https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)

Retry interval calculator that calculates in the manner of Exponential Backoff And Jitter

## Args

**`backoff_factor`**

The factor for the backoff interval calculation

**`jitter`**

The jitter logic implementation

### Ancestors

* [RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator")

### Class variables

`var backoff_factor : float`

The type of the None singleton.

`var jitter : [Jitter](jitter.html#slack_sdk.http_retry.jitter.Jitter "slack_sdk.http_retry.jitter.Jitter")`

The type of the None singleton.

### Inherited members

* `**[RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator")**`:
  * `[calculate_sleep_duration](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator.calculate_sleep_duration "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator.calculate_sleep_duration")`

`class ConnectionErrorRetryHandler (max_retry_count: int = 1,   interval_calculator: [RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator") = <slack_sdk.http_retry.builtin_interval_calculators.BackoffRetryIntervalCalculator object>,   error_types: List[Type[Exception]] = [<class 'urllib.error.URLError'>, <class 'ConnectionResetError'>, <class 'http.client.RemoteDisconnected'>])`

Expand source code

```typescript
class ConnectionErrorRetryHandler(RetryHandler):
    """RetryHandler that does retries for connectivity issues."""

    def __init__(
        self,
        max_retry_count: int = 1,
        interval_calculator: RetryIntervalCalculator = default_interval_calculator,
        error_types: List[Type[Exception]] = [
            # To cover URLError: <urlopen error [Errno 104] Connection reset by peer>
            URLError,
            ConnectionResetError,
            RemoteDisconnected,
        ],
    ):
        super().__init__(max_retry_count, interval_calculator)
        self.error_types_to_do_retries = error_types

    def _can_retry(
        self,
        *,
        state: RetryState,
        request: HttpRequest,
        response: Optional[HttpResponse] = None,
        error: Optional[Exception] = None,
    ) -> bool:
        if error is None:
            return False

        if isinstance(error, URLError):
            if response is not None:
                return False  # status 40x

        for error_type in self.error_types_to_do_retries:
            if isinstance(error, error_type):
                return True
        return False
```

RetryHandler that does retries for connectivity issues.

RetryHandler interface.

## Args (2)

**`max_retry_count`**

The maximum times to do retries

**`interval_calculator`**

Pass an interval calculator for customizing the logic

### Ancestors (2)

* [RetryHandler](handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")

### Inherited members (2)

* `**[RetryHandler](handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")**`:
  * `[interval_calculator](handler.html#slack_sdk.http_retry.handler.RetryHandler.interval_calculator "slack_sdk.http_retry.handler.RetryHandler.interval_calculator")`
  * `[max_retry_count](handler.html#slack_sdk.http_retry.handler.RetryHandler.max_retry_count "slack_sdk.http_retry.handler.RetryHandler.max_retry_count")`

`class FixedValueRetryIntervalCalculator (fixed_internal: float = 0.5)`

Expand source code

```typescript
class FixedValueRetryIntervalCalculator(RetryIntervalCalculator):
    """Retry interval calculator that uses a fixed value."""

    fixed_interval: float

    def __init__(self, fixed_internal: float = 0.5):
        """Retry interval calculator that uses a fixed value.

        Args:
            fixed_internal: The fixed interval seconds
        """
        self.fixed_interval = fixed_internal

    def calculate_sleep_duration(self, current_attempt: int) -> float:
        return self.fixed_interval
```

Retry interval calculator that uses a fixed value.

Retry interval calculator that uses a fixed value.

## Args (3)

**`fixed_internal`**

The fixed interval seconds

### Ancestors (3)

* [RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator")

### Class variables (2)

`var fixed_interval : float`

The type of the None singleton.

### Inherited members (3)

* `**[RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator")**`:
  * `[calculate_sleep_duration](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator.calculate_sleep_duration "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator.calculate_sleep_duration")`

`class HttpRequest (*,   method: str,   url: str,   headers: Dict[str, str | List[str]],   body_params: Dict[str, Any] | None = None,   data: bytes | None = None)`

Expand source code

```typescript
class HttpRequest:
    """HTTP request representation"""

    method: str
    url: str
    headers: Dict[str, Union[str, List[str]]]
    body_params: Optional[Dict[str, Any]]
    data: Optional[bytes]

    def __init__(
        self,
        *,
        method: str,
        url: str,
        headers: Dict[str, Union[str, List[str]]],
        body_params: Optional[Dict[str, Any]] = None,
        data: Optional[bytes] = None,
    ):
        self.method = method
        self.url = url
        self.headers = {k: v if isinstance(v, list) else [v] for k, v in headers.items()}
        self.body_params = body_params
        self.data = data

    @classmethod
    def from_urllib_http_request(cls, req: Request) -> "HttpRequest":
        return HttpRequest(
            method=req.method,  # type: ignore[arg-type]
            url=req.full_url,
            headers={k: v if isinstance(v, list) else [v] for k, v in req.headers.items()},
            data=req.data,  # type: ignore[arg-type]
        )
```

HTTP request representation

### Class variables (3)

`var body_params : Dict[str, Any] | None`

The type of the None singleton.

`var data : bytes | None`

The type of the None singleton.

`var headers : Dict[str, str | List[str]]`

The type of the None singleton.

`var method : str`

The type of the None singleton.

`var url : str`

The type of the None singleton.

### Static methods

`def from_urllib_http_request(req: urllib.request.Request) ‑> [HttpRequest](request.html#slack_sdk.http_retry.request.HttpRequest "slack_sdk.http_retry.request.HttpRequest")`

`class HttpResponse (*,   status_code: int | str,   headers: Dict[str, str | List[str]],   body: Dict[str, Any] | None = None,   data: bytes | None = None)`

Expand source code

```typescript
class HttpResponse:
    """HTTP response representation"""

    status_code: int
    headers: Dict[str, Union[List[str], str]]
    body: Optional[Dict[str, Any]]
    data: Optional[bytes]

    def __init__(
        self,
        *,
        status_code: Union[int, str],
        headers: Dict[str, Union[str, List[str]]],
        body: Optional[Dict[str, Any]] = None,
        data: Optional[bytes] = None,
    ):
        self.status_code = int(status_code)
        self.headers = {k: v if isinstance(v, list) else [v] for k, v in headers.items()}
        self.body = body
        self.data = data
```

HTTP response representation

### Class variables (4)

`var body : Dict[str, Any] | None`

The type of the None singleton.

`var data : bytes | None`

The type of the None singleton.

`var headers : Dict[str, str | List[str]]`

The type of the None singleton.

`var status_code : int`

The type of the None singleton.

`class Jitter`

Expand source code

```typescript
class Jitter:
    """Jitter interface"""

    def recalculate(self, duration: float) -> float:
        """Recalculate the given duration.
        see also: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/

        Args:
            duration: the duration in seconds

        Returns:
            A new duration that the jitter amount is added
        """
        raise NotImplementedError()
```

Jitter interface

### Subclasses

* [RandomJitter](jitter.html#slack_sdk.http_retry.jitter.RandomJitter "slack_sdk.http_retry.jitter.RandomJitter")

### Methods

`def recalculate(self, duration: float) ‑> float`

Expand source code

```python
def recalculate(self, duration: float) -> float:
    """Recalculate the given duration.
    see also: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/

    Args:
        duration: the duration in seconds

    Returns:
        A new duration that the jitter amount is added
    """
    raise NotImplementedError()
```

Recalculate the given duration. see also: [https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)

## Args (4)

**`duration`**

the duration in seconds

## Returns

A new duration that the jitter amount is added

`class RateLimitErrorRetryHandler (max_retry_count: int = 1,   interval_calculator: [RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator") = <slack_sdk.http_retry.builtin_interval_calculators.BackoffRetryIntervalCalculator object>)`

Expand source code

```typescript
class RateLimitErrorRetryHandler(RetryHandler):
    """RetryHandler that does retries for rate limited errors."""

    def _can_retry(
        self,
        *,
        state: RetryState,
        request: HttpRequest,
        response: Optional[HttpResponse] = None,
        error: Optional[Exception] = None,
    ) -> bool:
        return response is not None and response.status_code == 429

    def prepare_for_next_attempt(
        self,
        *,
        state: RetryState,
        request: HttpRequest,
        response: Optional[HttpResponse] = None,
        error: Optional[Exception] = None,
    ) -> None:
        if response is None:
            raise error  # type: ignore[misc]

        state.next_attempt_requested = True
        retry_after_header_name: Optional[str] = None
        for k in response.headers.keys():
            if k.lower() == "retry-after":
                retry_after_header_name = k
                break
        duration = 1
        if retry_after_header_name is None:
            # This situation usually does not arise. Just in case.
            duration += random.random()  # type: ignore[assignment]
        else:
            duration = int(response.headers.get(retry_after_header_name)[0]) + random.random()  # type: ignore[index, assignment] # noqa: E501
        time.sleep(duration)
        state.increment_current_attempt()
```

RetryHandler that does retries for rate limited errors.

RetryHandler interface.

## Args (5)

**`max_retry_count`**

The maximum times to do retries

**`interval_calculator`**

Pass an interval calculator for customizing the logic

### Ancestors (4)

* [RetryHandler](handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")

### Methods (2)

`def prepare_for_next_attempt(self,   *,   state: [RetryState](state.html#slack_sdk.http_retry.state.RetryState "slack_sdk.http_retry.state.RetryState"),   request: [HttpRequest](request.html#slack_sdk.http_retry.request.HttpRequest "slack_sdk.http_retry.request.HttpRequest"),   response: [HttpResponse](response.html#slack_sdk.http_retry.response.HttpResponse "slack_sdk.http_retry.response.HttpResponse") | None = None,   error: Exception | None = None) ‑> None`

Expand source code

```python
def prepare_for_next_attempt(
    self,
    *,
    state: RetryState,
    request: HttpRequest,
    response: Optional[HttpResponse] = None,
    error: Optional[Exception] = None,
) -> None:
    if response is None:
        raise error  # type: ignore[misc]

    state.next_attempt_requested = True
    retry_after_header_name: Optional[str] = None
    for k in response.headers.keys():
        if k.lower() == "retry-after":
            retry_after_header_name = k
            break
    duration = 1
    if retry_after_header_name is None:
        # This situation usually does not arise. Just in case.
        duration += random.random()  # type: ignore[assignment]
    else:
        duration = int(response.headers.get(retry_after_header_name)[0]) + random.random()  # type: ignore[index, assignment] # noqa: E501
    time.sleep(duration)
    state.increment_current_attempt()
```

### Inherited members (4)

* `**[RetryHandler](handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")**`:
  * `[interval_calculator](handler.html#slack_sdk.http_retry.handler.RetryHandler.interval_calculator "slack_sdk.http_retry.handler.RetryHandler.interval_calculator")`
  * `[max_retry_count](handler.html#slack_sdk.http_retry.handler.RetryHandler.max_retry_count "slack_sdk.http_retry.handler.RetryHandler.max_retry_count")`

`class RetryHandler (max_retry_count: int = 1,   interval_calculator: [RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator") = <slack_sdk.http_retry.builtin_interval_calculators.BackoffRetryIntervalCalculator object>)`

Expand source code

```typescript
class RetryHandler:
    """RetryHandler interface.
    You can pass an array of handlers to customize retry logics in supported API clients.
    """

    max_retry_count: int
    interval_calculator: RetryIntervalCalculator

    def __init__(
        self,
        max_retry_count: int = 1,
        interval_calculator: RetryIntervalCalculator = default_interval_calculator,
    ):
        """RetryHandler interface.

        Args:
            max_retry_count: The maximum times to do retries
            interval_calculator: Pass an interval calculator for customizing the logic
        """
        self.max_retry_count = max_retry_count
        self.interval_calculator = interval_calculator

    def can_retry(
        self,
        *,
        state: RetryState,
        request: HttpRequest,
        response: Optional[HttpResponse] = None,
        error: Optional[Exception] = None,
    ) -> bool:
        if state.current_attempt >= self.max_retry_count:
            return False
        return self._can_retry(
            state=state,
            request=request,
            response=response,
            error=error,
        )

    def _can_retry(
        self,
        *,
        state: RetryState,
        request: HttpRequest,
        response: Optional[HttpResponse] = None,
        error: Optional[Exception] = None,
    ) -> bool:
        raise NotImplementedError()

    def prepare_for_next_attempt(
        self,
        *,
        state: RetryState,
        request: HttpRequest,
        response: Optional[HttpResponse] = None,
        error: Optional[Exception] = None,
    ) -> None:
        state.next_attempt_requested = True
        duration = self.interval_calculator.calculate_sleep_duration(state.current_attempt)
        time.sleep(duration)
        state.increment_current_attempt()
```

RetryHandler interface. You can pass an array of handlers to customize retry logics in supported API clients.

RetryHandler interface.

## Args (6)

**`max_retry_count`**

The maximum times to do retries

**`interval_calculator`**

Pass an interval calculator for customizing the logic

### Subclasses (2)

* [ConnectionErrorRetryHandler](builtin_handlers.html#slack_sdk.http_retry.builtin_handlers.ConnectionErrorRetryHandler "slack_sdk.http_retry.builtin_handlers.ConnectionErrorRetryHandler")
* [RateLimitErrorRetryHandler](builtin_handlers.html#slack_sdk.http_retry.builtin_handlers.RateLimitErrorRetryHandler "slack_sdk.http_retry.builtin_handlers.RateLimitErrorRetryHandler")
* [ServerErrorRetryHandler](builtin_handlers.html#slack_sdk.http_retry.builtin_handlers.ServerErrorRetryHandler "slack_sdk.http_retry.builtin_handlers.ServerErrorRetryHandler")

### Class variables (5)

`var interval_calculator : [RetryIntervalCalculator](interval_calculator.html#slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator "slack_sdk.http_retry.interval_calculator.RetryIntervalCalculator")`

The type of the None singleton.

`var max_retry_count : int`

The type of the None singleton.

### Methods (3)

`def can_retry(self,   *,   state: [RetryState](state.html#slack_sdk.http_retry.state.RetryState "slack_sdk.http_retry.state.RetryState"),   request: [HttpRequest](request.html#slack_sdk.http_retry.request.HttpRequest "slack_sdk.http_retry.request.HttpRequest"),   response: [HttpResponse](response.html#slack_sdk.http_retry.response.HttpResponse "slack_sdk.http_retry.response.HttpResponse") | None = None,   error: Exception | None = None) ‑> bool`

Expand source code

```python
def can_retry(
    self,
    *,
    state: RetryState,
    request: HttpRequest,
    response: Optional[HttpResponse] = None,
    error: Optional[Exception] = None,
) -> bool:
    if state.current_attempt >= self.max_retry_count:
        return False
    return self._can_retry(
        state=state,
        request=request,
        response=response,
        error=error,
    )
```

`def prepare_for_next_attempt(self,   *,   state: [RetryState](state.html#slack_sdk.http_retry.state.RetryState "slack_sdk.http_retry.state.RetryState"),   request: [HttpRequest](request.html#slack_sdk.http_retry.request.HttpRequest "slack_sdk.http_retry.request.HttpRequest"),   response: [HttpResponse](response.html#slack_sdk.http_retry.response.HttpResponse "slack_sdk.http_retry.response.HttpResponse") | None = None,   error: Exception | None = None) ‑> None`

Expand source code

```python
def prepare_for_next_attempt(
    self,
    *,
    state: RetryState,
    request: HttpRequest,
    response: Optional[HttpResponse] = None,
    error: Optional[Exception] = None,
) -> None:
    state.next_attempt_requested = True
    duration = self.interval_calculator.calculate_sleep_duration(state.current_attempt)
    time.sleep(duration)
    state.increment_current_attempt()
```

`class RetryIntervalCalculator`

Expand source code

```typescript
class RetryIntervalCalculator:
    """Retry interval calculator interface."""

    def calculate_sleep_duration(self, current_attempt: int) -> float:
        """Calculates an interval duration in seconds.

        Args:
            current_attempt: the number of the current attempt (zero-origin; 0 means no retries are done so far)
        Returns:
            calculated interval duration in seconds
        """
        raise NotImplementedError()
```

Retry interval calculator interface.

### Subclasses (3)

* [BackoffRetryIntervalCalculator](builtin_interval_calculators.html#slack_sdk.http_retry.builtin_interval_calculators.BackoffRetryIntervalCalculator "slack_sdk.http_retry.builtin_interval_calculators.BackoffRetryIntervalCalculator")
* [FixedValueRetryIntervalCalculator](builtin_interval_calculators.html#slack_sdk.http_retry.builtin_interval_calculators.FixedValueRetryIntervalCalculator "slack_sdk.http_retry.builtin_interval_calculators.FixedValueRetryIntervalCalculator")

### Methods (4)

`def calculate_sleep_duration(self, current_attempt: int) ‑> float`

Expand source code

```typescript
def calculate_sleep_duration(self, current_attempt: int) -> float:
    """Calculates an interval duration in seconds.

    Args:
        current_attempt: the number of the current attempt (zero-origin; 0 means no retries are done so far)
    Returns:
        calculated interval duration in seconds
    """
    raise NotImplementedError()
```

Calculates an interval duration in seconds.

## Args (7)

**`current_attempt`**

the number of the current attempt (zero-origin; 0 means no retries are done so far)

## Returns (2)

calculated interval duration in seconds

`class RetryState (*, current_attempt: int = 0, custom_values: Dict[str, Any] | None = None)`

Expand source code

```typescript
class RetryState:
    next_attempt_requested: bool
    current_attempt: int  # zero-origin
    custom_values: Optional[Dict[str, Any]]

    def __init__(
        self,
        *,
        current_attempt: int = 0,
        custom_values: Optional[Dict[str, Any]] = None,
    ):
        self.next_attempt_requested = False
        self.current_attempt = current_attempt
        self.custom_values = custom_values

    def increment_current_attempt(self) -> int:
        self.current_attempt += 1
        return self.current_attempt
```

### Class variables (6)

`var current_attempt : int`

The type of the None singleton.

`var custom_values : Dict[str, Any] | None`

The type of the None singleton.

`var next_attempt_requested : bool`

The type of the None singleton.

### Methods (5)

`def increment_current_attempt(self) ‑> int`

Expand source code

```python
def increment_current_attempt(self) -> int:
    self.current_attempt += 1
    return self.current_attempt
```
