Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/socket_mode

# Module slack_bolt.adapter.socket_mode

Socket Mode adapter package provides the following implementations. If you don't have strong reasons to use 3rd party library based adapters, we recommend using the built-in client based one.

* `[slack_bolt.adapter.socket_mode.builtin](builtin/index.html "slack_bolt.adapter.socket_mode.builtin")`
* `[slack_bolt.adapter.socket_mode.websocket_client](websocket_client/index.html "slack_bolt.adapter.socket_mode.websocket_client")`
* `[slack_bolt.adapter.socket_mode.aiohttp](aiohttp/index.html "slack_bolt.adapter.socket_mode.aiohttp")`
* `[slack_bolt.adapter.socket_mode.websockets](websockets/index.html "slack_bolt.adapter.socket_mode.websockets")`

## Sub-modules

`[slack_bolt.adapter.socket_mode.aiohttp](aiohttp/index.html "slack_bolt.adapter.socket_mode.aiohttp")`

[`aiohttp`](https://pypi.org/project/aiohttp/) based implementation / asyncio compatible

`[slack_bolt.adapter.socket_mode.async_base_handler](async_base_handler.html "slack_bolt.adapter.socket_mode.async_base_handler")`

The base class of asyncio-based Socket Mode client implementation

`[slack_bolt.adapter.socket_mode.async_handler](async_handler.html "slack_bolt.adapter.socket_mode.async_handler")`

Default implementation is the aiohttp-based one.

`[slack_bolt.adapter.socket_mode.async_internals](async_internals.html "slack_bolt.adapter.socket_mode.async_internals")`

Internal functions

`[slack_bolt.adapter.socket_mode.base_handler](base_handler.html "slack_bolt.adapter.socket_mode.base_handler")`

The base class of Socket Mode client implementation. If you want to build asyncio-based ones, use `AsyncBaseSocketModeHandler` instead.

`[slack_bolt.adapter.socket_mode.builtin](builtin/index.html "slack_bolt.adapter.socket_mode.builtin")`

The built-in implementation, which does not have any external dependencies

`[slack_bolt.adapter.socket_mode.internals](internals.html "slack_bolt.adapter.socket_mode.internals")`

Internal functions

`[slack_bolt.adapter.socket_mode.websocket_client](websocket_client/index.html "slack_bolt.adapter.socket_mode.websocket_client")`

[`websocket-client`](https://pypi.org/project/websocket-client/) based implementation

`[slack_bolt.adapter.socket_mode.websockets](websockets/index.html "slack_bolt.adapter.socket_mode.websockets")`

[`websockets`](https://pypi.org/project/websockets/) based implementation / asyncio compatible

## Classes

`class SocketModeHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"),   app_token: str | None = None,   logger: logging.Logger | None = None,   web_client: slack_sdk.web.client.WebClient | None = None,   proxy: str | None = None,   proxy_headers: Dict[str, str] | None = None,   auto_reconnect_enabled: bool = True,   trace_enabled: bool = False,   all_message_trace_enabled: bool = False,   ping_pong_trace_enabled: bool = False,   ping_interval: float = 10,   receive_buffer_size: int = 1024,   concurrency: int = 10)`

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
        proxy: Optional[str] = None,
        proxy_headers: Optional[Dict[str, str]] = None,
        auto_reconnect_enabled: bool = True,
        trace_enabled: bool = False,
        all_message_trace_enabled: bool = False,
        ping_pong_trace_enabled: bool = False,
        ping_interval: float = 10,
        receive_buffer_size: int = 1024,
        concurrency: int = 10,
    ):
        """Socket Mode adapter for Bolt apps

        Args:
            app: The Bolt app
            app_token: App-level token starting with `xapp-`
            logger: Custom logger
            web_client: custom `slack_sdk.web.WebClient` instance
            proxy: HTTP proxy URL
            proxy_headers: Additional request header for proxy connections
            auto_reconnect_enabled: True if the auto-reconnect logic works
            trace_enabled: True if trace-level logging is enabled
            all_message_trace_enabled: True if trace-logging for all received WebSocket messages is enabled
            ping_pong_trace_enabled: True if trace-logging for all ping-pong communications
            ping_interval: The ping-pong internal (seconds)
            receive_buffer_size: The data length for a single socket recv operation
            concurrency: The size of the underlying thread pool
        """
        self.app = app
        self.app_token = app_token or os.environ["SLACK_APP_TOKEN"]
        self.client = SocketModeClient(
            app_token=self.app_token,
            logger=logger if logger is not None else app.logger,
            web_client=web_client if web_client is not None else app.client,
            proxy=proxy if proxy is not None else app.client.proxy,
            proxy_headers=proxy_headers,
            auto_reconnect_enabled=auto_reconnect_enabled,
            trace_enabled=trace_enabled,
            all_message_trace_enabled=all_message_trace_enabled,
            ping_pong_trace_enabled=ping_pong_trace_enabled,
            ping_interval=ping_interval,
            receive_buffer_size=receive_buffer_size,
            concurrency=concurrency,
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

## `proxy`

HTTP proxy URL

## `proxy_headers`

Additional request header for proxy connections

## `auto_reconnect_enabled`

True if the auto-reconnect logic works

## `trace_enabled`

True if trace-level logging is enabled

## `all_message_trace_enabled`

True if trace-logging for all received WebSocket messages is enabled

## `ping_pong_trace_enabled`

True if trace-logging for all ping-pong communications

## `ping_interval`

The ping-pong internal (seconds)

## `receive_buffer_size`

The data length for a single socket recv operation

## `concurrency`

The size of the underlying thread pool

### Ancestors

* [BaseSocketModeHandler](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler")

### Class variables

`var app_token : str`

The type of the None singleton.

### Inherited members

* `**[BaseSocketModeHandler](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler")**`:
  * `[app](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.app "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.app")`
  * `[client](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.client "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.client")`
  * `[close](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.close "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.close")`
  * `[connect](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.connect "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.connect")`
  * `[disconnect](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.disconnect "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.disconnect")`
  * `[handle](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.handle "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.handle")`
  * `[start](base_handler.html#slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.start "slack_bolt.adapter.socket_mode.base_handler.BaseSocketModeHandler.start")`
