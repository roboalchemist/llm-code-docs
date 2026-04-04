# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/
# Path: index

# Crate tower_http Copy item path

[Source](../src/tower_http/lib.rs.html#1-373)

Expand description

`async fn(HttpRequest) -> Result<HttpResponse, Error>`

## §Overview

tower-http is a library that provides HTTP-specific middleware and utilities
built on top of [tower](https://crates.io/crates/tower).

All middleware uses the [http](https://crates.io/crates/http) and [http-
body](https://crates.io/crates/http-body) crates as the HTTP abstractions.
That means they’re compatible with any library or framework that also uses
those crates, such as [hyper](https://crates.io/crates/hyper),
[tonic](https://crates.io/crates/tonic), and
[warp](https://crates.io/crates/warp).

## §Example server

This example shows how to apply middleware from tower-http to a
[`Service`](https://docs.rs/tower/latest/tower/trait.Service.html) and then
run that service using [hyper](https://crates.io/crates/hyper).

    
    
    use tower_http::{
        add_extension::AddExtensionLayer,
        compression::CompressionLayer,
        propagate_header::PropagateHeaderLayer,
        sensitive_headers::SetSensitiveRequestHeadersLayer,
        set_header::SetResponseHeaderLayer,
        trace::TraceLayer,
        validate_request::ValidateRequestHeaderLayer,
    };
    use tower::{ServiceBuilder, service_fn, BoxError};
    use http::{Request, Response, header::{HeaderName, CONTENT_TYPE, AUTHORIZATION}};
    use std::{sync::Arc, net::SocketAddr, convert::Infallible, iter::once};
    use bytes::Bytes;
    use http_body_util::Full;
    
    // Our request handler. This is where we would implement the application logic
    // for responding to HTTP requests...
    async fn handler(request: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, BoxError> {
        // ...
    }
    
    // Shared state across all request handlers --- in this case, a pool of database connections.
    struct State {
        pool: DatabaseConnectionPool,
    }
    
    #[tokio::main]
    async fn main() {
        // Construct the shared state.
        let state = State {
            pool: DatabaseConnectionPool::new(),
        };
    
        // Use tower's `ServiceBuilder` API to build a stack of tower middleware
        // wrapping our request handler.
        let service = ServiceBuilder::new()
            // Mark the `Authorization` request header as sensitive so it doesn't show in logs
            .layer(SetSensitiveRequestHeadersLayer::new(once(AUTHORIZATION)))
            // High level logging of requests and responses
            .layer(TraceLayer::new_for_http())
            // Share an `Arc<State>` with all requests
            .layer(AddExtensionLayer::new(Arc::new(state)))
            // Compress responses
            .layer(CompressionLayer::new())
            // Propagate `X-Request-Id`s from requests to responses
            .layer(PropagateHeaderLayer::new(HeaderName::from_static("x-request-id")))
            // If the response has a known size set the `Content-Length` header
            .layer(SetResponseHeaderLayer::overriding(CONTENT_TYPE, content_length_from_response))
            // Authorize requests using a token
            .layer(ValidateRequestHeaderLayer::bearer("passwordlol"))
            // Accept only application/json, application/* and */* in a request's ACCEPT header
            .layer(ValidateRequestHeaderLayer::accept("application/json"))
            // Wrap a `Service` in our middleware stack
            .service_fn(handler);
    }

Keep in mind that while this example uses
[hyper](https://crates.io/crates/hyper), tower-http supports any HTTP
client/server implementation that uses the
[http](https://crates.io/crates/http) and [http-
body](https://crates.io/crates/http-body) crates.

## §Example client

tower-http middleware can also be applied to HTTP clients:

    
    
    use tower_http::{
        decompression::DecompressionLayer,
        set_header::SetRequestHeaderLayer,
        trace::TraceLayer,
        classify::StatusInRangeAsFailures,
    };
    use tower::{ServiceBuilder, Service, ServiceExt};
    use hyper_util::{rt::TokioExecutor, client::legacy::Client};
    use http_body_util::Full;
    use bytes::Bytes;
    use http::{Request, HeaderValue, header::USER_AGENT};
    
    #[tokio::main]
    async fn main() {
    let client = Client::builder(TokioExecutor::new()).build_http();
        let mut client = ServiceBuilder::new()
            // Add tracing and consider server errors and client
            // errors as failures.
            .layer(TraceLayer::new(
                StatusInRangeAsFailures::new(400..=599).into_make_classifier()
            ))
            // Set a `User-Agent` header on all requests.
            .layer(SetRequestHeaderLayer::overriding(
                USER_AGENT,
                HeaderValue::from_static("tower-http demo")
            ))
            // Decompress response bodies
            .layer(DecompressionLayer::new())
            // Wrap a `Client` in our middleware stack.
            // This is possible because `Client` implements
            // `tower::Service`.
            .service(client);
    
        // Make a request
        let request = Request::builder()
            .uri("http://example.com")
            .body(Full::<Bytes>::default())
            .unwrap();
    
        let response = client
            .ready()
            .await
            .unwrap()
            .call(request)
            .await
            .unwrap();
    }

## §Feature Flags

All middleware are disabled by default and can be enabled using [cargo
features](https://doc.rust-lang.org/cargo/reference/features.html).

For example, to enable the [`Trace`](trace/struct.Trace.html "struct
tower_http::trace::Trace") middleware, add the “trace” feature flag in your
`Cargo.toml`:

    
    
    tower-http = { version = "0.1", features = ["trace"] }

You can use `"full"` to enable everything:

    
    
    tower-http = { version = "0.1", features = ["full"] }

## §Getting Help

If you’re new to tower its [guides](https://github.com/tower-
rs/tower/tree/master/guides) might help. In the tower-http repo we also have a
[number of examples](https://github.com/tower-rs/tower-
http/tree/master/examples) showing how to put everything together. You’re also
welcome to ask in the [`#tower` Discord channel](https://discord.gg/tokio) or
open an [issue](https://github.com/tower-rs/tower-http/issues/new) with your
question.

## Modules§

[add_extension](add_extension/index.html "mod tower_http::add_extension")`add-
extension`

    Middleware that clones a value into each request’s [extensions](https://docs.rs/http/latest/http/struct.Extensions.html).
[auth](auth/index.html "mod tower_http::auth")`auth`

    Authorization related middleware.
[body](body/index.html "mod tower_http::body")`catch-panic` or `decompression-
br` or `decompression-deflate` or `decompression-gzip` or `decompression-zstd`
or `fs` or `limit`

    Body types.
[catch_panic](catch_panic/index.html "mod tower_http::catch_panic")`catch-
panic`

    Convert panics into responses.
[classify](classify/index.html "mod tower_http::classify")

    Tools for classifying responses as either success or failure.
[compression](compression/index.html "mod
tower_http::compression")`compression-br` or `compression-deflate` or
`compression-gzip` or `compression-zstd`

    Middleware that compresses response bodies.
[cors](cors/index.html "mod tower_http::cors")`cors`

    Middleware which adds headers for [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
[decompression](decompression/index.html "mod
tower_http::decompression")`decompression-br` or `decompression-deflate` or
`decompression-gzip` or `decompression-zstd`

    Middleware that decompresses request and response bodies.
[follow_redirect](follow_redirect/index.html "mod
tower_http::follow_redirect")`follow-redirect`

    Middleware for following redirections.
[limit](limit/index.html "mod tower_http::limit")`limit`

    Middleware for limiting request bodies.
[map_request_body](map_request_body/index.html "mod
tower_http::map_request_body")`map-request-body`

    Apply a transformation to the request body.
[map_response_body](map_response_body/index.html "mod
tower_http::map_response_body")`map-response-body`

    Apply a transformation to the response body.
[metrics](metrics/index.html "mod tower_http::metrics")`metrics`

    Middlewares for adding metrics to services.
[normalize_path](normalize_path/index.html "mod
tower_http::normalize_path")`normalize-path`

    Middleware that normalizes paths.
[propagate_header](propagate_header/index.html "mod
tower_http::propagate_header")`propagate-header`

    Propagate a header from the request to the response.
[request_id](request_id/index.html "mod tower_http::request_id")`request-id`

    Set and propagate request ids.
[sensitive_headers](sensitive_headers/index.html "mod
tower_http::sensitive_headers")`sensitive-headers`

    Middlewares that mark headers as [sensitive](https://docs.rs/http/latest/http/header/struct.HeaderValue.html#method.set_sensitive).
[services](services/index.html "mod tower_http::services")

    [`Service`](https://docs.rs/tower/latest/tower/trait.Service.html)s that return responses without wrapping other [`Service`](https://docs.rs/tower/latest/tower/trait.Service.html)s.
[set_header](set_header/index.html "mod tower_http::set_header")`set-header`

    Middleware for setting headers on requests and responses.
[set_status](set_status/index.html "mod tower_http::set_status")`set-status`

    Middleware to override status codes.
[timeout](timeout/index.html "mod tower_http::timeout")`timeout`

    Middleware that applies a timeout to requests.
[trace](trace/index.html "mod tower_http::trace")`trace`

    Middleware that adds high level [tracing](https://crates.io/crates/tracing) to a [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service").
[validate_request](validate_request/index.html "mod
tower_http::validate_request")`validate-request`

    Middleware that validates requests.

## Enums§

[CompressionLevel](enum.CompressionLevel.html "enum
tower_http::CompressionLevel")`compression-br` or `compression-deflate` or
`compression-gzip` or `compression-zstd` or `decompression-br` or
`decompression-deflate` or `decompression-gzip` or `decompression-zstd`

    Level of compression data should be compressed with.
[LatencyUnit](enum.LatencyUnit.html "enum tower_http::LatencyUnit")

    The latency unit used to report latencies by middleware.

## Traits§

[ServiceBuilderExt](trait.ServiceBuilderExt.html "trait
tower_http::ServiceBuilderExt")`util`

    Extension trait that adds methods to [`tower::ServiceBuilder`](https://docs.rs/tower/0.5.2/x86_64-unknown-linux-gnu/tower/builder/struct.ServiceBuilder.html "struct tower::builder::ServiceBuilder") for adding middleware from tower-http.
[ServiceExt](trait.ServiceExt.html "trait tower_http::ServiceExt")`util`

    Extension trait that adds methods to any [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service") for adding middleware from tower-http.

## Type Aliases§

[BoxError](type.BoxError.html "type tower_http::BoxError")

    Alias for a type-erased error type.

