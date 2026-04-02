Source: https://docs.slack.dev/tools/bolt-python/reference/middleware/url_verification

# Module slack_bolt.middleware.url_verification

## Sub-modules

`[slack_bolt.middleware.url_verification.async_url_verification](async_url_verification.html "slack_bolt.middleware.url_verification.async_url_verification")`

`[slack_bolt.middleware.url_verification.url_verification](url_verification.html "slack_bolt.middleware.url_verification.url_verification")`

## Classes

`class UrlVerification (base_logger: logging.Logger | None = None)`

Expand source code

```python
class UrlVerification(Middleware):
    def __init__(self, base_logger: Optional[Logger] = None):
        """Handles url_verification requests.

        Refer to https://docs.slack.dev/reference/events/url_verification/ for details.

        Args:
            base_logger: The base logger
        """
        self.logger = get_bolt_logger(UrlVerification, base_logger=base_logger)

    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        # As this method is not supposed to be invoked by bolt-python users,
        # the naming conflict with the built-in one affects
        # only the internals of this method
        next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        if self._is_url_verification_request(req.body):
            return self._build_success_response(req.body)
        else:
            return next()

    # -----------------------------------------

    @staticmethod
    def _is_url_verification_request(body: dict) -> bool:
        return body is not None and body.get("type") == "url_verification"

    @staticmethod
    def _build_success_response(body: dict) -> BoltResponse:
        return BoltResponse(status=200, body={"challenge": body.get("challenge")})
```

A middleware can process request data before other middleware and listener functions.

Handles url\_verification requests.

Refer to [https://docs.slack.dev/reference/events/url\_verification/](https://docs.slack.dev/reference/events/url_verification/) for details.

## Args

## `base_logger`

The base logger

### Ancestors

* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [AsyncUrlVerification](async_url_verification.html#slack_bolt.middleware.url_verification.async_url_verification.AsyncUrlVerification "slack_bolt.middleware.url_verification.async_url_verification.AsyncUrlVerification")

### Inherited members

* `**[Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`
