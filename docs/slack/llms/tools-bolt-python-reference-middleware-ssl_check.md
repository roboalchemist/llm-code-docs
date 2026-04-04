Source: https://docs.slack.dev/tools/bolt-python/reference/middleware/ssl_check

# Module slack_bolt.middleware.ssl_check

## Sub-modules

`[slack_bolt.middleware.ssl_check.async_ssl_check](async_ssl_check.html "slack_bolt.middleware.ssl_check.async_ssl_check")`

`[slack_bolt.middleware.ssl_check.ssl_check](ssl_check.html "slack_bolt.middleware.ssl_check.ssl_check")`

## Classes

`class SslCheck (verification_token: str | None = None,   base_logger: logging.Logger | None = None)`

Expand source code

```python
class SslCheck(Middleware):
    verification_token: Optional[str]
    logger: Logger

    def __init__(
        self,
        verification_token: Optional[str] = None,
        base_logger: Optional[Logger] = None,
    ):
        """Handles `ssl_check` requests.
        Refer to https://docs.slack.dev/interactivity/implementing-slash-commands/ for details.

        Args:
            verification_token: The verification token to check
                (optional as it's already deprecated - https://docs.slack.dev/authentication/verifying-requests-from-slack/#deprecation)
            base_logger: The base logger
        """  # noqa: E501
        self.verification_token = verification_token
        self.logger = get_bolt_logger(SslCheck, base_logger=base_logger)

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
        if self._is_ssl_check_request(req.body):
            if self._verify_token_if_needed(req.body):
                return self._build_error_response()
            return self._build_success_response()
        else:
            return next()

    # -----------------------------------------

    @staticmethod
    def _is_ssl_check_request(body: dict):
        return "ssl_check" in body and body["ssl_check"] == "1"

    def _verify_token_if_needed(self, body: dict):
        return self.verification_token and self.verification_token == body["token"]

    @staticmethod
    def _build_success_response() -> BoltResponse:
        return BoltResponse(status=200, body="")

    @staticmethod
    def _build_error_response() -> BoltResponse:
        return BoltResponse(status=401, body={"error": "invalid verification token"})
```

A middleware can process request data before other middleware and listener functions.

Handles `[slack_bolt.middleware.ssl_check.ssl_check](ssl_check.html "slack_bolt.middleware.ssl_check.ssl_check")` requests. Refer to [https://docs.slack.dev/interactivity/implementing-slash-commands/](https://docs.slack.dev/interactivity/implementing-slash-commands/) for details.

## Args

## `verification_token`

The verification token to check (optional as it's already deprecated - [https://docs.slack.dev/authentication/verifying-requests-from-slack/#deprecation](https://docs.slack.dev/authentication/verifying-requests-from-slack/#deprecation))

## `base_logger`

The base logger

### Ancestors

* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [AsyncSslCheck](async_ssl_check.html#slack_bolt.middleware.ssl_check.async_ssl_check.AsyncSslCheck "slack_bolt.middleware.ssl_check.async_ssl_check.AsyncSslCheck")

### Class variables

`var logger : logging.Logger`

The type of the None singleton.

`var verification_token : str | None`

The type of the None singleton.

### Inherited members

* `**[Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`
