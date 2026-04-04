Source: https://docs.slack.dev/tools/bolt-python/reference/middleware/authorization

# Module slack_bolt.middleware.authorization

## Sub-modules

`[slack_bolt.middleware.authorization.async_authorization](async_authorization.html "slack_bolt.middleware.authorization.async_authorization")`

`[slack_bolt.middleware.authorization.async_internals](async_internals.html "slack_bolt.middleware.authorization.async_internals")`

`[slack_bolt.middleware.authorization.async_multi_teams_authorization](async_multi_teams_authorization.html "slack_bolt.middleware.authorization.async_multi_teams_authorization")`

`[slack_bolt.middleware.authorization.async_single_team_authorization](async_single_team_authorization.html "slack_bolt.middleware.authorization.async_single_team_authorization")`

`[slack_bolt.middleware.authorization.authorization](authorization.html "slack_bolt.middleware.authorization.authorization")`

`[slack_bolt.middleware.authorization.internals](internals.html "slack_bolt.middleware.authorization.internals")`

`[slack_bolt.middleware.authorization.multi_teams_authorization](multi_teams_authorization.html "slack_bolt.middleware.authorization.multi_teams_authorization")`

`[slack_bolt.middleware.authorization.single_team_authorization](single_team_authorization.html "slack_bolt.middleware.authorization.single_team_authorization")`

## Classes

`class Authorization`

Expand source code

```python
class Authorization(Middleware):
    pass
```

A middleware can process request data before other middleware and listener functions.

### Ancestors

* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Subclasses

* [MultiTeamsAuthorization](multi_teams_authorization.html#slack_bolt.middleware.authorization.multi_teams_authorization.MultiTeamsAuthorization "slack_bolt.middleware.authorization.multi_teams_authorization.MultiTeamsAuthorization")
* [SingleTeamAuthorization](single_team_authorization.html#slack_bolt.middleware.authorization.single_team_authorization.SingleTeamAuthorization "slack_bolt.middleware.authorization.single_team_authorization.SingleTeamAuthorization")

### Inherited members

* `**[Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

`class MultiTeamsAuthorization (*,   authorize: [Authorize](../../authorization/authorize.html#slack_bolt.authorization.authorize.Authorize "slack_bolt.authorization.authorize.Authorize"),   base_logger: logging.Logger | None = None,   user_token_resolution: str = 'authed_user',   user_facing_authorize_error_message: str | None = None)`

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

* [Authorization](authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")
* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Class variables

`var authorize : [Authorize](../../authorization/authorize.html#slack_bolt.authorization.authorize.Authorize "slack_bolt.authorization.authorize.Authorize")`

The type of the None singleton.

`var user_token_resolution : str`

The type of the None singleton.

### Inherited members

* `**[Authorization](authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.authorization.authorization.Authorization.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.authorization.authorization.Authorization.process")`

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

* [Authorization](authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")
* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Inherited members

* `**[Authorization](authorization.html#slack_bolt.middleware.authorization.authorization.Authorization "slack_bolt.middleware.authorization.authorization.Authorization")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.authorization.authorization.Authorization.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.authorization.authorization.Authorization.process")`
