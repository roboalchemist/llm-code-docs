Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/asgi

# Module slack_bolt.adapter.asgi

## Sub-modules

`[slack_bolt.adapter.asgi.aiohttp](aiohttp/index.html "slack_bolt.adapter.asgi.aiohttp")`

`[slack_bolt.adapter.asgi.async_handler](async_handler.html "slack_bolt.adapter.asgi.async_handler")`

`[slack_bolt.adapter.asgi.base_handler](base_handler.html "slack_bolt.adapter.asgi.base_handler")`

`[slack_bolt.adapter.asgi.builtin](builtin/index.html "slack_bolt.adapter.asgi.builtin")`

`[slack_bolt.adapter.asgi.http_request](http_request.html "slack_bolt.adapter.asgi.http_request")`

`[slack_bolt.adapter.asgi.http_response](http_response.html "slack_bolt.adapter.asgi.http_response")`

`[slack_bolt.adapter.asgi.utils](utils.html "slack_bolt.adapter.asgi.utils")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"),   path: str = '/slack/events')`

Expand source code

```python
class SlackRequestHandler(BaseSlackRequestHandler):
    def __init__(self, app: App, path: str = "/slack/events"):
        """Setup Bolt as an ASGI web framework, this will make your application compatible with ASGI web servers.
        This can be used for production deployment.

        With the default settings, `http://localhost:3000/slack/events`
        Run Bolt with [uvicron](https://www.uvicorn.org/)

            # Python
            app = App()
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
        return self.app.dispatch(
            BoltRequest(body=await request.get_raw_body(), query=request.query_string, headers=request.get_headers())
        )

    async def handle_installation(self, request: AsgiHttpRequest) -> BoltResponse:
        return self.app.oauth_flow.handle_installation(  # type: ignore[union-attr]
            BoltRequest(body=await request.get_raw_body(), query=request.query_string, headers=request.get_headers())
        )

    async def handle_callback(self, request: AsgiHttpRequest) -> BoltResponse:
        return self.app.oauth_flow.handle_callback(  # type: ignore[union-attr]
            BoltRequest(body=await request.get_raw_body(), query=request.query_string, headers=request.get_headers())
        )
```

Setup Bolt as an ASGI web framework, this will make your application compatible with ASGI web servers. This can be used for production deployment.

With the default settings, `http://localhost:3000/slack/events` Run Bolt with [uvicron](https://www.uvicorn.org/)

```text
# Python
app = App()
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

* [BaseSlackRequestHandler](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler")

### Subclasses

* [AsyncSlackRequestHandler](aiohttp/index.html#slack_bolt.adapter.asgi.aiohttp.AsyncSlackRequestHandler "slack_bolt.adapter.asgi.aiohttp.AsyncSlackRequestHandler")

### Inherited members

* `**[BaseSlackRequestHandler](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler")**`:
  * `[app](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.app "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.app")`
  * `[dispatch](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.dispatch "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.dispatch")`
  * `[handle_callback](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.handle_callback "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.handle_callback")`
  * `[handle_installation](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.handle_installation "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.handle_installation")`
  * `[path](base_handler.html#slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.path "slack_bolt.adapter.asgi.base_handler.BaseSlackRequestHandler.path")`
