Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/fastapi

# Module slack_bolt.adapter.fastapi

## Sub-modules

`[slack_bolt.adapter.fastapi.async_handler](async_handler.html "slack_bolt.adapter.fastapi.async_handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app

    async def handle(self, req: Request, addition_context_properties: Optional[Dict[str, Any]] = None) -> Response:
        body = await req.body()
        if req.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                if req.url.path == oauth_flow.install_path:
                    bolt_resp = oauth_flow.handle_installation(to_bolt_request(req, body, addition_context_properties))
                    return to_starlette_response(bolt_resp)
                elif req.url.path == oauth_flow.redirect_uri_path:
                    bolt_resp = oauth_flow.handle_callback(to_bolt_request(req, body, addition_context_properties))
                    return to_starlette_response(bolt_resp)
        elif req.method == "POST":
            bolt_resp = self.app.dispatch(to_bolt_request(req, body, addition_context_properties))
            return to_starlette_response(bolt_resp)

        return Response(
            status_code=404,
            content="Not found",
        )
```

### Methods

`async def handle(self,   req: starlette.requests.Request,   addition_context_properties: Dict[str, Any] | None = None) ‑> starlette.responses.Response`

Expand source code

```python
async def handle(self, req: Request, addition_context_properties: Optional[Dict[str, Any]] = None) -> Response:
    body = await req.body()
    if req.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            if req.url.path == oauth_flow.install_path:
                bolt_resp = oauth_flow.handle_installation(to_bolt_request(req, body, addition_context_properties))
                return to_starlette_response(bolt_resp)
            elif req.url.path == oauth_flow.redirect_uri_path:
                bolt_resp = oauth_flow.handle_callback(to_bolt_request(req, body, addition_context_properties))
                return to_starlette_response(bolt_resp)
    elif req.method == "POST":
        bolt_resp = self.app.dispatch(to_bolt_request(req, body, addition_context_properties))
        return to_starlette_response(bolt_resp)

    return Response(
        status_code=404,
        content="Not found",
    )
```
