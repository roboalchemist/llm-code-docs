Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/django

# Module slack_bolt.adapter.django

## Sub-modules

`[slack_bolt.adapter.django.handler](handler.html "slack_bolt.adapter.django.handler")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app
        listener_runner = self.app.listener_runner
        # This runner closes all thread-local connections in the thread when an execution completes
        self.app.listener_runner.lazy_listener_runner = DjangoThreadLazyListenerRunner(
            logger=listener_runner.logger,
            executor=listener_runner.listener_executor,
        )

        if not isinstance(listener_runner, ThreadListenerRunner):
            raise BoltError("Custom listener_runners are not compatible with this Django adapter.")

        if app.process_before_response is True:
            # As long as the app access Django models in the same thread,
            # Django cleans the connections up for you.
            self.app.logger.debug("App.process_before_response is set to True")
            return

        current_start_handler = listener_runner.listener_start_handler
        if current_start_handler is not None and not isinstance(current_start_handler, DefaultListenerStartHandler):
            # As we run release_thread_local_connections() before listener executions,
            # it's okay to skip calling the same connection clean-up method at the listener completion.
            message = """As you've already set app.listener_runner.listener_start_handler to your own one,
            Bolt skipped to set it to slack_sdk.adapter.django.DjangoListenerStartHandler.

            If you go with your own handler here, we highly recommend having the following lines of code
            in your handle() method to clean up unmanaged stale/old database connections:

            from django.db import close_old_connections
            close_old_connections()
            """
            self.app.logger.info(message)
        else:
            # for proper management of thread-local Django DB connections
            self.app.listener_runner.listener_start_handler = DjangoListenerStartHandler()
            self.app.logger.debug("DjangoListenerStartHandler has been enabled")

        current_completion_handler = listener_runner.listener_completion_handler
        if current_completion_handler is not None and not isinstance(
            current_completion_handler, DefaultListenerCompletionHandler
        ):
            # As we run release_thread_local_connections() before listener executions,
            # it's okay to skip calling the same connection clean-up method at the listener completion.
            message = """As you've already set app.listener_runner.listener_completion_handler to your own one,
            Bolt skipped to set it to slack_sdk.adapter.django.DjangoListenerCompletionHandler.
            """
            self.app.logger.info(message)
            return
        # for proper management of thread-local Django DB connections
        self.app.listener_runner.listener_completion_handler = DjangoListenerCompletionHandler()
        self.app.logger.debug("DjangoListenerCompletionHandler has been enabled")

    def handle(self, req: HttpRequest) -> HttpResponse:
        if req.method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                if req.path == oauth_flow.install_path:
                    bolt_resp = oauth_flow.handle_installation(to_bolt_request(req))
                    return to_django_response(bolt_resp)
                elif req.path == oauth_flow.redirect_uri_path:
                    bolt_resp = oauth_flow.handle_callback(to_bolt_request(req))
                    return to_django_response(bolt_resp)
        elif req.method == "POST":
            bolt_resp = self.app.dispatch(to_bolt_request(req))
            return to_django_response(bolt_resp)

        return HttpResponse(status=404, content=b"Not Found")
```

### Methods

`def handle(self, req: django.http.request.HttpRequest) ‑> django.http.response.HttpResponse`

Expand source code

```python
def handle(self, req: HttpRequest) -> HttpResponse:
    if req.method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            if req.path == oauth_flow.install_path:
                bolt_resp = oauth_flow.handle_installation(to_bolt_request(req))
                return to_django_response(bolt_resp)
            elif req.path == oauth_flow.redirect_uri_path:
                bolt_resp = oauth_flow.handle_callback(to_bolt_request(req))
                return to_django_response(bolt_resp)
    elif req.method == "POST":
        bolt_resp = self.app.dispatch(to_bolt_request(req))
        return to_django_response(bolt_resp)

    return HttpResponse(status=404, content=b"Not Found")
```
