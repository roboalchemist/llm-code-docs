Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/google_cloud_functions

# Module slack_bolt.adapter.google_cloud_functions

## Sub-modules

`[slack_bolt.adapter.google_cloud_functions.handler](handler.html "slack_bolt.adapter.google_cloud_functions.handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app
        # Note that lazy listener is not supported
        self.app.listener_runner.lazy_listener_runner = NoopLazyListenerRunner()
        if self.app.oauth_flow is not None:
            self.app.oauth_flow.settings.redirect_uri_page_renderer.install_path = "?"

    def handle(self, req: Request) -> Response:
        if req.method == "GET" and self.app.oauth_flow is not None:
            bolt_req = to_bolt_request(req)
            if "code" in req.args or "error" in req.args or "state" in req.args:
                bolt_resp = self.app.oauth_flow.handle_callback(bolt_req)
                return to_flask_response(bolt_resp)
            else:
                bolt_resp = self.app.oauth_flow.handle_installation(bolt_req)
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
    if req.method == "GET" and self.app.oauth_flow is not None:
        bolt_req = to_bolt_request(req)
        if "code" in req.args or "error" in req.args or "state" in req.args:
            bolt_resp = self.app.oauth_flow.handle_callback(bolt_req)
            return to_flask_response(bolt_resp)
        else:
            bolt_resp = self.app.oauth_flow.handle_installation(bolt_req)
            return to_flask_response(bolt_resp)
    elif req.method == "POST":
        bolt_resp = self.app.dispatch(to_bolt_request(req))
        return to_flask_response(bolt_resp)

    return make_response("Not Found", 404)
```
