Source: https://docs.slack.dev/tools/bolt-python/reference/context/fail

# Module slack_bolt.context.fail

## Sub-modules

`[slack_bolt.context.fail.async_fail](async_fail.html "slack_bolt.context.fail.async_fail")`

`[slack_bolt.context.fail.fail](fail.html "slack_bolt.context.fail.fail")`

## Classes

`class Fail (client: slack_sdk.web.client.WebClient, function_execution_id: str | None)`

Expand source code

```python
class Fail:
    client: WebClient
    function_execution_id: Optional[str]
    _called: bool

    def __init__(
        self,
        client: WebClient,
        function_execution_id: Optional[str],
    ):
        self.client = client
        self.function_execution_id = function_execution_id
        self._called = False

    def __call__(self, error: str) -> SlackResponse:
        """Signal that the custom function failed to complete.

        Kwargs:
            error: Error message to return to slack

        Returns:
            SlackResponse: The response object returned from slack

        Raises:
            ValueError: If this function cannot be used.
        """
        if self.function_execution_id is None:
            raise ValueError("fail is unsupported here as there is no function_execution_id")

        self._called = True
        return self.client.functions_completeError(function_execution_id=self.function_execution_id, error=error)

    def has_been_called(self) -> bool:
        """Check if this fail function has been called.

        Returns:
            bool: True if the fail function has been called, False otherwise.
        """
        return self._called
```

### Class variables

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var function_execution_id : str | None`

The type of the None singleton.

### Methods

`def has_been_called(self) ‑> bool`

Expand source code

```python
def has_been_called(self) -> bool:
    """Check if this fail function has been called.

    Returns:
        bool: True if the fail function has been called, False otherwise.
    """
    return self._called
```

Check if this fail function has been called.

## Returns

`bool`

True if the fail function has been called, False otherwise.
