# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/sensitive_headers/
# Path: sensitive_headers/

[tower_http](../index.html)

# Module sensitive_headers Copy item path

[Source](../../src/tower_http/sensitive_headers.rs.html#1-448)

Available on **crate feature`sensitive-headers`** only.

Expand description

Middlewares that mark headers as
[sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive).

## §Example

    
    
    use tower_http::sensitive_headers::SetSensitiveHeadersLayer;
    use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
    use http::{Request, Response, header::AUTHORIZATION};
    use http_body_util::Full;
    use bytes::Bytes;
    use std::{iter::once, convert::Infallible};
    
    async fn handle(req: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
        // ...
    }
    
    let mut service = ServiceBuilder::new()
        // Mark the `Authorization` header as sensitive so it doesn't show in logs
        //
        // `SetSensitiveHeadersLayer` will mark the header as sensitive on both the
        // request and response.
        //
        // The middleware is constructed from an iterator of headers to easily mark
        // multiple headers at once.
        .layer(SetSensitiveHeadersLayer::new(once(AUTHORIZATION)))
        .service(service_fn(handle));
    
    // Call the service.
    let response = service
        .ready()
        .await?
        .call(Request::new(Full::default()))
        .await?;

Its important to think about the order in which requests and responses arrive
at your middleware. For example to hide headers both on requests and responses
when using [`TraceLayer`](../trace/struct.TraceLayer.html "struct
tower_http::trace::TraceLayer") you have to apply
[`SetSensitiveRequestHeadersLayer`](struct.SetSensitiveRequestHeadersLayer.html
"struct tower_http::sensitive_headers::SetSensitiveRequestHeadersLayer")
before [`TraceLayer`](../trace/struct.TraceLayer.html "struct
tower_http::trace::TraceLayer") and
[`SetSensitiveResponseHeadersLayer`](struct.SetSensitiveResponseHeadersLayer.html
"struct tower_http::sensitive_headers::SetSensitiveResponseHeadersLayer")
afterwards.

    
    
    use tower_http::{
        trace::TraceLayer,
        sensitive_headers::{
            SetSensitiveRequestHeadersLayer,
            SetSensitiveResponseHeadersLayer,
        },
    };
    use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
    use http::header;
    use std::sync::Arc;
    
    let headers: Arc<[_]> = Arc::new([
        header::AUTHORIZATION,
        header::PROXY_AUTHORIZATION,
        header::COOKIE,
        header::SET_COOKIE,
    ]);
    
    let service = ServiceBuilder::new()
        .layer(SetSensitiveRequestHeadersLayer::from_shared(Arc::clone(&headers)))
        .layer(TraceLayer::new_for_http())
        .layer(SetSensitiveResponseHeadersLayer::from_shared(headers))
        .service_fn(handle);

## Structs§

[SetSensitiveHeadersLayer](struct.SetSensitiveHeadersLayer.html "struct
tower_http::sensitive_headers::SetSensitiveHeadersLayer")

    Mark headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive) on both requests and responses.
[SetSensitiveRequestHeaders](struct.SetSensitiveRequestHeaders.html "struct
tower_http::sensitive_headers::SetSensitiveRequestHeaders")

    Mark request headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive).
[SetSensitiveRequestHeadersLayer](struct.SetSensitiveRequestHeadersLayer.html
"struct tower_http::sensitive_headers::SetSensitiveRequestHeadersLayer")

    Mark request headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive).
[SetSensitiveResponseHeaders](struct.SetSensitiveResponseHeaders.html "struct
tower_http::sensitive_headers::SetSensitiveResponseHeaders")

    Mark response headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive).
[SetSensitiveResponseHeadersLayer](struct.SetSensitiveResponseHeadersLayer.html
"struct tower_http::sensitive_headers::SetSensitiveResponseHeadersLayer")

    Mark response headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive).
[SetSensitiveResponseHeadersResponseFuture](struct.SetSensitiveResponseHeadersResponseFuture.html
"struct
tower_http::sensitive_headers::SetSensitiveResponseHeadersResponseFuture")

    Response future for [`SetSensitiveResponseHeaders`](struct.SetSensitiveResponseHeaders.html "struct tower_http::sensitive_headers::SetSensitiveResponseHeaders").

## Type Aliases§

[SetSensitiveHeaders](type.SetSensitiveHeaders.html "type
tower_http::sensitive_headers::SetSensitiveHeaders")

    Mark headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive) on both requests and responses.

