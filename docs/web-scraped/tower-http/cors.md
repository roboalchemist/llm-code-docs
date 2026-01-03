# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/cors/
# Path: cors/

[tower_http](../index.html)

# Module cors Copy item path

[Source](../../src/tower_http/cors/mod.rs.html#1-820)

Available on **crate feature`cors`** only.

Expand description

Middleware which adds headers for [CORS](https://developer.mozilla.org/en-
US/docs/Web/HTTP/CORS).

## §Example

    
    
    use http::{Request, Response, Method, header};
    use http_body_util::Full;
    use bytes::Bytes;
    use tower::{ServiceBuilder, ServiceExt, Service};
    use tower_http::cors::{Any, CorsLayer};
    use std::convert::Infallible;
    
    async fn handle(request: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
        Ok(Response::new(Full::default()))
    }
    
    let cors = CorsLayer::new()
        // allow `GET` and `POST` when accessing the resource
        .allow_methods([Method::GET, Method::POST])
        // allow requests from any origin
        .allow_origin(Any);
    
    let mut service = ServiceBuilder::new()
        .layer(cors)
        .service_fn(handle);
    
    let request = Request::builder()
        .header(header::ORIGIN, "https://example.com")
        .body(Full::default())
        .unwrap();
    
    let response = service
        .ready()
        .await?
        .call(request)
        .await?;
    
    assert_eq!(
        response.headers().get(header::ACCESS_CONTROL_ALLOW_ORIGIN).unwrap(),
        "*",
    );

## Structs§

[AllowCredentials](struct.AllowCredentials.html "struct
tower_http::cors::AllowCredentials")

    Holds configuration for how to set the [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials) header.
[AllowHeaders](struct.AllowHeaders.html "struct
tower_http::cors::AllowHeaders")

    Holds configuration for how to set the [`Access-Control-Allow-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) header.
[AllowMethods](struct.AllowMethods.html "struct
tower_http::cors::AllowMethods")

    Holds configuration for how to set the [`Access-Control-Allow-Methods`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods) header.
[AllowOrigin](struct.AllowOrigin.html "struct tower_http::cors::AllowOrigin")

    Holds configuration for how to set the [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) header.
[AllowPrivateNetwork](struct.AllowPrivateNetwork.html "struct
tower_http::cors::AllowPrivateNetwork")

    Holds configuration for how to set the [`Access-Control-Allow-Private-Network`](https://wicg.github.io/private-network-access/) header.
[Any](struct.Any.html "struct tower_http::cors::Any")

    Represents a wildcard value (`*`) used with some CORS headers such as [`CorsLayer::allow_methods`](struct.CorsLayer.html#method.allow_methods "method tower_http::cors::CorsLayer::allow_methods").
[Cors](struct.Cors.html "struct tower_http::cors::Cors")

    Middleware which adds headers for [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
[CorsLayer](struct.CorsLayer.html "struct tower_http::cors::CorsLayer")

    Layer that applies the [`Cors`](struct.Cors.html "struct tower_http::cors::Cors") middleware which adds headers for [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
[ExposeHeaders](struct.ExposeHeaders.html "struct
tower_http::cors::ExposeHeaders")

    Holds configuration for how to set the [`Access-Control-Expose-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers) header.
[MaxAge](struct.MaxAge.html "struct tower_http::cors::MaxAge")

    Holds configuration for how to set the [`Access-Control-Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age) header.
[ResponseFuture](struct.ResponseFuture.html "struct
tower_http::cors::ResponseFuture")

    Response future for [`Cors`](struct.Cors.html "struct tower_http::cors::Cors").
[Vary](struct.Vary.html "struct tower_http::cors::Vary")

    Holds configuration for how to set the [`Vary`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary) header.

## Functions§

[any](fn.any.html "fn tower_http::cors::any")Deprecated

    Represents a wildcard value (`*`) used with some CORS headers such as [`CorsLayer::allow_methods`](struct.CorsLayer.html#method.allow_methods "method tower_http::cors::CorsLayer::allow_methods").
[preflight_request_headers](fn.preflight_request_headers.html "fn
tower_http::cors::preflight_request_headers")

    Returns an iterator over the three request headers that may be involved in a CORS preflight request.

