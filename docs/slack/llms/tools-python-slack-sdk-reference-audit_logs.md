Source: https://docs.slack.dev/tools/python-slack-sdk/reference/audit_logs

# Module slack_sdk.audit_logs

Audit Logs API is a set of APIs for monitoring what’s happening in your Enterprise Grid organization.

Refer to [https://docs.slack.dev/tools/python-slack-sdk/audit-logs](https://docs.slack.dev/tools/python-slack-sdk/audit-logs) for details.

## Sub-modules

`[slack_sdk.audit_logs.async_client](async_client.html "slack_sdk.audit_logs.async_client")`

`[slack_sdk.audit_logs.v1](v1/index.html "slack_sdk.audit_logs.v1")`

Audit Logs API is a set of APIs for monitoring what’s happening in your Enterprise Grid organization …

## Classes

`class AuditLogsClient (token: str,   timeout: int = 30,   ssl: ssl.SSLContext | None = None,   proxy: str | None = None,   base_url: str = 'https://api.slack.com/audit/v1/',   default_headers: Dict[str, str] | None = None,   user_agent_prefix: str | None = None,   user_agent_suffix: str | None = None,   logger: logging.Logger | None = None,   retry_handlers: List[[RetryHandler](../http_retry/handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")] | None = None)`

Expand source code

```typescript
class AuditLogsClient:
    BASE_URL = "https://api.slack.com/audit/v1/"

    token: str
    timeout: int
    ssl: Optional[SSLContext]
    proxy: Optional[str]
    base_url: str
    default_headers: Dict[str, str]
    logger: logging.Logger
    retry_handlers: List[RetryHandler]

    def __init__(
        self,
        token: str,
        timeout: int = 30,
        ssl: Optional[SSLContext] = None,
        proxy: Optional[str] = None,
        base_url: str = BASE_URL,
        default_headers: Optional[Dict[str, str]] = None,
        user_agent_prefix: Optional[str] = None,
        user_agent_suffix: Optional[str] = None,
        logger: Optional[logging.Logger] = None,
        retry_handlers: Optional[List[RetryHandler]] = None,
    ):
        """API client for Audit Logs API
        See https://docs.slack.dev/admins/audit-logs-api/ for more details

        Args:
            token: An admin user's token, which starts with `xoxp-`
            timeout: Request timeout (in seconds)
            ssl: `ssl.SSLContext` to use for requests
            proxy: Proxy URL (e.g., `localhost:9000`, `http://localhost:9000`)
            base_url: The base URL for API calls
            default_headers: Request headers to add to all requests
            user_agent_prefix: Prefix for User-Agent header value
            user_agent_suffix: Suffix for User-Agent header value
            logger: Custom logger
            retry_handlers: Retry handlers
        """
        self.token = token
        self.timeout = timeout
        self.ssl = ssl
        self.proxy = proxy
        self.base_url = base_url
        self.default_headers = default_headers if default_headers else {}
        self.default_headers["User-Agent"] = get_user_agent(user_agent_prefix, user_agent_suffix)
        self.logger = logger if logger is not None else logging.getLogger(__name__)
        self.retry_handlers = retry_handlers if retry_handlers is not None else default_retry_handlers()

        if self.proxy is None or len(self.proxy.strip()) == 0:
            env_variable = load_http_proxy_from_env(self.logger)
            if env_variable is not None:
                self.proxy = env_variable

    def schemas(
        self,
        *,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AuditLogsResponse:
        """Returns information about the kind of objects which the Audit Logs API
        returns as a list of all objects and a short description.
        Authentication not required.

        Args:
            query_params: Set any values if you want to add query params
            headers: Additional request headers
        Returns:
            API response
        """
        return self.api_call(
            path="schemas",
            query_params=query_params,
            headers=headers,
        )

    def actions(
        self,
        *,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AuditLogsResponse:
        """Returns information about the kind of actions that the Audit Logs API
        returns as a list of all actions and a short description of each.
        Authentication not required.

        Args:
            query_params: Set any values if you want to add query params
            headers: Additional request headers

        Returns:
            API response
        """
        return self.api_call(
            path="actions",
            query_params=query_params,
            headers=headers,
        )

    def logs(
        self,
        *,
        latest: Optional[int] = None,
        oldest: Optional[int] = None,
        limit: Optional[int] = None,
        action: Optional[str] = None,
        actor: Optional[str] = None,
        entity: Optional[str] = None,
        cursor: Optional[str] = None,
        additional_query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AuditLogsResponse:
        """This is the primary endpoint for retrieving actual audit events from your organization.
        It will return a list of actions that have occurred on the installed workspace or grid organization.
        Authentication required.

        The following filters can be applied in order to narrow the range of actions returned.
        Filters are added as query string parameters and can be combined together.
        Multiple filter parameters are additive (a boolean AND) and are separated
        with an ampersand (&) in the query string. Filtering is entirely optional.

        Args:
            latest: Unix timestamp of the most recent audit event to include (inclusive).
            oldest: Unix timestamp of the least recent audit event to include (inclusive).
                Data is not available prior to March 2018.
            limit: Number of results to optimistically return, maximum 9999.
            action: Name of the action.
            actor: User ID who initiated the action.
            entity: ID of the target entity of the action (such as a channel, workspace, organization, file).
            cursor: The next page cursor of pagination
            additional_query_params: Add anything else if you need to use the ones this library does not support
            headers: Additional request headers

        Returns:
            API response
        """
        query_params = {
            "latest": latest,
            "oldest": oldest,
            "limit": limit,
            "action": action,
            "actor": actor,
            "entity": entity,
            "cursor": cursor,
        }
        if additional_query_params is not None:
            query_params.update(additional_query_params)
        query_params = {k: v for k, v in query_params.items() if v is not None}
        return self.api_call(
            path="logs",
            query_params=query_params,
            headers=headers,
        )

    def api_call(
        self,
        *,
        http_verb: str = "GET",
        path: str,
        query_params: Optional[Dict[str, Any]] = None,
        body_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> AuditLogsResponse:
        """Performs a Slack API request and returns the result."""
        url = f"{self.base_url}{path}"
        query = _build_query(query_params)
        if len(query) > 0:
            url += f"?{query}"

        return self._perform_http_request(
            http_verb=http_verb,
            url=url,
            body=body_params,
            headers=_build_request_headers(
                token=self.token,
                default_headers=self.default_headers,
                additional_headers=headers,
            ),
        )

    def _perform_http_request(
        self,
        *,
        http_verb: str = "GET",
        url: str,
        body: Optional[Dict[str, Any]] = None,
        headers: Dict[str, str],
    ) -> AuditLogsResponse:
        if body is not None:
            body = json.dumps(body)  # type: ignore[assignment]
        headers["Content-Type"] = "application/json;charset=utf-8"

        if self.logger.level <= logging.DEBUG:
            headers_for_logging = {k: "(redacted)" if k.lower() == "authorization" else v for k, v in headers.items()}
            self.logger.debug(f"Sending a request - url: {url}, body: {body}, headers: {headers_for_logging}")

        # NOTE: Intentionally ignore the `http_verb` here
        # Slack APIs accepts any API method requests with POST methods
        req = Request(
            method=http_verb,
            url=url,
            data=body.encode("utf-8") if body is not None else None,  # type: ignore[attr-defined]
            headers=headers,
        )
        resp = None
        last_error = None

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
                resp = AuditLogsResponse(
                    url=url,
                    status_code=e.code,
                    raw_body=response_body,
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
        raise last_error  # type: ignore[misc]

    def _perform_http_request_internal(self, url: str, req: Request) -> AuditLogsResponse:
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

        http_resp: HTTPResponse
        if opener:
            http_resp = opener.open(req, timeout=self.timeout)
        else:
            http_resp = urlopen(req, context=self.ssl, timeout=self.timeout)
        charset: str = http_resp.headers.get_content_charset() or "utf-8"
        response_body: str = http_resp.read().decode(charset)
        resp = AuditLogsResponse(
            url=url,
            status_code=http_resp.status,
            raw_body=response_body,
            headers=http_resp.headers,  # type: ignore[arg-type]
        )
        _debug_log_response(self.logger, resp)
        return resp
```

API client for Audit Logs API See [https://docs.slack.dev/admins/audit-logs-api/](https://docs.slack.dev/admins/audit-logs-api/) for more details

## Args

**`token`**

An admin user's token, which starts with `xoxp-`

**`timeout`**

Request timeout (in seconds)

**`ssl`**

`ssl.SSLContext` to use for requests

**`proxy`**

Proxy URL (e.g., `localhost:9000`, `http://localhost:9000`)

**`base_url`**

The base URL for API calls

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

`var BASE_URL`

The type of the None singleton.

`var base_url : str`

The type of the None singleton.

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

`var token : str`

The type of the None singleton.

### Methods

`def actions(self,   *,   query_params: Dict[str, Any] | None = None,   headers: Dict[str, str] | None = None) ‑> [AuditLogsResponse](v1/response.html#slack_sdk.audit_logs.v1.response.AuditLogsResponse "slack_sdk.audit_logs.v1.response.AuditLogsResponse")`

Expand source code

```python
def actions(
    self,
    *,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> AuditLogsResponse:
    """Returns information about the kind of actions that the Audit Logs API
    returns as a list of all actions and a short description of each.
    Authentication not required.

    Args:
        query_params: Set any values if you want to add query params
        headers: Additional request headers

    Returns:
        API response
    """
    return self.api_call(
        path="actions",
        query_params=query_params,
        headers=headers,
    )
```

Returns information about the kind of actions that the Audit Logs API returns as a list of all actions and a short description of each. Authentication not required.

## Args (2)

**`query_params`**

Set any values if you want to add query params

**`headers`**

Additional request headers

## Returns

API response

`def api_call(self,   *,   http_verb: str = 'GET',   path: str,   query_params: Dict[str, Any] | None = None,   body_params: Dict[str, Any] | None = None,   headers: Dict[str, str] | None = None) ‑> [AuditLogsResponse](v1/response.html#slack_sdk.audit_logs.v1.response.AuditLogsResponse "slack_sdk.audit_logs.v1.response.AuditLogsResponse")`

Expand source code

```python
def api_call(
    self,
    *,
    http_verb: str = "GET",
    path: str,
    query_params: Optional[Dict[str, Any]] = None,
    body_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> AuditLogsResponse:
    """Performs a Slack API request and returns the result."""
    url = f"{self.base_url}{path}"
    query = _build_query(query_params)
    if len(query) > 0:
        url += f"?{query}"

    return self._perform_http_request(
        http_verb=http_verb,
        url=url,
        body=body_params,
        headers=_build_request_headers(
            token=self.token,
            default_headers=self.default_headers,
            additional_headers=headers,
        ),
    )
```

Performs a Slack API request and returns the result.

`def logs(self,   *,   latest: int | None = None,   oldest: int | None = None,   limit: int | None = None,   action: str | None = None,   actor: str | None = None,   entity: str | None = None,   cursor: str | None = None,   additional_query_params: Dict[str, Any] | None = None,   headers: Dict[str, str] | None = None) ‑> [AuditLogsResponse](v1/response.html#slack_sdk.audit_logs.v1.response.AuditLogsResponse "slack_sdk.audit_logs.v1.response.AuditLogsResponse")`

Expand source code

```typescript
def logs(
    self,
    *,
    latest: Optional[int] = None,
    oldest: Optional[int] = None,
    limit: Optional[int] = None,
    action: Optional[str] = None,
    actor: Optional[str] = None,
    entity: Optional[str] = None,
    cursor: Optional[str] = None,
    additional_query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> AuditLogsResponse:
    """This is the primary endpoint for retrieving actual audit events from your organization.
    It will return a list of actions that have occurred on the installed workspace or grid organization.
    Authentication required.

    The following filters can be applied in order to narrow the range of actions returned.
    Filters are added as query string parameters and can be combined together.
    Multiple filter parameters are additive (a boolean AND) and are separated
    with an ampersand (&) in the query string. Filtering is entirely optional.

    Args:
        latest: Unix timestamp of the most recent audit event to include (inclusive).
        oldest: Unix timestamp of the least recent audit event to include (inclusive).
            Data is not available prior to March 2018.
        limit: Number of results to optimistically return, maximum 9999.
        action: Name of the action.
        actor: User ID who initiated the action.
        entity: ID of the target entity of the action (such as a channel, workspace, organization, file).
        cursor: The next page cursor of pagination
        additional_query_params: Add anything else if you need to use the ones this library does not support
        headers: Additional request headers

    Returns:
        API response
    """
    query_params = {
        "latest": latest,
        "oldest": oldest,
        "limit": limit,
        "action": action,
        "actor": actor,
        "entity": entity,
        "cursor": cursor,
    }
    if additional_query_params is not None:
        query_params.update(additional_query_params)
    query_params = {k: v for k, v in query_params.items() if v is not None}
    return self.api_call(
        path="logs",
        query_params=query_params,
        headers=headers,
    )
```

This is the primary endpoint for retrieving actual audit events from your organization. It will return a list of actions that have occurred on the installed workspace or grid organization. Authentication required.

The following filters can be applied in order to narrow the range of actions returned. Filters are added as query string parameters and can be combined together. Multiple filter parameters are additive (a boolean AND) and are separated with an ampersand (&) in the query string. Filtering is entirely optional.

## Args (3)

**`latest`**

Unix timestamp of the most recent audit event to include (inclusive).

**`oldest`**

Unix timestamp of the least recent audit event to include (inclusive). Data is not available prior to March 2018.

**`limit`**

Number of results to optimistically return, maximum 9999.

**`action`**

Name of the action.

**`actor`**

User ID who initiated the action.

**`entity`**

ID of the target entity of the action (such as a channel, workspace, organization, file).

**`cursor`**

The next page cursor of pagination

**`additional_query_params`**

Add anything else if you need to use the ones this library does not support

**`headers`**

Additional request headers

## Returns (2)

API response

`def schemas(self,   *,   query_params: Dict[str, Any] | None = None,   headers: Dict[str, str] | None = None) ‑> [AuditLogsResponse](v1/response.html#slack_sdk.audit_logs.v1.response.AuditLogsResponse "slack_sdk.audit_logs.v1.response.AuditLogsResponse")`

Expand source code

```python
def schemas(
    self,
    *,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> AuditLogsResponse:
    """Returns information about the kind of objects which the Audit Logs API
    returns as a list of all objects and a short description.
    Authentication not required.

    Args:
        query_params: Set any values if you want to add query params
        headers: Additional request headers
    Returns:
        API response
    """
    return self.api_call(
        path="schemas",
        query_params=query_params,
        headers=headers,
    )
```

Returns information about the kind of objects which the Audit Logs API returns as a list of all objects and a short description. Authentication not required.

## Args (4)

**`query_params`**

Set any values if you want to add query params

**`headers`**

Additional request headers

## Returns (3)

API response

`class AuditLogsResponse (*, url: str, status_code: int, raw_body: str | None, headers: dict)`

Expand source code

```typescript
class AuditLogsResponse:
    url: str
    status_code: int
    headers: Dict[str, Any]
    raw_body: Optional[str]
    body: Optional[Dict[str, Any]]
    typed_body: Optional[LogsResponse]

    @property  # type: ignore[no-redef]
    def typed_body(self) -> Optional[LogsResponse]:
        if self.body is None:
            return None
        return LogsResponse(**self.body)

    def __init__(
        self,
        *,
        url: str,
        status_code: int,
        raw_body: Optional[str],
        headers: dict,
    ):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.raw_body = raw_body
        self.body = json.loads(raw_body) if raw_body is not None and raw_body.startswith("{") else None
```

### Class variables (2)

`var body : Dict[str, Any] | None`

The type of the None singleton.

`var headers : Dict[str, Any]`

The type of the None singleton.

`var raw_body : str | None`

The type of the None singleton.

`var status_code : int`

The type of the None singleton.

`var url : str`

The type of the None singleton.

### Instance variables

`prop typed_body : [LogsResponse](v1/logs.html#slack_sdk.audit_logs.v1.logs.LogsResponse "slack_sdk.audit_logs.v1.logs.LogsResponse") | None`

Expand source code

```python
@property  # type: ignore[no-redef]
def typed_body(self) -> Optional[LogsResponse]:
    if self.body is None:
        return None
    return LogsResponse(**self.body)
```
