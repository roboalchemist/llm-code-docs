Source: https://docs.slack.dev/tools/bolt-python/reference/middleware/attaching_function_token

# Module slack_bolt.middleware.attaching_function_token

## Sub-modules

`[slack_bolt.middleware.attaching_function_token.async_attaching_function_token](async_attaching_function_token.html "slack_bolt.middleware.attaching_function_token.async_attaching_function_token")`

`[slack_bolt.middleware.attaching_function_token.attaching_function_token](attaching_function_token.html "slack_bolt.middleware.attaching_function_token.attaching_function_token")`

## Classes

`class AttachingFunctionToken`

Expand source code

```python
class AttachingFunctionToken(Middleware):
    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        # This method is not supposed to be invoked by bolt-python users
        next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        if req.context.function_bot_access_token is not None:
            req.context.client.token = req.context.function_bot_access_token

        return next()
```

A middleware can process request data before other middleware and listener functions.

### Ancestors

* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Inherited members

* `**[Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`
