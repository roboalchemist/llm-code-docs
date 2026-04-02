Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/asgi/aiohttp

# Module slack_bolt.adapter.asgi.aiohttp

## Classes

`class AsyncSlackRequestHandler (app: [AsyncApp](../../../app/async_app.html#slack_bolt.app.async_app.AsyncApp "slack_bolt.app.async_app.AsyncApp"),   path: str = '/slack/events')`

Expand source code

```python
class AsyncSlackRequestHandler(SlackRequestHandler):
    app: AsyncApp

    def __init__(self, app: AsyncApp, path: str = "/slack/events"):
        """Setup Bolt as an ASGI web framework, this will make your application compatible with ASGI web servers.
        This can be used for production deployment.

        With the default settings, `http://localhost:3000/slack/events`
        Run Bolt with [uvicron](https://www.uvicorn.org/)

            # Python
            app = AsyncApp()
            api = SlackRequestHandler(app)

            # bash
            export SLACK_SIGNING_SECRET=***
            export SLACK_BOT_TOKEN=xoxb-***
            uvicorn app:api --port 3000 --log-level debug

        Args:
            app: Your bolt application
            path: The path to handle request from Slack (Default: `/slack/events`)
        """
        self.path = path
        self.app = app

    async def dispatch(self, request: AsgiHttpRequest) -> BoltResponse:
        return await self.app.async_dispatch(
            AsyncBoltRequest(body=await request.get_raw_body(), query=request.query_string, headers=request.get_headers())
        )

    async def handle_installation(self, request: AsgiHttpRequest) -> BoltResponse:
        return await self.app.oauth_flow.handle_installation(  # type: ignore[union-attr]
            AsyncBoltRequest(body=await request.get_raw_body(), query=request.query_string, headers=request.get_headers())
        )

    async def handle_callback(self, request: AsgiHttpRequest) -> BoltResponse:
        return await self.app.oauth_flow.handle_callback(  # type: ignore[union-attr]
            AsyncBoltRequest(body=await request.get_raw_body(), query=request.query_string, headers=request.get_headers())
        )
```

Setup Bolt as an ASGI web framework, this will make your application compatible with ASGI web servers. This can be used for production deployment.

With the default settings, `http://localhost:3000/slack/events` Run Bolt with [uvicron](https://www.uvicorn.org/)

```text
# Python
app = AsyncApp()
api = SlackRequestHandler(app)

# bash
export SLACK_SIGNING_SECRET=***
export SLACK_BOT_TOKEN=xoxb-***
uvicorn app:api --port 3000 --log-level debug
```

## Args

## `app`

Your bolt application

## `path`

The path to handle request from Slack (Default: `/slack/events`)

### Ancestors

* [SlackRequestHandler](../builtin/index.html#slack_bolt.adapter.asgi.builtin.SlackRequestHandler "slack_bolt.adapter.asgi.builtin.SlackRequestHandler")
* [BaseSlackRequestHandler](../base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler")

### Inherited members

* `**[SlackRequestHandler](../builtin/index.html#slack_bolt.adapter.asgi.builtin.SlackRequestHandler "slack_bolt.adapter.asgi.builtin.SlackRequestHandler")**`:
  * `[app](../base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.app "slack_bolt.adapter.asgi.builtin.SlackRequestHandler.app")`
  * `[dispatch](../base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.dispatch "slack_bolt.adapter.asgi.builtin.SlackRequestHandler.dispatch")`
  * `[handle_callback](../base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.handle_callback "slack_bolt.adapter.asgi.builtin.SlackRequestHandler.handle_callback")`
  * `[handle_installation](../base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.handle_installation "slack_bolt.adapter.asgi.builtin.SlackRequestHandler.handle_installation")`
  * `[path](../base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.path "slack_bolt.adapter.asgi.builtin.SlackRequestHandler.path")`
