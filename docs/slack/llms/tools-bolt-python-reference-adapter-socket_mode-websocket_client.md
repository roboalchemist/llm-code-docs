Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/socket_mode/websocket_client

# Module slack_bolt.adapter.socket_mode.websocket_client

[`websocket-client`](https://pypi.org/project/websocket-client/) based implementation

## Classes

`class SocketModeHandler (app: [App](../../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"),   app_token: str | None = None,   logger: logging.Logger | None = None,   web_client: slack_sdk.web.client.WebClient | None = None,   ping_interval: float = 10,   concurrency: int = 10,   http_proxy_host: str | None = None,   http_proxy_port: int | None = None,   http_proxy_auth: Tuple[str, str] | None = None,   proxy_type: str | None = None,   trace_enabled: bool = False)`

Expand source code

```python
class SocketModeHandler(BaseSocketModeHandler):
    app: App
    app_token: str
    client: SocketModeClient

    def __init__(
        self,
        app: App,
        app_token: Optional[str] = None,
        logger: Optional[Logger] = None,
        web_client: Optional[WebClient] = None,
        ping_interval: float = 10,
        concurrency: int = 10,
        http_proxy_host: Optional[str] = None,
        http_proxy_port: Optional[int] = None,
        http_proxy_auth: Optional[Tuple[str, str]] = None,
        proxy_type: Optional[str] = None,
        trace_enabled: bool = False,
    ):
        """Socket Mode adapter for Bolt apps

        Args:
            app: The Bolt app
            app_token: App-level token starting with `xapp-`
            logger: Custom logger
            web_client: custom `slack_sdk.web.WebClient` instance
            ping_interval: The ping-pong internal (seconds)
            concurrency: The size of the underlying thread pool
            http_proxy_host: HTTP proxy host
            http_proxy_port: HTTP proxy port
            http_proxy_auth: HTTP proxy authentication (username, password)
            proxy_type: Proxy type
            trace_enabled: True if trace-level logging is enabled
        """
        self.app = app
        self.app_token = app_token or os.environ["SLACK_APP_TOKEN"]
        self.client = SocketModeClient(
            app_token=self.app_token,
            logger=logger if logger is not None else app.logger,
            web_client=web_client if web_client is not None else app.client,
            ping_interval=ping_interval,
            concurrency=concurrency,
            http_proxy_host=http_proxy_host,
            http_proxy_port=http_proxy_port,
            http_proxy_auth=http_proxy_auth,
            proxy_type=proxy_type,
            trace_enabled=trace_enabled,
        )
        self.client.socket_mode_request_listeners.append(self.handle)  # type: ignore[arg-type]

    def handle(self, client: SocketModeClient, req: SocketModeRequest) -> None:  # type: ignore[override]
        start = time()
        bolt_resp: BoltResponse = run_bolt_app(self.app, req)
        send_response(client, req, bolt_resp, start)
```

Socket Mode adapter for Bolt apps

## Args

## `app`

The Bolt app

## `app_token`

App-level token starting with `xapp-`

## `logger`

Custom logger

## `web_client`

custom `slack_sdk.web.WebClient` instance

## `ping_interval`

The ping-pong internal (seconds)

## `concurrency`

The size of the underlying thread pool

## `http_proxy_host`

HTTP proxy host

## `http_proxy_port`

HTTP proxy port

## `http_proxy_auth`

HTTP proxy authentication (username, password)

## `proxy_type`

Proxy type

## `trace_enabled`

True if trace-level logging is enabled

### Ancestors

* [BaseSocketModeHandler](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler")

### Class variables

`var app_token : str`

The type of the None singleton.

### Inherited members

* `**[BaseSocketModeHandler](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler")**`:
  * `[app](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.app "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.app")`
  * `[client](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.client "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.client")`
  * `[close](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.close "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.close")`
  * `[connect](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.connect "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.connect")`
  * `[disconnect](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.disconnect "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.disconnect")`
  * `[handle](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.handle "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.handle")`
  * `[start](../base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.start "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.start")`
