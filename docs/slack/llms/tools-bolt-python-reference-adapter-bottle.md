Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/bottle

# Module slack_bolt.adapter.bottle

## Sub-modules

`[slack_bolt.adapter.bottle.handler](handler.html "slack_bolt.adapter.bottle.handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app

    def handle(self, req: Request, resp: Response) -> str:
        if req.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                if req.path == oauth_flow.install_path:
                    bolt_resp = oauth_flow.handle_installation(to_bolt_request(req))
                    set_response(bolt_resp, resp)
                    return bolt_resp.body or ""
                elif req.path == oauth_flow.redirect_uri_path:
                    bolt_resp = oauth_flow.handle_callback(to_bolt_request(req))
                    set_response(bolt_resp, resp)
                    return bolt_resp.body or ""
        elif req.method == "POST":
            bolt_resp = self.app.dispatch(to_bolt_request(req))
            set_response(bolt_resp, resp)
            return bolt_resp.body or ""

        resp.status = 404
        return "Not Found"
```

### Methods

`def handle(self, req: bottle.BaseRequest, resp: bottle.BaseResponse) ‑> str`

Expand source code

```python
def handle(self, req: Request, resp: Response) -> str:
    if req.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            if req.path == oauth_flow.install_path:
                bolt_resp = oauth_flow.handle_installation(to_bolt_request(req))
                set_response(bolt_resp, resp)
                return bolt_resp.body or ""
            elif req.path == oauth_flow.redirect_uri_path:
                bolt_resp = oauth_flow.handle_callback(to_bolt_request(req))
                set_response(bolt_resp, resp)
                return bolt_resp.body or ""
    elif req.method == "POST":
        bolt_resp = self.app.dispatch(to_bolt_request(req))
        set_response(bolt_resp, resp)
        return bolt_resp.body or ""

    resp.status = 404
    return "Not Found"
```
