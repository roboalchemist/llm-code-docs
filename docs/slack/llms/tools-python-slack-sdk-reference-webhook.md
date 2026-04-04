Source: https://docs.slack.dev/tools/python-slack-sdk/reference/webhook

# Module slack_sdk.webhook

You can use slack\_sdk.webhook.WebhookClient for Incoming Webhooks and message responses using response\_url in payloads.

## Sub-modules

`[slack_sdk.webhook.async_client](async_client.html "slack_sdk.webhook.async_client")`

`[slack_sdk.webhook.client](client.html "slack_sdk.webhook.client")`

`[slack_sdk.webhook.internal_utils](internal_utils.html "slack_sdk.webhook.internal_utils")`

`[slack_sdk.webhook.webhook_response](webhook_response.html "slack_sdk.webhook.webhook_response")`

## Classes

`class WebhookClient (url: str,   timeout: int = 30,   ssl: ssl.SSLContext | None = None,   proxy: str | None = None,   default_headers: Dict[str, str] | None = None,   user_agent_prefix: str | None = None,   user_agent_suffix: str | None = None,   logger: logging.Logger | None = None,   retry_handlers: List[[RetryHandler](../http_retry/handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")] | None = None)`

Expand source code

```typescript
class WebhookClient:
    url: str
    timeout: int
    ssl: Optional[SSLContext]
    proxy: Optional[str]
    default_headers: Dict[str, str]
    logger: logging.Logger
    retry_handlers: List[RetryHandler]

    def __init__(
        self,
        url: str,
        timeout: int = 30,
        ssl: Optional[SSLContext] = None,
        proxy: Optional[str] = None,
        default_headers: Optional[Dict[str, str]] = None,
        user_agent_prefix: Optional[str] = None,
        user_agent_suffix: Optional[str] = None,
        logger: Optional[logging.Logger] = None,
        retry_handlers: Optional[List[RetryHandler]] = None,
    ):
        """API client for Incoming Webhooks and `response_url`

        https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/

        Args:
            url: Complete URL to send data (e.g., `https://hooks.slack.com/XXX`)
            timeout: Request timeout (in seconds)
            ssl: `ssl.SSLContext` to use for requests
            proxy: Proxy URL (e.g., `localhost:9000`, `http://localhost:9000`)
            default_headers: Request headers to add to all requests
            user_agent_prefix: Prefix for User-Agent header value
            user_agent_suffix: Suffix for User-Agent header value
            logger: Custom logger
            retry_handlers: Retry handlers
        """
        self.url = url
        self.timeout = timeout
        self.ssl = ssl
        self.proxy = proxy
        self.default_headers = default_headers if default_headers else {}
        self.default_headers["User-Agent"] = get_user_agent(user_agent_prefix, user_agent_suffix)
        self.logger = logger if logger is not None else logging.getLogger(__name__)
        self.retry_handlers = retry_handlers if retry_handlers is not None else default_retry_handlers()

        if self.proxy is None or len(self.proxy.strip()) == 0:
            env_variable = load_http_proxy_from_env(self.logger)
            if env_variable is not None:
                self.proxy = env_variable

    def send(
        self,
        *,
        text: Optional[str] = None,
        attachments: Optional[Sequence[Union[Dict[str, Any], Attachment]]] = None,
        blocks: Optional[Sequence[Union[Dict[str, Any], Block]]] = None,
        response_type: Optional[str] = None,
        replace_original: Optional[bool] = None,
        delete_original: Optional[bool] = None,
        unfurl_links: Optional[bool] = None,
        unfurl_media: Optional[bool] = None,
        metadata: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> WebhookResponse:
        """Performs a Slack API request and returns the result.

        Args:
            text: The text message
                (even when having blocks, setting this as well is recommended as it works as fallback)
            attachments: A collection of attachments
            blocks: A collection of Block Kit UI components
            response_type: The type of message (either 'in_channel' or 'ephemeral')
            replace_original: True if you use this option for response_url requests
            delete_original: True if you use this option for response_url requests
            unfurl_links: Option to indicate whether text url should unfurl
            unfurl_media: Option to indicate whether media url should unfurl
            metadata: Metadata attached to the message
            headers: Request headers to append only for this request

        Returns:
            Webhook response
        """
        return self.send_dict(
            # It's fine to have None value elements here
            # because _build_body() filters them out when constructing the actual body data
            body={
                "text": text,
                "attachments": attachments,
                "blocks": blocks,
                "response_type": response_type,
                "replace_original": replace_original,
                "delete_original": delete_original,
                "unfurl_links": unfurl_links,
                "unfurl_media": unfurl_media,
                "metadata": metadata,
            },
            headers=headers,
        )

    def send_dict(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> WebhookResponse:
        """Performs a Slack API request and returns the result.

        Args:
            body: JSON data structure (it's still a dict at this point),
                if you give this argument, body_params and files will be skipped
            headers: Request headers to append only for this request
        Returns:
            Webhook response
        """
        return self._perform_http_request(
            body=_build_body(body),  # type: ignore[arg-type]
            headers=_build_request_headers(self.default_headers, headers),
        )

    def _perform_http_request(self, *, body: Dict[str, Any], headers: Dict[str, str]) -> WebhookResponse:
        raw_body = json.dumps(body)
        headers["Content-Type"] = "application/json;charset=utf-8"

        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"Sending a request - url: {self.url}, body: {raw_body}, headers: {headers}")

        url = self.url
        # NOTE: Intentionally ignore the `http_verb` here
        # Slack APIs accepts any API method requests with POST methods
        req = Request(method="POST", url=url, data=raw_body.encode("utf-8"), headers=headers)
        resp = None
        last_error = Exception("undefined internal error")

        retry_state = RetryState()
        counter_for_safety = 0
        while counter_for_safety < 100:
            counter_for_safety += 1
            # If this is a retry, the next try started here. We can reset the flag.
            retry_state.next_attempt_requested = False

            try:
                resp = self._perform_http_request_internal(url, req)
                # The resp is a 200 OK response
                return resp

            except HTTPError as e:
                # read the response body here
                charset = e.headers.get_content_charset() or "utf-8"
                response_body: str = e.read().decode(charset)
                # As adding new values to HTTPError#headers can be ignored, building a new dict object here
                response_headers = dict(e.headers.items())
                resp = WebhookResponse(
                    url=url,
                    status_code=e.code,
                    body=response_body,
                    headers=response_headers,
                )
                if e.code == 429:
                    # for backward-compatibility with WebClient (v.2.5.0 or older)
                    if "retry-after" not in resp.headers and "Retry-After" in resp.headers:
                        resp.headers["retry-after"] = resp.headers["Retry-After"]
                    if "Retry-After" not in resp.headers and "retry-after" in resp.headers:
                        resp.headers["Retry-After"] = resp.headers["retry-after"]
                _debug_log_response(self.logger, resp)

                # Try to find a retry handler for this error
                retry_request = RetryHttpRequest.from_urllib_http_request(req)
                retry_response = RetryHttpResponse(
                    status_code=e.code,
                    headers={k: [v] for k, v in e.headers.items()},
                    data=response_body.encode("utf-8") if response_body is not None else None,
                )
                for handler in self.retry_handlers:
                    if handler.can_retry(
                        state=retry_state,
                        request=retry_request,
                        response=retry_response,
                        error=e,
                    ):
                        if self.logger.level <= logging.DEBUG:
                            self.logger.info(
                                f"A retry handler found: {type(handler).__name__} for {req.method} {req.full_url} - {e}"
                            )
                        handler.prepare_for_next_attempt(
                            state=retry_state,
                            request=retry_request,
                            response=retry_response,
                            error=e,
                        )
                        break

                if retry_state.next_attempt_requested is False:
                    return resp

            except Exception as err:
                last_error = err
                self.logger.error(f"Failed to send a request to Slack API server: {err}")

                # Try to find a retry handler for this error
                retry_request = RetryHttpRequest.from_urllib_http_request(req)
                for handler in self.retry_handlers:
                    if handler.can_retry(
                        state=retry_state,
                        request=retry_request,
                        response=None,
                        error=err,
                    ):
                        if self.logger.level <= logging.DEBUG:
                            self.logger.info(
                                f"A retry handler found: {type(handler).__name__} for {req.method} {req.full_url} - {err}"
                            )
                        handler.prepare_for_next_attempt(
                            state=retry_state,
                            request=retry_request,
                            response=None,
                            error=err,
                        )
                        self.logger.info(f"Going to retry the same request: {req.method} {req.full_url}")
                        break

                if retry_state.next_attempt_requested is False:
                    raise err

        if resp is not None:
            return resp
        raise last_error

    def _perform_http_request_internal(self, url: str, req: Request):
        opener: Optional[OpenerDirector] = None
        # for security (BAN-B310)
        if url.lower().startswith("http"):
            if self.proxy is not None:
                if isinstance(self.proxy, str):
                    opener = urllib.request.build_opener(
                        ProxyHandler({"http": self.proxy, "https": self.proxy}),
                        HTTPSHandler(context=self.ssl),
                    )
                else:
                    raise SlackRequestError(f"Invalid proxy detected: {self.proxy} must be a str value")
        else:
            raise SlackRequestError(f"Invalid URL detected: {url}")

        http_resp: Optional[HTTPResponse] = None
        if opener:
            http_resp = opener.open(req, timeout=self.timeout)
        else:
            http_resp = urlopen(req, context=self.ssl, timeout=self.timeout)
        charset: str = http_resp.headers.get_content_charset() or "utf-8"
        response_body: str = http_resp.read().decode(charset)
        resp = WebhookResponse(
            url=url,
            status_code=http_resp.status,
            body=response_body,
            headers=http_resp.headers,  # type: ignore[arg-type]
        )
        _debug_log_response(self.logger, resp)
        return resp
```

API client for Incoming Webhooks and `response_url`

[https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/)

## Args

**`url`**

Complete URL to send data (e.g., `https://hooks.slack.com/XXX`)

**`timeout`**

Request timeout (in seconds)

**`ssl`**

`ssl.SSLContext` to use for requests

**`proxy`**

Proxy URL (e.g., `localhost:9000`, `http://localhost:9000`)

**`default_headers`**

Request headers to add to all requests

**`user_agent_prefix`**

Prefix for User-Agent header value

**`user_agent_suffix`**

Suffix for User-Agent header value

**`logger`**

Custom logger

**`retry_handlers`**

Retry handlers

### Class variables

`var default_headers : Dict[str, str]`

The type of the None singleton.

`var logger : logging.Logger`

The type of the None singleton.

`var proxy : str | None`

The type of the None singleton.

`var retry_handlers : List[[RetryHandler](../http_retry/handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")]`

The type of the None singleton.

`var ssl : ssl.SSLContext | None`

The type of the None singleton.

`var timeout : int`

The type of the None singleton.

`var url : str`

The type of the None singleton.

### Methods

`def send(self,   *,   text: str | None = None,   attachments: Sequence[Dict[str, Any] | [Attachment](../models/attachments/index.html#slack_sdk.models.attachments.Attachment "slack_sdk.models.attachments.Attachment")] | None = None,   blocks: Sequence[Dict[str, Any] | [Block](../models/blocks/blocks.html#slack_sdk.models.blocks.blocks.Block "slack_sdk.models.blocks.blocks.Block")] | None = None,   response_type: str | None = None,   replace_original: bool | None = None,   delete_original: bool | None = None,   unfurl_links: bool | None = None,   unfurl_media: bool | None = None,   metadata: Dict[str, Any] | None = None,   headers: Dict[str, str] | None = None) ‑> [WebhookResponse](webhook_response.html#slack_sdk.webhook.webhook_response.WebhookResponse "slack_sdk.webhook.webhook_response.WebhookResponse")`

Expand source code

```typescript
def send(
    self,
    *,
    text: Optional[str] = None,
    attachments: Optional[Sequence[Union[Dict[str, Any], Attachment]]] = None,
    blocks: Optional[Sequence[Union[Dict[str, Any], Block]]] = None,
    response_type: Optional[str] = None,
    replace_original: Optional[bool] = None,
    delete_original: Optional[bool] = None,
    unfurl_links: Optional[bool] = None,
    unfurl_media: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> WebhookResponse:
    """Performs a Slack API request and returns the result.

    Args:
        text: The text message
            (even when having blocks, setting this as well is recommended as it works as fallback)
        attachments: A collection of attachments
        blocks: A collection of Block Kit UI components
        response_type: The type of message (either 'in_channel' or 'ephemeral')
        replace_original: True if you use this option for response_url requests
        delete_original: True if you use this option for response_url requests
        unfurl_links: Option to indicate whether text url should unfurl
        unfurl_media: Option to indicate whether media url should unfurl
        metadata: Metadata attached to the message
        headers: Request headers to append only for this request

    Returns:
        Webhook response
    """
    return self.send_dict(
        # It's fine to have None value elements here
        # because _build_body() filters them out when constructing the actual body data
        body={
            "text": text,
            "attachments": attachments,
            "blocks": blocks,
            "response_type": response_type,
            "replace_original": replace_original,
            "delete_original": delete_original,
            "unfurl_links": unfurl_links,
            "unfurl_media": unfurl_media,
            "metadata": metadata,
        },
        headers=headers,
    )
```

Performs a Slack API request and returns the result.

## Args (2)

**`text`**

The text message (even when having blocks, setting this as well is recommended as it works as fallback)

**`attachments`**

A collection of attachments

**`blocks`**

A collection of Block Kit UI components

**`response_type`**

The type of message (either 'in\_channel' or 'ephemeral')

**`replace_original`**

True if you use this option for response\_url requests

**`delete_original`**

True if you use this option for response\_url requests

**`unfurl_links`**

Option to indicate whether text url should unfurl

**`unfurl_media`**

Option to indicate whether media url should unfurl

**`metadata`**

Metadata attached to the message

**`headers`**

Request headers to append only for this request

## Returns

Webhook response

`def send_dict(self, body: Dict[str, Any], headers: Dict[str, str] | None = None) ‑> [WebhookResponse](webhook_response.html#slack_sdk.webhook.webhook_response.WebhookResponse "slack_sdk.webhook.webhook_response.WebhookResponse")`

Expand source code

```python
def send_dict(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> WebhookResponse:
    """Performs a Slack API request and returns the result.

    Args:
        body: JSON data structure (it's still a dict at this point),
            if you give this argument, body_params and files will be skipped
        headers: Request headers to append only for this request
    Returns:
        Webhook response
    """
    return self._perform_http_request(
        body=_build_body(body),  # type: ignore[arg-type]
        headers=_build_request_headers(self.default_headers, headers),
    )
```

Performs a Slack API request and returns the result.

## Args (3)

**`body`**

JSON data structure (it's still a dict at this point), if you give this argument, body\_params and files will be skipped

**`headers`**

Request headers to append only for this request

## Returns (2)

Webhook response

`class WebhookResponse (*, url: str, status_code: int, body: str, headers: Dict[str, Any])`

Expand source code

```typescript
class WebhookResponse:
    def __init__(
        self,
        *,
        url: str,
        status_code: int,
        body: str,
        headers: Dict[str, Any],
    ):
        self.api_url = url
        self.status_code = status_code
        self.body = body
        self.headers = headers
```
