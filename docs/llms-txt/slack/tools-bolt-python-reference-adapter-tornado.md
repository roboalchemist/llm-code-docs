Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/tornado

# Module slack_bolt.adapter.tornado

## Sub-modules

`[slack_bolt.adapter.tornado.async_handler](async_handler.html "slack_bolt.adapter.tornado.async_handler")`

`[slack_bolt.adapter.tornado.handler](handler.html "slack_bolt.adapter.tornado.handler")`

## Classes

`class SlackEventsHandler (application: Application,   request: tornado.httputil.HTTPServerRequest,   **kwargs: Any)`

Expand source code

```python
class SlackEventsHandler(RequestHandler):
    def initialize(self, app: App):
        self.app = app

    def post(self):
        bolt_resp: BoltResponse = self.app.dispatch(to_bolt_request(self.request))
        set_response(self, bolt_resp)
        return
```

Base class for HTTP request handlers.

Subclasses must define at least one of the methods defined in the "Entry points" section below.

Applications should not construct `RequestHandler` objects directly and subclasses should not override `__init__` (override `~RequestHandler.initialize` instead).

### Ancestors

* tornado.web.RequestHandler

### Methods

`def initialize(self,   app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
def initialize(self, app: App):
    self.app = app
```

`def post(self)`

Expand source code

```python
def post(self):
    bolt_resp: BoltResponse = self.app.dispatch(to_bolt_request(self.request))
    set_response(self, bolt_resp)
    return
```

`class SlackOAuthHandler (application: Application,   request: tornado.httputil.HTTPServerRequest,   **kwargs: Any)`

Expand source code

```python
class SlackOAuthHandler(RequestHandler):
    def initialize(self, app: App):
        self.app = app

    def get(self):
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            if self.request.path == oauth_flow.install_path:
                bolt_resp = oauth_flow.handle_installation(to_bolt_request(self.request))
                set_response(self, bolt_resp)
                return
            elif self.request.path == oauth_flow.redirect_uri_path:
                bolt_resp = oauth_flow.handle_callback(to_bolt_request(self.request))
                set_response(self, bolt_resp)
                return
        self.set_status(404)
```

Base class for HTTP request handlers.

Subclasses must define at least one of the methods defined in the "Entry points" section below.

Applications should not construct `RequestHandler` objects directly and subclasses should not override `__init__` (override `~RequestHandler.initialize` instead).

### Ancestors

* tornado.web.RequestHandler

### Methods

`def get(self)`

Expand source code

```python
def get(self):
    if self.app.oauth_flow is not None:
        oauth_flow: OAuthFlow = self.app.oauth_flow
        if self.request.path == oauth_flow.install_path:
            bolt_resp = oauth_flow.handle_installation(to_bolt_request(self.request))
            set_response(self, bolt_resp)
            return
        elif self.request.path == oauth_flow.redirect_uri_path:
            bolt_resp = oauth_flow.handle_callback(to_bolt_request(self.request))
            set_response(self, bolt_resp)
            return
    self.set_status(404)
```

`def initialize(self,   app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
def initialize(self, app: App):
    self.app = app
```
