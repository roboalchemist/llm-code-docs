Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/socket_mode/aiohttp

# Module slack_bolt.adapter.socket_mode.aiohttp

[`aiohttp`](https://pypi.org/project/aiohttp/) based implementation / asyncio compatible

## Classes

`class AsyncSocketModeHandler (app: [AsyncApp](../../../app/async_app.html#slack_bolt.app.async_app.AsyncApp "slack_bolt.app.async_app.AsyncApp"),   app_token: str | None = None,   logger: logging.Logger | None = None,   web_client: slack_sdk.web.async_client.AsyncWebClient | None = None,   proxy: str | None = None,   ping_interval: float = 10,   loop: asyncio.events.AbstractEventLoop | None = None)`

Expand source code

```python
class AsyncSocketModeHandler(AsyncBaseSocketModeHandler):
    app: AsyncApp
    app_token: str
    client: SocketModeClient

    def __init__(
        self,
        app: AsyncApp,
        app_token: Optional[str] = None,
        logger: Optional[Logger] = None,
        web_client: Optional[AsyncWebClient] = None,
        proxy: Optional[str] = None,
        ping_interval: float = 10,
        loop: Optional[AbstractEventLoop] = None,
    ):
        self.app = app
        self.app_token = app_token or os.environ["SLACK_APP_TOKEN"]
        self.client = SocketModeClient(
            app_token=self.app_token,
            logger=logger if logger is not None else app.logger,
            web_client=web_client if web_client is not None else app.client,
            proxy=proxy,
            ping_interval=ping_interval,
            loop=loop,
        )
        self.client.socket_mode_request_listeners.append(self.handle)  # type: ignore[arg-type]

    async def handle(self, client: SocketModeClient, req: SocketModeRequest) -> None:  # type: ignore[override]
        start = time()
        bolt_resp: BoltResponse = await run_async_bolt_app(self.app, req)
        await send_async_response(client, req, bolt_resp, start)
```

### Ancestors

* [AsyncBaseSocketModeHandler](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler")

### Class variables

`var app_token : str`

The type of the None singleton.

### Inherited members

* `**[AsyncBaseSocketModeHandler](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler")**`:
  * `[app](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.app "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.app")`
  * `[client](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.client "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.client")`
  * `[close_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.close_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.close_async")`
  * `[connect_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.connect_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.connect_async")`
  * `[disconnect_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.disconnect_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.disconnect_async")`
  * `[handle](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.handle "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.handle")`
  * `[start_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.start_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.start_async")`

`class SocketModeHandler (app: [App](../../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"),   app_token: str | None = None,   logger: logging.Logger | None = None,   web_client: slack_sdk.web.async_client.AsyncWebClient | None = None,   proxy: str | None = None,   ping_interval: float = 10)`

Expand source code

```python
class SocketModeHandler(AsyncBaseSocketModeHandler):
    app: App
    app_token: str
    client: SocketModeClient

    def __init__(
        self,
        app: App,
        app_token: Optional[str] = None,
        logger: Optional[Logger] = None,
        web_client: Optional[AsyncWebClient] = None,
        proxy: Optional[str] = None,
        ping_interval: float = 10,
    ):
        """Socket Mode adapter for Bolt apps

        Args:
            app: The Bolt app
            app_token: App-level token starting with `xapp-`
            logger: Custom logger
            web_client: custom `slack_sdk.web.WebClient` instance
            proxy: HTTP proxy URL
            ping_interval: The ping-pong internal (seconds)
        """
        self.app = app
        self.app_token = app_token or os.environ["SLACK_APP_TOKEN"]
        self.client = SocketModeClient(
            app_token=self.app_token,
            logger=logger if logger is not None else app.logger,
            web_client=web_client if web_client is not None else app.client,  # type: ignore[arg-type]
            proxy=proxy,
            ping_interval=ping_interval,
        )
        self.client.socket_mode_request_listeners.append(self.handle)  # type: ignore[arg-type]

    async def handle(self, client: SocketModeClient, req: SocketModeRequest) -> None:  # type: ignore[override]
        start = time()
        bolt_resp: BoltResponse = run_bolt_app(self.app, req)
        await send_async_response(client, req, bolt_resp, start)
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

## `ping_interval`

The ping-pong internal (seconds)

### Ancestors

* [AsyncBaseSocketModeHandler](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler")

### Class variables

`var app_token : str`

The type of the None singleton.

### Inherited members

* `**[AsyncBaseSocketModeHandler](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler")**`:
  * `[app](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.app "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.app")`
  * `[client](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.client "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.client")`
  * `[close_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.close_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.close_async")`
  * `[connect_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.connect_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.connect_async")`
  * `[disconnect_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.disconnect_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.disconnect_async")`
  * `[handle](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.handle "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.handle")`
  * `[start_async](../async_base_handler.html#slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.start_async "slack_bolt.adapter.socket_mode.async_base_handler.AsyncBaseSocketModeHandler.start_async")`
