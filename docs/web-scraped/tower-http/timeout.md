# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/timeout/
# Path: timeout/

[tower_http](../index.html)

# Module timeout Copy item path

[Source](../../src/tower_http/timeout/mod.rs.html#1-50)

Available on **crate feature`timeout`** only.

Expand description

Middleware that applies a timeout to requests.

If the request does not complete within the specified timeout, it will be
aborted and a response with an empty body and a custom status code will be
returned.

## §Differences from `tower::timeout`

tower’s [`Timeout`](tower::timeout::Timeout) middleware uses an error to
signal timeout, i.e. it changes the error type to
[`BoxError`](https://docs.rs/tower/0.5.2/x86_64-unknown-linux-
gnu/tower/type.BoxError.html "type tower::BoxError"). For HTTP services that
is rarely what you want as returning errors will terminate the connection
without sending a response.

This middleware won’t change the error type and instead returns a response
with an empty body and the specified status code. That means if your service’s
error type is [`Infallible`](https://doc.rust-
lang.org/nightly/core/convert/enum.Infallible.html "enum
core::convert::Infallible"), it will still be [`Infallible`](https://doc.rust-
lang.org/nightly/core/convert/enum.Infallible.html "enum
core::convert::Infallible") after applying this middleware.

## §Example

    
    
    use http::{Request, Response, StatusCode};
    use http_body_util::Full;
    use bytes::Bytes;
    use std::{convert::Infallible, time::Duration};
    use tower::ServiceBuilder;
    use tower_http::timeout::TimeoutLayer;
    
    async fn handle(_: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
        // ...
    }
    
    let svc = ServiceBuilder::new()
        // Timeout requests after 30 seconds with the specified status code
        .layer(TimeoutLayer::with_status_code(StatusCode::REQUEST_TIMEOUT, Duration::from_secs(30)))
        .service_fn(handle);

## Structs§

[RequestBodyTimeout](struct.RequestBodyTimeout.html "struct
tower_http::timeout::RequestBodyTimeout")

    Applies a [`TimeoutBody`](struct.TimeoutBody.html "struct tower_http::timeout::TimeoutBody") to the request body.
[RequestBodyTimeoutLayer](struct.RequestBodyTimeoutLayer.html "struct
tower_http::timeout::RequestBodyTimeoutLayer")

    Applies a [`TimeoutBody`](struct.TimeoutBody.html "struct tower_http::timeout::TimeoutBody") to the request body.
[ResponseBodyTimeout](struct.ResponseBodyTimeout.html "struct
tower_http::timeout::ResponseBodyTimeout")

    Applies a [`TimeoutBody`](struct.TimeoutBody.html "struct tower_http::timeout::TimeoutBody") to the response body.
[ResponseBodyTimeoutLayer](struct.ResponseBodyTimeoutLayer.html "struct
tower_http::timeout::ResponseBodyTimeoutLayer")

    Applies a [`TimeoutBody`](struct.TimeoutBody.html "struct tower_http::timeout::TimeoutBody") to the response body.
[Timeout](struct.Timeout.html "struct tower_http::timeout::Timeout")

    Middleware which apply a timeout to requests.
[TimeoutBody](struct.TimeoutBody.html "struct
tower_http::timeout::TimeoutBody")

    Middleware that applies a timeout to request and response bodies.
[TimeoutError](struct.TimeoutError.html "struct
tower_http::timeout::TimeoutError")

    Error for [`TimeoutBody`](struct.TimeoutBody.html "struct tower_http::timeout::TimeoutBody").
[TimeoutLayer](struct.TimeoutLayer.html "struct
tower_http::timeout::TimeoutLayer")

    Layer that applies the [`Timeout`](struct.Timeout.html "struct tower_http::timeout::Timeout") middleware which apply a timeout to requests.

