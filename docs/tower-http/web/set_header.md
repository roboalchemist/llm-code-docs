# Source: https://docs.rs/tower-http/latest/tower_http/set_header/

[tower_http](../index.html)
# Module set_header Copy item path

[Source](../../src/tower_http/set_header/mod.rs.html#1-110)
Available on
**crate feature set-header**
only.
Expand description
Middleware for setting headers on requests and responses.

See request and response for more details.

## Modules§

[request](request/index.html)
Set a header on the request.
[response](response/index.html)
Set a header on the response.
## Structs§

[SetRequestHeader](struct.SetRequestHeader.html)
Middleware that sets a header on the request.
[SetRequestHeaderLayer](struct.SetRequestHeaderLayer.html)
Layer that applies
[SetRequestHeader](struct.SetRequestHeader.html)
which adds a request header.
[SetResponseHeader](struct.SetResponseHeader.html)
Middleware that sets a header on the response.
[SetResponseHeaderLayer](struct.SetResponseHeaderLayer.html)
Layer that applies
[SetResponseHeader](struct.SetResponseHeader.html)
which adds a response header.
## Traits§

[MakeHeaderValue](trait.MakeHeaderValue.html)
Trait for producing header values.