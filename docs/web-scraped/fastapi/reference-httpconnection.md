# Source: https://fastapi.tiangolo.com/reference/httpconnection/

# `HTTPConnection` class[&para;](#httpconnection-class)

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

You can import it from `fastapi.requests`:

`from fastapi.requests import HTTPConnection
`

## 
``            fastapi.requests.HTTPConnection

[&para;](#fastapi.requests.HTTPConnection)

`HTTPConnection(scope, receive=None)
`

              Bases: `Mapping[str, Any]`

A base class for incoming HTTP connections, that is used to provide
any functionality that is common to both `Request` and `WebSocket`.

                    Source code in `starlette/requests.py`

77
78
79

`def __init__(self, scope: Scope, receive: Receive | None = None) -> None:
    assert scope["type"] in ("http", "websocket")
    self.scope = scope
`

### 
``            scope

      `instance-attribute`

[&para;](#fastapi.requests.HTTPConnection.scope)

`scope = scope
`

### 
``            app

      `property`

[&para;](#fastapi.requests.HTTPConnection.app)

`app
`

### 
``            url

      `property`

[&para;](#fastapi.requests.HTTPConnection.url)

`url
`

### 
``            base_url

      `property`

[&para;](#fastapi.requests.HTTPConnection.base_url)

`base_url
`

### 
``            headers

      `property`

[&para;](#fastapi.requests.HTTPConnection.headers)

`headers
`

### 
``            query_params

      `property`

[&para;](#fastapi.requests.HTTPConnection.query_params)

`query_params
`

### 
``            path_params

      `property`

[&para;](#fastapi.requests.HTTPConnection.path_params)

`path_params
`

### 
``            cookies

      `property`

[&para;](#fastapi.requests.HTTPConnection.cookies)

`cookies
`

### 
``            client

      `property`

[&para;](#fastapi.requests.HTTPConnection.client)

`client
`

### 
``            session

      `property`

[&para;](#fastapi.requests.HTTPConnection.session)

`session
`

### 
``            auth

      `property`

[&para;](#fastapi.requests.HTTPConnection.auth)

`auth
`

### 
``            user

      `property`

[&para;](#fastapi.requests.HTTPConnection.user)

`user
`

### 
``            state

      `property`

[&para;](#fastapi.requests.HTTPConnection.state)

`state
`

### 
``            url_for

[&para;](#fastapi.requests.HTTPConnection.url_for)

`url_for(name, /, **path_params)
`

              Source code in `starlette/requests.py`

184
185
186
187
188
189

`def url_for(self, name: str, /, **path_params: Any) -> URL:
    url_path_provider: Router | Starlette | None = self.scope.get("router") or self.scope.get("app")
    if url_path_provider is None:
        raise RuntimeError("The `url_for` method can only be used inside a Starlette application or with a router.")
    url_path = url_path_provider.url_path_for(name, **path_params)
    return url_path.make_absolute_url(base_url=self.base_url)
`