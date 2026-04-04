Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/wsgi

# Module slack_bolt.adapter.wsgi

## Sub-modules

`[slack_bolt.adapter.wsgi.handler](handler.html "slack_bolt.adapter.wsgi.handler")`

`[slack_bolt.adapter.wsgi.http_request](http_request.html "slack_bolt.adapter.wsgi.http_request")`

`[slack_bolt.adapter.wsgi.http_response](http_response.html "slack_bolt.adapter.wsgi.http_response")`

`[slack_bolt.adapter.wsgi.internals](internals.html "slack_bolt.adapter.wsgi.internals")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"),   path: str = '/slack/events')`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App, path: str = "/slack/events"):
        """Setup Bolt as a WSGI web framework, this will make your application compatible with WSGI web servers.
        This can be used for production deployments.

        With the default settings, `http://localhost:3000/slack/events`
        Run Bolt with [gunicorn](https://gunicorn.org/)

        # Python
            app = App()

            api = SlackRequestHandler(app)

        # bash
            export SLACK_SIGNING_SECRET=***

            export SLACK_BOT_TOKEN=xoxb-***

            gunicorn app:api -b 0.0.0.0:3000 --log-level debug

        Args:
            app: Your bolt application
            path: The path to handle request from Slack (Default: `/slack/events`)
        """
        self.path = path
        self.app = app

    def dispatch(self, request: WsgiHttpRequest) -> BoltResponse:
        return self.app.dispatch(
            BoltRequest(body=request.get_body(), query=request.query_string, headers=request.get_headers())
        )

    def handle_installation(self, request: WsgiHttpRequest) -> BoltResponse:
        return self.app.oauth_flow.handle_installation(  # type: ignore[union-attr]
            BoltRequest(body=request.get_body(), query=request.query_string, headers=request.get_headers())
        )

    def handle_callback(self, request: WsgiHttpRequest) -> BoltResponse:
        return self.app.oauth_flow.handle_callback(  # type: ignore[union-attr]
            BoltRequest(body=request.get_body(), query=request.query_string, headers=request.get_headers())
        )

    def _get_http_response(self, request: WsgiHttpRequest) -> WsgiHttpResponse:
        if request.method == "GET":
            if self.app.oauth_flow is not None:
                if request.path == self.app.oauth_flow.install_path:
                    bolt_response = self.handle_installation(request)
                    return WsgiHttpResponse(
                        status=bolt_response.status, headers=bolt_response.headers, body=bolt_response.body
                    )
                elif request.path == self.app.oauth_flow.redirect_uri_path:
                    bolt_response = self.handle_callback(request)
                    return WsgiHttpResponse(
                        status=bolt_response.status, headers=bolt_response.headers, body=bolt_response.body
                    )
        if request.method == "POST" and request.path == self.path:
            bolt_response = self.dispatch(request)
            return WsgiHttpResponse(status=bolt_response.status, headers=bolt_response.headers, body=bolt_response.body)
        return WsgiHttpResponse(status=404, headers={"content-type": ["text/plain;charset=utf-8"]}, body="Not Found")

    def __call__(
        self,
        environ: Dict[str, Any],
        start_response: Callable[[str, List[Tuple[str, str]]], None],
    ) -> Iterable[bytes]:
        request = WsgiHttpRequest(environ)
        if "HTTP" in request.protocol:
            response: WsgiHttpResponse = self._get_http_response(
                request=request,
            )
            start_response(response.status, response.get_headers())
            return response.get_body()
        raise TypeError(f"Unsupported SERVER_PROTOCOL: {request.protocol}")
```

Setup Bolt as a WSGI web framework, this will make your application compatible with WSGI web servers. This can be used for production deployments.

With the default settings, `http://localhost:3000/slack/events` Run Bolt with [gunicorn](https://gunicorn.org/)

# Python

```text
app = App()

api = SlackRequestHandler(app)
```

# bash

```javascript
export SLACK_SIGNING_SECRET=***

export SLACK_BOT_TOKEN=xoxb-***

gunicorn app:api -b 0.0.0.0:3000 --log-level debug
```

## Args

## `app`

Your bolt application

## `path`

The path to handle request from Slack (Default: `/slack/events`)

### Methods

`def dispatch(self,   request: [WsgiHttpRequest](http_request.html#slack_bolt.adapter.wsgi.http_request.WsgiHttpRequest "slack_bolt.adapter.wsgi.http_request.WsgiHttpRequest")) ‑> [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Expand source code

```python
def dispatch(self, request: WsgiHttpRequest) -> BoltResponse:
    return self.app.dispatch(
        BoltRequest(body=request.get_body(), query=request.query_string, headers=request.get_headers())
    )
```

`def handle_callback(self,   request: [WsgiHttpRequest](http_request.html#slack_bolt.adapter.wsgi.http_request.WsgiHttpRequest "slack_bolt.adapter.wsgi.http_request.WsgiHttpRequest")) ‑> [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Expand source code

```python
def handle_callback(self, request: WsgiHttpRequest) -> BoltResponse:
    return self.app.oauth_flow.handle_callback(  # type: ignore[union-attr]
        BoltRequest(body=request.get_body(), query=request.query_string, headers=request.get_headers())
    )
```

`def handle_installation(self,   request: [WsgiHttpRequest](http_request.html#slack_bolt.adapter.wsgi.http_request.WsgiHttpRequest "slack_bolt.adapter.wsgi.http_request.WsgiHttpRequest")) ‑> [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Expand source code

```python
def handle_installation(self, request: WsgiHttpRequest) -> BoltResponse:
    return self.app.oauth_flow.handle_installation(  # type: ignore[union-attr]
        BoltRequest(body=request.get_body(), query=request.query_string, headers=request.get_headers())
    )
```
