Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/pyramid

# Module slack_bolt.adapter.pyramid

## Sub-modules

`[slack_bolt.adapter.pyramid.handler](handler.html "slack_bolt.adapter.pyramid.handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app

    def handle(self, request: Request) -> Response:
        if request.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                if request.path == oauth_flow.install_path:
                    bolt_req = _attach_pyramid_request_to_context(to_bolt_request(request), request)
                    bolt_resp = oauth_flow.handle_installation(bolt_req)
                    return to_pyramid_response(bolt_resp)
                elif request.path == oauth_flow.redirect_uri_path:
                    bolt_req = _attach_pyramid_request_to_context(to_bolt_request(request), request)
                    bolt_resp = oauth_flow.handle_callback(bolt_req)
                    return to_pyramid_response(bolt_resp)
        elif request.method == "POST":
            bolt_req = _attach_pyramid_request_to_context(to_bolt_request(request), request)
            bolt_resp = self.app.dispatch(bolt_req)
            return to_pyramid_response(bolt_resp)

        return Response(status=404, body="Not found")
```

### Methods

`def handle(self, request: pyramid.request.Request) ‑> pyramid.response.Response`

Expand source code

```python
def handle(self, request: Request) -> Response:
    if request.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            if request.path == oauth_flow.install_path:
                bolt_req = _attach_pyramid_request_to_context(to_bolt_request(request), request)
                bolt_resp = oauth_flow.handle_installation(bolt_req)
                return to_pyramid_response(bolt_resp)
            elif request.path == oauth_flow.redirect_uri_path:
                bolt_req = _attach_pyramid_request_to_context(to_bolt_request(request), request)
                bolt_resp = oauth_flow.handle_callback(bolt_req)
                return to_pyramid_response(bolt_resp)
    elif request.method == "POST":
        bolt_req = _attach_pyramid_request_to_context(to_bolt_request(request), request)
        bolt_resp = self.app.dispatch(bolt_req)
        return to_pyramid_response(bolt_resp)

    return Response(status=404, body="Not found")
```
