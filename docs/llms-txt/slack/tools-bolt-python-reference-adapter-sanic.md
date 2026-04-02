Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/sanic

# Module slack_bolt.adapter.sanic

## Sub-modules

`[slack_bolt.adapter.sanic.async_handler](async_handler.html "slack_bolt.adapter.sanic.async_handler")`

## Classes

`class AsyncSlackRequestHandler (app: [AsyncApp](../../app/async_app.html#slack_bolt.app.async_app.AsyncApp "slack_bolt.app.async_app.AsyncApp"))`

Expand source code

```python
class AsyncSlackRequestHandler:
    def __init__(self, app: AsyncApp):
        self.app = app

    async def handle(self, req: Request, addition_context_properties: Optional[Dict[str, Any]] = None) -> HTTPResponse:
        if req.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: AsyncOAuthFlow = self.app.oauth_flow
                if req.path == oauth_flow.install_path:
                    bolt_resp = await oauth_flow.handle_installation(to_async_bolt_request(req, addition_context_properties))
                    return to_sanic_response(bolt_resp)
                elif req.path == oauth_flow.redirect_uri_path:
                    bolt_resp = await oauth_flow.handle_callback(to_async_bolt_request(req, addition_context_properties))
                    return to_sanic_response(bolt_resp)

        elif req.method == "POST":
            bolt_resp = await self.app.async_dispatch(to_async_bolt_request(req, addition_context_properties))
            return to_sanic_response(bolt_resp)

        return HTTPResponse(
            status=404,
            body="Not found",
        )
```

### Methods

`async def handle(self,   req: sanic.request.types.Request,   addition_context_properties: Dict[str, Any] | None = None) ‑> sanic.response.types.HTTPResponse`

Expand source code

```python
async def handle(self, req: Request, addition_context_properties: Optional[Dict[str, Any]] = None) -> HTTPResponse:
    if req.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: AsyncOAuthFlow = self.app.oauth_flow
            if req.path == oauth_flow.install_path:
                bolt_resp = await oauth_flow.handle_installation(to_async_bolt_request(req, addition_context_properties))
                return to_sanic_response(bolt_resp)
            elif req.path == oauth_flow.redirect_uri_path:
                bolt_resp = await oauth_flow.handle_callback(to_async_bolt_request(req, addition_context_properties))
                return to_sanic_response(bolt_resp)

    elif req.method == "POST":
        bolt_resp = await self.app.async_dispatch(to_async_bolt_request(req, addition_context_properties))
        return to_sanic_response(bolt_resp)

    return HTTPResponse(
        status=404,
        body="Not found",
    )
```
