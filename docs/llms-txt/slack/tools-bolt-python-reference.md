Source: https://docs.slack.dev/tools/bolt-python/reference

# Package slack_bolt

A Python framework to build Slack apps in a flash with the latest platform features.Read the [getting started guide](https://docs.slack.dev/tools/bolt-python/building-an-app) and look at our [code examples](https://github.com/slackapi/bolt-python/tree/main/examples) to learn how to build apps using Bolt.

* Website: [https://docs.slack.dev/tools/bolt-python/](https://docs.slack.dev/tools/bolt-python/)
* GitHub repository: [https://github.com/slackapi/bolt-python](https://github.com/slackapi/bolt-python)
* The class representing a Bolt app: `[slack_bolt.app.app](app/app.html "slack_bolt.app.app")`

## Sub-modules

`[slack_bolt.adapter](adapter/index.html "slack_bolt.adapter")`

Adapter modules for running Bolt apps along with Web frameworks or Socket Mode.

`[slack_bolt.app](app/index.html "slack_bolt.app")`

Application interface in Bolt …

`[slack_bolt.async_app](async_app.html "slack_bolt.async_app")`

Module for creating asyncio based apps …

`[slack_bolt.authorization](authorization/index.html "slack_bolt.authorization")`

Authorization is the process of determining which Slack credentials should be available while processing an incoming Slack event …

`[slack_bolt.context](context/index.html "slack_bolt.context")`

All listeners have access to a context dictionary, which can be used to enrich events with additional information. Bolt automatically attaches …

`[slack_bolt.error](error/index.html "slack_bolt.error")`

Bolt specific error types.

`[slack_bolt.kwargs_injection](kwargs_injection/index.html "slack_bolt.kwargs_injection")`

For middleware/listener arguments, Bolt does flexible data injection in accordance with their names …

`[slack_bolt.lazy_listener](lazy_listener/index.html "slack_bolt.lazy_listener")`

Lazy listener runner is a beta feature for the apps running on Function-as-a-Service platforms …

`[slack_bolt.listener](listener/index.html "slack_bolt.listener")`

Listeners process an incoming request from Slack if the request's type or data structure matches the predefined conditions of the listener. Typically, …

`[slack_bolt.listener_matcher](listener_matcher/index.html "slack_bolt.listener_matcher")`

A listener matcher is a simplified version of listener middleware. A listener matcher function returns bool value instead of `next()` method …

`[slack_bolt.logger](logger/index.html "slack_bolt.logger")`

Bolt for Python relies on the standard `logging` module.

`[slack_bolt.middleware](middleware/index.html "slack_bolt.middleware")`

A middleware processes request data and calls `next()` method if the execution chain should continue running the following middleware …

`[slack_bolt.oauth](oauth/index.html "slack_bolt.oauth")`

Slack OAuth flow support for building an app that is installable in any workspaces …

`[slack_bolt.request](request/index.html "slack_bolt.request")`

Incoming request from Slack through either HTTP request or Socket Mode connection …

`[slack_bolt.response](response/index.html "slack_bolt.response")`

This interface represents Bolt's synchronous response to Slack …

`[slack_bolt.util](util/index.html "slack_bolt.util")`

Internal utilities for the Bolt framework.

`[slack_bolt.version](version.html "slack_bolt.version")`

Check the latest version at [https://pypi.org/project/slack-bolt/](https://pypi.org/project/slack-bolt/)

`[slack_bolt.workflows](workflows/index.html "slack_bolt.workflows")`

Steps from apps enables developers to build their own steps …

## Classes

`class Ack`

Expand source code

```python
class Ack:
    response: Optional[BoltResponse]

    def __init__(self):
        self.response: Optional[BoltResponse] = None

    def __call__(
        self,
        text: Union[str, dict] = "",  # text: str or whole_response: dict
        blocks: Optional[Sequence[Union[dict, Block]]] = None,
        attachments: Optional[Sequence[Union[dict, Attachment]]] = None,
        unfurl_links: Optional[bool] = None,
        unfurl_media: Optional[bool] = None,
        response_type: Optional[str] = None,  # in_channel / ephemeral
        # block_suggestion / dialog_suggestion
        options: Optional[Sequence[Union[dict, Option]]] = None,
        option_groups: Optional[Sequence[Union[dict, OptionGroup]]] = None,
        # view_submission
        response_action: Optional[str] = None,  # errors / update / push / clear
        errors: Optional[Dict[str, str]] = None,
        view: Optional[Union[dict, View]] = None,
    ) -> BoltResponse:
        return _set_response(
            self,
            text_or_whole_response=text,
            blocks=blocks,
            attachments=attachments,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            response_type=response_type,
            options=options,
            option_groups=option_groups,
            response_action=response_action,
            errors=errors,
            view=view,
        )
```

### Class variables

`var response : [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None`

The type of the None singleton.

`class App (*,   logger: logging.Logger | None = None,   name: str | None = None,   process_before_response: bool = False,   raise_error_for_unhandled_request: bool = False,   signing_secret: str | None = None,   token: str | None = None,   token_verification_enabled: bool = True,   client: slack_sdk.web.client.WebClient | None = None,   before_authorize: [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware") | Callable[..., Any] | None = None,   authorize: Callable[..., [AuthorizeResult](authorization/authorize_result.html#slack_bolt.authorization.authorize_result.AuthorizeResult "slack_bolt.authorization.authorize_result.AuthorizeResult")] | None = None,   user_facing_authorize_error_message: str | None = None,   installation_store: slack_sdk.oauth.installation_store.installation_store.InstallationStore | None = None,   installation_store_bot_only: bool | None = None,   request_verification_enabled: bool = True,   ignoring_self_events_enabled: bool = True,   ignoring_self_assistant_message_events_enabled: bool = True,   ssl_check_enabled: bool = True,   url_verification_enabled: bool = True,   attaching_function_token_enabled: bool = True,   oauth_settings: [OAuthSettings](oauth/oauth_settings.html#slack_bolt.oauth.oauth_settings.OAuthSettings "slack_bolt.oauth.oauth_settings.OAuthSettings") | None = None,   oauth_flow: [OAuthFlow](oauth/oauth_flow.html#slack_bolt.oauth.oauth_flow.OAuthFlow "slack_bolt.oauth.oauth_flow.OAuthFlow") | None = None,   verification_token: str | None = None,   listener_executor: concurrent.futures._base.Executor | None = None,   assistant_thread_context_store: [AssistantThreadContextStore](context/assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore") | None = None)`

Expand source code

```python
class App:
    def __init__(
        self,
        *,
        logger: Optional[logging.Logger] = None,
        # Used in logger
        name: Optional[str] = None,
        # Set True when you run this app on a FaaS platform
        process_before_response: bool = False,
        # Set True if you want to handle an unhandled request as an exception
        raise_error_for_unhandled_request: bool = False,
        # Basic Information > Credentials > Signing Secret
        signing_secret: Optional[str] = None,
        # for single-workspace apps
        token: Optional[str] = None,
        token_verification_enabled: bool = True,
        client: Optional[WebClient] = None,
        # for multi-workspace apps
        before_authorize: Optional[Union[Middleware, Callable[..., Any]]] = None,
        authorize: Optional[Callable[..., AuthorizeResult]] = None,
        user_facing_authorize_error_message: Optional[str] = None,
        installation_store: Optional[InstallationStore] = None,
        # for either only bot scope usage or v1.0.x compatibility
        installation_store_bot_only: Optional[bool] = None,
        # for customizing the built-in middleware
        request_verification_enabled: bool = True,
        ignoring_self_events_enabled: bool = True,
        ignoring_self_assistant_message_events_enabled: bool = True,
        ssl_check_enabled: bool = True,
        url_verification_enabled: bool = True,
        attaching_function_token_enabled: bool = True,
        # for the OAuth flow
        oauth_settings: Optional[OAuthSettings] = None,
        oauth_flow: Optional[OAuthFlow] = None,
        # No need to set (the value is used only in response to ssl_check requests)
        verification_token: Optional[str] = None,
        # Set this one only when you want to customize the executor
        listener_executor: Optional[Executor] = None,
        # for AI Agents & Assistants
        assistant_thread_context_store: Optional[AssistantThreadContextStore] = None,
    ):
        """Bolt App that provides functionalities to register middleware/listeners.

            import os
            from slack_bolt import App

            # Initializes your app with your bot token and signing secret
            app = App(
                token=os.environ.get("SLACK_BOT_TOKEN"),
                signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
            )

            # Listens to incoming messages that contain "hello"
            @app.message("hello")
            def message_hello(message, say):
                # say() sends a message to the channel where the event was triggered
                say(f"Hey there <@{message['user']}>!")

            # Start your app
            if __name__ == "__main__":
                app.start(port=int(os.environ.get("PORT", 3000)))

        Refer to https://docs.slack.dev/tools/bolt-python/building-an-app for details.

        If you would like to build an OAuth app for enabling the app to run with multiple workspaces,
        refer to https://docs.slack.dev/tools/bolt-python/concepts/authenticating-oauth to learn how to configure the app.

        Args:
            logger: The custom logger that can be used in this app.
            name: The application name that will be used in logging. If absent, the source file name will be used.
            process_before_response: True if this app runs on Function as a Service. (Default: False)
            raise_error_for_unhandled_request: True if you want to raise exceptions for unhandled requests
                and use @app.error listeners instead of
                the built-in handler, which pints warning logs and returns 404 to Slack (Default: False)
            signing_secret: The Signing Secret value used for verifying requests from Slack.
            token: The bot/user access token required only for single-workspace app.
            token_verification_enabled: Verifies the validity of the given token if True.
            client: The singleton `slack_sdk.WebClient` instance for this app.
            before_authorize: A global middleware that can be executed right before authorize function
            authorize: The function to authorize an incoming request from Slack
                by checking if there is a team/user in the installation data.
            user_facing_authorize_error_message: The user-facing error message to display
                when the app is installed but the installation is not managed by this app's installation store
            installation_store: The module offering save/find operations of installation data
            installation_store_bot_only: Use `InstallationStore#find_bot()` if True (Default: False)
            request_verification_enabled: False if you would like to disable the built-in middleware (Default: True).
                `RequestVerification` is a built-in middleware that verifies the signature in HTTP Mode requests.
                Make sure if it's safe enough when you turn a built-in middleware off.
                We strongly recommend using RequestVerification for better security.
                If you have a proxy that verifies request signature in front of the Bolt app,
                it's totally fine to disable RequestVerification to avoid duplication of work.
                Don't turn it off just for easiness of development.
            ignoring_self_events_enabled: False if you would like to disable the built-in middleware (Default: True).
                `IgnoringSelfEvents` is a built-in middleware that enables Bolt apps to easily skip the events
                generated by this app's bot user (this is useful for avoiding code error causing an infinite loop).
            ignoring_self_assistant_message_events_enabled: False if you would like to disable the built-in middleware.
                `IgnoringSelfEvents` for this app's bot user message events within an assistant thread
                This is useful for avoiding code error causing an infinite loop; Default: True
            url_verification_enabled: False if you would like to disable the built-in middleware (Default: True).
                `UrlVerification` is a built-in middleware that handles url_verification requests
                that verify the endpoint for Events API in HTTP Mode requests.
            attaching_function_token_enabled: False if you would like to disable the built-in middleware (Default: True).
                `AttachingFunctionToken` is a built-in middleware that injects the just-in-time workflow-execution tokens
                when your app receives `function_executed` or interactivity events scoped to a custom step.
            ssl_check_enabled: bool = False if you would like to disable the built-in middleware (Default: True).
                `SslCheck` is a built-in middleware that handles ssl_check requests from Slack.
            oauth_settings: The settings related to Slack app installation flow (OAuth flow)
            oauth_flow: Instantiated `slack_bolt.oauth.OAuthFlow`. This is always prioritized over oauth_settings.
            verification_token: Deprecated verification mechanism. This can be used only for ssl_check requests.
            listener_executor: Custom executor to run background tasks. If absent, the default `ThreadPoolExecutor` will
                be used.
            assistant_thread_context_store: Custom AssistantThreadContext store (Default: the built-in implementation,
                which uses a parent message's metadata to store the latest context)
        """
        if signing_secret is None:
            signing_secret = os.environ.get("SLACK_SIGNING_SECRET", "")
        token = token or os.environ.get("SLACK_BOT_TOKEN")

        self._name: str = name or inspect.stack()[1].filename.split(os.path.sep)[-1]
        self._signing_secret: str = signing_secret

        self._verification_token: Optional[str] = verification_token or os.environ.get("SLACK_VERIFICATION_TOKEN", None)
        # If a logger is explicitly passed when initializing, the logger works as the base logger.
        # The base logger's logging settings will be propagated to all the loggers created by bolt-python.
        self._base_logger = logger
        # The framework logger is supposed to be used for the internal logging.
        # Also, it's accessible via `app.logger` as the app's singleton logger.
        self._framework_logger = logger or get_bolt_logger(App)
        self._raise_error_for_unhandled_request = raise_error_for_unhandled_request

        self._token: Optional[str] = token

        if client is not None:
            if not isinstance(client, WebClient):
                raise BoltError(error_client_invalid_type())
            self._client = client
            self._token = client.token
            if token is not None:
                self._framework_logger.warning(warning_client_prioritized_and_token_skipped())
        else:
            self._client = create_web_client(
                # NOTE: the token here can be None
                token=token,
                logger=self._framework_logger,
            )

        # --------------------------------------
        # Authorize & OAuthFlow initialization
        # --------------------------------------

        self._before_authorize: Optional[Middleware] = None
        if before_authorize is not None:
            if callable(before_authorize):
                self._before_authorize = CustomMiddleware(
                    app_name=self._name,
                    func=before_authorize,
                    base_logger=self._framework_logger,
                )
            elif isinstance(before_authorize, Middleware):
                self._before_authorize = before_authorize

        self._authorize: Optional[Authorize] = None
        if authorize is not None:
            if isinstance(authorize, Authorize):
                # As long as an advanced developer understands what they're doing,
                # bolt-python should not prevent customizing authorize middleware
                self._authorize = authorize
            else:
                if oauth_settings is not None or oauth_flow is not None:
                    # If the given authorize is a simple function,
                    # it does not work along with installation_store.
                    raise BoltError(error_authorize_conflicts())
                self._authorize = CallableAuthorize(logger=self._framework_logger, func=authorize)

        self._installation_store: Optional[InstallationStore] = installation_store
        if self._installation_store is not None and self._authorize is None:
            settings = oauth_flow.settings if oauth_flow is not None else oauth_settings
            self._authorize = InstallationStoreAuthorize(
                installation_store=self._installation_store,
                client_id=settings.client_id if settings is not None else None,
                client_secret=settings.client_secret if settings is not None else None,
                logger=self._framework_logger,
                bot_only=installation_store_bot_only or False,
                client=self._client,  # for proxy use cases etc.
                user_token_resolution=(settings.user_token_resolution if settings is not None else "authed_user"),
            )

        self._oauth_flow: Optional[OAuthFlow] = None

        if (
            oauth_settings is None
            and os.environ.get("SLACK_CLIENT_ID") is not None
            and os.environ.get("SLACK_CLIENT_SECRET") is not None
        ):
            # initialize with the default settings
            oauth_settings = OAuthSettings()

            if oauth_flow is None and installation_store is None:
                # show info-level log for avoiding confusions
                self._framework_logger.info(info_default_oauth_settings_loaded())

        if oauth_flow is not None:
            self._oauth_flow = oauth_flow
            installation_store = select_consistent_installation_store(
                client_id=self._oauth_flow.client_id,
                app_store=self._installation_store,
                oauth_flow_store=self._oauth_flow.settings.installation_store,
                logger=self._framework_logger,
            )
            self._installation_store = installation_store
            if installation_store is not None:
                self._oauth_flow.settings.installation_store = installation_store

            if self._oauth_flow._client is None:
                self._oauth_flow._client = self._client
            if self._authorize is None:
                self._authorize = self._oauth_flow.settings.authorize
        elif oauth_settings is not None:
            installation_store = select_consistent_installation_store(
                client_id=oauth_settings.client_id,
                app_store=self._installation_store,
                oauth_flow_store=oauth_settings.installation_store,
                logger=self._framework_logger,
            )
            self._installation_store = installation_store
            if installation_store is not None:
                oauth_settings.installation_store = installation_store
            self._oauth_flow = OAuthFlow(client=self.client, logger=self.logger, settings=oauth_settings)
            if self._authorize is None:
                self._authorize = self._oauth_flow.settings.authorize
            self._authorize.token_rotation_expiration_minutes = oauth_settings.token_rotation_expiration_minutes  # type: ignore[attr-defined] # noqa: E501

        if (self._installation_store is not None or self._authorize is not None) and self._token is not None:
            self._token = None
            self._framework_logger.warning(warning_token_skipped())

        # after setting bot_only here, __init__ cannot replace authorize function
        if installation_store_bot_only is not None and self._oauth_flow is not None:
            app_bot_only = installation_store_bot_only or False
            oauth_flow_bot_only = self._oauth_flow.settings.installation_store_bot_only
            if app_bot_only != oauth_flow_bot_only:
                self.logger.warning(warning_bot_only_conflicts())
                self._oauth_flow.settings.installation_store_bot_only = app_bot_only
                self._authorize.bot_only = app_bot_only  # type: ignore[union-attr]

        self._tokens_revocation_listeners: Optional[TokenRevocationListeners] = None
        if self._installation_store is not None:
            self._tokens_revocation_listeners = TokenRevocationListeners(self._installation_store)

        # --------------------------------------
        # Middleware Initialization
        # --------------------------------------

        self._middleware_list: List[Middleware] = []
        self._listeners: List[Listener] = []

        if listener_executor is None:
            listener_executor = ThreadPoolExecutor(max_workers=5)

        self._assistant_thread_context_store = assistant_thread_context_store

        self._process_before_response = process_before_response
        self._listener_runner = ThreadListenerRunner(
            logger=self._framework_logger,
            process_before_response=process_before_response,
            listener_error_handler=DefaultListenerErrorHandler(logger=self._framework_logger),
            listener_start_handler=DefaultListenerStartHandler(logger=self._framework_logger),
            listener_completion_handler=DefaultListenerCompletionHandler(logger=self._framework_logger),
            listener_executor=listener_executor,
            lazy_listener_runner=ThreadLazyListenerRunner(
                logger=self._framework_logger,
                executor=listener_executor,
            ),
        )
        self._middleware_error_handler: MiddlewareErrorHandler = DefaultMiddlewareErrorHandler(
            logger=self._framework_logger,
        )

        self._init_middleware_list_done = False
        self._init_middleware_list(
            token_verification_enabled=token_verification_enabled,
            request_verification_enabled=request_verification_enabled,
            ignoring_self_events_enabled=ignoring_self_events_enabled,
            ignoring_self_assistant_message_events_enabled=ignoring_self_assistant_message_events_enabled,
            ssl_check_enabled=ssl_check_enabled,
            url_verification_enabled=url_verification_enabled,
            attaching_function_token_enabled=attaching_function_token_enabled,
            user_facing_authorize_error_message=user_facing_authorize_error_message,
        )

    def _init_middleware_list(
        self,
        token_verification_enabled: bool = True,
        request_verification_enabled: bool = True,
        ignoring_self_events_enabled: bool = True,
        ignoring_self_assistant_message_events_enabled: bool = True,
        ssl_check_enabled: bool = True,
        url_verification_enabled: bool = True,
        attaching_function_token_enabled: bool = True,
        user_facing_authorize_error_message: Optional[str] = None,
    ):
        if self._init_middleware_list_done:
            return
        if ssl_check_enabled is True:
            self._middleware_list.append(
                SslCheck(
                    verification_token=self._verification_token,
                    base_logger=self._base_logger,
                )
            )
        if request_verification_enabled is True:
            self._middleware_list.append(RequestVerification(self._signing_secret, base_logger=self._base_logger))

        if self._before_authorize is not None:
            self._middleware_list.append(self._before_authorize)

        # As authorize is required for making a Bolt app function, we don't offer the flag to disable this
        if self._oauth_flow is None:
            if self._token is not None:
                try:
                    auth_test_result = None
                    if token_verification_enabled:
                        # This API call is for eagerly validating the token
                        auth_test_result = self._client.auth_test(token=self._token)
                    self._middleware_list.append(
                        SingleTeamAuthorization(
                            auth_test_result=auth_test_result,
                            base_logger=self._base_logger,
                            user_facing_authorize_error_message=user_facing_authorize_error_message,
                        )
                    )
                except SlackApiError as err:
                    raise BoltError(error_auth_test_failure(err.response))
            elif self._authorize is not None:
                self._middleware_list.append(
                    MultiTeamsAuthorization(
                        authorize=self._authorize,
                        base_logger=self._base_logger,
                        user_facing_authorize_error_message=user_facing_authorize_error_message,
                    )
                )
            else:
                raise BoltError(error_token_required())
        elif self._authorize is not None:
            self._middleware_list.append(
                MultiTeamsAuthorization(
                    authorize=self._authorize,
                    base_logger=self._base_logger,
                    user_token_resolution=self._oauth_flow.settings.user_token_resolution,
                    user_facing_authorize_error_message=user_facing_authorize_error_message,
                )
            )
        else:
            raise BoltError(error_oauth_flow_or_authorize_required())

        if ignoring_self_events_enabled is True:
            self._middleware_list.append(
                IgnoringSelfEvents(
                    base_logger=self._base_logger,
                    ignoring_self_assistant_message_events_enabled=ignoring_self_assistant_message_events_enabled,
                )
            )
        if url_verification_enabled is True:
            self._middleware_list.append(UrlVerification(base_logger=self._base_logger))
        if attaching_function_token_enabled is True:
            self._middleware_list.append(AttachingFunctionToken())
        self._init_middleware_list_done = True

    # -------------------------
    # accessors

    @property
    def name(self) -> str:
        """The name of this app (default: the filename)"""
        return self._name

    @property
    def oauth_flow(self) -> Optional[OAuthFlow]:
        """Configured `OAuthFlow` object if exists."""
        return self._oauth_flow

    @property
    def logger(self) -> logging.Logger:
        """The logger this app uses."""
        return self._framework_logger

    @property
    def client(self) -> WebClient:
        """The singleton `slack_sdk.WebClient` instance in this app."""
        return self._client

    @property
    def installation_store(self) -> Optional[InstallationStore]:
        """The `slack_sdk.oauth.InstallationStore` that can be used in the `authorize` middleware."""
        return self._installation_store

    @property
    def listener_runner(self) -> ThreadListenerRunner:
        """The thread executor for asynchronously running listeners."""
        return self._listener_runner

    @property
    def process_before_response(self) -> bool:
        return self._process_before_response or False

    # -------------------------
    # standalone server

    def start(
        self,
        port: int = 3000,
        path: str = "/slack/events",
        http_server_logger_enabled: bool = True,
    ) -> None:
        """Starts a web server for local development.

            # With the default settings, `http://localhost:3000/slack/events`
            # is available for handling incoming requests from Slack
            app.start()

        This method internally starts a Web server process built with the `http.server` module.
        For production, consider using a production-ready WSGI server such as Gunicorn.

        Args:
            port: The port to listen on (Default: 3000)
            path: The path to handle request from Slack (Default: `/slack/events`)
            http_server_logger_enabled: The flag to enable http.server logging if True (Default: True)
        """
        self._development_server = SlackAppDevelopmentServer(
            port=port,
            path=path,
            app=self,
            oauth_flow=self.oauth_flow,
            http_server_logger_enabled=http_server_logger_enabled,
        )
        self._development_server.start()

    # -------------------------
    # main dispatcher

    def dispatch(self, req: BoltRequest) -> BoltResponse:
        """Applies all middleware and dispatches an incoming request from Slack to the right code path.

        Args:
            req: An incoming request from Slack

        Returns:
            The response generated by this Bolt app
        """
        starting_time = time.time()
        self._init_context(req)

        resp: Optional[BoltResponse] = BoltResponse(status=200, body="")
        middleware_state = {"next_called": False}

        def middleware_next():
            middleware_state["next_called"] = True

        try:
            for middleware in self._middleware_list:
                middleware_state["next_called"] = False
                if self._framework_logger.level <= logging.DEBUG:
                    self._framework_logger.debug(debug_applying_middleware(middleware.name))
                resp = middleware.process(req=req, resp=resp, next=middleware_next)  # type: ignore[arg-type]
                if not middleware_state["next_called"]:
                    if resp is None:
                        # next() method was not called without providing the response to return to Slack
                        # This should not be an intentional handling in usual use cases.
                        resp = BoltResponse(status=404, body={"error": "no next() calls in middleware"})
                        if self._raise_error_for_unhandled_request is True:
                            try:
                                raise BoltUnhandledRequestError(
                                    request=req,
                                    current_response=resp,
                                    last_global_middleware_name=middleware.name,
                                )
                            except BoltUnhandledRequestError as e:
                                self._listener_runner.listener_error_handler.handle(
                                    error=e,
                                    request=req,
                                    response=resp,
                                )
                            return resp
                        self._framework_logger.warning(warning_unhandled_by_global_middleware(middleware.name, req))
                        return resp
                    return resp

            for listener in self._listeners:
                listener_name = get_name_for_callable(listener.ack_function)
                self._framework_logger.debug(debug_checking_listener(listener_name))
                if listener.matches(req=req, resp=resp):  # type: ignore[arg-type]
                    # run all the middleware attached to this listener first
                    middleware_resp, next_was_not_called = listener.run_middleware(
                        req=req, resp=resp  # type: ignore[arg-type]
                    )
                    if next_was_not_called:
                        if middleware_resp is not None:
                            if self._framework_logger.level <= logging.DEBUG:
                                debug_message = debug_return_listener_middleware_response(
                                    listener_name,
                                    middleware_resp.status,
                                    middleware_resp.body,
                                    starting_time,
                                )
                                self._framework_logger.debug(debug_message)
                            return middleware_resp
                        # The last listener middleware didn't call next() method.
                        # This means the listener is not for this incoming request.
                        continue

                    if middleware_resp is not None:
                        resp = middleware_resp

                    self._framework_logger.debug(debug_running_listener(listener_name))
                    listener_response: Optional[BoltResponse] = self._listener_runner.run(
                        request=req,
                        response=resp,  # type: ignore[arg-type]
                        listener_name=listener_name,
                        listener=listener,
                    )
                    if listener_response is not None:
                        return listener_response

            if resp is None:
                resp = BoltResponse(status=404, body={"error": "unhandled request"})
            if self._raise_error_for_unhandled_request is True:
                try:
                    raise BoltUnhandledRequestError(
                        request=req,
                        current_response=resp,
                    )
                except BoltUnhandledRequestError as e:
                    self._listener_runner.listener_error_handler.handle(
                        error=e,
                        request=req,
                        response=resp,
                    )
                return resp
            return self._handle_unmatched_requests(req, resp)
        except Exception as error:
            resp = BoltResponse(status=500, body="")
            self._middleware_error_handler.handle(
                error=error,
                request=req,
                response=resp,
            )
            return resp

    def _handle_unmatched_requests(self, req: BoltRequest, resp: BoltResponse) -> BoltResponse:
        self._framework_logger.warning(warning_unhandled_request(req))
        return resp

    # -------------------------
    # middleware

    def use(self, *args) -> Optional[Callable]:
        """Registers a new global middleware to this app. This method can be used as either a decorator or a method.

        Refer to `App#middleware()` method's docstring for details."""
        return self.middleware(*args)

    def middleware(self, *args) -> Optional[Callable]:
        """Registers a new middleware to this app.
        This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.middleware
            def middleware_func(logger, body, next):
                logger.info(f"request body: {body}")
                next()

            # Pass a function to this method
            app.middleware(middleware_func)

        Refer to https://docs.slack.dev/tools/bolt-python/concepts/global-middleware for details.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            *args: A function that works as a global middleware.
        """
        if len(args) > 0:
            middleware_or_callable = args[0]
            if isinstance(middleware_or_callable, Middleware):
                middleware: Middleware = middleware_or_callable
                self._middleware_list.append(middleware)
                if isinstance(middleware, Assistant) and middleware.thread_context_store is not None:
                    self._assistant_thread_context_store = middleware.thread_context_store
            elif callable(middleware_or_callable):
                self._middleware_list.append(
                    CustomMiddleware(
                        app_name=self.name,
                        func=middleware_or_callable,
                        base_logger=self._base_logger,
                    )
                )
                return middleware_or_callable
            else:
                raise BoltError(f"Unexpected type for a middleware ({type(middleware_or_callable)})")
        return None

    # -------------------------
    # AI Agents & Assistants

    def assistant(self, assistant: Assistant) -> Optional[Callable]:
        return self.middleware(assistant)

    # -------------------------
    # Workflows: Steps from apps

    def step(
        self,
        callback_id: Union[str, Pattern, WorkflowStep, WorkflowStepBuilder],
        edit: Optional[Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]]] = None,
        save: Optional[Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]]] = None,
        execute: Optional[Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]]] = None,
    ):
        """
        Deprecated:
            Steps from apps for legacy workflows are now deprecated.
            Use new custom steps: https://docs.slack.dev/workflows/workflow-steps/

        Registers a new step from app listener.

        Unlike others, this method doesn't behave as a decorator.
        If you want to register a step from app by a decorator, use `WorkflowStepBuilder`'s methods.

            # Create a new WorkflowStep instance
            from slack_bolt.workflows.step import WorkflowStep
            ws = WorkflowStep(
                callback_id="add_task",
                edit=edit,
                save=save,
                execute=execute,
            )
            # Pass Step to set up listeners
            app.step(ws)

        Refer to https://docs.slack.dev/legacy/legacy-steps-from-apps/ for details of steps from apps.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        For further information about WorkflowStep specific function arguments
        such as `configure`, `update`, `complete`, and `fail`,
        refer to `slack_bolt.workflows.step.utilities` API documents.

        Args:
            callback_id: The Callback ID for this step from app
            edit: The function for displaying a modal in the Workflow Builder
            save: The function for handling configuration in the Workflow Builder
            execute: The function for handling the step execution
        """
        warnings.warn(
            (
                "Steps from apps for legacy workflows are now deprecated. "
                "Use new custom steps: https://docs.slack.dev/workflows/workflow-steps/"
            ),
            category=DeprecationWarning,
        )
        step = callback_id
        if isinstance(callback_id, (str, Pattern)):
            step = WorkflowStep(
                callback_id=callback_id,
                edit=edit,  # type: ignore[arg-type]
                save=save,  # type: ignore[arg-type]
                execute=execute,  # type: ignore[arg-type]
                base_logger=self._base_logger,
            )
        elif isinstance(step, WorkflowStepBuilder):
            step = step.build(base_logger=self._base_logger)
        elif not isinstance(step, WorkflowStep):
            raise BoltError(f"Invalid step object ({type(step)})")

        self.use(WorkflowStepMiddleware(step))

    # -------------------------
    # global error handler

    def error(self, func: Callable[..., Optional[BoltResponse]]) -> Callable[..., Optional[BoltResponse]]:
        """Updates the global error handler. This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.error
            def custom_error_handler(error, body, logger):
                logger.exception(f"Error: {error}")
                logger.info(f"Request body: {body}")

            # Pass a function to this method
            app.error(custom_error_handler)

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            func: The function that is supposed to be executed
                when getting an unhandled error in Bolt app.
        """
        self._listener_runner.listener_error_handler = CustomListenerErrorHandler(
            logger=self._framework_logger,
            func=func,
        )
        self._middleware_error_handler = CustomMiddlewareErrorHandler(
            logger=self._framework_logger,
            func=func,
        )
        return func

    # -------------------------
    # events

    def event(
        self,
        event: Union[
            str,
            Pattern,
            Dict[str, Optional[Union[str, Sequence[Optional[Union[str, Pattern]]]]]],
        ],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new event listener. This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.event("team_join")
            def ask_for_introduction(event, say):
                welcome_channel_id = "C12345"
                user_id = event["user"]
                text = f"Welcome to the team, <@{user_id}>! :tada: You can introduce yourself in this channel."
                say(text=text, channel=welcome_channel_id)

            # Pass a function to this method
            app.event("team_join")(ask_for_introduction)

        Refer to https://docs.slack.dev/apis/events-api/ for details of Events API.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            event: The conditions that match a request payload.
                If you pass a dict for this, you can have type, subtype in the constraint.
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.event(event, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware, True)

        return __call__

    def message(
        self,
        keyword: Union[str, Pattern] = "",
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new message event listener. This method can be used as either a decorator or a method.
        Check the `App#event` method's docstring for details.

            # Use this method as a decorator
            @app.message(":wave:")
            def say_hello(message, say):
                user = message['user']
                say(f"Hi there, <@{user}>!")

            # Pass a function to this method
            app.message(":wave:")(say_hello)

        Refer to https://docs.slack.dev/reference/events/message/ for details of `message` events.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            keyword: The keyword to match
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """
        matchers = list(matchers) if matchers else []
        middleware = list(middleware) if middleware else []

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            constraints = {
                "type": "message",
                "subtype": (
                    # In most cases, new message events come with no subtype.
                    None,
                    # As of Jan 2021, most bot messages no longer have the subtype bot_message.
                    # By contrast, messages posted using classic app's bot token still have the subtype.
                    "bot_message",
                    # If an end-user posts a message with "Also send to #channel" checked,
                    # the message event comes with this subtype.
                    "thread_broadcast",
                    # If an end-user posts a message with attached files,
                    # the message event comes with this subtype.
                    "file_share",
                ),
            }
            primary_matcher = builtin_matchers.message_event(
                keyword=keyword, constraints=constraints, base_logger=self._base_logger
            )
            middleware.insert(0, MessageListenerMatches(keyword))
            return self._register_listener(list(functions), primary_matcher, matchers, middleware, True)

        return __call__

    def function(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
        auto_acknowledge: bool = True,
        ack_timeout: int = 3,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new Function listener.
        This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.function("reverse")
            def reverse_string(ack: Ack, inputs: dict, complete: Complete, fail: Fail):
                try:
                    ack()
                    string_to_reverse = inputs["stringToReverse"]
                    complete(outputs={"reverseString": string_to_reverse[::-1]})
                except Exception as e:
                    fail(f"Cannot reverse string (error: {e})")
                    raise e

            # Pass a function to this method
            app.function("reverse")(reverse_string)

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            callback_id: The callback id to identify the function
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        if auto_acknowledge is True:
            if ack_timeout != 3:
                self._framework_logger.warning(warning_ack_timeout_has_no_effect(callback_id, ack_timeout))

        matchers = list(matchers) if matchers else []
        middleware = list(middleware) if middleware else []

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.function_executed(callback_id=callback_id, base_logger=self._base_logger)
            return self._register_listener(functions, primary_matcher, matchers, middleware, auto_acknowledge, ack_timeout)

        return __call__

    # -------------------------
    # slash commands

    def command(
        self,
        command: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new slash command listener.
        This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.command("/echo")
            def repeat_text(ack, say, command):
                # Acknowledge command request
                ack()
                say(f"{command['text']}")

            # Pass a function to this method
            app.command("/echo")(repeat_text)

        Refer to https://docs.slack.dev/interactivity/implementing-slash-commands/ for details of Slash Commands.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            command: The conditions that match a request payload
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.command(command, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    # -------------------------
    # shortcut

    def shortcut(
        self,
        constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new shortcut listener.
        This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.shortcut("open_modal")
            def open_modal(ack, body, client):
                # Acknowledge the command request
                ack()
                # Call views_open with the built-in client
                client.views_open(
                    # Pass a valid trigger_id within 3 seconds of receiving it
                    trigger_id=body["trigger_id"],
                    # View payload
                    view={ ... }
                )

            # Pass a function to this method
            app.shortcut("open_modal")(open_modal)

        Refer to https://docs.slack.dev/interactivity/implementing-shortcuts/ for details about Shortcuts.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            constraints: The conditions that match a request payload.
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.shortcut(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def global_shortcut(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new global shortcut listener."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.global_shortcut(callback_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def message_shortcut(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new message shortcut listener."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.message_shortcut(callback_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    # -------------------------
    # action

    def action(
        self,
        constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new action listener. This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.action("approve_button")
            def update_message(ack):
                ack()

            # Pass a function to this method
            app.action("approve_button")(update_message)

        * Refer to https://docs.slack.dev/reference/interaction-payloads/block_actions-payload/ for actions in `blocks`.
        * Refer to https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/ for actions in `attachments`.
        * Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for actions in dialogs.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            constraints: The conditions that match a request payload
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.action(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def block_action(
        self,
        constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `block_actions` action listener.
        Refer to https://docs.slack.dev/reference/interaction-payloads/block_actions-payload/ for details.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.block_action(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def attachment_action(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `interactive_message` action listener.
        Refer to https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/ for details."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.attachment_action(callback_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def dialog_submission(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `dialog_submission` listener.
        Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for details."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.dialog_submission(callback_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def dialog_cancellation(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `dialog_cancellation` listener.
        Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for details."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.dialog_cancellation(callback_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    # -------------------------
    # view

    def view(
        self,
        constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `view_submission`/`view_closed` event listener.
        This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.view("view_1")
            def handle_submission(ack, body, client, view):
                # Assume there's an input block with `block_c` as the block_id and `dreamy_input`
                hopes_and_dreams = view["state"]["values"]["block_c"]["dreamy_input"]
                user = body["user"]["id"]
                # Validate the inputs
                errors = {}
                if hopes_and_dreams is not None and len(hopes_and_dreams) <= 5:
                    errors["block_c"] = "The value must be longer than 5 characters"
                if len(errors) > 0:
                    ack(response_action="errors", errors=errors)
                    return
                # Acknowledge the view_submission event and close the modal
                ack()
                # Do whatever you want with the input data - here we're saving it to a DB

            # Pass a function to this method
            app.view("view_1")(handle_submission)

        Refer to https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload for details of payloads.

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            constraints: The conditions that match a request payload
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.view(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def view_submission(
        self,
        constraints: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `view_submission` listener.
        Refer to https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view_submission for
        details.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.view_submission(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def view_closed(
        self,
        constraints: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `view_closed` listener.
        Refer to https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view_closed for details."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.view_closed(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    # -------------------------
    # options

    def options(
        self,
        constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new options listener.
        This method can be used as either a decorator or a method.

            # Use this method as a decorator
            @app.options("menu_selection")
            def show_menu_options(ack):
                options = [
                    {
                        "text": {"type": "plain_text", "text": "Option 1"},
                        "value": "1-1",
                    },
                    {
                        "text": {"type": "plain_text", "text": "Option 2"},
                        "value": "1-2",
                    },
                ]
                ack(options=options)

            # Pass a function to this method
            app.options("menu_selection")(show_menu_options)

        Refer to the following documents for details:

        * https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_select
        * https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external_multi_select

        To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

        Args:
            matchers: A list of listener matcher functions.
                Only when all the matchers return True, the listener function can be invoked.
            middleware: A list of lister middleware functions.
                Only when all the middleware call `next()` method, the listener function can be invoked.
        """

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.options(constraints, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def block_suggestion(
        self,
        action_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `block_suggestion` listener."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.block_suggestion(action_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    def dialog_suggestion(
        self,
        callback_id: Union[str, Pattern],
        matchers: Optional[Sequence[Callable[..., bool]]] = None,
        middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    ) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
        """Registers a new `dialog_suggestion` listener.
        Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for details."""

        def __call__(*args, **kwargs):
            functions = self._to_listener_functions(kwargs) if kwargs else list(args)
            primary_matcher = builtin_matchers.dialog_suggestion(callback_id, base_logger=self._base_logger)
            return self._register_listener(list(functions), primary_matcher, matchers, middleware)

        return __call__

    # -------------------------
    # built-in listener functions

    def default_tokens_revoked_event_listener(
        self,
    ) -> Callable[..., Optional[BoltResponse]]:
        if self._tokens_revocation_listeners is None:
            raise BoltError(error_installation_store_required_for_builtin_listeners())
        return self._tokens_revocation_listeners.handle_tokens_revoked_events

    def default_app_uninstalled_event_listener(
        self,
    ) -> Callable[..., Optional[BoltResponse]]:
        if self._tokens_revocation_listeners is None:
            raise BoltError(error_installation_store_required_for_builtin_listeners())
        return self._tokens_revocation_listeners.handle_app_uninstalled_events

    def enable_token_revocation_listeners(self) -> None:
        self.event("tokens_revoked")(self.default_tokens_revoked_event_listener())
        self.event("app_uninstalled")(self.default_app_uninstalled_event_listener())

    # -------------------------

    def _init_context(self, req: BoltRequest):
        req.context["logger"] = get_bolt_app_logger(app_name=self.name, base_logger=self._base_logger)
        req.context["token"] = self._token
        # Prior to version 1.15, when the token is static, self._client was passed to `req.context`.
        # The intention was to avoid creating a new instance per request
        # in the interest of runtime performance/memory footprint optimization.
        # However, developers may want to replace the token held by req.context.client in some situations.
        # In this case, this behavior can result in thread-unsafe data modification on `self._client`.
        # (`self._client` a.k.a. `app.client` is a singleton object per an App instance)
        # Thus, we've changed the behavior to create a new instance per request regardless of token argument
        # in the App initialization starting v1.15.
        # The overhead brought by this change is slight so that we believe that it is ignorable in any cases.
        client_per_request: WebClient = WebClient(
            token=self._token,  # this can be None, and it can be set later on
            base_url=self._client.base_url,
            timeout=self._client.timeout,
            ssl=self._client.ssl,
            proxy=self._client.proxy,
            headers=self._client.headers,
            team_id=req.context.team_id,
            logger=self._client.logger,
            retry_handlers=self._client.retry_handlers.copy() if self._client.retry_handlers is not None else None,
        )
        req.context["client"] = client_per_request

        # Most apps do not need this "listener_runner" instance.
        # It is intended for apps that start lazy listeners from their custom global middleware.
        req.context["listener_runner"] = self.listener_runner

        # For AI Agents & Assistants
        if is_assistant_event(req.body):
            assistant = AssistantUtilities(
                payload=to_event(req.body),  # type:ignore[arg-type]
                context=req.context,
                thread_context_store=self._assistant_thread_context_store,
            )
            req.context["say"] = assistant.say
            req.context["set_status"] = assistant.set_status
            req.context["set_title"] = assistant.set_title
            req.context["set_suggested_prompts"] = assistant.set_suggested_prompts
            req.context["get_thread_context"] = assistant.get_thread_context
            req.context["save_thread_context"] = assistant.save_thread_context

    @staticmethod
    def _to_listener_functions(
        kwargs: dict,
    ) -> Optional[Sequence[Callable[..., Optional[BoltResponse]]]]:
        if kwargs:
            functions = [kwargs["ack"]]
            for sub in kwargs["lazy"]:
                functions.append(sub)
            return functions
        return None

    def _register_listener(
        self,
        functions: Sequence[Callable[..., Optional[BoltResponse]]],
        primary_matcher: ListenerMatcher,
        matchers: Optional[Sequence[Callable[..., bool]]],
        middleware: Optional[Sequence[Union[Callable, Middleware]]],
        auto_acknowledgement: bool = False,
        ack_timeout: int = 3,
    ) -> Optional[Callable[..., Optional[BoltResponse]]]:
        value_to_return = None
        if not isinstance(functions, list):
            functions = list(functions)
        if len(functions) == 1:
            # In the case where the function is registered using decorator,
            # the registration should return the original function.
            value_to_return = functions[0]

        listener_matchers: List[ListenerMatcher] = [
            CustomListenerMatcher(app_name=self.name, func=f, base_logger=self._base_logger) for f in (matchers or [])
        ]
        listener_matchers.insert(0, primary_matcher)
        listener_middleware = []
        for m in middleware or []:
            if isinstance(m, Middleware):
                listener_middleware.append(m)
            elif callable(m):
                listener_middleware.append(CustomMiddleware(app_name=self.name, func=m, base_logger=self._base_logger))
            else:
                raise ValueError(error_unexpected_listener_middleware(type(m)))

        self._listeners.append(
            CustomListener(
                app_name=self.name,
                ack_function=functions.pop(0),
                lazy_functions=functions,  # type:ignore[arg-type]
                matchers=listener_matchers,
                middleware=listener_middleware,
                auto_acknowledgement=auto_acknowledgement,
                ack_timeout=ack_timeout,
                base_logger=self._base_logger,
            )
        )
        return value_to_return
```

Bolt App that provides functionalities to register middleware/listeners.

```javascript
import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to incoming messages that contain "hello"
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
```

Refer to [https://docs.slack.dev/tools/bolt-python/building-an-app](https://docs.slack.dev/tools/bolt-python/building-an-app) for details.

If you would like to build an OAuth app for enabling the app to run with multiple workspaces, refer to [https://docs.slack.dev/tools/bolt-python/concepts/authenticating-oauth](https://docs.slack.dev/tools/bolt-python/concepts/authenticating-oauth) to learn how to configure the app.

## Args

## `logger`

The custom logger that can be used in this app.

## `name`

The application name that will be used in logging. If absent, the source file name will be used.

## `process_before_response`

True if this app runs on Function as a Service. (Default: False)

## `raise_error_for_unhandled_request`

True if you want to raise exceptions for unhandled requests and use @app.error listeners instead of the built-in handler, which pints warning logs and returns 404 to Slack (Default: False)

## `signing_secret`

The Signing Secret value used for verifying requests from Slack.

## `token`

The bot/user access token required only for single-workspace app.

## `token_verification_enabled`

Verifies the validity of the given token if True.

## `client`

The singleton `slack_sdk.WebClient` instance for this app.

## `before_authorize`

A global middleware that can be executed right before authorize function

## `authorize`

The function to authorize an incoming request from Slack by checking if there is a team/user in the installation data.

## `user_facing_authorize_error_message`

The user-facing error message to display when the app is installed but the installation is not managed by this app's installation store

## `installation_store`

The module offering save/find operations of installation data

## `installation_store_bot_only`

Use `InstallationStore#find_bot()` if True (Default: False)

## `request_verification_enabled`

False if you would like to disable the built-in middleware (Default: True). `RequestVerification` is a built-in middleware that verifies the signature in HTTP Mode requests. Make sure if it's safe enough when you turn a built-in middleware off. We strongly recommend using RequestVerification for better security. If you have a proxy that verifies request signature in front of the Bolt app, it's totally fine to disable RequestVerification to avoid duplication of work. Don't turn it off just for easiness of development.

## `ignoring_self_events_enabled`

False if you would like to disable the built-in middleware (Default: True). `IgnoringSelfEvents` is a built-in middleware that enables Bolt apps to easily skip the events generated by this app's bot user (this is useful for avoiding code error causing an infinite loop).

## `ignoring_self_assistant_message_events_enabled`

False if you would like to disable the built-in middleware. `IgnoringSelfEvents` for this app's bot user message events within an assistant thread This is useful for avoiding code error causing an infinite loop; Default: True

## `url_verification_enabled`

False if you would like to disable the built-in middleware (Default: True). `UrlVerification` is a built-in middleware that handles url\_verification requests that verify the endpoint for Events API in HTTP Mode requests.

## `attaching_function_token_enabled`

False if you would like to disable the built-in middleware (Default: True). `AttachingFunctionToken` is a built-in middleware that injects the just-in-time workflow-execution tokens when your app receives `function_executed` or interactivity events scoped to a custom step.

## `ssl_check_enabled`

bool = False if you would like to disable the built-in middleware (Default: True). `SslCheck` is a built-in middleware that handles ssl\_check requests from Slack.

## `oauth_settings`

The settings related to Slack app installation flow (OAuth flow)

## `oauth_flow`

Instantiated `[OAuthFlow](oauth/index.html#slack_bolt.oauth.OAuthFlow "slack_bolt.oauth.OAuthFlow")`. This is always prioritized over oauth\_settings.

## `verification_token`

Deprecated verification mechanism. This can be used only for ssl\_check requests.

## `listener_executor`

Custom executor to run background tasks. If absent, the default `ThreadPoolExecutor` will be used.

## `assistant_thread_context_store`

Custom AssistantThreadContext store (Default: the built-in implementation, which uses a parent message's metadata to store the latest context)

### Instance variables

`prop client : slack_sdk.web.client.WebClient`

Expand source code

```text
@property
def client(self) -> WebClient:
    """The singleton `slack_sdk.WebClient` instance in this app."""
    return self._client
```

The singleton `slack_sdk.WebClient` instance in this app.

`prop installation_store : slack_sdk.oauth.installation_store.installation_store.InstallationStore | None`

Expand source code

```text
@property
def installation_store(self) -> Optional[InstallationStore]:
    """The `slack_sdk.oauth.InstallationStore` that can be used in the `authorize` middleware."""
    return self._installation_store
```

The `slack_sdk.oauth.InstallationStore` that can be used in the `authorize` middleware.

`prop listener_runner : [ThreadListenerRunner](listener/thread_runner.html#slack_bolt.listener.thread_runner.ThreadListenerRunner "slack_bolt.listener.thread_runner.ThreadListenerRunner")`

Expand source code

```text
@property
def listener_runner(self) -> ThreadListenerRunner:
    """The thread executor for asynchronously running listeners."""
    return self._listener_runner
```

The thread executor for asynchronously running listeners.

`prop logger : logging.Logger`

Expand source code

```text
@property
def logger(self) -> logging.Logger:
    """The logger this app uses."""
    return self._framework_logger
```

The logger this app uses.

`prop name : str`

Expand source code

```text
@property
def name(self) -> str:
    """The name of this app (default: the filename)"""
    return self._name
```

The name of this app (default: the filename)

`prop oauth_flow : [OAuthFlow](oauth/oauth_flow.html#slack_bolt.oauth.oauth_flow.OAuthFlow "slack_bolt.oauth.oauth_flow.OAuthFlow") | None`

Expand source code

```text
@property
def oauth_flow(self) -> Optional[OAuthFlow]:
    """Configured `OAuthFlow` object if exists."""
    return self._oauth_flow
```

Configured `OAuthFlow` object if exists.

`prop process_before_response : bool`

Expand source code

```text
@property
def process_before_response(self) -> bool:
    return self._process_before_response or False
```

### Methods

`def action(self,   constraints: str | Pattern | Dict[str, str | Pattern],   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def action(
    self,
    constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new action listener. This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.action("approve_button")
        def update_message(ack):
            ack()

        # Pass a function to this method
        app.action("approve_button")(update_message)

    * Refer to https://docs.slack.dev/reference/interaction-payloads/block_actions-payload/ for actions in `blocks`.
    * Refer to https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/ for actions in `attachments`.
    * Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for actions in dialogs.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        constraints: The conditions that match a request payload
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.action(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new action listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.action("approve_button")
def update_message(ack):
    ack()

# Pass a function to this method
app.action("approve_button")(update_message)
```

* Refer to [https://docs.slack.dev/reference/interaction-payloads/block\_actions-payload/](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload/) for actions in `blocks`.
* Refer to [https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/](https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/) for actions in `attachments`.
* Refer to [https://docs.slack.dev/legacy/legacy-dialogs/](https://docs.slack.dev/legacy/legacy-dialogs/) for actions in dialogs.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `constraints`

The conditions that match a request payload

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def assistant(self,   assistant: [Assistant](middleware/assistant/assistant.html#slack_bolt.middleware.assistant.assistant.Assistant "slack_bolt.middleware.assistant.assistant.Assistant")) ‑> Callable | None`

Expand source code

```python
def assistant(self, assistant: Assistant) -> Optional[Callable]:
    return self.middleware(assistant)
```

`def attachment_action(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def attachment_action(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `interactive_message` action listener.
    Refer to https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/ for details."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.attachment_action(callback_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `interactive_message` action listener. Refer to [https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/](https://docs.slack.dev/legacy/legacy-messaging/legacy-message-buttons/) for details.

`def block_action(self,   constraints: str | Pattern | Dict[str, str | Pattern],   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def block_action(
    self,
    constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `block_actions` action listener.
    Refer to https://docs.slack.dev/reference/interaction-payloads/block_actions-payload/ for details.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.block_action(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `block_actions` action listener. Refer to [https://docs.slack.dev/reference/interaction-payloads/block\_actions-payload/](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload/) for details.

`def block_suggestion(self,   action_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def block_suggestion(
    self,
    action_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `block_suggestion` listener."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.block_suggestion(action_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `block_suggestion` listener.

`def command(self,   command: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def command(
    self,
    command: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new slash command listener.
    This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.command("/echo")
        def repeat_text(ack, say, command):
            # Acknowledge command request
            ack()
            say(f"{command['text']}")

        # Pass a function to this method
        app.command("/echo")(repeat_text)

    Refer to https://docs.slack.dev/interactivity/implementing-slash-commands/ for details of Slash Commands.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        command: The conditions that match a request payload
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.command(command, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new slash command listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.command("/echo")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(f"{command['text']}")

# Pass a function to this method
app.command("/echo")(repeat_text)
```

Refer to [https://docs.slack.dev/interactivity/implementing-slash-commands/](https://docs.slack.dev/interactivity/implementing-slash-commands/) for details of Slash Commands.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `command`

The conditions that match a request payload

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def default_app_uninstalled_event_listener(self) ‑> Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None]`

Expand source code

```python
def default_app_uninstalled_event_listener(
    self,
) -> Callable[..., Optional[BoltResponse]]:
    if self._tokens_revocation_listeners is None:
        raise BoltError(error_installation_store_required_for_builtin_listeners())
    return self._tokens_revocation_listeners.handle_app_uninstalled_events
```

`def default_tokens_revoked_event_listener(self) ‑> Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None]`

Expand source code

```python
def default_tokens_revoked_event_listener(
    self,
) -> Callable[..., Optional[BoltResponse]]:
    if self._tokens_revocation_listeners is None:
        raise BoltError(error_installation_store_required_for_builtin_listeners())
    return self._tokens_revocation_listeners.handle_tokens_revoked_events
```

`def dialog_cancellation(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def dialog_cancellation(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `dialog_cancellation` listener.
    Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for details."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.dialog_cancellation(callback_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `dialog_cancellation` listener. Refer to [https://docs.slack.dev/legacy/legacy-dialogs/](https://docs.slack.dev/legacy/legacy-dialogs/) for details.

`def dialog_submission(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def dialog_submission(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `dialog_submission` listener.
    Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for details."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.dialog_submission(callback_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `dialog_submission` listener. Refer to [https://docs.slack.dev/legacy/legacy-dialogs/](https://docs.slack.dev/legacy/legacy-dialogs/) for details.

`def dialog_suggestion(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def dialog_suggestion(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `dialog_suggestion` listener.
    Refer to https://docs.slack.dev/legacy/legacy-dialogs/ for details."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.dialog_suggestion(callback_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `dialog_suggestion` listener. Refer to [https://docs.slack.dev/legacy/legacy-dialogs/](https://docs.slack.dev/legacy/legacy-dialogs/) for details.

`def dispatch(self,   req: [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")) ‑> [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Expand source code

```python
def dispatch(self, req: BoltRequest) -> BoltResponse:
    """Applies all middleware and dispatches an incoming request from Slack to the right code path.

    Args:
        req: An incoming request from Slack

    Returns:
        The response generated by this Bolt app
    """
    starting_time = time.time()
    self._init_context(req)

    resp: Optional[BoltResponse] = BoltResponse(status=200, body="")
    middleware_state = {"next_called": False}

    def middleware_next():
        middleware_state["next_called"] = True

    try:
        for middleware in self._middleware_list:
            middleware_state["next_called"] = False
            if self._framework_logger.level <= logging.DEBUG:
                self._framework_logger.debug(debug_applying_middleware(middleware.name))
            resp = middleware.process(req=req, resp=resp, next=middleware_next)  # type: ignore[arg-type]
            if not middleware_state["next_called"]:
                if resp is None:
                    # next() method was not called without providing the response to return to Slack
                    # This should not be an intentional handling in usual use cases.
                    resp = BoltResponse(status=404, body={"error": "no next() calls in middleware"})
                    if self._raise_error_for_unhandled_request is True:
                        try:
                            raise BoltUnhandledRequestError(
                                request=req,
                                current_response=resp,
                                last_global_middleware_name=middleware.name,
                            )
                        except BoltUnhandledRequestError as e:
                            self._listener_runner.listener_error_handler.handle(
                                error=e,
                                request=req,
                                response=resp,
                            )
                        return resp
                    self._framework_logger.warning(warning_unhandled_by_global_middleware(middleware.name, req))
                    return resp
                return resp

        for listener in self._listeners:
            listener_name = get_name_for_callable(listener.ack_function)
            self._framework_logger.debug(debug_checking_listener(listener_name))
            if listener.matches(req=req, resp=resp):  # type: ignore[arg-type]
                # run all the middleware attached to this listener first
                middleware_resp, next_was_not_called = listener.run_middleware(
                    req=req, resp=resp  # type: ignore[arg-type]
                )
                if next_was_not_called:
                    if middleware_resp is not None:
                        if self._framework_logger.level <= logging.DEBUG:
                            debug_message = debug_return_listener_middleware_response(
                                listener_name,
                                middleware_resp.status,
                                middleware_resp.body,
                                starting_time,
                            )
                            self._framework_logger.debug(debug_message)
                        return middleware_resp
                    # The last listener middleware didn't call next() method.
                    # This means the listener is not for this incoming request.
                    continue

                if middleware_resp is not None:
                    resp = middleware_resp

                self._framework_logger.debug(debug_running_listener(listener_name))
                listener_response: Optional[BoltResponse] = self._listener_runner.run(
                    request=req,
                    response=resp,  # type: ignore[arg-type]
                    listener_name=listener_name,
                    listener=listener,
                )
                if listener_response is not None:
                    return listener_response

        if resp is None:
            resp = BoltResponse(status=404, body={"error": "unhandled request"})
        if self._raise_error_for_unhandled_request is True:
            try:
                raise BoltUnhandledRequestError(
                    request=req,
                    current_response=resp,
                )
            except BoltUnhandledRequestError as e:
                self._listener_runner.listener_error_handler.handle(
                    error=e,
                    request=req,
                    response=resp,
                )
            return resp
        return self._handle_unmatched_requests(req, resp)
    except Exception as error:
        resp = BoltResponse(status=500, body="")
        self._middleware_error_handler.handle(
            error=error,
            request=req,
            response=resp,
        )
        return resp
```

Applies all middleware and dispatches an incoming request from Slack to the right code path.

## Args

## `req`

An incoming request from Slack

## Returns

The response generated by this Bolt app

`def enable_token_revocation_listeners(self) ‑> None`

Expand source code

```python
def enable_token_revocation_listeners(self) -> None:
    self.event("tokens_revoked")(self.default_tokens_revoked_event_listener())
    self.event("app_uninstalled")(self.default_app_uninstalled_event_listener())
```

`def error(self,   func: Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None]) ‑> Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None]`

Expand source code

```python
def error(self, func: Callable[..., Optional[BoltResponse]]) -> Callable[..., Optional[BoltResponse]]:
    """Updates the global error handler. This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.error
        def custom_error_handler(error, body, logger):
            logger.exception(f"Error: {error}")
            logger.info(f"Request body: {body}")

        # Pass a function to this method
        app.error(custom_error_handler)

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        func: The function that is supposed to be executed
            when getting an unhandled error in Bolt app.
    """
    self._listener_runner.listener_error_handler = CustomListenerErrorHandler(
        logger=self._framework_logger,
        func=func,
    )
    self._middleware_error_handler = CustomMiddlewareErrorHandler(
        logger=self._framework_logger,
        func=func,
    )
    return func
```

Updates the global error handler. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.error
def custom_error_handler(error, body, logger):
    logger.exception(f"Error: {error}")
    logger.info(f"Request body: {body}")

# Pass a function to this method
app.error(custom_error_handler)
```

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `func`

The function that is supposed to be executed when getting an unhandled error in Bolt app.

`def event(self,   event: str | Pattern | Dict[str, str | Sequence[str | Pattern | None] | None],   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def event(
    self,
    event: Union[
        str,
        Pattern,
        Dict[str, Optional[Union[str, Sequence[Optional[Union[str, Pattern]]]]]],
    ],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new event listener. This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.event("team_join")
        def ask_for_introduction(event, say):
            welcome_channel_id = "C12345"
            user_id = event["user"]
            text = f"Welcome to the team, <@{user_id}>! :tada: You can introduce yourself in this channel."
            say(text=text, channel=welcome_channel_id)

        # Pass a function to this method
        app.event("team_join")(ask_for_introduction)

    Refer to https://docs.slack.dev/apis/events-api/ for details of Events API.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        event: The conditions that match a request payload.
            If you pass a dict for this, you can have type, subtype in the constraint.
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.event(event, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware, True)

    return __call__
```

Registers a new event listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.event("team_join")
def ask_for_introduction(event, say):
    welcome_channel_id = "C12345"
    user_id = event["user"]
    text = f"Welcome to the team, <@{user_id}>! :tada: You can introduce yourself in this channel."
    say(text=text, channel=welcome_channel_id)

# Pass a function to this method
app.event("team_join")(ask_for_introduction)
```

Refer to [https://docs.slack.dev/apis/events-api/](https://docs.slack.dev/apis/events-api/) for details of Events API.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `event`

The conditions that match a request payload. If you pass a dict for this, you can have type, subtype in the constraint.

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def function(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None,   auto_acknowledge: bool = True,   ack_timeout: int = 3) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def function(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
    auto_acknowledge: bool = True,
    ack_timeout: int = 3,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new Function listener.
    This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.function("reverse")
        def reverse_string(ack: Ack, inputs: dict, complete: Complete, fail: Fail):
            try:
                ack()
                string_to_reverse = inputs["stringToReverse"]
                complete(outputs={"reverseString": string_to_reverse[::-1]})
            except Exception as e:
                fail(f"Cannot reverse string (error: {e})")
                raise e

        # Pass a function to this method
        app.function("reverse")(reverse_string)

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        callback_id: The callback id to identify the function
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    if auto_acknowledge is True:
        if ack_timeout != 3:
            self._framework_logger.warning(warning_ack_timeout_has_no_effect(callback_id, ack_timeout))

    matchers = list(matchers) if matchers else []
    middleware = list(middleware) if middleware else []

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.function_executed(callback_id=callback_id, base_logger=self._base_logger)
        return self._register_listener(functions, primary_matcher, matchers, middleware, auto_acknowledge, ack_timeout)

    return __call__
```

Registers a new Function listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.function("reverse")
def reverse_string(ack: Ack, inputs: dict, complete: Complete, fail: Fail):
    try:
        ack()
        string_to_reverse = inputs["stringToReverse"]
        complete(outputs={"reverseString": string_to_reverse[::-1]})
    except Exception as e:
        fail(f"Cannot reverse string (error: {e})")
        raise e

# Pass a function to this method
app.function("reverse")(reverse_string)
```

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `callback_id`

The callback id to identify the function

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def global_shortcut(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def global_shortcut(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new global shortcut listener."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.global_shortcut(callback_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new global shortcut listener.

`def message(self,   keyword: str | Pattern = '',   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def message(
    self,
    keyword: Union[str, Pattern] = "",
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new message event listener. This method can be used as either a decorator or a method.
    Check the `App#event` method's docstring for details.

        # Use this method as a decorator
        @app.message(":wave:")
        def say_hello(message, say):
            user = message['user']
            say(f"Hi there, <@{user}>!")

        # Pass a function to this method
        app.message(":wave:")(say_hello)

    Refer to https://docs.slack.dev/reference/events/message/ for details of `message` events.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        keyword: The keyword to match
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """
    matchers = list(matchers) if matchers else []
    middleware = list(middleware) if middleware else []

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        constraints = {
            "type": "message",
            "subtype": (
                # In most cases, new message events come with no subtype.
                None,
                # As of Jan 2021, most bot messages no longer have the subtype bot_message.
                # By contrast, messages posted using classic app's bot token still have the subtype.
                "bot_message",
                # If an end-user posts a message with "Also send to #channel" checked,
                # the message event comes with this subtype.
                "thread_broadcast",
                # If an end-user posts a message with attached files,
                # the message event comes with this subtype.
                "file_share",
            ),
        }
        primary_matcher = builtin_matchers.message_event(
            keyword=keyword, constraints=constraints, base_logger=self._base_logger
        )
        middleware.insert(0, MessageListenerMatches(keyword))
        return self._register_listener(list(functions), primary_matcher, matchers, middleware, True)

    return __call__
```

Registers a new message event listener. This method can be used as either a decorator or a method. Check the `App#event` method's docstring for details.

```text
# Use this method as a decorator
@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")

# Pass a function to this method
app.message(":wave:")(say_hello)
```

Refer to [https://docs.slack.dev/reference/events/message/](https://docs.slack.dev/reference/events/message/) for details of `message` events.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `keyword`

The keyword to match

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def message_shortcut(self,   callback_id: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def message_shortcut(
    self,
    callback_id: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new message shortcut listener."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.message_shortcut(callback_id, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new message shortcut listener.

`def middleware(self, *args) ‑> Callable | None`

Expand source code

```python
def middleware(self, *args) -> Optional[Callable]:
    """Registers a new middleware to this app.
    This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.middleware
        def middleware_func(logger, body, next):
            logger.info(f"request body: {body}")
            next()

        # Pass a function to this method
        app.middleware(middleware_func)

    Refer to https://docs.slack.dev/tools/bolt-python/concepts/global-middleware for details.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        *args: A function that works as a global middleware.
    """
    if len(args) > 0:
        middleware_or_callable = args[0]
        if isinstance(middleware_or_callable, Middleware):
            middleware: Middleware = middleware_or_callable
            self._middleware_list.append(middleware)
            if isinstance(middleware, Assistant) and middleware.thread_context_store is not None:
                self._assistant_thread_context_store = middleware.thread_context_store
        elif callable(middleware_or_callable):
            self._middleware_list.append(
                CustomMiddleware(
                    app_name=self.name,
                    func=middleware_or_callable,
                    base_logger=self._base_logger,
                )
            )
            return middleware_or_callable
        else:
            raise BoltError(f"Unexpected type for a middleware ({type(middleware_or_callable)})")
    return None
```

Registers a new middleware to this app. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.middleware
def middleware_func(logger, body, next):
    logger.info(f"request body: {body}")
    next()

# Pass a function to this method
app.middleware(middleware_func)
```

Refer to [https://docs.slack.dev/tools/bolt-python/concepts/global-middleware](https://docs.slack.dev/tools/bolt-python/concepts/global-middleware) for details.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `*args`

A function that works as a global middleware.

`def options(self,   constraints: str | Pattern | Dict[str, str | Pattern],   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def options(
    self,
    constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new options listener.
    This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.options("menu_selection")
        def show_menu_options(ack):
            options = [
                {
                    "text": {"type": "plain_text", "text": "Option 1"},
                    "value": "1-1",
                },
                {
                    "text": {"type": "plain_text", "text": "Option 2"},
                    "value": "1-2",
                },
            ]
            ack(options=options)

        # Pass a function to this method
        app.options("menu_selection")(show_menu_options)

    Refer to the following documents for details:

    * https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_select
    * https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external_multi_select

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.options(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new options listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.options("menu_selection")
def show_menu_options(ack):
    options = [
        {
            "text": {"type": "plain_text", "text": "Option 1"},
            "value": "1-1",
        },
        {
            "text": {"type": "plain_text", "text": "Option 2"},
            "value": "1-2",
        },
    ]
    ack(options=options)

# Pass a function to this method
app.options("menu_selection")(show_menu_options)
```

Refer to the following documents for details:

* [https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external\_select](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_select)
* [https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external\_multi\_select](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external_multi_select)

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def shortcut(self,   constraints: str | Pattern | Dict[str, str | Pattern],   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def shortcut(
    self,
    constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new shortcut listener.
    This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.shortcut("open_modal")
        def open_modal(ack, body, client):
            # Acknowledge the command request
            ack()
            # Call views_open with the built-in client
            client.views_open(
                # Pass a valid trigger_id within 3 seconds of receiving it
                trigger_id=body["trigger_id"],
                # View payload
                view={ ... }
            )

        # Pass a function to this method
        app.shortcut("open_modal")(open_modal)

    Refer to https://docs.slack.dev/interactivity/implementing-shortcuts/ for details about Shortcuts.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        constraints: The conditions that match a request payload.
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.shortcut(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new shortcut listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.shortcut("open_modal")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={ ... }
    )

# Pass a function to this method
app.shortcut("open_modal")(open_modal)
```

Refer to [https://docs.slack.dev/interactivity/implementing-shortcuts/](https://docs.slack.dev/interactivity/implementing-shortcuts/) for details about Shortcuts.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `constraints`

The conditions that match a request payload.

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def start(self,   port: int = 3000,   path: str = '/slack/events',   http_server_logger_enabled: bool = True) ‑> None`

Expand source code

```python
def start(
    self,
    port: int = 3000,
    path: str = "/slack/events",
    http_server_logger_enabled: bool = True,
) -> None:
    """Starts a web server for local development.

        # With the default settings, `http://localhost:3000/slack/events`
        # is available for handling incoming requests from Slack
        app.start()

    This method internally starts a Web server process built with the `http.server` module.
    For production, consider using a production-ready WSGI server such as Gunicorn.

    Args:
        port: The port to listen on (Default: 3000)
        path: The path to handle request from Slack (Default: `/slack/events`)
        http_server_logger_enabled: The flag to enable http.server logging if True (Default: True)
    """
    self._development_server = SlackAppDevelopmentServer(
        port=port,
        path=path,
        app=self,
        oauth_flow=self.oauth_flow,
        http_server_logger_enabled=http_server_logger_enabled,
    )
    self._development_server.start()
```

Starts a web server for local development.

```text
# With the default settings, `http://localhost:3000/slack/events`
# is available for handling incoming requests from Slack
app.start()
```

This method internally starts a Web server process built with the `http.server` module. For production, consider using a production-ready WSGI server such as Gunicorn.

## Args

## `port`

The port to listen on (Default: 3000)

## `path`

The path to handle request from Slack (Default: `/slack/events`)

## `http_server_logger_enabled`

The flag to enable http.server logging if True (Default: True)

`def step(self,   callback_id: str | Pattern | [WorkflowStep](workflows/step/step.html#slack_bolt.workflows.step.step.WorkflowStep "slack_bolt.workflows.step.step.WorkflowStep") | [WorkflowStepBuilder](workflows/step/step.html#slack_bolt.workflows.step.step.WorkflowStepBuilder "slack_bolt.workflows.step.step.WorkflowStepBuilder"),   edit: Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | [Listener](listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Sequence[Callable] | None = None,   save: Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | [Listener](listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Sequence[Callable] | None = None,   execute: Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | [Listener](listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Sequence[Callable] | None = None)`

Expand source code

```python
def step(
    self,
    callback_id: Union[str, Pattern, WorkflowStep, WorkflowStepBuilder],
    edit: Optional[Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]]] = None,
    save: Optional[Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]]] = None,
    execute: Optional[Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]]] = None,
):
    """
    Deprecated:
        Steps from apps for legacy workflows are now deprecated.
        Use new custom steps: https://docs.slack.dev/workflows/workflow-steps/

    Registers a new step from app listener.

    Unlike others, this method doesn't behave as a decorator.
    If you want to register a step from app by a decorator, use `WorkflowStepBuilder`'s methods.

        # Create a new WorkflowStep instance
        from slack_bolt.workflows.step import WorkflowStep
        ws = WorkflowStep(
            callback_id="add_task",
            edit=edit,
            save=save,
            execute=execute,
        )
        # Pass Step to set up listeners
        app.step(ws)

    Refer to https://docs.slack.dev/legacy/legacy-steps-from-apps/ for details of steps from apps.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    For further information about WorkflowStep specific function arguments
    such as `configure`, `update`, `complete`, and `fail`,
    refer to `slack_bolt.workflows.step.utilities` API documents.

    Args:
        callback_id: The Callback ID for this step from app
        edit: The function for displaying a modal in the Workflow Builder
        save: The function for handling configuration in the Workflow Builder
        execute: The function for handling the step execution
    """
    warnings.warn(
        (
            "Steps from apps for legacy workflows are now deprecated. "
            "Use new custom steps: https://docs.slack.dev/workflows/workflow-steps/"
        ),
        category=DeprecationWarning,
    )
    step = callback_id
    if isinstance(callback_id, (str, Pattern)):
        step = WorkflowStep(
            callback_id=callback_id,
            edit=edit,  # type: ignore[arg-type]
            save=save,  # type: ignore[arg-type]
            execute=execute,  # type: ignore[arg-type]
            base_logger=self._base_logger,
        )
    elif isinstance(step, WorkflowStepBuilder):
        step = step.build(base_logger=self._base_logger)
    elif not isinstance(step, WorkflowStep):
        raise BoltError(f"Invalid step object ({type(step)})")

    self.use(WorkflowStepMiddleware(step))
```

## Deprecated

Steps from apps for legacy workflows are now deprecated. Use new custom steps: [https://docs.slack.dev/workflows/workflow-steps/](https://docs.slack.dev/workflows/workflow-steps/)

Registers a new step from app listener.

Unlike others, this method doesn't behave as a decorator. If you want to register a step from app by a decorator, use `WorkflowStepBuilder`'s methods.

```text
# Create a new WorkflowStep instance
from slack_bolt.workflows.step import WorkflowStep
ws = WorkflowStep(
    callback_id="add_task",
    edit=edit,
    save=save,
    execute=execute,
)
# Pass Step to set up listeners
app.step(ws)
```

Refer to [https://docs.slack.dev/legacy/legacy-steps-from-apps/](https://docs.slack.dev/legacy/legacy-steps-from-apps/) for details of steps from apps.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

For further information about WorkflowStep specific function arguments such as `configure`, `update`, `complete`, and `fail`, refer to `[slack_bolt.workflows.step.utilities](workflows/step/utilities/index.html "slack_bolt.workflows.step.utilities")` API documents.

## Args

## `callback_id`

The Callback ID for this step from app

## `edit`

The function for displaying a modal in the Workflow Builder

## `save`

The function for handling configuration in the Workflow Builder

## `execute`

The function for handling the step execution

`def use(self, *args) ‑> Callable | None`

Expand source code

```python
def use(self, *args) -> Optional[Callable]:
    """Registers a new global middleware to this app. This method can be used as either a decorator or a method.

    Refer to `App#middleware()` method's docstring for details."""
    return self.middleware(*args)
```

Registers a new global middleware to this app. This method can be used as either a decorator or a method.

Refer to `App#middleware()` method's docstring for details.

`def view(self,   constraints: str | Pattern | Dict[str, str | Pattern],   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def view(
    self,
    constraints: Union[str, Pattern, Dict[str, Union[str, Pattern]]],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `view_submission`/`view_closed` event listener.
    This method can be used as either a decorator or a method.

        # Use this method as a decorator
        @app.view("view_1")
        def handle_submission(ack, body, client, view):
            # Assume there's an input block with `block_c` as the block_id and `dreamy_input`
            hopes_and_dreams = view["state"]["values"]["block_c"]["dreamy_input"]
            user = body["user"]["id"]
            # Validate the inputs
            errors = {}
            if hopes_and_dreams is not None and len(hopes_and_dreams) <= 5:
                errors["block_c"] = "The value must be longer than 5 characters"
            if len(errors) > 0:
                ack(response_action="errors", errors=errors)
                return
            # Acknowledge the view_submission event and close the modal
            ack()
            # Do whatever you want with the input data - here we're saving it to a DB

        # Pass a function to this method
        app.view("view_1")(handle_submission)

    Refer to https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload for details of payloads.

    To learn available arguments for middleware/listeners, see `slack_bolt.kwargs_injection.args`'s API document.

    Args:
        constraints: The conditions that match a request payload
        matchers: A list of listener matcher functions.
            Only when all the matchers return True, the listener function can be invoked.
        middleware: A list of lister middleware functions.
            Only when all the middleware call `next()` method, the listener function can be invoked.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.view(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `view_submission`/`view_closed` event listener. This method can be used as either a decorator or a method.

```text
# Use this method as a decorator
@app.view("view_1")
def handle_submission(ack, body, client, view):
    # Assume there's an input block with <code>block\_c</code> as the block_id and <code>dreamy\_input</code>
    hopes_and_dreams = view["state"]["values"]["block_c"]["dreamy_input"]
    user = body["user"]["id"]
    # Validate the inputs
    errors = {}
    if hopes_and_dreams is not None and len(hopes_and_dreams) <= 5:
        errors["block_c"] = "The value must be longer than 5 characters"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    # Acknowledge the view_submission event and close the modal
    ack()
    # Do whatever you want with the input data - here we're saving it to a DB

# Pass a function to this method
app.view("view_1")(handle_submission)
```

Refer to [https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload) for details of payloads.

To learn available arguments for middleware/listeners, see `[slack_bolt.kwargs_injection.args](kwargs_injection/args.html "slack_bolt.kwargs_injection.args")`'s API document.

## Args

## `constraints`

The conditions that match a request payload

## `matchers`

A list of listener matcher functions. Only when all the matchers return True, the listener function can be invoked.

## `middleware`

A list of lister middleware functions. Only when all the middleware call `next()` method, the listener function can be invoked.

`def view_closed(self,   constraints: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def view_closed(
    self,
    constraints: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `view_closed` listener.
    Refer to https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view_closed for details."""

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.view_closed(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `view_closed` listener. Refer to [https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view\_closed](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view_closed) for details.

`def view_submission(self,   constraints: str | Pattern,   matchers: Sequence[Callable[..., bool]] | None = None,   middleware: Sequence[Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None) ‑> Callable[..., Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | None]`

Expand source code

```python
def view_submission(
    self,
    constraints: Union[str, Pattern],
    matchers: Optional[Sequence[Callable[..., bool]]] = None,
    middleware: Optional[Sequence[Union[Callable, Middleware]]] = None,
) -> Callable[..., Optional[Callable[..., Optional[BoltResponse]]]]:
    """Registers a new `view_submission` listener.
    Refer to https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view_submission for
    details.
    """

    def __call__(*args, **kwargs):
        functions = self._to_listener_functions(kwargs) if kwargs else list(args)
        primary_matcher = builtin_matchers.view_submission(constraints, base_logger=self._base_logger)
        return self._register_listener(list(functions), primary_matcher, matchers, middleware)

    return __call__
```

Registers a new `view_submission` listener. Refer to [https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view\_submission](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload/#view_submission) for details.

`class Args (*,   logger: logging.Logger,   client: slack_sdk.web.client.WebClient,   req: [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse"),   context: [BoltContext](context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext"),   body: Dict[str, Any],   payload: Dict[str, Any],   options: Dict[str, Any] | None = None,   shortcut: Dict[str, Any] | None = None,   action: Dict[str, Any] | None = None,   view: Dict[str, Any] | None = None,   command: Dict[str, Any] | None = None,   event: Dict[str, Any] | None = None,   message: Dict[str, Any] | None = None,   ack: [Ack](context/ack/ack.html#slack_bolt.context.ack.ack.Ack "slack_bolt.context.ack.ack.Ack"),   say: [Say](context/say/say.html#slack_bolt.context.say.say.Say "slack_bolt.context.say.say.Say"),   respond: [Respond](context/respond/respond.html#slack_bolt.context.respond.respond.Respond "slack_bolt.context.respond.respond.Respond"),   complete: [Complete](context/complete/complete.html#slack_bolt.context.complete.complete.Complete "slack_bolt.context.complete.complete.Complete"),   fail: [Fail](context/fail/fail.html#slack_bolt.context.fail.fail.Fail "slack_bolt.context.fail.fail.Fail"),   set_status: [SetStatus](context/set_status/set_status.html#slack_bolt.context.set_status.set_status.SetStatus "slack_bolt.context.set_status.set_status.SetStatus") | None = None,   set_title: [SetTitle](context/set_title/set_title.html#slack_bolt.context.set_title.set_title.SetTitle "slack_bolt.context.set_title.set_title.SetTitle") | None = None,   set_suggested_prompts: [SetSuggestedPrompts](context/set_suggested_prompts/set_suggested_prompts.html#slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts "slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts") | None = None,   get_thread_context: [GetThreadContext](context/get_thread_context/get_thread_context.html#slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext "slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext") | None = None,   save_thread_context: [SaveThreadContext](context/save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext") | None = None,   next: Callable[[], None],   **kwargs)`

Expand source code

```python
class Args:
    """All the arguments in this class are available in any middleware / listeners.
    You can inject the named variables in the argument list in arbitrary order.

        @app.action("link_button")
        def handle_buttons(ack, respond, logger, context, body, client):
            logger.info(f"request body: {body}")
            ack()
            if context.channel_id is not None:
                respond("Hi!")
            client.views_open(
                trigger_id=body["trigger_id"],
                view={ ... }
            )

    Alternatively, you can include a parameter named `args` and it will be injected with an instance of this class.

        @app.action("link_button")
        def handle_buttons(args):
            args.logger.info(f"request body: {args.body}")
            args.ack()
            if args.context.channel_id is not None:
                args.respond("Hi!")
            args.client.views_open(
                trigger_id=args.body["trigger_id"],
                view={ ... }
            )

    """

    client: WebClient
    """`slack_sdk.web.WebClient` instance with a valid token"""
    logger: Logger
    """Logger instance"""
    req: BoltRequest
    """Incoming request from Slack"""
    resp: BoltResponse
    """Response representation"""
    request: BoltRequest
    """Incoming request from Slack"""
    response: BoltResponse
    """Response representation"""
    context: BoltContext
    """Context data associated with the incoming request"""
    body: Dict[str, Any]
    """Parsed request body data"""
    # payload
    payload: Dict[str, Any]
    """The unwrapped core data in the request body"""
    options: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.options` listener"""
    shortcut: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.shortcut` listener"""
    action: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.action` listener"""
    view: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.view` listener"""
    command: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.command` listener"""
    event: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.event` listener"""
    message: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.message` listener"""
    # utilities
    ack: Ack
    """`ack()` utility function, which returns acknowledgement to the Slack servers"""
    say: Say
    """`say()` utility function, which calls `chat.postMessage` API with the associated channel ID"""
    respond: Respond
    """`respond()` utility function, which utilizes the associated `response_url`"""
    complete: Complete
    """`complete()` utility function, signals a successful completion of the custom function"""
    fail: Fail
    """`fail()` utility function, signal that the custom function failed to complete"""
    set_status: Optional[SetStatus]
    """`set_status()` utility function for AI Agents & Assistants"""
    set_title: Optional[SetTitle]
    """`set_title()` utility function for AI Agents & Assistants"""
    set_suggested_prompts: Optional[SetSuggestedPrompts]
    """`set_suggested_prompts()` utility function for AI Agents & Assistants"""
    get_thread_context: Optional[GetThreadContext]
    """`get_thread_context()` utility function for AI Agents & Assistants"""
    save_thread_context: Optional[SaveThreadContext]
    """`save_thread_context()` utility function for AI Agents & Assistants"""
    # middleware
    next: Callable[[], None]
    """`next()` utility function, which tells the middleware chain that it can continue with the next one"""
    next_: Callable[[], None]
    """An alias of `next()` for avoiding the Python built-in method overrides in middleware functions"""

    def __init__(
        self,
        *,
        logger: logging.Logger,
        client: WebClient,
        req: BoltRequest,
        resp: BoltResponse,
        context: BoltContext,
        body: Dict[str, Any],
        payload: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None,
        shortcut: Optional[Dict[str, Any]] = None,
        action: Optional[Dict[str, Any]] = None,
        view: Optional[Dict[str, Any]] = None,
        command: Optional[Dict[str, Any]] = None,
        event: Optional[Dict[str, Any]] = None,
        message: Optional[Dict[str, Any]] = None,
        ack: Ack,
        say: Say,
        respond: Respond,
        complete: Complete,
        fail: Fail,
        set_status: Optional[SetStatus] = None,
        set_title: Optional[SetTitle] = None,
        set_suggested_prompts: Optional[SetSuggestedPrompts] = None,
        get_thread_context: Optional[GetThreadContext] = None,
        save_thread_context: Optional[SaveThreadContext] = None,
        # As this method is not supposed to be invoked by bolt-python users,
        # the naming conflict with the built-in one affects
        # only the internals of this method
        next: Callable[[], None],
        **kwargs,  # noqa
    ):
        self.logger: logging.Logger = logger
        self.client: WebClient = client
        self.request = self.req = req
        self.response = self.resp = resp
        self.context: BoltContext = context

        self.body: Dict[str, Any] = body
        self.payload: Dict[str, Any] = payload
        self.options: Optional[Dict[str, Any]] = options
        self.shortcut: Optional[Dict[str, Any]] = shortcut
        self.action: Optional[Dict[str, Any]] = action
        self.view: Optional[Dict[str, Any]] = view
        self.command: Optional[Dict[str, Any]] = command
        self.event: Optional[Dict[str, Any]] = event
        self.message: Optional[Dict[str, Any]] = message

        self.ack: Ack = ack
        self.say: Say = say
        self.respond: Respond = respond
        self.complete: Complete = complete
        self.fail: Fail = fail

        self.set_status = set_status
        self.set_title = set_title
        self.set_suggested_prompts = set_suggested_prompts
        self.get_thread_context = get_thread_context
        self.save_thread_context = save_thread_context

        self.next: Callable[[], None] = next
        self.next_: Callable[[], None] = next
```

All the arguments in this class are available in any middleware / listeners. You can inject the named variables in the argument list in arbitrary order.

```text
@app.action("link_button")
def handle_buttons(ack, respond, logger, context, body, client):
    logger.info(f"request body: {body}")
    ack()
    if context.channel_id is not None:
        respond("Hi!")
    client.views_open(
        trigger_id=body["trigger_id"],
        view={ ... }
    )
```

Alternatively, you can include a parameter named `args` and it will be injected with an instance of this class.

```text
@app.action("link_button")
def handle_buttons(args):
    args.logger.info(f"request body: {args.body}")
    args.ack()
    if args.context.channel_id is not None:
        args.respond("Hi!")
    args.client.views_open(
        trigger_id=args.body["trigger_id"],
        view={ ... }
    )
```

### Class variables

`var ack : [Ack](context/ack/ack.html#slack_bolt.context.ack.ack.Ack "slack_bolt.context.ack.ack.Ack")`

`ack()` utility function, which returns acknowledgement to the Slack servers

`var action : Dict[str, Any] | None`

An alias for payload in an `@app.action` listener

`var body : Dict[str, Any]`

Parsed request body data

`var client : slack_sdk.web.client.WebClient`

`slack_sdk.web.WebClient` instance with a valid token

`var command : Dict[str, Any] | None`

An alias for payload in an `@app.command` listener

`var complete : [Complete](context/complete/complete.html#slack_bolt.context.complete.complete.Complete "slack_bolt.context.complete.complete.Complete")`

`complete()` utility function, signals a successful completion of the custom function

`var context : [BoltContext](context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext")`

Context data associated with the incoming request

`var event : Dict[str, Any] | None`

An alias for payload in an `@app.event` listener

`var fail : [Fail](context/fail/fail.html#slack_bolt.context.fail.fail.Fail "slack_bolt.context.fail.fail.Fail")`

`fail()` utility function, signal that the custom function failed to complete

`var get_thread_context : [GetThreadContext](context/get_thread_context/get_thread_context.html#slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext "slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext") | None`

`get_thread_context()` utility function for AI Agents & Assistants

`var logger : logging.Logger`

Logger instance

`var message : Dict[str, Any] | None`

An alias for payload in an `@app.message` listener

`var next : Callable[[], None]`

`next()` utility function, which tells the middleware chain that it can continue with the next one

`var next_ : Callable[[], None]`

An alias of `next()` for avoiding the Python built-in method overrides in middleware functions

`var options : Dict[str, Any] | None`

An alias for payload in an `@app.options` listener

`var payload : Dict[str, Any]`

The unwrapped core data in the request body

`var req : [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")`

Incoming request from Slack

`var request : [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")`

Incoming request from Slack

`var resp : [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Response representation

`var respond : [Respond](context/respond/respond.html#slack_bolt.context.respond.respond.Respond "slack_bolt.context.respond.respond.Respond")`

`respond()` utility function, which utilizes the associated `response_url`

`var response : [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Response representation

`var save_thread_context : [SaveThreadContext](context/save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext") | None`

`save_thread_context()` utility function for AI Agents & Assistants

`var say : [Say](context/say/say.html#slack_bolt.context.say.say.Say "slack_bolt.context.say.say.Say")`

`say()` utility function, which calls `chat.postMessage` API with the associated channel ID

`var set_status : [SetStatus](context/set_status/set_status.html#slack_bolt.context.set_status.set_status.SetStatus "slack_bolt.context.set_status.set_status.SetStatus") | None`

`set_status()` utility function for AI Agents & Assistants

`var set_suggested_prompts : [SetSuggestedPrompts](context/set_suggested_prompts/set_suggested_prompts.html#slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts "slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts") | None`

`set_suggested_prompts()` utility function for AI Agents & Assistants

`var set_title : [SetTitle](context/set_title/set_title.html#slack_bolt.context.set_title.set_title.SetTitle "slack_bolt.context.set_title.set_title.SetTitle") | None`

`set_title()` utility function for AI Agents & Assistants

`var shortcut : Dict[str, Any] | None`

An alias for payload in an `@app.shortcut` listener

`var view : Dict[str, Any] | None`

An alias for payload in an `@app.view` listener

`class Assistant (*,   app_name: str = 'assistant',   thread_context_store: [AssistantThreadContextStore](context/assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore") | None = None,   logger: logging.Logger | None = None)`

Expand source code

```python
class Assistant(Middleware):
    _thread_started_listeners: Optional[List[Listener]]
    _thread_context_changed_listeners: Optional[List[Listener]]
    _user_message_listeners: Optional[List[Listener]]
    _bot_message_listeners: Optional[List[Listener]]

    thread_context_store: Optional[AssistantThreadContextStore]
    base_logger: Optional[logging.Logger]

    def __init__(
        self,
        *,
        app_name: str = "assistant",
        thread_context_store: Optional[AssistantThreadContextStore] = None,
        logger: Optional[logging.Logger] = None,
    ):
        self.app_name = app_name
        self.thread_context_store = thread_context_store
        self.base_logger = logger

        self._thread_started_listeners = None
        self._thread_context_changed_listeners = None
        self._user_message_listeners = None
        self._bot_message_listeners = None

    def thread_started(
        self,
        *args,
        matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
        middleware: Optional[Union[Callable, Middleware]] = None,
        lazy: Optional[List[Callable[..., None]]] = None,
    ):
        if self._thread_started_listeners is None:
            self._thread_started_listeners = []
        all_matchers = self._merge_matchers(is_assistant_thread_started_event, matchers)
        if is_used_without_argument(args):
            func = args[0]
            self._thread_started_listeners.append(
                self.build_listener(
                    listener_or_functions=func,
                    matchers=all_matchers,
                    middleware=middleware,  # type:ignore[arg-type]
                )
            )
            return func

        def _inner(func):
            functions = [func] + (lazy if lazy is not None else [])
            self._thread_started_listeners.append(
                self.build_listener(
                    listener_or_functions=functions,
                    matchers=all_matchers,
                    middleware=middleware,
                )
            )

            @wraps(func)
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrapper

        return _inner

    def user_message(
        self,
        *args,
        matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
        middleware: Optional[Union[Callable, Middleware]] = None,
        lazy: Optional[List[Callable[..., None]]] = None,
    ):
        if self._user_message_listeners is None:
            self._user_message_listeners = []
        all_matchers = self._merge_matchers(is_user_message_event_in_assistant_thread, matchers)
        if is_used_without_argument(args):
            func = args[0]
            self._user_message_listeners.append(
                self.build_listener(
                    listener_or_functions=func,
                    matchers=all_matchers,
                    middleware=middleware,  # type:ignore[arg-type]
                )
            )
            return func

        def _inner(func):
            functions = [func] + (lazy if lazy is not None else [])
            self._user_message_listeners.append(
                self.build_listener(
                    listener_or_functions=functions,
                    matchers=all_matchers,
                    middleware=middleware,
                )
            )

            @wraps(func)
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrapper

        return _inner

    def bot_message(
        self,
        *args,
        matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
        middleware: Optional[Union[Callable, Middleware]] = None,
        lazy: Optional[List[Callable[..., None]]] = None,
    ):
        if self._bot_message_listeners is None:
            self._bot_message_listeners = []
        all_matchers = self._merge_matchers(is_bot_message_event_in_assistant_thread, matchers)
        if is_used_without_argument(args):
            func = args[0]
            self._bot_message_listeners.append(
                self.build_listener(
                    listener_or_functions=func,
                    matchers=all_matchers,
                    middleware=middleware,  # type:ignore[arg-type]
                )
            )
            return func

        def _inner(func):
            functions = [func] + (lazy if lazy is not None else [])
            self._bot_message_listeners.append(
                self.build_listener(
                    listener_or_functions=functions,
                    matchers=all_matchers,
                    middleware=middleware,
                )
            )

            @wraps(func)
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrapper

        return _inner

    def thread_context_changed(
        self,
        *args,
        matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
        middleware: Optional[Union[Callable, Middleware]] = None,
        lazy: Optional[List[Callable[..., None]]] = None,
    ):
        if self._thread_context_changed_listeners is None:
            self._thread_context_changed_listeners = []
        all_matchers = self._merge_matchers(is_assistant_thread_context_changed_event, matchers)
        if is_used_without_argument(args):
            func = args[0]
            self._thread_context_changed_listeners.append(
                self.build_listener(
                    listener_or_functions=func,
                    matchers=all_matchers,
                    middleware=middleware,  # type:ignore[arg-type]
                )
            )
            return func

        def _inner(func):
            functions = [func] + (lazy if lazy is not None else [])
            self._thread_context_changed_listeners.append(
                self.build_listener(
                    listener_or_functions=functions,
                    matchers=all_matchers,
                    middleware=middleware,
                )
            )

            @wraps(func)
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrapper

        return _inner

    def _merge_matchers(
        self,
        primary_matcher: Callable[..., bool],
        custom_matchers: Optional[Union[Callable[..., bool], ListenerMatcher]],
    ):
        return [CustomListenerMatcher(app_name=self.app_name, func=primary_matcher)] + (
            custom_matchers or []
        )  # type:ignore[operator]

    @staticmethod
    def default_thread_context_changed(save_thread_context: SaveThreadContext, payload: dict):
        save_thread_context(payload["assistant_thread"]["context"])

    def process(  # type:ignore[return]
        self, *, req: BoltRequest, resp: BoltResponse, next: Callable[[], BoltResponse]
    ) -> Optional[BoltResponse]:
        if self._thread_context_changed_listeners is None:
            self.thread_context_changed(self.default_thread_context_changed)

        listener_runner: ThreadListenerRunner = req.context.listener_runner
        for listeners in [
            self._thread_started_listeners,
            self._thread_context_changed_listeners,
            self._user_message_listeners,
            self._bot_message_listeners,
        ]:
            if listeners is not None:
                for listener in listeners:
                    if listener.matches(req=req, resp=resp):
                        return listener_runner.run(
                            request=req,
                            response=resp,
                            listener_name="assistant_listener",
                            listener=listener,
                        )
        if is_other_message_sub_event_in_assistant_thread(req.body):
            # message_changed, message_deleted, etc.
            return req.context.ack()

        next()

    def build_listener(
        self,
        listener_or_functions: Union[Listener, Callable, List[Callable]],
        matchers: Optional[List[Union[ListenerMatcher, Callable[..., bool]]]] = None,
        middleware: Optional[List[Middleware]] = None,
        base_logger: Optional[Logger] = None,
    ) -> Listener:
        if isinstance(listener_or_functions, Callable):  # type:ignore[arg-type]
            listener_or_functions = [listener_or_functions]  # type:ignore[list-item]

        if isinstance(listener_or_functions, Listener):
            return listener_or_functions
        elif isinstance(listener_or_functions, list):
            middleware = middleware if middleware else []
            functions = listener_or_functions
            ack_function = functions.pop(0)

            matchers = matchers if matchers else []
            listener_matchers: List[ListenerMatcher] = []
            for matcher in matchers:
                if isinstance(matcher, ListenerMatcher):
                    listener_matchers.append(matcher)
                elif isinstance(matcher, Callable):  # type:ignore[arg-type]
                    listener_matchers.append(
                        build_listener_matcher(
                            func=matcher,
                            asyncio=False,
                            base_logger=base_logger,
                        )
                    )
            return CustomListener(
                app_name=self.app_name,
                matchers=listener_matchers,
                middleware=middleware,
                ack_function=ack_function,
                lazy_functions=functions,
                auto_acknowledgement=True,
                base_logger=base_logger or self.base_logger,
            )
        else:
            raise BoltError(f"Invalid listener: {type(listener_or_functions)} detected")
```

A middleware can process request data before other middleware and listener functions.

### Ancestors

* [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Class variables

`var base_logger : logging.Logger | None`

The type of the None singleton.

`var thread_context_store : [AssistantThreadContextStore](context/assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore") | None`

The type of the None singleton.

### Static methods

`def default_thread_context_changed(save_thread_context: [SaveThreadContext](context/save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext"),   payload: dict)`

Expand source code

```text
@staticmethod
def default_thread_context_changed(save_thread_context: SaveThreadContext, payload: dict):
    save_thread_context(payload["assistant_thread"]["context"])
```

### Methods

`def bot_message(self,   *args,   matchers: Callable[..., bool] | [ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher") | None = None,   middleware: Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware") | None = None,   lazy: List[Callable[..., None]] | None = None)`

Expand source code

```python
def bot_message(
    self,
    *args,
    matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
    middleware: Optional[Union[Callable, Middleware]] = None,
    lazy: Optional[List[Callable[..., None]]] = None,
):
    if self._bot_message_listeners is None:
        self._bot_message_listeners = []
    all_matchers = self._merge_matchers(is_bot_message_event_in_assistant_thread, matchers)
    if is_used_without_argument(args):
        func = args[0]
        self._bot_message_listeners.append(
            self.build_listener(
                listener_or_functions=func,
                matchers=all_matchers,
                middleware=middleware,  # type:ignore[arg-type]
            )
        )
        return func

    def _inner(func):
        functions = [func] + (lazy if lazy is not None else [])
        self._bot_message_listeners.append(
            self.build_listener(
                listener_or_functions=functions,
                matchers=all_matchers,
                middleware=middleware,
            )
        )

        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrapper

    return _inner
```

`def build_listener(self,   listener_or_functions: [Listener](listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Callable | List[Callable],   matchers: List[[ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher") | Callable[..., bool]] | None = None,   middleware: List[[Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None,   base_logger: logging.Logger | None = None) ‑> [Listener](listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")`

Expand source code

```python
def build_listener(
    self,
    listener_or_functions: Union[Listener, Callable, List[Callable]],
    matchers: Optional[List[Union[ListenerMatcher, Callable[..., bool]]]] = None,
    middleware: Optional[List[Middleware]] = None,
    base_logger: Optional[Logger] = None,
) -> Listener:
    if isinstance(listener_or_functions, Callable):  # type:ignore[arg-type]
        listener_or_functions = [listener_or_functions]  # type:ignore[list-item]

    if isinstance(listener_or_functions, Listener):
        return listener_or_functions
    elif isinstance(listener_or_functions, list):
        middleware = middleware if middleware else []
        functions = listener_or_functions
        ack_function = functions.pop(0)

        matchers = matchers if matchers else []
        listener_matchers: List[ListenerMatcher] = []
        for matcher in matchers:
            if isinstance(matcher, ListenerMatcher):
                listener_matchers.append(matcher)
            elif isinstance(matcher, Callable):  # type:ignore[arg-type]
                listener_matchers.append(
                    build_listener_matcher(
                        func=matcher,
                        asyncio=False,
                        base_logger=base_logger,
                    )
                )
        return CustomListener(
            app_name=self.app_name,
            matchers=listener_matchers,
            middleware=middleware,
            ack_function=ack_function,
            lazy_functions=functions,
            auto_acknowledgement=True,
            base_logger=base_logger or self.base_logger,
        )
    else:
        raise BoltError(f"Invalid listener: {type(listener_or_functions)} detected")
```

`def thread_context_changed(self,   *args,   matchers: Callable[..., bool] | [ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher") | None = None,   middleware: Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware") | None = None,   lazy: List[Callable[..., None]] | None = None)`

Expand source code

```python
def thread_context_changed(
    self,
    *args,
    matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
    middleware: Optional[Union[Callable, Middleware]] = None,
    lazy: Optional[List[Callable[..., None]]] = None,
):
    if self._thread_context_changed_listeners is None:
        self._thread_context_changed_listeners = []
    all_matchers = self._merge_matchers(is_assistant_thread_context_changed_event, matchers)
    if is_used_without_argument(args):
        func = args[0]
        self._thread_context_changed_listeners.append(
            self.build_listener(
                listener_or_functions=func,
                matchers=all_matchers,
                middleware=middleware,  # type:ignore[arg-type]
            )
        )
        return func

    def _inner(func):
        functions = [func] + (lazy if lazy is not None else [])
        self._thread_context_changed_listeners.append(
            self.build_listener(
                listener_or_functions=functions,
                matchers=all_matchers,
                middleware=middleware,
            )
        )

        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrapper

    return _inner
```

`def thread_started(self,   *args,   matchers: Callable[..., bool] | [ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher") | None = None,   middleware: Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware") | None = None,   lazy: List[Callable[..., None]] | None = None)`

Expand source code

```python
def thread_started(
    self,
    *args,
    matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
    middleware: Optional[Union[Callable, Middleware]] = None,
    lazy: Optional[List[Callable[..., None]]] = None,
):
    if self._thread_started_listeners is None:
        self._thread_started_listeners = []
    all_matchers = self._merge_matchers(is_assistant_thread_started_event, matchers)
    if is_used_without_argument(args):
        func = args[0]
        self._thread_started_listeners.append(
            self.build_listener(
                listener_or_functions=func,
                matchers=all_matchers,
                middleware=middleware,  # type:ignore[arg-type]
            )
        )
        return func

    def _inner(func):
        functions = [func] + (lazy if lazy is not None else [])
        self._thread_started_listeners.append(
            self.build_listener(
                listener_or_functions=functions,
                matchers=all_matchers,
                middleware=middleware,
            )
        )

        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrapper

    return _inner
```

`def user_message(self,   *args,   matchers: Callable[..., bool] | [ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher") | None = None,   middleware: Callable | [Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware") | None = None,   lazy: List[Callable[..., None]] | None = None)`

Expand source code

```python
def user_message(
    self,
    *args,
    matchers: Optional[Union[Callable[..., bool], ListenerMatcher]] = None,
    middleware: Optional[Union[Callable, Middleware]] = None,
    lazy: Optional[List[Callable[..., None]]] = None,
):
    if self._user_message_listeners is None:
        self._user_message_listeners = []
    all_matchers = self._merge_matchers(is_user_message_event_in_assistant_thread, matchers)
    if is_used_without_argument(args):
        func = args[0]
        self._user_message_listeners.append(
            self.build_listener(
                listener_or_functions=func,
                matchers=all_matchers,
                middleware=middleware,  # type:ignore[arg-type]
            )
        )
        return func

    def _inner(func):
        functions = [func] + (lazy if lazy is not None else [])
        self._user_message_listeners.append(
            self.build_listener(
                listener_or_functions=functions,
                matchers=all_matchers,
                middleware=middleware,
            )
        )

        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrapper

    return _inner
```

### Inherited members

* `**[Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`

`class AssistantThreadContext (payload: dict)`

Expand source code

```python
class AssistantThreadContext(dict):
    enterprise_id: Optional[str]
    team_id: Optional[str]
    channel_id: str

    def __init__(self, payload: dict):
        dict.__init__(self, **payload)
        self.enterprise_id = payload.get("enterprise_id")
        self.team_id = payload.get("team_id")
        self.channel_id = payload["channel_id"]
```

dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)

### Ancestors

* builtins.dict

### Class variables

`var channel_id : str`

The type of the None singleton.

`var enterprise_id : str | None`

The type of the None singleton.

`var team_id : str | None`

The type of the None singleton.

`class AssistantThreadContextStore`

Expand source code

```python
class AssistantThreadContextStore:
    def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:
        raise NotImplementedError()

    def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:
        raise NotImplementedError()
```

### Subclasses

* [DefaultAssistantThreadContextStore](context/assistant/thread_context_store/default_store.html#slack_bolt.context.assistant.thread_context_store.default_store.DefaultAssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.default_store.DefaultAssistantThreadContextStore")
* [FileAssistantThreadContextStore](context/assistant/thread_context_store/file/index.html#slack_bolt.context.assistant.thread_context_store.file.FileAssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.file.FileAssistantThreadContextStore")

### Methods

`def find(self, *, channel_id: str, thread_ts: str) ‑> [AssistantThreadContext](context/assistant/thread_context/index.html#slack_bolt.context.assistant.thread_context.AssistantThreadContext "slack_bolt.context.assistant.thread_context.AssistantThreadContext") | None`

Expand source code

```python
def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:
    raise NotImplementedError()
```

`def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) ‑> None`

Expand source code

```python
def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:
    raise NotImplementedError()
```

`class BoltContext (*args, **kwargs)`

Expand source code

```python
class BoltContext(BaseContext):
    """Context object associated with a request from Slack."""

    def to_copyable(self) -> "BoltContext":
        new_dict = {}
        for prop_name, prop_value in self.items():
            if prop_name in self.copyable_standard_property_names:
                # all the standard properties are copiable
                new_dict[prop_name] = prop_value
            elif prop_name in self.non_copyable_standard_property_names:
                # Do nothing with this property (e.g., listener_runner)
                continue
            else:
                try:
                    copied_value = create_copy(prop_value)
                    new_dict[prop_name] = copied_value
                except TypeError as te:
                    self.logger.warning(
                        f"Skipped setting '{prop_name}' to a copied request for lazy listeners "
                        "due to a deep-copy creation error. Consider passing the value not as part of context object "
                        f"(error: {te})"
                    )
        return BoltContext(new_dict)

    # The return type is intentionally string to avoid circular imports
    @property
    def listener_runner(self) -> "ThreadListenerRunner":  # type: ignore[name-defined]
        """The properly configured listener_runner that is available for middleware/listeners."""
        return self["listener_runner"]

    @property
    def client(self) -> WebClient:
        """The `WebClient` instance available for this request.

            @app.event("app_mention")
            def handle_events(context):
                context.client.chat_postMessage(
                    channel=context.channel_id,
                    text="Thanks!",
                )

            # You can access "client" this way too.
            @app.event("app_mention")
            def handle_events(client, context):
                client.chat_postMessage(
                    channel=context.channel_id,
                    text="Thanks!",
                )

        Returns:
            `WebClient` instance
        """
        if "client" not in self:
            self["client"] = WebClient(token=None)
        return self["client"]

    @property
    def ack(self) -> Ack:
        """`ack()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack):
                ack()

        Returns:
            Callable `ack()` function
        """
        if "ack" not in self:
            self["ack"] = Ack()
        return self["ack"]

    @property
    def say(self) -> Say:
        """`say()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()
                context.say("Hi!")

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack, say):
                ack()
                say("Hi!")

        Returns:
            Callable `say()` function
        """
        if "say" not in self:
            self["say"] = Say(client=self.client, channel=self.channel_id, thread_ts=self.thread_ts)
        return self["say"]

    @property
    def respond(self) -> Optional[Respond]:
        """`respond()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()
                context.respond("Hi!")

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack, respond):
                ack()
                respond("Hi!")

        Returns:
            Callable `respond()` function
        """
        if "respond" not in self:
            self["respond"] = Respond(
                response_url=self.response_url,
                proxy=self.client.proxy,
                ssl=self.client.ssl,
            )
        return self["respond"]

    @property
    def complete(self) -> Complete:
        """`complete()` function for this request. Once a custom function's state is set to complete,
        any outputs the function returns will be passed along to the next step of its housing workflow,
        or complete the workflow if the function is the last step in a workflow. Additionally,
        any interactivity handlers associated to a function invocation will no longer be invocable.

            @app.function("reverse")
            def handle_button_clicks(ack, complete):
                ack()
                complete(outputs={"stringReverse":"olleh"})

            @app.function("reverse")
            def handle_button_clicks(context):
                context.ack()
                context.complete(outputs={"stringReverse":"olleh"})

        Returns:
            Callable `complete()` function
        """
        if "complete" not in self:
            self["complete"] = Complete(client=self.client, function_execution_id=self.function_execution_id)
        return self["complete"]

    @property
    def fail(self) -> Fail:
        """`fail()` function for this request. Once a custom function's state is set to error,
        its housing workflow will be interrupted and any provided error message will be passed
        on to the end user through SlackBot. Additionally, any interactivity handlers associated
        to a function invocation will no longer be invocable.

            @app.function("reverse")
            def handle_button_clicks(ack, fail):
                ack()
                fail(error="something went wrong")

            @app.function("reverse")
            def handle_button_clicks(context):
                context.ack()
                context.fail(error="something went wrong")

        Returns:
            Callable `fail()` function
        """
        if "fail" not in self:
            self["fail"] = Fail(client=self.client, function_execution_id=self.function_execution_id)
        return self["fail"]

    @property
    def set_title(self) -> Optional[SetTitle]:
        return self.get("set_title")

    @property
    def set_status(self) -> Optional[SetStatus]:
        return self.get("set_status")

    @property
    def set_suggested_prompts(self) -> Optional[SetSuggestedPrompts]:
        return self.get("set_suggested_prompts")

    @property
    def get_thread_context(self) -> Optional[GetThreadContext]:
        return self.get("get_thread_context")

    @property
    def save_thread_context(self) -> Optional[SaveThreadContext]:
        return self.get("save_thread_context")
```

Context object associated with a request from Slack.

### Ancestors

* [BaseContext](context/base_context.html#slack_bolt.context.base_context.BaseContext "slack_bolt.context.base_context.BaseContext")
* builtins.dict

### Instance variables

`prop ack : [Ack](context/ack/ack.html#slack_bolt.context.ack.ack.Ack "slack_bolt.context.ack.ack.Ack")`

Expand source code

```text
@property
def ack(self) -> Ack:
    """`ack()` function for this request.

        @app.action("button")
        def handle_button_clicks(context):
            context.ack()

        # You can access "ack" this way too.
        @app.action("button")
        def handle_button_clicks(ack):
            ack()

    Returns:
        Callable `ack()` function
    """
    if "ack" not in self:
        self["ack"] = Ack()
    return self["ack"]
```

`ack()` function for this request.

```text
@app.action("button")
def handle_button_clicks(context):
    context.ack()

# You can access "ack" this way too.
@app.action("button")
def handle_button_clicks(ack):
    ack()
```

## Returns

Callable `ack()` function

`prop client : slack_sdk.web.client.WebClient`

Expand source code

```text
@property
def client(self) -> WebClient:
    """The `WebClient` instance available for this request.

        @app.event("app_mention")
        def handle_events(context):
            context.client.chat_postMessage(
                channel=context.channel_id,
                text="Thanks!",
            )

        # You can access "client" this way too.
        @app.event("app_mention")
        def handle_events(client, context):
            client.chat_postMessage(
                channel=context.channel_id,
                text="Thanks!",
            )

    Returns:
        `WebClient` instance
    """
    if "client" not in self:
        self["client"] = WebClient(token=None)
    return self["client"]
```

The `WebClient` instance available for this request.

```text
@app.event("app_mention")
def handle_events(context):
    context.client.chat_postMessage(
        channel=context.channel_id,
        text="Thanks!",
    )

# You can access "client" this way too.
@app.event("app_mention")
def handle_events(client, context):
    client.chat_postMessage(
        channel=context.channel_id,
        text="Thanks!",
    )
```

## Returns

`WebClient` instance

`prop complete : [Complete](context/complete/complete.html#slack_bolt.context.complete.complete.Complete "slack_bolt.context.complete.complete.Complete")`

Expand source code

```text
@property
def complete(self) -> Complete:
    """`complete()` function for this request. Once a custom function's state is set to complete,
    any outputs the function returns will be passed along to the next step of its housing workflow,
    or complete the workflow if the function is the last step in a workflow. Additionally,
    any interactivity handlers associated to a function invocation will no longer be invocable.

        @app.function("reverse")
        def handle_button_clicks(ack, complete):
            ack()
            complete(outputs={"stringReverse":"olleh"})

        @app.function("reverse")
        def handle_button_clicks(context):
            context.ack()
            context.complete(outputs={"stringReverse":"olleh"})

    Returns:
        Callable `complete()` function
    """
    if "complete" not in self:
        self["complete"] = Complete(client=self.client, function_execution_id=self.function_execution_id)
    return self["complete"]
```

`complete()` function for this request. Once a custom function's state is set to complete, any outputs the function returns will be passed along to the next step of its housing workflow, or complete the workflow if the function is the last step in a workflow. Additionally, any interactivity handlers associated to a function invocation will no longer be invocable.

```text
@app.function("reverse")
def handle_button_clicks(ack, complete):
    ack()
    complete(outputs={"stringReverse":"olleh"})

@app.function("reverse")
def handle_button_clicks(context):
    context.ack()
    context.complete(outputs={"stringReverse":"olleh"})
```

## Returns

Callable `complete()` function

`prop fail : [Fail](context/fail/fail.html#slack_bolt.context.fail.fail.Fail "slack_bolt.context.fail.fail.Fail")`

Expand source code

```text
@property
def fail(self) -> Fail:
    """`fail()` function for this request. Once a custom function's state is set to error,
    its housing workflow will be interrupted and any provided error message will be passed
    on to the end user through SlackBot. Additionally, any interactivity handlers associated
    to a function invocation will no longer be invocable.

        @app.function("reverse")
        def handle_button_clicks(ack, fail):
            ack()
            fail(error="something went wrong")

        @app.function("reverse")
        def handle_button_clicks(context):
            context.ack()
            context.fail(error="something went wrong")

    Returns:
        Callable `fail()` function
    """
    if "fail" not in self:
        self["fail"] = Fail(client=self.client, function_execution_id=self.function_execution_id)
    return self["fail"]
```

`fail()` function for this request. Once a custom function's state is set to error, its housing workflow will be interrupted and any provided error message will be passed on to the end user through SlackBot. Additionally, any interactivity handlers associated to a function invocation will no longer be invocable.

```text
@app.function("reverse")
def handle_button_clicks(ack, fail):
    ack()
    fail(error="something went wrong")

@app.function("reverse")
def handle_button_clicks(context):
    context.ack()
    context.fail(error="something went wrong")
```

## Returns

Callable `fail()` function

`prop get_thread_context : [GetThreadContext](context/get_thread_context/get_thread_context.html#slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext "slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext") | None`

Expand source code

```text
@property
def get_thread_context(self) -> Optional[GetThreadContext]:
    return self.get("get_thread_context")
```

`prop listener_runner : ThreadListenerRunner`

Expand source code

```text
@property
def listener_runner(self) -> "ThreadListenerRunner":  # type: ignore[name-defined]
    """The properly configured listener_runner that is available for middleware/listeners."""
    return self["listener_runner"]
```

The properly configured listener\_runner that is available for middleware/listeners.

`prop respond : [Respond](context/respond/respond.html#slack_bolt.context.respond.respond.Respond "slack_bolt.context.respond.respond.Respond") | None`

Expand source code

```text
@property
def respond(self) -> Optional[Respond]:
    """`respond()` function for this request.

        @app.action("button")
        def handle_button_clicks(context):
            context.ack()
            context.respond("Hi!")

        # You can access "ack" this way too.
        @app.action("button")
        def handle_button_clicks(ack, respond):
            ack()
            respond("Hi!")

    Returns:
        Callable `respond()` function
    """
    if "respond" not in self:
        self["respond"] = Respond(
            response_url=self.response_url,
            proxy=self.client.proxy,
            ssl=self.client.ssl,
        )
    return self["respond"]
```

`respond()` function for this request.

```text
@app.action("button")
def handle_button_clicks(context):
    context.ack()
    context.respond("Hi!")

# You can access "ack" this way too.
@app.action("button")
def handle_button_clicks(ack, respond):
    ack()
    respond("Hi!")
```

## Returns

Callable `respond()` function

`prop save_thread_context : [SaveThreadContext](context/save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext") | None`

Expand source code

```text
@property
def save_thread_context(self) -> Optional[SaveThreadContext]:
    return self.get("save_thread_context")
```

`prop say : [Say](context/say/say.html#slack_bolt.context.say.say.Say "slack_bolt.context.say.say.Say")`

Expand source code

```text
@property
def say(self) -> Say:
    """`say()` function for this request.

        @app.action("button")
        def handle_button_clicks(context):
            context.ack()
            context.say("Hi!")

        # You can access "ack" this way too.
        @app.action("button")
        def handle_button_clicks(ack, say):
            ack()
            say("Hi!")

    Returns:
        Callable `say()` function
    """
    if "say" not in self:
        self["say"] = Say(client=self.client, channel=self.channel_id, thread_ts=self.thread_ts)
    return self["say"]
```

`say()` function for this request.

```text
@app.action("button")
def handle_button_clicks(context):
    context.ack()
    context.say("Hi!")

# You can access "ack" this way too.
@app.action("button")
def handle_button_clicks(ack, say):
    ack()
    say("Hi!")
```

## Returns

Callable `say()` function

`prop set_status : [SetStatus](context/set_status/set_status.html#slack_bolt.context.set_status.set_status.SetStatus "slack_bolt.context.set_status.set_status.SetStatus") | None`

Expand source code

```text
@property
def set_status(self) -> Optional[SetStatus]:
    return self.get("set_status")
```

`prop set_suggested_prompts : [SetSuggestedPrompts](context/set_suggested_prompts/set_suggested_prompts.html#slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts "slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts") | None`

Expand source code

```text
@property
def set_suggested_prompts(self) -> Optional[SetSuggestedPrompts]:
    return self.get("set_suggested_prompts")
```

`prop set_title : [SetTitle](context/set_title/set_title.html#slack_bolt.context.set_title.set_title.SetTitle "slack_bolt.context.set_title.set_title.SetTitle") | None`

Expand source code

```text
@property
def set_title(self) -> Optional[SetTitle]:
    return self.get("set_title")
```

### Methods

`def to_copyable(self) ‑> [BoltContext](context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext")`

Expand source code

```python
def to_copyable(self) -> "BoltContext":
    new_dict = {}
    for prop_name, prop_value in self.items():
        if prop_name in self.copyable_standard_property_names:
            # all the standard properties are copiable
            new_dict[prop_name] = prop_value
        elif prop_name in self.non_copyable_standard_property_names:
            # Do nothing with this property (e.g., listener_runner)
            continue
        else:
            try:
                copied_value = create_copy(prop_value)
                new_dict[prop_name] = copied_value
            except TypeError as te:
                self.logger.warning(
                    f"Skipped setting '{prop_name}' to a copied request for lazy listeners "
                    "due to a deep-copy creation error. Consider passing the value not as part of context object "
                    f"(error: {te})"
                )
    return BoltContext(new_dict)
```

### Inherited members

* `**[BaseContext](context/base_context.html#slack_bolt.context.base_context.BaseContext "slack_bolt.context.base_context.BaseContext")**`:
  * `[actor_enterprise_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.actor_enterprise_id "slack_bolt.context.base_context.BaseContext.actor_enterprise_id")`
  * `[actor_team_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.actor_team_id "slack_bolt.context.base_context.BaseContext.actor_team_id")`
  * `[actor_user_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.actor_user_id "slack_bolt.context.base_context.BaseContext.actor_user_id")`
  * `[authorize_result](context/base_context.html#slack_bolt.context.base_context.BaseContext.authorize_result "slack_bolt.context.base_context.BaseContext.authorize_result")`
  * `[bot_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.bot_id "slack_bolt.context.base_context.BaseContext.bot_id")`
  * `[bot_token](context/base_context.html#slack_bolt.context.base_context.BaseContext.bot_token "slack_bolt.context.base_context.BaseContext.bot_token")`
  * `[bot_user_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.bot_user_id "slack_bolt.context.base_context.BaseContext.bot_user_id")`
  * `[channel_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.channel_id "slack_bolt.context.base_context.BaseContext.channel_id")`
  * `[copyable_standard_property_names](context/base_context.html#slack_bolt.context.base_context.BaseContext.copyable_standard_property_names "slack_bolt.context.base_context.BaseContext.copyable_standard_property_names")`
  * `[enterprise_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.enterprise_id "slack_bolt.context.base_context.BaseContext.enterprise_id")`
  * `[function_bot_access_token](context/base_context.html#slack_bolt.context.base_context.BaseContext.function_bot_access_token "slack_bolt.context.base_context.BaseContext.function_bot_access_token")`
  * `[function_execution_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.function_execution_id "slack_bolt.context.base_context.BaseContext.function_execution_id")`
  * `[inputs](context/base_context.html#slack_bolt.context.base_context.BaseContext.inputs "slack_bolt.context.base_context.BaseContext.inputs")`
  * `[is_enterprise_install](context/base_context.html#slack_bolt.context.base_context.BaseContext.is_enterprise_install "slack_bolt.context.base_context.BaseContext.is_enterprise_install")`
  * `[logger](context/base_context.html#slack_bolt.context.base_context.BaseContext.logger "slack_bolt.context.base_context.BaseContext.logger")`
  * `[matches](context/base_context.html#slack_bolt.context.base_context.BaseContext.matches "slack_bolt.context.base_context.BaseContext.matches")`
  * `[non_copyable_standard_property_names](context/base_context.html#slack_bolt.context.base_context.BaseContext.non_copyable_standard_property_names "slack_bolt.context.base_context.BaseContext.non_copyable_standard_property_names")`
  * `[response_url](context/base_context.html#slack_bolt.context.base_context.BaseContext.response_url "slack_bolt.context.base_context.BaseContext.response_url")`
  * `[standard_property_names](context/base_context.html#slack_bolt.context.base_context.BaseContext.standard_property_names "slack_bolt.context.base_context.BaseContext.standard_property_names")`
  * `[team_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.team_id "slack_bolt.context.base_context.BaseContext.team_id")`
  * `[thread_ts](context/base_context.html#slack_bolt.context.base_context.BaseContext.thread_ts "slack_bolt.context.base_context.BaseContext.thread_ts")`
  * `[token](context/base_context.html#slack_bolt.context.base_context.BaseContext.token "slack_bolt.context.base_context.BaseContext.token")`
  * `[user_id](context/base_context.html#slack_bolt.context.base_context.BaseContext.user_id "slack_bolt.context.base_context.BaseContext.user_id")`
  * `[user_token](context/base_context.html#slack_bolt.context.base_context.BaseContext.user_token "slack_bolt.context.base_context.BaseContext.user_token")`

`class BoltRequest (*,   body: str | dict,   query: str | Dict[str, str] | Dict[str, Sequence[str]] | None = None,   headers: Dict[str, str | Sequence[str]] | None = None,   context: Dict[str, Any] | None = None,   mode: str = 'http')`

Expand source code

```python
class BoltRequest:
    raw_body: str
    query: Dict[str, Sequence[str]]
    headers: Dict[str, Sequence[str]]
    content_type: Optional[str]
    body: Dict[str, Any]
    context: BoltContext
    lazy_only: bool
    lazy_function_name: Optional[str]
    mode: str  # either "http" or "socket_mode"

    def __init__(
        self,
        *,
        body: Union[str, dict],
        query: Optional[Union[str, Dict[str, str], Dict[str, Sequence[str]]]] = None,
        headers: Optional[Dict[str, Union[str, Sequence[str]]]] = None,
        context: Optional[Dict[str, Any]] = None,
        mode: str = "http",  # either "http" or "socket_mode"
    ):
        """Request to a Bolt app.

        Args:
            body: The raw request body (only plain text is supported for "http" mode)
            query: The query string data in any data format.
            headers: The request headers.
            context: The context in this request.
            mode: The mode used for this request. (either "http" or "socket_mode")
        """
        if mode == "http":
            # HTTP Mode
            if body is not None and not isinstance(body, str):
                raise BoltError(error_message_raw_body_required_in_http_mode())
            self.raw_body = body if body is not None else ""
        else:
            # Socket Mode
            if body is not None and isinstance(body, str):
                self.raw_body = body
            else:
                # We don't convert the dict value to str
                # as doing so does not guarantee to keep the original structure/format.
                self.raw_body = ""

        self.query = parse_query(query)
        self.headers = build_normalized_headers(headers)
        self.content_type = extract_content_type(self.headers)

        if isinstance(body, str):
            self.body = parse_body(self.raw_body, self.content_type)
        elif isinstance(body, dict):
            self.body = body
        else:
            self.body = {}

        self.context = build_context(BoltContext(context if context else {}), self.body)
        self.lazy_only = bool(self.headers.get("x-slack-bolt-lazy-only", [False])[0])
        self.lazy_function_name = self.headers.get("x-slack-bolt-lazy-function-name", [None])[0]
        self.mode = mode

    def to_copyable(self) -> "BoltRequest":
        body: Union[str, dict] = self.raw_body if self.mode == "http" else self.body
        return BoltRequest(
            body=body,
            query=self.query,
            headers=self.headers,
            context=self.context.to_copyable(),
            mode=self.mode,
        )
```

Request to a Bolt app.

## Args

## `body`

The raw request body (only plain text is supported for "http" mode)

## `query`

The query string data in any data format.

## `headers`

The request headers.

## `context`

The context in this request.

## `mode`

The mode used for this request. (either "http" or "socket\_mode")

### Class variables

`var body : Dict[str, Any]`

The type of the None singleton.

`var content_type : str | None`

The type of the None singleton.

`var context : [BoltContext](context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext")`

The type of the None singleton.

`var headers : Dict[str, Sequence[str]]`

The type of the None singleton.

`var lazy_function_name : str | None`

The type of the None singleton.

`var lazy_only : bool`

The type of the None singleton.

`var mode : str`

The type of the None singleton.

`var query : Dict[str, Sequence[str]]`

The type of the None singleton.

`var raw_body : str`

The type of the None singleton.

### Methods

`def to_copyable(self) ‑> [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")`

Expand source code

```python
def to_copyable(self) -> "BoltRequest":
    body: Union[str, dict] = self.raw_body if self.mode == "http" else self.body
    return BoltRequest(
        body=body,
        query=self.query,
        headers=self.headers,
        context=self.context.to_copyable(),
        mode=self.mode,
    )
```

`class BoltResponse (*,   status: int,   body: str | dict = '',   headers: Dict[str, str | Sequence[str]] | None = None)`

Expand source code

```python
class BoltResponse:
    status: int
    body: str
    headers: Dict[str, Sequence[str]]

    def __init__(
        self,
        *,
        status: int,
        body: Union[str, dict] = "",
        headers: Optional[Dict[str, Union[str, Sequence[str]]]] = None,
    ):
        """The response from a Bolt app.

        Args:
            status: HTTP status code
            body: The response body (dict and str are supported)
            headers: The response headers.
        """
        self.status: int = status
        self.body: str = json.dumps(body) if isinstance(body, dict) else body
        self.headers: Dict[str, Sequence[str]] = {}
        if headers is not None:
            for name, value in headers.items():
                if value is None:
                    continue
                if isinstance(value, list):
                    self.headers[name.lower()] = value
                elif isinstance(value, set):
                    self.headers[name.lower()] = list(value)
                else:
                    self.headers[name.lower()] = [str(value)]

        if "content-type" not in self.headers.keys():
            if self.body and self.body.startswith("{"):
                self.headers["content-type"] = ["application/json;charset=utf-8"]
            else:
                self.headers["content-type"] = ["text/plain;charset=utf-8"]

    def first_headers(self) -> Dict[str, str]:
        return {k: list(v)[0] for k, v in self.headers.items()}

    def first_headers_without_set_cookie(self) -> Dict[str, str]:
        return {k: list(v)[0] for k, v in self.headers.items() if k != "set-cookie"}

    def cookies(self) -> Sequence[SimpleCookie]:
        header_values = self.headers.get("set-cookie", [])
        return [self._to_simple_cookie(v) for v in header_values]

    @staticmethod
    def _to_simple_cookie(header_value: str) -> SimpleCookie:
        c = SimpleCookie()
        c.load(header_value)
        return c
```

The response from a Bolt app.

## Args

## `status`

HTTP status code

## `body`

The response body (dict and str are supported)

## `headers`

The response headers.

### Class variables

`var body : str`

The type of the None singleton.

`var headers : Dict[str, Sequence[str]]`

The type of the None singleton.

`var status : int`

The type of the None singleton.

### Methods

`def cookies(self) ‑> Sequence[http.cookies.SimpleCookie]`

Expand source code

```python
def cookies(self) -> Sequence[SimpleCookie]:
    header_values = self.headers.get("set-cookie", [])
    return [self._to_simple_cookie(v) for v in header_values]
```

`def first_headers(self) ‑> Dict[str, str]`

Expand source code

```python
def first_headers(self) -> Dict[str, str]:
    return {k: list(v)[0] for k, v in self.headers.items()}
```

`def first_headers_without_set_cookie(self) ‑> Dict[str, str]`

Expand source code

```python
def first_headers_without_set_cookie(self) -> Dict[str, str]:
    return {k: list(v)[0] for k, v in self.headers.items() if k != "set-cookie"}
```

`class Complete (client: slack_sdk.web.client.WebClient, function_execution_id: str | None)`

Expand source code

```python
class Complete:
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

    def __call__(self, outputs: Optional[Dict[str, Any]] = None) -> SlackResponse:
        """Signal the successful completion of the custom function.

        Kwargs:
            outputs: Json serializable object containing the output values

        Returns:
            SlackResponse: The response object returned from slack

        Raises:
            ValueError: If this function cannot be used.
        """
        if self.function_execution_id is None:
            raise ValueError("complete is unsupported here as there is no function_execution_id")

        self._called = True
        return self.client.functions_completeSuccess(function_execution_id=self.function_execution_id, outputs=outputs or {})

    def has_been_called(self) -> bool:
        """Check if this complete function has been called.

        Returns:
            bool: True if the complete function has been called, False otherwise.
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
    """Check if this complete function has been called.

    Returns:
        bool: True if the complete function has been called, False otherwise.
    """
    return self._called
```

Check if this complete function has been called.

## Returns

`bool`

True if the complete function has been called, False otherwise.

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

* [ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")

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

* `**[ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")**`:
  * `[matches](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher.matches "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher.matches")`

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

`class FileAssistantThreadContextStore (base_dir: str = '/Users/wbergamin/.bolt-app-assistant-thread-contexts')`

Expand source code

```python
class FileAssistantThreadContextStore(AssistantThreadContextStore):

    def __init__(
        self,
        base_dir: str = str(Path.home()) + "/.bolt-app-assistant-thread-contexts",
    ):
        self.base_dir = base_dir
        self._mkdir(self.base_dir)

    def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:
        path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
        with open(path, "w") as f:
            f.write(json.dumps(context))

    def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:
        path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
        try:
            with open(path) as f:
                data = json.loads(f.read())
                if data.get("channel_id") is not None:
                    return AssistantThreadContext(data)
        except FileNotFoundError:
            pass
        return None

    @staticmethod
    def _mkdir(path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
```

### Ancestors

* [AssistantThreadContextStore](context/assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore")

### Methods

`def find(self, *, channel_id: str, thread_ts: str) ‑> [AssistantThreadContext](context/assistant/thread_context/index.html#slack_bolt.context.assistant.thread_context.AssistantThreadContext "slack_bolt.context.assistant.thread_context.AssistantThreadContext") | None`

Expand source code

```python
def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:
    path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
    try:
        with open(path) as f:
            data = json.loads(f.read())
            if data.get("channel_id") is not None:
                return AssistantThreadContext(data)
    except FileNotFoundError:
        pass
    return None
```

`def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) ‑> None`

Expand source code

```python
def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:
    path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
    with open(path, "w") as f:
        f.write(json.dumps(context))
```

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

* [CustomListener](listener/custom_listener.html#slack_bolt.listener.custom_listener.CustomListener "slack_bolt.listener.custom_listener.CustomListener")

### Class variables

`var ack_function : Callable[..., [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")]`

The type of the None singleton.

`var ack_timeout : int`

The type of the None singleton.

`var auto_acknowledgement : bool`

The type of the None singleton.

`var lazy_functions : Sequence[Callable[..., None]]`

The type of the None singleton.

`var matchers : Sequence[[ListenerMatcher](listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")]`

The type of the None singleton.

`var middleware : Sequence[[Middleware](middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")]`

The type of the None singleton.

### Methods

`def matches(self,   *,   req: [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> bool`

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

`def run_ack_function(self,   *,   request: [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   response: [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None`

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

`def run_middleware(self,   *,   req: [BoltRequest](request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")) ‑> Tuple[[BoltResponse](response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None, bool]`

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

`class Respond (*,   response_url: str | None,   proxy: str | None = None,   ssl: ssl.SSLContext | None = None)`

Expand source code

```python
class Respond:
    response_url: Optional[str]
    proxy: Optional[str]
    ssl: Optional[SSLContext]

    def __init__(
        self,
        *,
        response_url: Optional[str],
        proxy: Optional[str] = None,
        ssl: Optional[SSLContext] = None,
    ):
        self.response_url = response_url
        self.proxy = proxy
        self.ssl = ssl

    def __call__(
        self,
        text: Union[str, dict] = "",
        blocks: Optional[Sequence[Union[dict, Block]]] = None,
        attachments: Optional[Sequence[Union[dict, Attachment]]] = None,
        response_type: Optional[str] = None,
        replace_original: Optional[bool] = None,
        delete_original: Optional[bool] = None,
        unfurl_links: Optional[bool] = None,
        unfurl_media: Optional[bool] = None,
        thread_ts: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> WebhookResponse:
        if self.response_url is not None:
            client = WebhookClient(
                url=self.response_url,
                proxy=self.proxy,
                ssl=self.ssl,
            )
            text_or_whole_response: Union[str, dict] = text
            if isinstance(text_or_whole_response, str):
                text = text_or_whole_response
                message = _build_message(
                    text=text,
                    blocks=blocks,
                    attachments=attachments,
                    response_type=response_type,
                    replace_original=replace_original,
                    delete_original=delete_original,
                    unfurl_links=unfurl_links,
                    unfurl_media=unfurl_media,
                    thread_ts=thread_ts,
                    metadata=metadata,
                )
                return client.send_dict(message)
            elif isinstance(text_or_whole_response, dict):
                message = _build_message(**text_or_whole_response)
                return client.send_dict(message)
            else:
                raise ValueError(f"The arg is unexpected type ({type(text_or_whole_response)})")
        else:
            raise ValueError("respond is unsupported here as there is no response_url")
```

### Class variables

`var proxy : str | None`

The type of the None singleton.

`var response_url : str | None`

The type of the None singleton.

`var ssl : ssl.SSLContext | None`

The type of the None singleton.

`class SaveThreadContext (thread_context_store: [AssistantThreadContextStore](context/assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore"),   channel_id: str,   thread_ts: str)`

Expand source code

```python
class SaveThreadContext:
    thread_context_store: AssistantThreadContextStore
    channel_id: str
    thread_ts: str

    def __init__(
        self,
        thread_context_store: AssistantThreadContextStore,
        channel_id: str,
        thread_ts: str,
    ):
        self.thread_context_store = thread_context_store
        self.channel_id = channel_id
        self.thread_ts = thread_ts

    def __call__(self, new_context: Dict[str, str]) -> None:
        self.thread_context_store.save(
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
            context=new_context,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var thread_context_store : [AssistantThreadContextStore](context/assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore")`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.

`class Say (client: slack_sdk.web.client.WebClient | None,   channel: str | None,   thread_ts: str | None = None,   metadata: Dict | slack_sdk.models.metadata.Metadata | None = None,   build_metadata: Callable[[], Dict | slack_sdk.models.metadata.Metadata | None] | None = None)`

Expand source code

```python
class Say:
    client: Optional[WebClient]
    channel: Optional[str]
    thread_ts: Optional[str]
    metadata: Optional[Union[Dict, Metadata]]
    build_metadata: Optional[Callable[[], Optional[Union[Dict, Metadata]]]]

    def __init__(
        self,
        client: Optional[WebClient],
        channel: Optional[str],
        thread_ts: Optional[str] = None,
        metadata: Optional[Union[Dict, Metadata]] = None,
        build_metadata: Optional[Callable[[], Optional[Union[Dict, Metadata]]]] = None,
    ):
        self.client = client
        self.channel = channel
        self.thread_ts = thread_ts
        self.metadata = metadata
        self.build_metadata = build_metadata

    def __call__(
        self,
        text: Union[str, dict] = "",
        blocks: Optional[Sequence[Union[Dict, Block]]] = None,
        attachments: Optional[Sequence[Union[Dict, Attachment]]] = None,
        channel: Optional[str] = None,
        as_user: Optional[bool] = None,
        thread_ts: Optional[str] = None,
        reply_broadcast: Optional[bool] = None,
        unfurl_links: Optional[bool] = None,
        unfurl_media: Optional[bool] = None,
        icon_emoji: Optional[str] = None,
        icon_url: Optional[str] = None,
        username: Optional[str] = None,
        markdown_text: Optional[str] = None,
        mrkdwn: Optional[bool] = None,
        link_names: Optional[bool] = None,
        parse: Optional[str] = None,  # none, full
        metadata: Optional[Union[Dict, Metadata]] = None,
        **kwargs,
    ) -> SlackResponse:
        if _can_say(self, channel):
            text_or_whole_response: Union[str, dict] = text
            if isinstance(text_or_whole_response, str):
                text = text_or_whole_response
                if metadata is None:
                    metadata = self.build_metadata() if self.build_metadata is not None else self.metadata
                return self.client.chat_postMessage(  # type: ignore[union-attr]
                    channel=channel or self.channel,  # type: ignore[arg-type]
                    text=text,
                    blocks=blocks,
                    attachments=attachments,
                    as_user=as_user,
                    thread_ts=thread_ts or self.thread_ts,
                    reply_broadcast=reply_broadcast,
                    unfurl_links=unfurl_links,
                    unfurl_media=unfurl_media,
                    icon_emoji=icon_emoji,
                    icon_url=icon_url,
                    username=username,
                    markdown_text=markdown_text,
                    mrkdwn=mrkdwn,
                    link_names=link_names,
                    parse=parse,
                    metadata=metadata,
                    **kwargs,
                )
            elif isinstance(text_or_whole_response, dict):
                message: dict = create_copy(text_or_whole_response)
                if "channel" not in message:
                    message["channel"] = channel or self.channel
                if "thread_ts" not in message:
                    message["thread_ts"] = thread_ts or self.thread_ts
                if "metadata" not in message:
                    metadata = self.build_metadata() if self.build_metadata is not None else self.metadata
                    message["metadata"] = metadata
                return self.client.chat_postMessage(**message)  # type: ignore[union-attr]
            else:
                raise ValueError(f"The arg is unexpected type ({type(text_or_whole_response)})")
        else:
            raise ValueError("say without channel_id here is unsupported")
```

### Class variables

`var build_metadata : Callable[[], Dict | slack_sdk.models.metadata.Metadata | None] | None`

The type of the None singleton.

`var channel : str | None`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient | None`

The type of the None singleton.

`var metadata : Dict | slack_sdk.models.metadata.Metadata | None`

The type of the None singleton.

`var thread_ts : str | None`

The type of the None singleton.

`class SetStatus (client: slack_sdk.web.client.WebClient, channel_id: str, thread_ts: str)`

Expand source code

```python
class SetStatus:
    client: WebClient
    channel_id: str
    thread_ts: str

    def __init__(
        self,
        client: WebClient,
        channel_id: str,
        thread_ts: str,
    ):
        self.client = client
        self.channel_id = channel_id
        self.thread_ts = thread_ts

    def __call__(
        self,
        status: str,
        loading_messages: Optional[List[str]] = None,
        **kwargs,
    ) -> SlackResponse:
        return self.client.assistant_threads_setStatus(
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
            status=status,
            loading_messages=loading_messages,
            **kwargs,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.

`class SetSuggestedPrompts (client: slack_sdk.web.client.WebClient, channel_id: str, thread_ts: str)`

Expand source code

```python
class SetSuggestedPrompts:
    client: WebClient
    channel_id: str
    thread_ts: str

    def __init__(
        self,
        client: WebClient,
        channel_id: str,
        thread_ts: str,
    ):
        self.client = client
        self.channel_id = channel_id
        self.thread_ts = thread_ts

    def __call__(
        self,
        prompts: Sequence[Union[str, Dict[str, str]]],
        title: Optional[str] = None,
    ) -> SlackResponse:
        prompts_arg: List[Dict[str, str]] = []
        for prompt in prompts:
            if isinstance(prompt, str):
                prompts_arg.append({"title": prompt, "message": prompt})
            else:
                prompts_arg.append(prompt)

        return self.client.assistant_threads_setSuggestedPrompts(
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
            prompts=prompts_arg,
            title=title,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.

`class SetTitle (client: slack_sdk.web.client.WebClient, channel_id: str, thread_ts: str)`

Expand source code

```python
class SetTitle:
    client: WebClient
    channel_id: str
    thread_ts: str

    def __init__(
        self,
        client: WebClient,
        channel_id: str,
        thread_ts: str,
    ):
        self.client = client
        self.channel_id = channel_id
        self.thread_ts = thread_ts

    def __call__(self, title: str) -> SlackResponse:
        return self.client.assistant_threads_setTitle(
            title=title,
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.
