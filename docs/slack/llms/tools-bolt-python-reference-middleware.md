Source: https://docs.slack.dev/tools/bolt-python/reference/middleware

# Module slack_bolt.middleware

A middleware processes request data and calls `next()` method if the execution chain should continue running the following middleware.

Middleware can be used globally before all listener executions. It's also possible to run a middleware only for a particular listener.

## Sub-modules

`[slack_bolt.middleware.assistant](assistant/index.html "slack_bolt.middleware.assistant")`

`[slack_bolt.middleware.async_builtins](async_builtins.html "slack_bolt.middleware.async_builtins")`

`[slack_bolt.middleware.async_custom_middleware](async_custom_middleware.html "slack_bolt.middleware.async_custom_middleware")`

`[slack_bolt.middleware.async_middleware](async_middleware.html "slack_bolt.middleware.async_middleware")`

`[slack_bolt.middleware.async_middleware_error_handler](async_middleware_error_handler.html "slack_bolt.middleware.async_middleware_error_handler")`

`[slack_bolt.middleware.attaching_function_token](attaching_function_token/index.html "slack_bolt.middleware.attaching_function_token")`

`[slack_bolt.middleware.authorization](authorization/index.html "slack_bolt.middleware.authorization")`

`[slack_bolt.middleware.custom_middleware](custom_middleware.html "slack_bolt.middleware.custom_middleware")`

`[slack_bolt.middleware.ignoring_self_events](ignoring_self_events/index.html "slack_bolt.middleware.ignoring_self_events")`

`[slack_bolt.middleware.message_listener_matches](message_listener_matches/index.html "slack_bolt.middleware.message_listener_matches")`

`[slack_bolt.middleware.middleware](middleware.html "slack_bolt.middleware.middleware")`

`[slack_bolt.middleware.middleware_error_handler](middleware_error_handler.html "slack_bolt.middleware.middleware_error_handler")`

`[slack_bolt.middleware.request_verification](request_verification/index.html "slack_bolt.middleware.request_verification")`

`[slack_bolt.middleware.ssl_check](ssl_check/index.html "slack_bolt.middleware.ssl_check")`

`[slack_bolt.middleware.url_verification](url_verification/index.html "slack_bolt.middleware.url_verification")`

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

* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Inherited members

* `**[Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

`class CustomMiddleware (*, app_name: str, func: Callable, base_logger: logging.Logger | None = None)`

Expand source code

```python
class CustomMiddleware(Middleware):
    app_name: str
    func: Callable[..., Any]
    arg_names: MutableSequence[str]
    logger: Logger

    def __init__(self, *, app_name: str, func: Callable, base_logger: Optional[Logger] = None):
        self.app_name = app_name
        self.func = func
        self.arg_names = get_arg_names_of_callable(func)
        self.logger = get_bolt_app_logger(self.app_name, self.func, base_logger)

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
        return self.func(
            **build_required_kwargs(
                logger=self.logger,
                required_arg_names=self.arg_names,
                request=req,
                response=resp,
                next_func=next,  # type: ignore[arg-type]
                this_func=self.func,
            )
        )

    @property
    def name(self) -> str:
        return f"CustomMiddleware(func={get_name_for_callable(self.func)})"
```

A middleware can process request data before other middleware and listener functions.

### Ancestors

* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Class variables

`var app_name : str`

The type of the None singleton.

`var arg_names : MutableSequence[str]`

The type of the None singleton.

`var func : Callable[..., Any]`

The type of the None singleton.

`var logger : logging.Logger`

The type of the None singleton.

### Inherited members

* `**[Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

`class IgnoringSelfEvents (base_logger: logging.Logger | None = None,   ignoring_self_assistant_message_events_enabled: bool = True)`

Expand source code

```python
class IgnoringSelfEvents(Middleware):
    def __init__(
        self,
        base_logger: Optional[logging.Logger] = None,
        ignoring_self_assistant_message_events_enabled: bool = True,
    ):
        """Ignores the events generated by this bot user itself."""
        self.logger = get_bolt_logger(IgnoringSelfEvents, base_logger=base_logger)
        self.ignoring_self_assistant_message_events_enabled = ignoring_self_assistant_message_events_enabled

    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        auth_result = req.context.authorize_result
        # message events can have $.event.bot_id while it does not have its user_id
        bot_id = req.body.get("event", {}).get("bot_id")
        if self._is_self_event(auth_result, req.context.user_id, bot_id, req.body):  # type: ignore[arg-type]
            if self.ignoring_self_assistant_message_events_enabled is False:
                if is_bot_message_event_in_assistant_thread(req.body):
                    # Assistant#bot_message handler acknowledges this pattern
                    return next()

            self._debug_log(req.body)
            return req.context.ack()
        else:
            return next()

    # -----------------------------------------

    # It's an Events API event that isn't of type message,
    # but the user ID might match our own app. Filter these out.
    # However, some events still must be fired, because they can make sense.
    events_that_should_be_kept = ["member_joined_channel", "member_left_channel"]

    @classmethod
    def _is_self_event(
        cls,
        auth_result: AuthorizeResult,
        user_id: Optional[str],
        bot_id: Optional[str],
        body: Dict[str, Any],
    ):
        return (
            auth_result is not None
            and (
                (user_id is not None and user_id == auth_result.bot_user_id)
                or (bot_id is not None and bot_id == auth_result.bot_id)  # for bot_message events
            )
            and body.get("event") is not None
            and body.get("event", {}).get("type") not in cls.events_that_should_be_kept
        )

    def _debug_log(self, body: dict):
        if self.logger.level <= logging.DEBUG:
            event = body.get("event")
            self.logger.debug(f"Skipped self event: {event}")
```

A middleware can process request data before other middleware and listener functions.

Ignores the events generated by this bot user itself.

### Ancestors

* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [AsyncIgnoringSelfEvents](ignoring_self_events/async_ignoring_self_events.html#slack_bolt.middleware.ignoring_self_events.async_ignoring_self_events.AsyncIgnoringSelfEvents "slack_bolt.middleware.ignoring_self_events.async_ignoring_self_events.AsyncIgnoringSelfEvents")

### Class variables

`var events_that_should_be_kept`

The type of the None singleton.

### Inherited members

* `**[Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

`class Middleware`

Expand source code

```python
class Middleware(metaclass=ABCMeta):
    """A middleware can process request data before other middleware and listener functions."""

    @abstractmethod
    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        # As this method is not supposed to be invoked by bolt-python users,
        # the naming conflict with the built-in one affects
        # only the internals of this method
        next: Callable[[], BoltResponse],
    ) -> Optional[BoltResponse]:
        """Processes a request data before other middleware and listeners.
        A middleware calls `next()` function if the chain should continue.

            @app.middleware
            def simple_middleware(req, resp, next):
                # do something here
                next()

        This `process(req, resp, next)` method is supposed to be invoked only inside bolt-python.
        If you want to avoid the name `next()` in your middleware functions, you can use `next_()` method instead.

            @app.middleware
            def simple_middleware(req, resp, next_):
                # do something here
                next_()

        Args:
            req: The incoming request
            resp: The response
            next: The function to tell the chain that it can continue

        Returns:
            Processed response (optional)
        """
        raise NotImplementedError()

    @property
    def name(self) -> str:
        """The name of this middleware"""
        return f"{self.__module__}.{self.__class__.__name__}"
```

A middleware can process request data before other middleware and listener functions.

### Subclasses

* [Assistant](assistant/assistant.html#slack_bolt.middleware.assistant.assistant.Assistant "slack_bolt.middleware.assistant.assistant.Assistant")
* [AttachingFunctionToken](attaching_function_token/attaching_function_token.html#slack_bolt.middleware.attaching_function_token.attaching_function_token.AttachingFunctionToken "slack_bolt.middleware.attaching_function_token.attaching_function_token.AttachingFunctionToken")
* [Authorization](authorization/authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")
* [CustomMiddleware](custom_middleware.html#slack_bolt.middleware.custom_middleware.CustomMiddleware "slack_bolt.middleware.custom_middleware.CustomMiddleware")
* [IgnoringSelfEvents](ignoring_self_events/ignoring_self_events.html#slack_bolt.middleware.ignoring_self_events.ignoring_self_events.IgnoringSelfEvents "slack_bolt.middleware.ignoring_self_events.ignoring_self_events.IgnoringSelfEvents")
* [MessageListenerMatches](message_listener_matches/message_listener_matches.html#slack_bolt.middleware.message_listener_matches.message_listener_matches.MessageListenerMatches "slack_bolt.middleware.message_listener_matches.message_listener_matches.MessageListenerMatches")
* [RequestVerification](request_verification/request_verification.html#slack_bolt.middleware.request_verification.request_verification.RequestVerification "slack_bolt.middleware.request_verification.request_verification.RequestVerification")
* [SslCheck](ssl_check/ssl_check.html#slack_bolt.middleware.ssl_check.ssl_check.SslCheck "slack_bolt.middleware.ssl_check.ssl_check.SslCheck")
* [UrlVerification](url_verification/url_verification.html#slack_bolt.middleware.url_verification.url_verification.UrlVerification "slack_bolt.middleware.url_verification.url_verification.UrlVerification")
* [WorkflowStepMiddleware](../workflows/step/step_middleware.html#slack_bolt.workflows.step.step_middleware.WorkflowStepMiddleware "slack_bolt.workflows.step.step_middleware.WorkflowStepMiddleware")

### Instance variables

`prop name : str`

Expand source code

```text
@property
def name(self) -> str:
    """The name of this middleware"""
    return f"{self.__module__}.{self.__class__.__name__}"
```

The name of this middleware

### Methods

`def process(self,   *,   req: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse"),   next: Callable[[], [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")]) ‑> [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None`

Expand source code

```text
@abstractmethod
def process(
    self,
    *,
    req: BoltRequest,
    resp: BoltResponse,
    # As this method is not supposed to be invoked by bolt-python users,
    # the naming conflict with the built-in one affects
    # only the internals of this method
    next: Callable[[], BoltResponse],
) -> Optional[BoltResponse]:
    """Processes a request data before other middleware and listeners.
    A middleware calls `next()` function if the chain should continue.

        @app.middleware
        def simple_middleware(req, resp, next):
            # do something here
            next()

    This `process(req, resp, next)` method is supposed to be invoked only inside bolt-python.
    If you want to avoid the name `next()` in your middleware functions, you can use `next_()` method instead.

        @app.middleware
        def simple_middleware(req, resp, next_):
            # do something here
            next_()

    Args:
        req: The incoming request
        resp: The response
        next: The function to tell the chain that it can continue

    Returns:
        Processed response (optional)
    """
    raise NotImplementedError()
```

Processes a request data before other middleware and listeners. A middleware calls `next()` function if the chain should continue.

```text
@app.middleware
def simple_middleware(req, resp, next):
    # do something here
    next()
```

This `process(req, resp, next)` method is supposed to be invoked only inside bolt-python. If you want to avoid the name `next()` in your middleware functions, you can use `next_()` method instead.

```text
@app.middleware
def simple_middleware(req, resp, next_):
    # do something here
    next_()
```

## Args

## `req`

The incoming request

## `resp`

The response

## `next`

The function to tell the chain that it can continue

## Returns

Processed response (optional)

`class MultiTeamsAuthorization (*,   authorize: [Authorize](../authorization/authorize.html#slack_bolt.authorization.authorize.Authorize "slack_bolt.authorization.authorize.Authorize"),   base_logger: logging.Logger | None = None,   user_token_resolution: str = 'authed_user',   user_facing_authorize_error_message: str | None = None)`

Expand source code

```python
class MultiTeamsAuthorization(Authorization):
    authorize: Authorize
    user_token_resolution: str

    def __init__(
        self,
        *,
        authorize: Authorize,
        base_logger: Optional[Logger] = None,
        user_token_resolution: str = "authed_user",
        user_facing_authorize_error_message: Optional[str] = None,
    ):
        """Multi-workspace authorization.

        Args:
            authorize: The function to authorize incoming requests from Slack.
            base_logger: The base logger
            user_token_resolution: "authed_user" or "actor"
            user_facing_authorize_error_message: The user-facing error message when installation is not found
        """
        self.authorize = authorize
        self.logger = get_bolt_logger(MultiTeamsAuthorization, base_logger=base_logger)
        self.user_token_resolution = user_token_resolution
        self.user_facing_authorize_error_message = (
            user_facing_authorize_error_message or _build_user_facing_authorize_error_message()
        )

    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        if _is_no_auth_required(req):
            return next()

        if _is_no_auth_test_call_required(req):
            req.context.set_authorize_result(
                AuthorizeResult(
                    enterprise_id=req.context.enterprise_id,
                    team_id=req.context.team_id,
                    user_id=req.context.user_id,
                )
            )
            return next()

        try:
            auth_result: Optional[AuthorizeResult] = None
            if self.user_token_resolution == "actor":
                auth_result = self.authorize(
                    context=req.context,
                    enterprise_id=req.context.enterprise_id,
                    team_id=req.context.team_id,
                    user_id=req.context.user_id,
                    actor_enterprise_id=req.context.actor_enterprise_id,
                    actor_team_id=req.context.actor_team_id,
                    actor_user_id=req.context.actor_user_id,
                )
            else:
                auth_result = self.authorize(
                    context=req.context,
                    enterprise_id=req.context.enterprise_id,
                    team_id=req.context.team_id,
                    user_id=req.context.user_id,
                )
            if auth_result is not None:
                req.context.set_authorize_result(auth_result)
                token = auth_result.bot_token or auth_result.user_token
                req.context["token"] = token
                # As App#_init_context() generates a new WebClient for this request,
                # it's safe to modify this instance.
                req.context.client.token = token
                return next()
            else:
                # This situation can arise if:
                # * A developer installed the app from the "Install to Workspace" button in Slack app config page
                # * The InstallationStore failed to save or deleted the installation for this workspace
                self.logger.error(
                    "Although the app should be installed into this workspace, "
                    "the AuthorizeResult (returned value from authorize) for it was not found."
                )
                if req.context.response_url is not None:
                    req.context.respond(self.user_facing_authorize_error_message)  # type: ignore[misc]
                    return BoltResponse(status=200, body="")
                return _build_user_facing_error_response(self.user_facing_authorize_error_message)

        except SlackApiError as e:
            self.logger.error(f"Failed to authorize with the given token ({e})")
            return _build_user_facing_error_response(self.user_facing_authorize_error_message)
```

A middleware can process request data before other middleware and listener functions.

Multi-workspace authorization.

## Args

## `authorize`

The function to authorize incoming requests from Slack.

## `base_logger`

The base logger

## `user_token_resolution`

"authed\_user" or "actor"

## `user_facing_authorize_error_message`

The user-facing error message when installation is not found

### Ancestors

* [Authorization](authorization/authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")
* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Class variables

`var authorize : [Authorize](../authorization/authorize.html#slack_bolt.authorization.authorize.Authorize "slack_bolt.authorization.authorize.Authorize")`

The type of the None singleton.

`var user_token_resolution : str`

The type of the None singleton.

### Inherited members

* `**[Authorization](authorization/authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.authorization.authorization.Authorization.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.authorization.authorization.Authorization.process")`

`class RequestVerification (signing_secret: str, base_logger: logging.Logger | None = None)`

Expand source code

```python
class RequestVerification(Middleware):
    def __init__(self, signing_secret: str, base_logger: Optional[Logger] = None):
        """Verifies an incoming request by checking the validity of
        `x-slack-signature`, `x-slack-request-timestamp`, and its body data.

        Refer to https://docs.slack.dev/authentication/verifying-requests-from-slack/ for details.

        Args:
            signing_secret: The signing secret
            base_logger: The base logger
        """
        self.verifier = SignatureVerifier(signing_secret=signing_secret)
        self.logger = get_bolt_logger(RequestVerification, base_logger=base_logger)

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
        if self._can_skip(req.mode, req.body):
            return next()

        body = req.raw_body
        timestamp = req.headers.get("x-slack-request-timestamp", ["0"])[0]
        signature = req.headers.get("x-slack-signature", [""])[0]
        if self.verifier.is_valid(body, timestamp, signature):
            return next()
        else:
            self._debug_log_error(signature, timestamp, body)
            return self._build_error_response()

    # -----------------------------------------

    @staticmethod
    def _can_skip(mode: str, body: Dict[str, Any]) -> bool:
        return mode == "socket_mode" or (body is not None and body.get("ssl_check") == "1")

    @staticmethod
    def _build_error_response() -> BoltResponse:
        return BoltResponse(status=401, body={"error": "invalid request"})

    def _debug_log_error(self, signature, timestamp, body) -> None:
        self.logger.info(
            "Invalid request signature detected " f"(signature: {signature}, timestamp: {timestamp}, body: {body})"
        )
```

A middleware can process request data before other middleware and listener functions.

Verifies an incoming request by checking the validity of `x-slack-signature`, `x-slack-request-timestamp`, and its body data.

Refer to [https://docs.slack.dev/authentication/verifying-requests-from-slack/](https://docs.slack.dev/authentication/verifying-requests-from-slack/) for details.

## Args

## `signing_secret`

The signing secret

## `base_logger`

The base logger

### Ancestors

* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [AsyncRequestVerification](request_verification/async_request_verification.html#slack_bolt.middleware.request_verification.async_request_verification.AsyncRequestVerification "slack_bolt.middleware.request_verification.async_request_verification.AsyncRequestVerification")

### Inherited members

* `**[Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

`class SingleTeamAuthorization (*,   auth_test_result: slack_sdk.web.slack_response.SlackResponse | None = None,   base_logger: logging.Logger | None = None,   user_facing_authorize_error_message: str | None = None)`

Expand source code

```python
class SingleTeamAuthorization(Authorization):
    def __init__(
        self,
        *,
        auth_test_result: Optional[SlackResponse] = None,
        base_logger: Optional[Logger] = None,
        user_facing_authorize_error_message: Optional[str] = None,
    ):
        """Single-workspace authorization.

        Args:
            auth_test_result: The initial `auth.test` API call result.
            base_logger: The base logger
        """
        self.auth_test_result = auth_test_result
        self.logger = get_bolt_logger(SingleTeamAuthorization, base_logger=base_logger)
        self.user_facing_authorize_error_message = (
            user_facing_authorize_error_message or _build_user_facing_authorize_error_message()
        )

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

        if _is_no_auth_required(req):
            return next()

        if _is_no_auth_test_call_required(req):
            req.context.set_authorize_result(
                AuthorizeResult(
                    enterprise_id=req.context.enterprise_id,
                    team_id=req.context.team_id,
                    user_id=req.context.user_id,
                )
            )
            return next()

        try:
            if not self.auth_test_result:
                self.auth_test_result = req.context.client.auth_test()

            if self.auth_test_result:
                req.context.set_authorize_result(
                    _to_authorize_result(
                        auth_test_result=self.auth_test_result,
                        token=req.context.client.token,
                        request_user_id=req.context.user_id,
                    )
                )
                return next()
            else:
                # Just in case
                self.logger.error("auth.test API call result is unexpectedly None")
                if req.context.response_url is not None:
                    req.context.respond(self.user_facing_authorize_error_message)  # type: ignore[misc]
                    return BoltResponse(status=200, body="")
                return _build_user_facing_error_response(self.user_facing_authorize_error_message)
        except SlackApiError as e:
            self.logger.error(f"Failed to authorize with the given token ({e})")
            return _build_user_facing_error_response(self.user_facing_authorize_error_message)
```

A middleware can process request data before other middleware and listener functions.

Single-workspace authorization.

## Args

## `auth_test_result`

The initial `auth.test` API call result.

## `base_logger`

The base logger

### Ancestors

* [Authorization](authorization/authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")
* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Inherited members

* `**[Authorization](authorization/authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.authorization.authorization.Authorization.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.authorization.authorization.Authorization.process")`

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

Handles `[slack_bolt.middleware.ssl_check](ssl_check/index.html "slack_bolt.middleware.ssl_check")` requests. Refer to [https://docs.slack.dev/interactivity/implementing-slash-commands/](https://docs.slack.dev/interactivity/implementing-slash-commands/) for details.

## Args

## `verification_token`

The verification token to check (optional as it's already deprecated - [https://docs.slack.dev/authentication/verifying-requests-from-slack/#deprecation](https://docs.slack.dev/authentication/verifying-requests-from-slack/#deprecation))

## `base_logger`

The base logger

### Ancestors

* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [AsyncSslCheck](ssl_check/async_ssl_check.html#slack_bolt.middleware.ssl_check.async_ssl_check.AsyncSslCheck "slack_bolt.middleware.ssl_check.async_ssl_check.AsyncSslCheck")

### Class variables

`var logger : logging.Logger`

The type of the None singleton.

`var verification_token : str | None`

The type of the None singleton.

### Inherited members

* `**[Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

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

* [Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [AsyncUrlVerification](url_verification/async_url_verification.html#slack_bolt.middleware.url_verification.async_url_verification.AsyncUrlVerification "slack_bolt.middleware.url_verification.async_url_verification.AsyncUrlVerification")

### Inherited members

* `**[Middleware](middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`
