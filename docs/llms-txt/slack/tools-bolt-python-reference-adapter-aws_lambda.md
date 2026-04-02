Source: https://docs.slack.dev/tools/bolt-python/reference/adapter/aws_lambda

# Module slack_bolt.adapter.aws_lambda

## Sub-modules

`[slack_bolt.adapter.aws_lambda.chalice_handler](chalice_handler.html "slack_bolt.adapter.aws_lambda.chalice_handler")`

`[slack_bolt.adapter.aws_lambda.chalice_lazy_listener_runner](chalice_lazy_listener_runner.html "slack_bolt.adapter.aws_lambda.chalice_lazy_listener_runner")`

`[slack_bolt.adapter.aws_lambda.handler](handler.html "slack_bolt.adapter.aws_lambda.handler")`

`[slack_bolt.adapter.aws_lambda.internals](internals.html "slack_bolt.adapter.aws_lambda.internals")`

`[slack_bolt.adapter.aws_lambda.lambda_s3_oauth_flow](lambda_s3_oauth_flow.html "slack_bolt.adapter.aws_lambda.lambda_s3_oauth_flow")`

`[slack_bolt.adapter.aws_lambda.lazy_listener_runner](lazy_listener_runner.html "slack_bolt.adapter.aws_lambda.lazy_listener_runner")`

`[slack_bolt.adapter.aws_lambda.local_lambda_client](local_lambda_client.html "slack_bolt.adapter.aws_lambda.local_lambda_client")`

## Classes

`class SlackRequestHandler (app: [App](../../app/app.html#slack_bolt.app.app.App "slack_bolt.app.app.App"))`

Expand source code

```python
class SlackRequestHandler:
    def __init__(self, app: App):
        self.app = app
        self.logger = get_bolt_app_logger(app.name, SlackRequestHandler, app.logger)
        self.app.listener_runner.lazy_listener_runner = LambdaLazyListenerRunner(self.logger)
        if self.app.oauth_flow is not None:
            self.app.oauth_flow.settings.redirect_uri_page_renderer.install_path = "?"

    @classmethod
    def clear_all_log_handlers(cls):
        # https://stackoverflow.com/questions/37703609/using-python-logging-with-aws-lambda
        root = logging.getLogger()
        if root.handlers:
            for handler in root.handlers:
                root.removeHandler(handler)

    def handle(self, event, context):
        self.logger.debug(f"Incoming event: {event}, context: {context}")

        method = event.get("requestContext", {}).get("http", {}).get("method")
        if method is None:
            method = event.get("requestContext", {}).get("httpMethod")

        if method is None:
            return not_found()
        if method == "GET":
            if self.app.oauth_flow is not None:
                oauth_flow: OAuthFlow = self.app.oauth_flow
                bolt_req: BoltRequest = to_bolt_request(event)
                query = bolt_req.query
                is_callback = query is not None and (
                    (_first_value(query, "code") is not None and _first_value(query, "state") is not None)
                    or _first_value(query, "error") is not None
                )
                if is_callback:
                    bolt_resp = oauth_flow.handle_callback(bolt_req)
                    return to_aws_response(bolt_resp)
                else:
                    bolt_resp = oauth_flow.handle_installation(bolt_req)
                    return to_aws_response(bolt_resp)
        elif method == "POST":
            bolt_req = to_bolt_request(event)
            # https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
            aws_lambda_function_name = context.function_name
            bolt_req.context["aws_lambda_function_name"] = aws_lambda_function_name
            bolt_req.context["aws_lambda_invoked_function_arn"] = context.invoked_function_arn
            bolt_req.context["lambda_request"] = event
            bolt_resp = self.app.dispatch(bolt_req)
            aws_response = to_aws_response(bolt_resp)
            return aws_response
        elif method == "NONE":
            bolt_req = to_bolt_request(event)
            bolt_resp = self.app.dispatch(bolt_req)
            aws_response = to_aws_response(bolt_resp)
            return aws_response

        return not_found()
```

### Static methods

`def clear_all_log_handlers()`

### Methods

`def handle(self, event, context)`

Expand source code

```python
def handle(self, event, context):
    self.logger.debug(f"Incoming event: {event}, context: {context}")

    method = event.get("requestContext", {}).get("http", {}).get("method")
    if method is None:
        method = event.get("requestContext", {}).get("httpMethod")

    if method is None:
        return not_found()
    if method == "GET":
        if self.app.oauth_flow is not None:
            oauth_flow: OAuthFlow = self.app.oauth_flow
            bolt_req: BoltRequest = to_bolt_request(event)
            query = bolt_req.query
            is_callback = query is not None and (
                (_first_value(query, "code") is not None and _first_value(query, "state") is not None)
                or _first_value(query, "error") is not None
            )
            if is_callback:
                bolt_resp = oauth_flow.handle_callback(bolt_req)
                return to_aws_response(bolt_resp)
            else:
                bolt_resp = oauth_flow.handle_installation(bolt_req)
                return to_aws_response(bolt_resp)
    elif method == "POST":
        bolt_req = to_bolt_request(event)
        # https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
        aws_lambda_function_name = context.function_name
        bolt_req.context["aws_lambda_function_name"] = aws_lambda_function_name
        bolt_req.context["aws_lambda_invoked_function_arn"] = context.invoked_function_arn
        bolt_req.context["lambda_request"] = event
        bolt_resp = self.app.dispatch(bolt_req)
        aws_response = to_aws_response(bolt_resp)
        return aws_response
    elif method == "NONE":
        bolt_req = to_bolt_request(event)
        bolt_resp = self.app.dispatch(bolt_req)
        aws_response = to_aws_response(bolt_resp)
        return aws_response

    return not_found()
```
