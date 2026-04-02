Source: https://docs.slack.dev/tools/bolt-python/reference/listener_matcher

# Module slack_bolt.listener_matcher

A listener matcher is a simplified version of listener middleware. A listener matcher function returns bool value instead of `next()` method invocation inside. This interface enables developers to utilize simple predicate functions for additional listener conditions.

## Sub-modules

`[slack_bolt.listener_matcher.async_builtins](async_builtins.html "slack_bolt.listener_matcher.async_builtins")`

`[slack_bolt.listener_matcher.async_listener_matcher](async_listener_matcher.html "slack_bolt.listener_matcher.async_listener_matcher")`

`[slack_bolt.listener_matcher.builtins](builtins.html "slack_bolt.listener_matcher.builtins")`

`[slack_bolt.listener_matcher.custom_listener_matcher](custom_listener_matcher.html "slack_bolt.listener_matcher.custom_listener_matcher")`

`[slack_bolt.listener_matcher.listener_matcher](listener_matcher.html "slack_bolt.listener_matcher.listener_matcher")`

## Classes

`class CustomListenerMatcher (*,   app_name: str,   func: Callable[..., bool],   base_logger: logging.Logger | None = None)`

Expand source code

```python
class CustomListenerMatcher(ListenerMatcher):
    app_name: str
    func: Callable[..., bool]
    arg_names: MutableSequence[str]
    logger: Logger

    def __init__(self, *, app_name: str, func: Callable[..., bool], base_logger: Optional[Logger] = None):
        self.app_name = app_name
        self.func = func
        self.arg_names = get_arg_names_of_callable(func)
        self.logger = get_bolt_app_logger(self.app_name, self.func, base_logger)

    def matches(self, req: BoltRequest, resp: BoltResponse) -> bool:
        return self.func(
            **build_required_kwargs(
                logger=self.logger,
                required_arg_names=self.arg_names,
                request=req,
                response=resp,
                this_func=self.func,
            )
        )
```

### Ancestors

* [ListenerMatcher](listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")

### Class variables

`var app_name : str`

The type of the None singleton.

`var arg_names : MutableSequence[str]`

The type of the None singleton.

`var func : Callable[..., bool]`

The type of the None singleton.

`var logger : logging.Logger`

The type of the None singleton.

### Inherited members

* `**[ListenerMatcher](listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")**`:
  * `[matches](listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher.matches "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher.matches")`

`class ListenerMatcher`

Expand source code

```python
class ListenerMatcher(metaclass=ABCMeta):
    @abstractmethod
    def matches(self, req: BoltRequest, resp: BoltResponse) -> bool:
        """Matches against the request and returns True if matched.

        Args:
            req: The request
            resp: The response

        Returns:
            True if matched.
        """
        raise NotImplementedError()
```

### Subclasses

* [BuiltinListenerMatcher](builtins.html#slack_bolt.listener_matcher.builtins.BuiltinListenerMatcher "slack_bolt.listener_matcher.builtins.BuiltinListenerMatcher")
* [CustomListenerMatcher](custom_listener_matcher.html#slack_bolt.listener_matcher.custom_listener_matcher.CustomListenerMatcher "slack_bolt.listener_matcher.custom_listener_matcher.CustomListenerMatcher")

### Methods

`def matches(self,   req: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> bool`

Expand source code

```text
@abstractmethod
def matches(self, req: BoltRequest, resp: BoltResponse) -> bool:
    """Matches against the request and returns True if matched.

    Args:
        req: The request
        resp: The response

    Returns:
        True if matched.
    """
    raise NotImplementedError()
```

Matches against the request and returns True if matched.

## Args

## `req`

The request

## `resp`

The response

## Returns

True if matched.
