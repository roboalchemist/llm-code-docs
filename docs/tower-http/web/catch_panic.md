# Source: https://docs.rs/tower-http/latest/tower_http/catch_panic/

[tower_http](../index.html)
# Module catch_panic Copy item path

[Source](../../src/tower_http/catch_panic.rs.html#1-409)
Available on
**crate feature catch-panic**
only.
Expand description
Convert panics into responses.

Note that using panics for error handling is not recommended. Prefer instead to use Result
whenever possible.

## §Example

```
use http::{Request, Response, header::HeaderName};
use std::convert::Infallible;
use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
use tower_http::catch_panic::CatchPanicLayer;
use http_body_util::Full;
use bytes::Bytes;

async fn handle(req: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
    panic!("something went wrong...")
}

let mut svc = ServiceBuilder::new()
    // Catch panics and convert them into responses.
    .layer(CatchPanicLayer::new())
    .service_fn(handle);

// Call the service.
let request = Request::new(Full::default());

let response = svc.ready().await?.call(request).await?;

assert_eq!(response.status(), 500);
```

Using a custom panic handler:

```
use http::{Request, StatusCode, Response, header::{self, HeaderName}};
use std::{any::Any, convert::Infallible};
use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
use tower_http::catch_panic::CatchPanicLayer;
use bytes::Bytes;
use http_body_util::Full;

async fn handle(req: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
    panic!("something went wrong...")
}

fn handle_panic(err: Box<dyn Any + Send + 'static>) -> Response<Full<Bytes>> {
    let details = if let Some(s) = err.downcast_ref::<String>() {
        s.clone()
    } else if let Some(s) = err.downcast_ref::<&str>() {
        s.to_string()
    } else {
        "Unknown panic message".to_string()
    };

    let body = serde_json::json!({
        "error": {
            "kind": "panic",
            "details": details,
        }
    });
    let body = serde_json::to_string(&body).unwrap();

    Response::builder()
        .status(StatusCode::INTERNAL_SERVER_ERROR)
        .header(header::CONTENT_TYPE, "application/json")
        .body(Full::from(body))
        .unwrap()
}

let svc = ServiceBuilder::new()
    // Use `handle_panic` to create the response.
    .layer(CatchPanicLayer::custom(handle_panic))
    .service_fn(handle);
```

## Structs§

[CatchPanic](struct.CatchPanic.html)
Middleware that catches panics and converts them into
`500 Internal Server`
responses.
[CatchPanicLayer](struct.CatchPanicLayer.html)
Layer that applies the
[CatchPanic](struct.CatchPanic.html)
middleware that catches panics and converts them into
`500 Internal Server`
responses.
[DefaultResponseForPanic](struct.DefaultResponseForPanic.html)
The default
`ResponseForPanic`
used by
`CatchPanic`
.
[ResponseFuture](struct.ResponseFuture.html)
Response future for
[CatchPanic](struct.CatchPanic.html)
.
## Traits§

[ResponseForPanic](trait.ResponseForPanic.html)
Trait for creating responses from panics.