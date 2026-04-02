Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/flask

# Module slack_bolt.adapter.flask

## Sub-modules

`[slack_bolt.adapter.flask.handler](handler.html "slack_bolt.adapter.flask.handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app

    def handle(self, req: Request) -> Response:
        if req.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                if req.path == oauth_flow.install_path:
                    bolt_resp = oauth_flow.handle_installation(to_bolt_request(req))
                    return to_flask_response(bolt_resp)
                elif req.path == oauth_flow.redirect_uri_path:
                    bolt_resp = oauth_flow.handle_callback(to_bolt_request(req))
                    return to_flask_response(bolt_resp)
        elif req.method == "POST":
            bolt_resp = self.app.dispatch(to_bolt_request(req))
            return to_flask_response(bolt_resp)

        return make_response("Not Found", 404)
```

### Methods

`def handle(self, req: flask.wrappers.Request) ‑> flask.wrappers.Response`

Expand source code

```python
def handle(self, req: Request) -> Response:
    if req.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            if req.path == oauth_flow.install_path:
                bolt_resp = oauth_flow.handle_installation(to_bolt_request(req))
                return to_flask_response(bolt_resp)
            elif req.path == oauth_flow.redirect_uri_path:
                bolt_resp = oauth_flow.handle_callback(to_bolt_request(req))
                return to_flask_response(bolt_resp)
    elif req.method == "POST":
        bolt_resp = self.app.dispatch(to_bolt_request(req))
        return to_flask_response(bolt_resp)

    return make_response("Not Found", 404)
```
