Source: https://docs.slack.dev/tools/bolt-python/reference/lazy_listener

# Module slack_bolt.lazy_listener

Lazy listener runner is a beta feature for the apps running on Function-as-a-Service platforms.

```python
def respond_to_slack_within_3_seconds(body, ack):
    text = body.get("text")
    if text is None or len(text) == 0:
        ack(f":x: Usage: /start-process (description here)")
    else:
        ack(f"Accepted! (task: {body['text']})")

import time
def run_long_process(respond, body):
    time.sleep(5)  # longer than 3 seconds
    respond(f"Completed! (task: {body['text']})")

app.command("/start-process")(
    # ack() is still called within 3 seconds
    ack=respond_to_slack_within_3_seconds,
    # Lazy function is responsible for processing the event
    lazy=[run_long_process]
)
```

Refer to [https://docs.slack.dev/tools/bolt-python/concepts/lazy-listeners](https://docs.slack.dev/tools/bolt-python/concepts/lazy-listeners) for more details.

## Sub-modules

`[slack_bolt.lazy_listener.async_internals](async_internals.html "slack_bolt.lazy_listener.async_internals")`

`[slack_bolt.lazy_listener.async_runner](async_runner.html "slack_bolt.lazy_listener.async_runner")`

`[slack_bolt.lazy_listener.asyncio_runner](asyncio_runner.html "slack_bolt.lazy_listener.asyncio_runner")`

`[slack_bolt.lazy_listener.internals](internals.html "slack_bolt.lazy_listener.internals")`

`[slack_bolt.lazy_listener.runner](runner.html "slack_bolt.lazy_listener.runner")`

`[slack_bolt.lazy_listener.thread_runner](thread_runner.html "slack_bolt.lazy_listener.thread_runner")`

## Classes

`class LazyListenerRunner`

Expand source code

```python
class LazyListenerRunner(metaclass=ABCMeta):
    logger: Logger

    @abstractmethod
    def start(self, function: Callable[..., None], request: BoltRequest) -> None:
        """Starts a new lazy listener execution.

        Args:
            function: The function to run.
            request: The request to pass to the function. The object must be thread-safe.
        """
        raise NotImplementedError()

    def run(self, function: Callable[..., None], request: BoltRequest) -> None:
        """Synchronously runs the function with a given request data.

        Args:
            function: The function to run.
            request: The request to pass to the function. The object must be thread-safe.
        """
        build_runnable_function(
            func=function,
            logger=self.logger,
            request=request,
        )()
```

### Subclasses

* [ChaliceLazyListenerRunner](../adapter/aws_lambda/chalice_lazy_listener_runner.html#slack_bolt.adapter.aws_lambda.chalice_lazy_listener_runner.ChaliceLazyListenerRunner "slack_bolt.adapter.aws_lambda.chalice_lazy_listener_runner.ChaliceLazyListenerRunner")
* [LambdaLazyListenerRunner](../adapter/aws_lambda/lazy_listener_runner.html#slack_bolt.adapter.aws_lambda.lazy_listener_runner.LambdaLazyListenerRunner "slack_bolt.adapter.aws_lambda.lazy_listener_runner.LambdaLazyListenerRunner")
* [NoopLazyListenerRunner](../adapter/google_cloud_functions/handler.html#slack_bolt.adapter.google_cloud_functions.handler.NoopLazyListenerRunner "slack_bolt.adapter.google_cloud_functions.handler.NoopLazyListenerRunner")
* [ThreadLazyListenerRunner](thread_runner.html#slack_bolt.lazy_listener.thread_runner.ThreadLazyListenerRunner "slack_bolt.lazy_listener.thread_runner.ThreadLazyListenerRunner")

### Class variables

`var logger : logging.Logger`

The type of the None singleton.

### Methods

`def run(self,   function: Callable[..., None],   request: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")) ‑> None`

Expand source code

```python
def run(self, function: Callable[..., None], request: BoltRequest) -> None:
    """Synchronously runs the function with a given request data.

    Args:
        function: The function to run.
        request: The request to pass to the function. The object must be thread-safe.
    """
    build_runnable_function(
        func=function,
        logger=self.logger,
        request=request,
    )()
```

Synchronously runs the function with a given request data.

## Args

## `function`

The function to run.

## `request`

The request to pass to the function. The object must be thread-safe.

`def start(self,   function: Callable[..., None],   request: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")) ‑> None`

Expand source code

```text
@abstractmethod
def start(self, function: Callable[..., None], request: BoltRequest) -> None:
    """Starts a new lazy listener execution.

    Args:
        function: The function to run.
        request: The request to pass to the function. The object must be thread-safe.
    """
    raise NotImplementedError()
```

Starts a new lazy listener execution.

## Args

## `function`

The function to run.

## `request`

The request to pass to the function. The object must be thread-safe.

`class ThreadLazyListenerRunner (logger: logging.Logger, executor: concurrent.futures._base.Executor)`

Expand source code

```python
class ThreadLazyListenerRunner(LazyListenerRunner):
    logger: Logger

    def __init__(
        self,
        logger: Logger,
        executor: Executor,
    ):
        self.logger = logger
        self.executor = executor

    def start(self, function: Callable[..., None], request: BoltRequest) -> None:
        self.executor.submit(
            build_runnable_function(
                func=function,
                logger=self.logger,
                request=request,
            )
        )
```

### Ancestors

* [LazyListenerRunner](runner.html#slack_bolt.lazy_listener.runner.LazyListenerRunner "slack_bolt.lazy_listener.runner.LazyListenerRunner")

### Subclasses

* [DjangoThreadLazyListenerRunner](../adapter/django/handler.html#slack_bolt.adapter.django.handler.DjangoThreadLazyListenerRunner "slack_bolt.adapter.django.handler.DjangoThreadLazyListenerRunner")

### Inherited members

* `**[LazyListenerRunner](runner.html#slack_bolt.lazy_listener.runner.LazyListenerRunner "slack_bolt.lazy_listener.runner.LazyListenerRunner")**`:
  * `[logger](runner.html#slack_bolt.lazy_listener.runner.LazyListenerRunner.logger "slack_bolt.lazy_listener.runner.LazyListenerRunner.logger")`
  * `[run](runner.html#slack_bolt.lazy_listener.runner.LazyListenerRunner.run "slack_bolt.lazy_listener.runner.LazyListenerRunner.run")`
  * `[start](runner.html#slack_bolt.lazy_listener.runner.LazyListenerRunner.start "slack_bolt.lazy_listener.runner.LazyListenerRunner.start")`
