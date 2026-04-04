Source: https://docs.slack.dev/tools/python-slack-sdk/reference/scim

# Module slack_sdk.scim

SCIM API is a set of APIs for provisioning and managing user accounts and groups. SCIM is used by Single Sign-On (SSO) services and identity providers to manage people across a variety of tools, including Slack.

Refer to [https://docs.slack.dev/tools/python-slack-sdk/scim](https://docs.slack.dev/tools/python-slack-sdk/scim) for details.

## Sub-modules

`[slack_sdk.scim.async_client](async_client.html "slack_sdk.scim.async_client")`

`[slack_sdk.scim.v1](v1/index.html "slack_sdk.scim.v1")`

SCIM API is a set of APIs for provisioning and managing user accounts and groups. SCIM is used by Single Sign-On (SSO) services and identity providers …

## Classes

`class Group (*,   display_name: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   id: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   members: List[[GroupMember](v1/group.html#slack_sdk.scim.v1.group.GroupMember "slack_sdk.scim.v1.group.GroupMember")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   meta: [GroupMeta](v1/group.html#slack_sdk.scim.v1.group.GroupMeta "slack_sdk.scim.v1.group.GroupMeta") | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   schemas: List[str] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   **kwargs)`

Expand source code

```typescript
class Group:
    display_name: Union[Optional[str], DefaultArg]
    id: Union[Optional[str], DefaultArg]
    members: Union[Optional[List[GroupMember]], DefaultArg]
    meta: Union[Optional[GroupMeta], DefaultArg]
    schemas: Union[Optional[List[str]], DefaultArg]
    unknown_fields: Dict[str, Any]

    def __init__(
        self,
        *,
        display_name: Union[Optional[str], DefaultArg] = NotGiven,
        id: Union[Optional[str], DefaultArg] = NotGiven,
        members: Union[Optional[List[GroupMember]], DefaultArg] = NotGiven,
        meta: Union[Optional[GroupMeta], DefaultArg] = NotGiven,
        schemas: Union[Optional[List[str]], DefaultArg] = NotGiven,
        **kwargs,
    ) -> None:
        self.display_name = display_name
        self.id = id
        self.members = (
            [a if isinstance(a, GroupMember) else GroupMember(**a) for a in members] if _is_iterable(members) else members
        )
        self.meta = GroupMeta(**meta) if meta is not None and isinstance(meta, dict) else meta
        self.schemas = schemas
        self.unknown_fields = kwargs

    def to_dict(self):
        return _to_dict_without_not_given(self)

    def __repr__(self):
        return f"<slack_sdk.scim.{self.__class__.__name__}: {self.to_dict()}>"
```

### Class variables

`var display_name : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var id : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var members : List[[GroupMember](v1/group.html#slack_sdk.scim.v1.group.GroupMember "slack_sdk.scim.v1.group.GroupMember")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var meta : [GroupMeta](v1/group.html#slack_sdk.scim.v1.group.GroupMeta "slack_sdk.scim.v1.group.GroupMeta") | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var schemas : List[str] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var unknown_fields : Dict[str, Any]`

The type of the None singleton.

### Methods

`def to_dict(self)`

Expand source code

```python
def to_dict(self):
    return _to_dict_without_not_given(self)
```

`class ReadGroupResponse (underlying: [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse"))`

Expand source code

```typescript
class ReadGroupResponse(SCIMResponse):
    group: Group

    @property
    def group(self) -> Group:
        return Group(**self.snake_cased_body)

    def __init__(self, underlying: SCIMResponse):
        self.underlying = underlying
        self.url = underlying.url
        self.status_code = underlying.status_code
        self.headers = underlying.headers
        self.raw_body = underlying.raw_body
        self.body = underlying.body
        self._snake_cased_body = None
```

### Ancestors

* [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")

### Instance variables

`prop group : [Group](v1/group.html#slack_sdk.scim.v1.group.Group "slack_sdk.scim.v1.group.Group")`

Expand source code

```python
@property
def group(self) -> Group:
    return Group(**self.snake_cased_body)
```

### Inherited members

* `**[SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")**`:
  * `[body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.body "slack_sdk.scim.v1.response.SCIMResponse.body")`
  * `[headers](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.headers "slack_sdk.scim.v1.response.SCIMResponse.headers")`
  * `[raw_body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.raw_body "slack_sdk.scim.v1.response.SCIMResponse.raw_body")`
  * `[status_code](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.status_code "slack_sdk.scim.v1.response.SCIMResponse.status_code")`
  * `[url](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.url "slack_sdk.scim.v1.response.SCIMResponse.url")`

`class ReadUserResponse (underlying: [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse"))`

Expand source code

```typescript
class ReadUserResponse(SCIMResponse):
    user: User

    @property
    def user(self) -> User:
        return User(**self.snake_cased_body)

    def __init__(self, underlying: SCIMResponse):
        self.underlying = underlying
        self.url = underlying.url
        self.status_code = underlying.status_code
        self.headers = underlying.headers
        self.raw_body = underlying.raw_body
        self.body = underlying.body
        self._snake_cased_body = None
```

### Ancestors (2)

* [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")

### Instance variables (2)

`prop user : [User](v1/user.html#slack_sdk.scim.v1.user.User "slack_sdk.scim.v1.user.User")`

Expand source code

```python
@property
def user(self) -> User:
    return User(**self.snake_cased_body)
```

### Inherited members (2)

* `**[SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")**`:
  * `[body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.body "slack_sdk.scim.v1.response.SCIMResponse.body")`
  * `[headers](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.headers "slack_sdk.scim.v1.response.SCIMResponse.headers")`
  * `[raw_body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.raw_body "slack_sdk.scim.v1.response.SCIMResponse.raw_body")`
  * `[status_code](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.status_code "slack_sdk.scim.v1.response.SCIMResponse.status_code")`
  * `[url](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.url "slack_sdk.scim.v1.response.SCIMResponse.url")`

`class SCIMClient (token: str,   timeout: int = 30,   ssl: ssl.SSLContext | None = None,   proxy: str | None = None,   base_url: str = 'https://api.slack.com/scim/v1/',   default_headers: Dict[str, str] | None = None,   user_agent_prefix: str | None = None,   user_agent_suffix: str | None = None,   logger: logging.Logger | None = None,   retry_handlers: List[[RetryHandler](../http_retry/handler.html#slack_sdk.http_retry.handler.RetryHandler "slack_sdk.http_retry.handler.RetryHandler")] | None = None)`

Expand source code

```typescript
class SCIMClient:
    BASE_URL = "https://api.slack.com/scim/v1/"

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
        """API client for SCIM API
        See https://docs.slack.dev/admins/scim-api/ for more details

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

    # -------------------------
    # Users
    # -------------------------

    def search_users(
        self,
        *,
        # Pagination required as of August 30, 2019.
        count: int,
        start_index: int,
        filter: Optional[str] = None,
    ) -> SearchUsersResponse:
        return SearchUsersResponse(
            self.api_call(
                http_verb="GET",
                path="Users",
                query_params={
                    "filter": filter,
                    "count": count,
                    "startIndex": start_index,
                },
            )
        )

    def read_user(self, id: str) -> ReadUserResponse:
        return ReadUserResponse(self.api_call(http_verb="GET", path=f"Users/{quote(id)}"))

    def create_user(self, user: Union[Dict[str, Any], User]) -> UserCreateResponse:
        return UserCreateResponse(
            self.api_call(
                http_verb="POST",
                path="Users",
                body_params=user.to_dict() if isinstance(user, User) else _to_dict_without_not_given(user),
            )
        )

    def patch_user(self, id: str, partial_user: Union[Dict[str, Any], User]) -> UserPatchResponse:
        return UserPatchResponse(
            self.api_call(
                http_verb="PATCH",
                path=f"Users/{quote(id)}",
                body_params=(
                    partial_user.to_dict() if isinstance(partial_user, User) else _to_dict_without_not_given(partial_user)
                ),
            )
        )

    def update_user(self, user: Union[Dict[str, Any], User]) -> UserUpdateResponse:
        user_id = user.id if isinstance(user, User) else user["id"]
        return UserUpdateResponse(
            self.api_call(
                http_verb="PUT",
                path=f"Users/{quote(user_id)}",
                body_params=user.to_dict() if isinstance(user, User) else _to_dict_without_not_given(user),
            )
        )

    def delete_user(self, id: str) -> UserDeleteResponse:
        return UserDeleteResponse(
            self.api_call(
                http_verb="DELETE",
                path=f"Users/{quote(id)}",
            )
        )

    # -------------------------
    # Groups
    # -------------------------

    def search_groups(
        self,
        *,
        # Pagination required as of August 30, 2019.
        count: int,
        start_index: int,
        filter: Optional[str] = None,
    ) -> SearchGroupsResponse:
        return SearchGroupsResponse(
            self.api_call(
                http_verb="GET",
                path="Groups",
                query_params={
                    "filter": filter,
                    "count": count,
                    "startIndex": start_index,
                },
            )
        )

    def read_group(self, id: str) -> ReadGroupResponse:
        return ReadGroupResponse(self.api_call(http_verb="GET", path=f"Groups/{quote(id)}"))

    def create_group(self, group: Union[Dict[str, Any], Group]) -> GroupCreateResponse:
        return GroupCreateResponse(
            self.api_call(
                http_verb="POST",
                path="Groups",
                body_params=group.to_dict() if isinstance(group, Group) else _to_dict_without_not_given(group),
            )
        )

    def patch_group(self, id: str, partial_group: Union[Dict[str, Any], Group]) -> GroupPatchResponse:
        return GroupPatchResponse(
            self.api_call(
                http_verb="PATCH",
                path=f"Groups/{quote(id)}",
                body_params=(
                    partial_group.to_dict()
                    if isinstance(partial_group, Group)
                    else _to_dict_without_not_given(partial_group)
                ),
            )
        )

    def update_group(self, group: Union[Dict[str, Any], Group]) -> GroupUpdateResponse:
        group_id = group.id if isinstance(group, Group) else group["id"]
        return GroupUpdateResponse(
            self.api_call(
                http_verb="PUT",
                path=f"Groups/{quote(group_id)}",
                body_params=group.to_dict() if isinstance(group, Group) else _to_dict_without_not_given(group),
            )
        )

    def delete_group(self, id: str) -> GroupDeleteResponse:
        return GroupDeleteResponse(
            self.api_call(
                http_verb="DELETE",
                path=f"Groups/{quote(id)}",
            )
        )

    # -------------------------

    def api_call(
        self,
        *,
        http_verb: str,
        path: str,
        query_params: Optional[Dict[str, Any]] = None,
        body_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> SCIMResponse:
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
    ) -> SCIMResponse:
        if body is not None:
            if body.get("schemas") is None:
                body["schemas"] = ["urn:scim:schemas:core:1.0"]
            body = json.dumps(body)
        headers["Content-Type"] = "application/json;charset=utf-8"

        if self.logger.level <= logging.DEBUG:
            headers_for_logging = {k: "(redacted)" if k.lower() == "authorization" else v for k, v in headers.items()}
            self.logger.debug(f"Sending a request - {http_verb} url: {url}, body: {body}, headers: {headers_for_logging}")

        # NOTE: Intentionally ignore the `http_verb` here
        # Slack APIs accepts any API method requests with POST methods
        req = Request(
            method=http_verb,
            url=url,
            data=body.encode("utf-8") if body is not None else None,
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
                resp = SCIMResponse(
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
        raise last_error

    def _perform_http_request_internal(self, url: str, req: Request) -> SCIMResponse:
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

        # NOTE: BAN-B310 is already checked above
        http_resp: Optional[HTTPResponse] = None
        if opener:
            http_resp = opener.open(req, timeout=self.timeout)
        else:
            http_resp = urlopen(req, context=self.ssl, timeout=self.timeout)
        charset: str = http_resp.headers.get_content_charset() or "utf-8"
        response_body: str = http_resp.read().decode(charset)
        resp = SCIMResponse(
            url=url,
            status_code=http_resp.status,
            raw_body=response_body,
            headers=http_resp.headers,
        )
        _debug_log_response(self.logger, resp)
        return resp
```

API client for SCIM API See [https://docs.slack.dev/admins/scim-api/](https://docs.slack.dev/admins/scim-api/) for more details

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

### Class variables (2)

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

### Methods (2)

`def api_call(self,   *,   http_verb: str,   path: str,   query_params: Dict[str, Any] | None = None,   body_params: Dict[str, Any] | None = None,   headers: Dict[str, str] | None = None) ‑> [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")`

Expand source code

```python
def api_call(
    self,
    *,
    http_verb: str,
    path: str,
    query_params: Optional[Dict[str, Any]] = None,
    body_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> SCIMResponse:
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

`def create_group(self,   group: Dict[str, Any] | [Group](v1/group.html#slack_sdk.scim.v1.group.Group "slack_sdk.scim.v1.group.Group")) ‑> [GroupCreateResponse](v1/response.html#slack_sdk.scim.v1.response.GroupCreateResponse "slack_sdk.scim.v1.response.GroupCreateResponse")`

Expand source code

```python
def create_group(self, group: Union[Dict[str, Any], Group]) -> GroupCreateResponse:
    return GroupCreateResponse(
        self.api_call(
            http_verb="POST",
            path="Groups",
            body_params=group.to_dict() if isinstance(group, Group) else _to_dict_without_not_given(group),
        )
    )
```

`def create_user(self,   user: Dict[str, Any] | [User](v1/user.html#slack_sdk.scim.v1.user.User "slack_sdk.scim.v1.user.User")) ‑> [UserCreateResponse](v1/response.html#slack_sdk.scim.v1.response.UserCreateResponse "slack_sdk.scim.v1.response.UserCreateResponse")`

Expand source code

```python
def create_user(self, user: Union[Dict[str, Any], User]) -> UserCreateResponse:
    return UserCreateResponse(
        self.api_call(
            http_verb="POST",
            path="Users",
            body_params=user.to_dict() if isinstance(user, User) else _to_dict_without_not_given(user),
        )
    )
```

`def delete_group(self, id: str) ‑> [GroupDeleteResponse](v1/response.html#slack_sdk.scim.v1.response.GroupDeleteResponse "slack_sdk.scim.v1.response.GroupDeleteResponse")`

Expand source code

```python
def delete_group(self, id: str) -> GroupDeleteResponse:
    return GroupDeleteResponse(
        self.api_call(
            http_verb="DELETE",
            path=f"Groups/{quote(id)}",
        )
    )
```

`def delete_user(self, id: str) ‑> [UserDeleteResponse](v1/response.html#slack_sdk.scim.v1.response.UserDeleteResponse "slack_sdk.scim.v1.response.UserDeleteResponse")`

Expand source code

```python
def delete_user(self, id: str) -> UserDeleteResponse:
    return UserDeleteResponse(
        self.api_call(
            http_verb="DELETE",
            path=f"Users/{quote(id)}",
        )
    )
```

`def patch_group(self,   id: str,   partial_group: Dict[str, Any] | [Group](v1/group.html#slack_sdk.scim.v1.group.Group "slack_sdk.scim.v1.group.Group")) ‑> [GroupPatchResponse](v1/response.html#slack_sdk.scim.v1.response.GroupPatchResponse "slack_sdk.scim.v1.response.GroupPatchResponse")`

Expand source code

```python
def patch_group(self, id: str, partial_group: Union[Dict[str, Any], Group]) -> GroupPatchResponse:
    return GroupPatchResponse(
        self.api_call(
            http_verb="PATCH",
            path=f"Groups/{quote(id)}",
            body_params=(
                partial_group.to_dict()
                if isinstance(partial_group, Group)
                else _to_dict_without_not_given(partial_group)
            ),
        )
    )
```

`def patch_user(self,   id: str,   partial_user: Dict[str, Any] | [User](v1/user.html#slack_sdk.scim.v1.user.User "slack_sdk.scim.v1.user.User")) ‑> [UserPatchResponse](v1/response.html#slack_sdk.scim.v1.response.UserPatchResponse "slack_sdk.scim.v1.response.UserPatchResponse")`

Expand source code

```python
def patch_user(self, id: str, partial_user: Union[Dict[str, Any], User]) -> UserPatchResponse:
    return UserPatchResponse(
        self.api_call(
            http_verb="PATCH",
            path=f"Users/{quote(id)}",
            body_params=(
                partial_user.to_dict() if isinstance(partial_user, User) else _to_dict_without_not_given(partial_user)
            ),
        )
    )
```

`def read_group(self, id: str) ‑> [ReadGroupResponse](v1/response.html#slack_sdk.scim.v1.response.ReadGroupResponse "slack_sdk.scim.v1.response.ReadGroupResponse")`

Expand source code

```python
def read_group(self, id: str) -> ReadGroupResponse:
    return ReadGroupResponse(self.api_call(http_verb="GET", path=f"Groups/{quote(id)}"))
```

`def read_user(self, id: str) ‑> [ReadUserResponse](v1/response.html#slack_sdk.scim.v1.response.ReadUserResponse "slack_sdk.scim.v1.response.ReadUserResponse")`

Expand source code

```python
def read_user(self, id: str) -> ReadUserResponse:
    return ReadUserResponse(self.api_call(http_verb="GET", path=f"Users/{quote(id)}"))
```

`def search_groups(self, *, count: int, start_index: int, filter: str | None = None) ‑> [SearchGroupsResponse](v1/response.html#slack_sdk.scim.v1.response.SearchGroupsResponse "slack_sdk.scim.v1.response.SearchGroupsResponse")`

Expand source code

```python
def search_groups(
    self,
    *,
    # Pagination required as of August 30, 2019.
    count: int,
    start_index: int,
    filter: Optional[str] = None,
) -> SearchGroupsResponse:
    return SearchGroupsResponse(
        self.api_call(
            http_verb="GET",
            path="Groups",
            query_params={
                "filter": filter,
                "count": count,
                "startIndex": start_index,
            },
        )
    )
```

`def search_users(self, *, count: int, start_index: int, filter: str | None = None) ‑> [SearchUsersResponse](v1/response.html#slack_sdk.scim.v1.response.SearchUsersResponse "slack_sdk.scim.v1.response.SearchUsersResponse")`

Expand source code

```python
def search_users(
    self,
    *,
    # Pagination required as of August 30, 2019.
    count: int,
    start_index: int,
    filter: Optional[str] = None,
) -> SearchUsersResponse:
    return SearchUsersResponse(
        self.api_call(
            http_verb="GET",
            path="Users",
            query_params={
                "filter": filter,
                "count": count,
                "startIndex": start_index,
            },
        )
    )
```

`def update_group(self,   group: Dict[str, Any] | [Group](v1/group.html#slack_sdk.scim.v1.group.Group "slack_sdk.scim.v1.group.Group")) ‑> [GroupUpdateResponse](v1/response.html#slack_sdk.scim.v1.response.GroupUpdateResponse "slack_sdk.scim.v1.response.GroupUpdateResponse")`

Expand source code

```python
def update_group(self, group: Union[Dict[str, Any], Group]) -> GroupUpdateResponse:
    group_id = group.id if isinstance(group, Group) else group["id"]
    return GroupUpdateResponse(
        self.api_call(
            http_verb="PUT",
            path=f"Groups/{quote(group_id)}",
            body_params=group.to_dict() if isinstance(group, Group) else _to_dict_without_not_given(group),
        )
    )
```

`def update_user(self,   user: Dict[str, Any] | [User](v1/user.html#slack_sdk.scim.v1.user.User "slack_sdk.scim.v1.user.User")) ‑> [UserUpdateResponse](v1/response.html#slack_sdk.scim.v1.response.UserUpdateResponse "slack_sdk.scim.v1.response.UserUpdateResponse")`

Expand source code

```python
def update_user(self, user: Union[Dict[str, Any], User]) -> UserUpdateResponse:
    user_id = user.id if isinstance(user, User) else user["id"]
    return UserUpdateResponse(
        self.api_call(
            http_verb="PUT",
            path=f"Users/{quote(user_id)}",
            body_params=user.to_dict() if isinstance(user, User) else _to_dict_without_not_given(user),
        )
    )
```

`class SCIMResponse (*, url: str, status_code: int, raw_body: str | None, headers: dict)`

Expand source code

```typescript
class SCIMResponse:
    url: str
    status_code: int
    headers: Dict[str, Any]
    raw_body: Optional[str]
    body: Optional[Dict[str, Any]]
    snake_cased_body: Optional[Dict[str, Any]]

    errors: Optional[Errors]

    @property
    def snake_cased_body(self) -> Optional[Dict[str, Any]]:
        if self._snake_cased_body is None:
            self._snake_cased_body = _to_snake_cased(self.body)
        return self._snake_cased_body

    @property
    def errors(self) -> Optional[Errors]:
        errors = self.snake_cased_body.get("errors")
        if errors is None:
            return None
        return Errors(**errors)

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
        self._snake_cased_body = None  # build this when it's accessed for the first time

    def __repr__(self):
        dict_value = {}
        for key, value in vars(self).items():
            dict_value[key] = value.to_dict() if hasattr(value, "to_dict") else value

        if dict_value:
            return f"<slack_sdk.scim.v1.{self.__class__.__name__}: {dict_value}>"
        else:
            return self.__str__()
```

### Subclasses

* [GroupCreateResponse](v1/response.html#slack_sdk.scim.v1.response.GroupCreateResponse "slack_sdk.scim.v1.response.GroupCreateResponse")
* [GroupDeleteResponse](v1/response.html#slack_sdk.scim.v1.response.GroupDeleteResponse "slack_sdk.scim.v1.response.GroupDeleteResponse")
* [GroupPatchResponse](v1/response.html#slack_sdk.scim.v1.response.GroupPatchResponse "slack_sdk.scim.v1.response.GroupPatchResponse")
* [GroupUpdateResponse](v1/response.html#slack_sdk.scim.v1.response.GroupUpdateResponse "slack_sdk.scim.v1.response.GroupUpdateResponse")
* [ReadGroupResponse](v1/response.html#slack_sdk.scim.v1.response.ReadGroupResponse "slack_sdk.scim.v1.response.ReadGroupResponse")
* [ReadUserResponse](v1/response.html#slack_sdk.scim.v1.response.ReadUserResponse "slack_sdk.scim.v1.response.ReadUserResponse")
* [SearchGroupsResponse](v1/response.html#slack_sdk.scim.v1.response.SearchGroupsResponse "slack_sdk.scim.v1.response.SearchGroupsResponse")
* [SearchUsersResponse](v1/response.html#slack_sdk.scim.v1.response.SearchUsersResponse "slack_sdk.scim.v1.response.SearchUsersResponse")
* [UserCreateResponse](v1/response.html#slack_sdk.scim.v1.response.UserCreateResponse "slack_sdk.scim.v1.response.UserCreateResponse")
* [UserDeleteResponse](v1/response.html#slack_sdk.scim.v1.response.UserDeleteResponse "slack_sdk.scim.v1.response.UserDeleteResponse")
* [UserPatchResponse](v1/response.html#slack_sdk.scim.v1.response.UserPatchResponse "slack_sdk.scim.v1.response.UserPatchResponse")
* [UserUpdateResponse](v1/response.html#slack_sdk.scim.v1.response.UserUpdateResponse "slack_sdk.scim.v1.response.UserUpdateResponse")

### Class variables (3)

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

### Instance variables (3)

`prop errors : [Errors](v1/response.html#slack_sdk.scim.v1.response.Errors "slack_sdk.scim.v1.response.Errors") | None`

Expand source code

```python
@property
def errors(self) -> Optional[Errors]:
    errors = self.snake_cased_body.get("errors")
    if errors is None:
        return None
    return Errors(**errors)
```

`prop snake_cased_body : Dict[str, Any] | None`

Expand source code

```python
@property
def snake_cased_body(self) -> Optional[Dict[str, Any]]:
    if self._snake_cased_body is None:
        self._snake_cased_body = _to_snake_cased(self.body)
    return self._snake_cased_body
```

`class SearchGroupsResponse (underlying: [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse"))`

Expand source code

```typescript
class SearchGroupsResponse(SCIMResponse):
    groups: List[Group]

    @property
    def groups(self) -> List[Group]:
        return [Group(**r) for r in self.snake_cased_body.get("resources")]

    def __init__(self, underlying: SCIMResponse):
        self.underlying = underlying
        self.url = underlying.url
        self.status_code = underlying.status_code
        self.headers = underlying.headers
        self.raw_body = underlying.raw_body
        self.body = underlying.body
        self._snake_cased_body = None
```

### Ancestors (3)

* [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")

### Instance variables (4)

`prop groups : List[[Group](v1/group.html#slack_sdk.scim.v1.group.Group "slack_sdk.scim.v1.group.Group")]`

Expand source code

```python
@property
def groups(self) -> List[Group]:
    return [Group(**r) for r in self.snake_cased_body.get("resources")]
```

### Inherited members (3)

* `**[SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")**`:
  * `[body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.body "slack_sdk.scim.v1.response.SCIMResponse.body")`
  * `[headers](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.headers "slack_sdk.scim.v1.response.SCIMResponse.headers")`
  * `[raw_body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.raw_body "slack_sdk.scim.v1.response.SCIMResponse.raw_body")`
  * `[status_code](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.status_code "slack_sdk.scim.v1.response.SCIMResponse.status_code")`
  * `[url](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.url "slack_sdk.scim.v1.response.SCIMResponse.url")`

`class SearchUsersResponse (underlying: [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse"))`

Expand source code

```typescript
class SearchUsersResponse(SCIMResponse):
    users: List[User]

    @property
    def users(self) -> List[User]:
        return [User(**r) for r in self.snake_cased_body.get("resources")]

    def __init__(self, underlying: SCIMResponse):
        self.underlying = underlying
        self.url = underlying.url
        self.status_code = underlying.status_code
        self.headers = underlying.headers
        self.raw_body = underlying.raw_body
        self.body = underlying.body
        self._snake_cased_body = None
```

### Ancestors (4)

* [SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")

### Instance variables (5)

`prop users : List[[User](v1/user.html#slack_sdk.scim.v1.user.User "slack_sdk.scim.v1.user.User")]`

Expand source code

```python
@property
def users(self) -> List[User]:
    return [User(**r) for r in self.snake_cased_body.get("resources")]
```

### Inherited members (4)

* `**[SCIMResponse](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse "slack_sdk.scim.v1.response.SCIMResponse")**`:
  * `[body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.body "slack_sdk.scim.v1.response.SCIMResponse.body")`
  * `[headers](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.headers "slack_sdk.scim.v1.response.SCIMResponse.headers")`
  * `[raw_body](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.raw_body "slack_sdk.scim.v1.response.SCIMResponse.raw_body")`
  * `[status_code](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.status_code "slack_sdk.scim.v1.response.SCIMResponse.status_code")`
  * `[url](v1/response.html#slack_sdk.scim.v1.response.SCIMResponse.url "slack_sdk.scim.v1.response.SCIMResponse.url")`

`class User (*,   active: bool | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   addresses: List[[UserAddress](v1/user.html#slack_sdk.scim.v1.user.UserAddress "slack_sdk.scim.v1.user.UserAddress") | Dict[str, Any]] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   display_name: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   emails: List[[TypeAndValue](v1/types.html#slack_sdk.scim.v1.types.TypeAndValue "slack_sdk.scim.v1.types.TypeAndValue") | Dict[str, Any]] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   external_id: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   groups: List[[UserGroup](v1/user.html#slack_sdk.scim.v1.user.UserGroup "slack_sdk.scim.v1.user.UserGroup") | Dict[str, Any]] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   id: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   meta: [UserMeta](v1/user.html#slack_sdk.scim.v1.user.UserMeta "slack_sdk.scim.v1.user.UserMeta") | Dict[str, Any] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   name: [UserName](v1/user.html#slack_sdk.scim.v1.user.UserName "slack_sdk.scim.v1.user.UserName") | Dict[str, Any] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   nick_name: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   phone_numbers: List[[TypeAndValue](v1/types.html#slack_sdk.scim.v1.types.TypeAndValue "slack_sdk.scim.v1.types.TypeAndValue") | Dict[str, Any]] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   photos: List[[UserPhoto](v1/user.html#slack_sdk.scim.v1.user.UserPhoto "slack_sdk.scim.v1.user.UserPhoto") | Dict[str, Any]] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   profile_url: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   roles: List[[TypeAndValue](v1/types.html#slack_sdk.scim.v1.types.TypeAndValue "slack_sdk.scim.v1.types.TypeAndValue") | Dict[str, Any]] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   schemas: List[str] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   timezone: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   title: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   user_name: str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None = <slack_sdk.scim.v1.default_arg.DefaultArg object>,   **kwargs)`

Expand source code

```typescript
class User:
    active: Union[Optional[bool], DefaultArg]
    addresses: Union[Optional[List[UserAddress]], DefaultArg]
    display_name: Union[Optional[str], DefaultArg]
    emails: Union[Optional[List[TypeAndValue]], DefaultArg]
    external_id: Union[Optional[str], DefaultArg]
    groups: Union[Optional[List[UserGroup]], DefaultArg]
    id: Union[Optional[str], DefaultArg]
    meta: Union[Optional[UserMeta], DefaultArg]
    name: Union[Optional[UserName], DefaultArg]
    nick_name: Union[Optional[str], DefaultArg]
    phone_numbers: Union[Optional[List[TypeAndValue]], DefaultArg]
    photos: Union[Optional[List[UserPhoto]], DefaultArg]
    profile_url: Union[Optional[str], DefaultArg]
    roles: Union[Optional[List[TypeAndValue]], DefaultArg]
    schemas: Union[Optional[List[str]], DefaultArg]
    timezone: Union[Optional[str], DefaultArg]
    title: Union[Optional[str], DefaultArg]
    user_name: Union[Optional[str], DefaultArg]
    unknown_fields: Dict[str, Any]

    def __init__(
        self,
        *,
        active: Union[Optional[bool], DefaultArg] = NotGiven,
        addresses: Union[Optional[List[Union[UserAddress, Dict[str, Any]]]], DefaultArg] = NotGiven,
        display_name: Union[Optional[str], DefaultArg] = NotGiven,
        emails: Union[Optional[List[Union[TypeAndValue, Dict[str, Any]]]], DefaultArg] = NotGiven,
        external_id: Union[Optional[str], DefaultArg] = NotGiven,
        groups: Union[Optional[List[Union[UserGroup, Dict[str, Any]]]], DefaultArg] = NotGiven,
        id: Union[Optional[str], DefaultArg] = NotGiven,
        meta: Union[Optional[Union[UserMeta, Dict[str, Any]]], DefaultArg] = NotGiven,
        name: Union[Optional[Union[UserName, Dict[str, Any]]], DefaultArg] = NotGiven,
        nick_name: Union[Optional[str], DefaultArg] = NotGiven,
        phone_numbers: Union[Optional[List[Union[TypeAndValue, Dict[str, Any]]]], DefaultArg] = NotGiven,
        photos: Union[Optional[List[Union[UserPhoto, Dict[str, Any]]]], DefaultArg] = NotGiven,
        profile_url: Union[Optional[str], DefaultArg] = NotGiven,
        roles: Union[Optional[List[Union[TypeAndValue, Dict[str, Any]]]], DefaultArg] = NotGiven,
        schemas: Union[Optional[List[str]], DefaultArg] = NotGiven,
        timezone: Union[Optional[str], DefaultArg] = NotGiven,
        title: Union[Optional[str], DefaultArg] = NotGiven,
        user_name: Union[Optional[str], DefaultArg] = NotGiven,
        **kwargs,
    ) -> None:
        self.active = active
        self.addresses = (
            [a if isinstance(a, UserAddress) else UserAddress(**a) for a in addresses]  # type: ignore
            if _is_iterable(addresses)
            else addresses
        )
        self.display_name = display_name
        self.emails = (
            [a if isinstance(a, TypeAndValue) else TypeAndValue(**a) for a in emails]  # type: ignore
            if _is_iterable(emails)
            else emails
        )
        self.external_id = external_id
        self.groups = (
            [a if isinstance(a, UserGroup) else UserGroup(**a) for a in groups]  # type: ignore
            if _is_iterable(groups)
            else groups
        )
        self.id = id
        self.meta = UserMeta(**meta) if meta is not None and isinstance(meta, dict) else meta
        self.name = UserName(**name) if name is not None and isinstance(name, dict) else name
        self.nick_name = nick_name
        self.phone_numbers = (
            [a if isinstance(a, TypeAndValue) else TypeAndValue(**a) for a in phone_numbers]  # type: ignore
            if _is_iterable(phone_numbers)
            else phone_numbers
        )
        self.photos = (
            [a if isinstance(a, UserPhoto) else UserPhoto(**a) for a in photos]  # type: ignore
            if _is_iterable(photos)
            else photos
        )
        self.profile_url = profile_url
        self.roles = (
            [a if isinstance(a, TypeAndValue) else TypeAndValue(**a) for a in roles]  # type: ignore
            if _is_iterable(roles)
            else roles
        )
        self.schemas = schemas
        self.timezone = timezone
        self.title = title
        self.user_name = user_name

        self.unknown_fields = kwargs

    def to_dict(self):
        return _to_dict_without_not_given(self)

    def __repr__(self):
        return f"<slack_sdk.scim.{self.__class__.__name__}: {self.to_dict()}>"
```

### Class variables (4)

`var active : bool | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var addresses : List[[UserAddress](v1/user.html#slack_sdk.scim.v1.user.UserAddress "slack_sdk.scim.v1.user.UserAddress")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var display_name : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var emails : List[[TypeAndValue](v1/types.html#slack_sdk.scim.v1.types.TypeAndValue "slack_sdk.scim.v1.types.TypeAndValue")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var external_id : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var groups : List[[UserGroup](v1/user.html#slack_sdk.scim.v1.user.UserGroup "slack_sdk.scim.v1.user.UserGroup")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var id : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var meta : [UserMeta](v1/user.html#slack_sdk.scim.v1.user.UserMeta "slack_sdk.scim.v1.user.UserMeta") | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var name : [UserName](v1/user.html#slack_sdk.scim.v1.user.UserName "slack_sdk.scim.v1.user.UserName") | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var nick_name : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var phone_numbers : List[[TypeAndValue](v1/types.html#slack_sdk.scim.v1.types.TypeAndValue "slack_sdk.scim.v1.types.TypeAndValue")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var photos : List[[UserPhoto](v1/user.html#slack_sdk.scim.v1.user.UserPhoto "slack_sdk.scim.v1.user.UserPhoto")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var profile_url : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var roles : List[[TypeAndValue](v1/types.html#slack_sdk.scim.v1.types.TypeAndValue "slack_sdk.scim.v1.types.TypeAndValue")] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var schemas : List[str] | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var timezone : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var title : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

`var unknown_fields : Dict[str, Any]`

The type of the None singleton.

`var user_name : str | [DefaultArg](v1/default_arg.html#slack_sdk.scim.v1.default_arg.DefaultArg "slack_sdk.scim.v1.default_arg.DefaultArg") | None`

The type of the None singleton.

### Methods (3)

`def to_dict(self)`

Expand source code

```python
def to_dict(self):
    return _to_dict_without_not_given(self)
```
