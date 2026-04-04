# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/propagate_header/
# Path: propagate_header/

[tower_http](../index.html)

# Module propagate_header Copy item path

[Source](../../src/tower_http/propagate_header.rs.html#1-154)

Available on **crate feature`propagate-header`** only.

Expand description

Propagate a header from the request to the response.

## §Example

    
    
    use http::{Request, Response, header::HeaderName};
    use std::convert::Infallible;
    use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
    use tower_http::propagate_header::PropagateHeaderLayer;
    use bytes::Bytes;
    use http_body_util::Full;
    
    async fn handle(req: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
        // ...
    }
    
    let mut svc = ServiceBuilder::new()
        // This will copy `x-request-id` headers from requests onto responses.
        .layer(PropagateHeaderLayer::new(HeaderName::from_static("x-request-id")))
        .service_fn(handle);
    
    // Call the service.
    let request = Request::builder()
        .header("x-request-id", "1337")
        .body(Full::default())?;
    
    let response = svc.ready().await?.call(request).await?;
    
    assert_eq!(response.headers()["x-request-id"], "1337");

## Structs§

[PropagateHeader](struct.PropagateHeader.html "struct
tower_http::propagate_header::PropagateHeader")

    Middleware that propagates headers from requests to responses.
[PropagateHeaderLayer](struct.PropagateHeaderLayer.html "struct
tower_http::propagate_header::PropagateHeaderLayer")

    Layer that applies [`PropagateHeader`](struct.PropagateHeader.html "struct tower_http::propagate_header::PropagateHeader") which propagates headers from requests to responses.
[ResponseFuture](struct.ResponseFuture.html "struct
tower_http::propagate_header::ResponseFuture")

    Response future for [`PropagateHeader`](struct.PropagateHeader.html "struct tower_http::propagate_header::PropagateHeader").

