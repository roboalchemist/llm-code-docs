# Source: https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html

Title: Built-in middleware — Litestar Framework

URL Source: https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html

Markdown Content:
CORS[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#cors "Link to this heading")
--------------------------------------------------------------------------------------------------------------

[CORS (Cross-Origin Resource Sharing)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a common security mechanism that is often implemented using middleware. To enable CORS in a litestar application simply pass an instance of [`CORSConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.cors.CORSConfig "litestar.config.cors.CORSConfig") to [`Litestar`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar "litestar.app.Litestar"):

from litestar import Litestar
from litestar.config.cors import CORSConfig

cors_config = CORSConfig(allow_origins=["https://www.example.com"])

app = Litestar(route_handlers=[...], cors_config=cors_config)

CSRF[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#csrf "Link to this heading")
--------------------------------------------------------------------------------------------------------------

[CSRF (Cross-site request forgery)](https://owasp.org/www-community/attacks/csrf) is a type of attack where unauthorized commands are submitted from a user that the web application trusts. This attack often uses social engineering that tricks the victim into clicking a URL that contains a maliciously crafted, unauthorized request for a particular Web application. The user’s browser then sends this maliciously crafted request to the targeted Web application. If the user is in an active session with the Web application, the application treats this new request as an authorized request submitted by the user. Thus, the attacker can force the user to perform an action the user didn’t intend, for example:

POST /send-money HTTP/1.1
Host: target.web.app
Content-Type: application/x-www-form-urlencoded

amount=1000usd&to=attacker@evil.com

This middleware prevents CSRF attacks by doing the following:

1.   On the first “safe” request (e.g GET) - set a cookie with a special token created by the server

2.   On each subsequent “unsafe” request (e.g POST) - make sure the request contains either a
form field or an additional header that has this token (more on this below)

To enable CSRF protection in a Litestar application simply pass an instance of [`CSRFConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.csrf.CSRFConfig "litestar.config.csrf.CSRFConfig") to the Litestar constructor:

from litestar import Litestar, get, post
from litestar.config.csrf import CSRFConfig

@get()
async def get_resource() -> str:
    # GET is one of the safe methods
    return "some_resource"

@post("{id:int}")
async def create_resource(id: int) -> bool:
    # POST is one of the unsafe methods
    return True

csrf_config = CSRFConfig(secret="my-secret")

app = Litestar([get_resource, create_resource], csrf_config=csrf_config)

The following snippet demonstrates how to change the cookie name to `"some-cookie-name"` and header name to `"some-header-name"`.

csrf_config = CSRFConfig(secret="my-secret", cookie_name='some-cookie-name', header_name='some-header-name')

A CSRF protected route can be accessed by any client that can make a request with either the header or form-data key.

Note

The form-data key can not be currently configured. It should only be passed via the key `"_csrf_token"`

In Python, any client such as [requests](https://github.com/psf/requests) or [httpx](https://github.com/encode/httpx) can be used. The usage of clients or sessions is recommended due to the cookie persistence it offers across requests. The following is an example using [httpx.Client](https://www.python-httpx.org/api/#client).

import httpx

with httpx.Client() as client:
    get_response = client.get("http://localhost:8000/")

    # "csrftoken" is the default cookie name
    csrf = get_response.cookies["csrftoken"]

    # "x-csrftoken" is the default header name
    post_response_using_header = client.post("http://localhost:8000/1", headers={"x-csrftoken": csrf})
    assert post_response_using_header.status_code == 201

    # "_csrf_token" is the default *non* configurable form-data key
    post_response_using_form_data = client.post("http://localhost:8000/1", data={"_csrf_token": csrf})
    assert post_response_using_form_data.status_code == 201

    # despite the header being passed, this request will fail as it does not have a cookie in its session
    # note the usage of ``httpx.post`` instead of ``client.post``
    post_response_with_no_persisted_cookie = httpx.post("http://localhost:8000/1", headers={"x-csrftoken": csrf})
    assert post_response_with_no_persisted_cookie.status_code == 403
    assert "CSRF token verification failed" in post_response_with_no_persisted_cookie.text

Routes can be marked as being exempt from the protection offered by this middleware via [handler opts](https://docs.litestar.dev/latest/usage/routing/handlers.html#handler-opts)

@post("/post", exclude_from_csrf=True)
def handler() -> None: ...

If you need to exempt many routes at once you might want to consider using the [`exclude`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.csrf.CSRFConfig.exclude "litestar.config.csrf.CSRFConfig.exclude") kwarg which accepts list of path patterns to skip in the middleware.

Allowed Hosts[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#allowed-hosts "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

Another common security mechanism is to require that each incoming request has a `"Host"` or `"X-Forwarded-Host"` header, and then to restrict hosts to a specific set of domains - what’s called “allowed hosts”.

Litestar includes an [`AllowedHostsMiddleware`](https://docs.litestar.dev/latest/reference/middleware/allowed_hosts.html#litestar.middleware.allowed_hosts.AllowedHostsMiddleware "litestar.middleware.allowed_hosts.AllowedHostsMiddleware") class that can be easily enabled by either passing an instance of [`AllowedHostsConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.allowed_hosts.AllowedHostsConfig "litestar.config.allowed_hosts.AllowedHostsConfig") or a list of domains to [`Litestar`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar "litestar.app.Litestar"):

from litestar import Litestar
from litestar.config.allowed_hosts import AllowedHostsConfig

app = Litestar(
    route_handlers=[...],
    allowed_hosts=AllowedHostsConfig(
        allowed_hosts=["*.example.com", "www.wikipedia.org"]
    ),
)

Note

You can use wildcard prefixes (`*.`) in the beginning of a domain to match any combination of subdomains. Thus, `*.example.com` will match `www.example.com` but also `x.y.z.example.com` etc. You can also simply put `*` in trusted hosts, which means allow all. This is akin to turning the middleware off, so in this case it may be better to not enable it in the first place. You should note that a wildcard can only be used in the prefix of a domain name, not in the middle or end. Doing so will result in a validation exception being raised.

Compression[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#compression "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

HTML responses can optionally be compressed. Litestar has built in support for gzip and brotli. Gzip support is provided through the built-in Starlette classes, and brotli support can be added by installing the `brotli` extras.

You can enable either backend by passing an instance of [`CompressionConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.compression.CompressionConfig "litestar.config.compression.CompressionConfig") to `compression_config` of [`Litestar`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar "litestar.app.Litestar").

### GZIP[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#gzip "Link to this heading")

You can enable gzip compression of responses by passing an instance of [`CompressionConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.compression.CompressionConfig "litestar.config.compression.CompressionConfig") with the `backend` parameter set to `"gzip"`.

You can configure the following additional gzip-specific values:

*   `minimum_size`: the minimum threshold for response size to enable compression. Smaller responses will not be
compressed. Defaults is `500`, i.e. half a kilobyte.

*   `gzip_compress_level`: a range between 0-9, see the [official python docs](https://docs.python.org/3/library/gzip.html).
Defaults to `9` , which is the maximum value.

from litestar import Litestar
from litestar.config.compression import CompressionConfig

app = Litestar(
    route_handlers=[...],
    compression_config=CompressionConfig(backend="gzip", gzip_compress_level=9),
)

### Brotli[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#brotli "Link to this heading")

The [Brotli](https://pypi.org/project/Brotli) package is required to run this middleware. It is available as an extras to litestar with the `brotli` extra (`pip install 'litestar[brotli]'`).

You can enable brotli compression of responses by passing an instance of [`CompressionConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.compression.CompressionConfig "litestar.config.compression.CompressionConfig") with the `backend` parameter set to `"brotli"`.

You can configure the following additional brotli-specific values:

*   `minimum_size`: the minimum threshold for response size to enable compression. Smaller responses will not be
compressed. Default is 500, i.e. half a kilobyte

*   `brotli_quality`: Range [0-11], Controls the compression-speed vs compression-density tradeoff. The higher the
quality, the slower the compression. Defaults to 5

*   `brotli_mode`: The compression mode can be `"generic"` (for mixed content), `"text"` (for UTF-8 format text input), or
`"font"` (for WOFF 2.0). Defaults to `"text"`

*   `brotli_lgwin`: Base 2 logarithm of size. Range [10-24]. Defaults to 22.

*   `brotli_lgblock`: Base 2 logarithm of the maximum input block size. Range [16-24]. If set to 0, the value will
be set based on the quality. Defaults to 0

*   `brotli_gzip_fallback`: a boolean to indicate if gzip should be used if brotli is not supported

from litestar import Litestar
from litestar.config.compression import CompressionConfig

app = Litestar(
    route_handlers=[...],
    compression_config=CompressionConfig(backend="brotli", brotli_gzip_fallback=True),
)

Rate-Limit Middleware[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#rate-limit-middleware "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

Litestar includes an optional [`RateLimitMiddleware`](https://docs.litestar.dev/latest/reference/middleware/rate_limit.html#litestar.middleware.rate_limit.RateLimitMiddleware "litestar.middleware.rate_limit.RateLimitMiddleware") that follows the [IETF RateLimit draft specification](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/).

To use the rate limit middleware, use the [`RateLimitConfig`](https://docs.litestar.dev/latest/reference/middleware/rate_limit.html#litestar.middleware.rate_limit.RateLimitConfig "litestar.middleware.rate_limit.RateLimitConfig"):

from litestar import Litestar, MediaType, get
from litestar.middleware.rate_limit import RateLimitConfig

rate_limit_config = RateLimitConfig(rate_limit=("minute", 1), exclude=["/schema"])

@get("/", media_type=MediaType.TEXT, sync_to_thread=False)
def handler() -> str:
 """Handler which should not be accessed more than once per minute."""
    return "ok"

app = Litestar(route_handlers=[handler], middleware=[rate_limit_config.middleware])

The only required configuration kwarg is `rate_limit`, which expects a tuple containing a time-unit (`"second"`, `"minute"`, `"hour"`, `"day"`) and a value for the request quota (integer).

### Using behind a proxy[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#using-behind-a-proxy "Link to this heading")

The default mode for uniquely identifiying client uses the client’s address. When an application is running behind a proxy, that address will be the proxy’s, not the “real” address of the end-user.

While there are special headers set by proxies to retrieve the remote client’s actual address (`X-FORWARDED-FOR`), their values should not implicitly be trusted, as any client is free to set them to whatever value they want. A rate-limit could easily be circumvented by spoofing these, and simply attaching a new, random address to each request.

The best way to handle applications running behind a proxy is to use a middleware that updates the client’s address in a secure way, such as uvicorn’s [ProxyHeaderMiddleware](https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py) or hypercon’s [ProxyFixMiddleware](https://hypercorn.readthedocs.io/en/latest/how_to_guides/proxy_fix.html) .

Logging Middleware[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#logging-middleware "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Litestar ships with a robust logging middleware that allows logging HTTP request and responses while building on the Litestar’s [logging configuration](https://docs.litestar.dev/latest/usage/logging.html#logging-usage):

Python 3.8+

from typing import Dict

from litestar import Litestar, get
from litestar.logging.config import LoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig

logging_middleware_config = LoggingMiddlewareConfig()

@get("/", sync_to_thread=False)
def my_handler() -> Dict[str, str]:
    return {"hello": "world"}

app = Litestar(
    route_handlers=[my_handler],
    logging_config=LoggingConfig(),
    middleware=[logging_middleware_config.middleware],
)

Python 3.9+

from litestar import Litestar, get
from litestar.logging.config import LoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig

logging_middleware_config = LoggingMiddlewareConfig()

@get("/", sync_to_thread=False)
def my_handler() -> dict[str, str]:
    return {"hello": "world"}

app = Litestar(
    route_handlers=[my_handler],
    logging_config=LoggingConfig(),
    middleware=[logging_middleware_config.middleware],
)

The logging middleware uses the logger configuration defined on the application level, which allows for using any supported logging tool, depending on the configuration used (see [logging configuration](https://docs.litestar.dev/latest/usage/logging.html#logging-usage) for more details).

### Obfuscating Logging Output[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#obfuscating-logging-output "Link to this heading")

Sometimes certain data, e.g. request or response headers, needs to be obfuscated. This is supported by the middleware configuration:

from litestar.middleware.logging import LoggingMiddlewareConfig

logging_middleware_config = LoggingMiddlewareConfig(
    request_cookies_to_obfuscate={"my-custom-session-key"},
    response_cookies_to_obfuscate={"my-custom-session-key"},
    request_headers_to_obfuscate={"my-custom-header"},
    response_headers_to_obfuscate={"my-custom-header"},
)

The middleware will obfuscate the headers `Authorization` and `X-API-KEY` , and the cookie `session` by default.

### Compression and Logging of Response Body[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#compression-and-logging-of-response-body "Link to this heading")

If both [`CompressionConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.compression.CompressionConfig "litestar.config.compression.CompressionConfig") and [`LoggingMiddleware`](https://docs.litestar.dev/latest/reference/middleware/logging.html#litestar.middleware.logging.LoggingMiddleware "litestar.middleware.logging.LoggingMiddleware") have been defined for the application, the response body will be omitted from response logging if it has been compressed, even if `"body"` has been included in [`response_log_fields`](https://docs.litestar.dev/latest/reference/middleware/logging.html#litestar.middleware.logging.LoggingMiddlewareConfig.response_log_fields "litestar.middleware.logging.LoggingMiddlewareConfig.response_log_fields"). To force the body of compressed responses to be logged, set [`include_compressed_body`](https://docs.litestar.dev/latest/reference/middleware/logging.html#litestar.middleware.logging.LoggingMiddlewareConfig.include_compressed_body "litestar.middleware.logging.LoggingMiddlewareConfig.include_compressed_body") to `True` , in addition to including `"body"` in `response_log_fields`.

Session Middleware[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#session-middleware "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Litestar includes a [`SessionMiddleware`](https://docs.litestar.dev/latest/reference/middleware/session/base.html#litestar.middleware.session.base.SessionMiddleware "litestar.middleware.session.base.SessionMiddleware"), offering client- and server-side sessions. Server-side sessions are backed by Litestar’s [stores](https://docs.litestar.dev/latest/usage/stores.html), which offer support for:

*   In memory sessions

*   File based sessions

*   Redis based sessions

*   Valkey based sessions

*   Database based [Session Middleware](https://advanced-alchemy.litestar.dev/latest/usage/frameworks/litestar.html#session-middleware "(in advanced_alchemy)")

### Setting up the middleware[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#setting-up-the-middleware "Link to this heading")

To start using sessions in your application all you have to do is create an instance of a [`configuration`](https://docs.litestar.dev/latest/reference/middleware/session/base.html#litestar.middleware.session.base.BaseBackendConfig "litestar.middleware.session.base.BaseBackendConfig") object and add its middleware to your application’s middleware stack:

Python 3.8+

Hello World[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#id2 "Link to this code")

from os import urandom
from typing import Dict

from litestar import Litestar, Request, delete, get, post
from litestar.middleware.session.client_side import CookieBackendConfig

# we initialize to config with a 16 byte key, i.e. 128 a bit key.
# in real world usage we should inject the secret from the environment
session_config = CookieBackendConfig(secret=urandom(16))  # type: ignore[arg-type]

@get("/session", sync_to_thread=False)
def check_session_handler(request: Request) -> Dict[str, bool]:
 """Handler function that accesses request.session."""
    return {"has_session": request.session != {}}

@post("/session", sync_to_thread=False)
def create_session_handler(request: Request) -> None:
 """Handler to set the session."""
    if not request.session:
        # value can be a dictionary or pydantic model
        request.set_session({"username": "moishezuchmir"})

@delete("/session", sync_to_thread=False)
def delete_session_handler(request: Request) -> None:
 """Handler to clear the session."""
    if request.session:
        request.clear_session()

app = Litestar(
    route_handlers=[check_session_handler, create_session_handler, delete_session_handler],
    middleware=[session_config.middleware],
)

Python 3.9+

Hello World[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#id3 "Link to this code")

from os import urandom

from litestar import Litestar, Request, delete, get, post
from litestar.middleware.session.client_side import CookieBackendConfig

# we initialize to config with a 16 byte key, i.e. 128 a bit key.
# in real world usage we should inject the secret from the environment
session_config = CookieBackendConfig(secret=urandom(16))  # type: ignore[arg-type]

@get("/session", sync_to_thread=False)
def check_session_handler(request: Request) -> dict[str, bool]:
 """Handler function that accesses request.session."""
    return {"has_session": request.session != {}}

@post("/session", sync_to_thread=False)
def create_session_handler(request: Request) -> None:
 """Handler to set the session."""
    if not request.session:
        # value can be a dictionary or pydantic model
        request.set_session({"username": "moishezuchmir"})

@delete("/session", sync_to_thread=False)
def delete_session_handler(request: Request) -> None:
 """Handler to clear the session."""
    if request.session:
        request.clear_session()

app = Litestar(
    route_handlers=[check_session_handler, create_session_handler, delete_session_handler],
    middleware=[session_config.middleware],
)

Note

Since both client- and server-side sessions rely on cookies (one for storing the actual session data, the other for storing the session ID), they share most of the cookie configuration. A complete reference of the cookie configuration can be found at [`BaseBackendConfig`](https://docs.litestar.dev/latest/reference/middleware/session/base.html#litestar.middleware.session.base.BaseBackendConfig "litestar.middleware.session.base.BaseBackendConfig").

### Client-side sessions[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#client-side-sessions "Link to this heading")

Client side sessions are available through the [`ClientSideSessionBackend`](https://docs.litestar.dev/latest/reference/middleware/session/client_side.html#litestar.middleware.session.client_side.ClientSideSessionBackend "litestar.middleware.session.client_side.ClientSideSessionBackend"), which offers strong AES-CGM encryption security best practices while support cookie splitting.

Important

`ClientSideSessionBackend` requires the [cryptography](https://cryptography.io/en/latest/) library, which can be installed together with litestar as an extra using `pip install 'litestar[cryptography]'`

`cookie_backend.py`[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#id4 "Link to this code")

from os import urandom

from litestar import Litestar
from litestar.middleware.session.client_side import CookieBackendConfig

session_config = CookieBackendConfig(secret=urandom(16))  # type: ignore

app = Litestar(middleware=[session_config.middleware])

### Server-side sessions[#](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#server-side-sessions "Link to this heading")

Server side session store data - as the name suggests - on the server instead of the client. They use a cookie containing a session ID which is a randomly generated string to identify a client and load the appropriate data from the store

from pathlib import Path

from litestar import Litestar
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar.stores.file import FileStore

app = Litestar(
    middleware=[ServerSideSessionConfig().middleware],
    stores={"sessions": FileStore(path=Path("session_data"))},
)
