Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/cherrypy

# Module slack_bolt.adapter.cherrypy

## Sub-modules

`[slack_bolt.adapter.cherrypy.handler](handler.html "slack_bolt.adapter.cherrypy.handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app

    def handle(self) -> bytes:
        req = cherrypy.request
        if req.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                request_path = req.wsgi_environ["REQUEST_URI"].split("?")[0]
                if request_path == oauth_flow.install_path:
                    bolt_resp = oauth_flow.handle_installation(build_bolt_request())
                    set_response_status_and_headers(bolt_resp)
                    return (bolt_resp.body or "").encode("utf-8")
                elif request_path == oauth_flow.redirect_uri_path:
                    bolt_resp = oauth_flow.handle_callback(build_bolt_request())
                    set_response_status_and_headers(bolt_resp)
                    return (bolt_resp.body or "").encode("utf-8")
        elif req.method == "POST":
            bolt_resp = self.app.dispatch(build_bolt_request())
            set_response_status_and_headers(bolt_resp)
            return (bolt_resp.body or "").encode("utf-8")

        cherrypy.response.status = 404
        return "Not Found".encode("utf-8")
```

### Methods

`def handle(self) ‑> bytes`

Expand source code

```python
def handle(self) -> bytes:
    req = cherrypy.request
    if req.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            request_path = req.wsgi_environ["REQUEST_URI"].split("?")[0]
            if request_path == oauth_flow.install_path:
                bolt_resp = oauth_flow.handle_installation(build_bolt_request())
                set_response_status_and_headers(bolt_resp)
                return (bolt_resp.body or "").encode("utf-8")
            elif request_path == oauth_flow.redirect_uri_path:
                bolt_resp = oauth_flow.handle_callback(build_bolt_request())
                set_response_status_and_headers(bolt_resp)
                return (bolt_resp.body or "").encode("utf-8")
    elif req.method == "POST":
        bolt_resp = self.app.dispatch(build_bolt_request())
        set_response_status_and_headers(bolt_resp)
        return (bolt_resp.body or "").encode("utf-8")

    cherrypy.response.status = 404
    return "Not Found".encode("utf-8")
```
