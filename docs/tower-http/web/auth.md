# Source: https://docs.rs/tower-http/latest/tower_http/auth/

[tower_http](../index.html)
# Module auth Copy item path

[Source](../../src/tower_http/auth/mod.rs.html#1-13)
Available on
**crate feature auth**
only.
Expand description
Authorization related middleware.

## Modules§

[add_authorization](add_authorization/index.html)
Add authorization to requests using the
[Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
header.
[async_require_authorization](async_require_authorization/index.html)
Authorize requests using the
[Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
header asynchronously.
[require_authorization](require_authorization/index.html)
Deprecated
Authorize requests using
[ValidateRequest](../validate_request/trait.ValidateRequest.html)
.
## Structs§

[AddAuthorization](struct.AddAuthorization.html)
Middleware that adds authorization all requests using the
[Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
header.
[AddAuthorizationLayer](struct.AddAuthorizationLayer.html)
Layer that applies
[AddAuthorization](struct.AddAuthorization.html)
which adds authorization to all requests using the
[Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
header.
[AsyncRequireAuthorization](struct.AsyncRequireAuthorization.html)
Middleware that authorizes all requests using the
[Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
header.
[AsyncRequireAuthorizationLayer](struct.AsyncRequireAuthorizationLayer.html)
Layer that applies
[AsyncRequireAuthorization](struct.AsyncRequireAuthorization.html)
which authorizes all requests using the
[Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
header.
## Traits§

[AsyncAuthorizeRequest](trait.AsyncAuthorizeRequest.html)
Trait for authorizing requests.