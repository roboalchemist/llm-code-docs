# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/request_id/
# Path: request_id/

[tower_http](../index.html)

# Module request_id Copy item path

[Source](../../src/tower_http/request_id.rs.html#1-604)

Available on **crate feature`request-id`** only.

Expand description

Set and propagate request ids.

## §Example

    
    
    use http::{Request, Response, header::HeaderName};
    use tower::{Service, ServiceExt, ServiceBuilder};
    use tower_http::request_id::{
        SetRequestIdLayer, PropagateRequestIdLayer, MakeRequestId, RequestId,
    };
    use http_body_util::Full;
    use bytes::Bytes;
    use std::sync::{Arc, atomic::{AtomicU64, Ordering}};
    
    // A `MakeRequestId` that increments an atomic counter
    #[derive(Clone, Default)]
    struct MyMakeRequestId {
        counter: Arc<AtomicU64>,
    }
    
    impl MakeRequestId for MyMakeRequestId {
        fn make_request_id<B>(&mut self, request: &Request<B>) -> Option<RequestId> {
            let request_id = self.counter
                .fetch_add(1, Ordering::SeqCst)
                .to_string()
                .parse()
                .unwrap();
    
            Some(RequestId::new(request_id))
        }
    }
    
    let x_request_id = HeaderName::from_static("x-request-id");
    
    let mut svc = ServiceBuilder::new()
        // set `x-request-id` header on all requests
        .layer(SetRequestIdLayer::new(
            x_request_id.clone(),
            MyMakeRequestId::default(),
        ))
        // propagate `x-request-id` headers from request to response
        .layer(PropagateRequestIdLayer::new(x_request_id))
        .service(handler);
    
    let request = Request::new(Full::default());
    let response = svc.ready().await?.call(request).await?;
    
    assert_eq!(response.headers()["x-request-id"], "0");

Additional convenience methods are available on
[`ServiceBuilderExt`](../trait.ServiceBuilderExt.html "trait
tower_http::ServiceBuilderExt"):

    
    
    use tower_http::ServiceBuilderExt;
    
    let mut svc = ServiceBuilder::new()
        .set_x_request_id(MyMakeRequestId::default())
        .propagate_x_request_id()
        .service(handler);
    
    let request = Request::new(Full::default());
    let response = svc.ready().await?.call(request).await?;
    
    assert_eq!(response.headers()["x-request-id"], "0");

See [`SetRequestId`](struct.SetRequestId.html "struct
tower_http::request_id::SetRequestId") and
[`PropagateRequestId`](struct.PropagateRequestId.html "struct
tower_http::request_id::PropagateRequestId") for more details.

## §Using `Trace`

To have request ids show up correctly in logs produced by
[`Trace`](../trace/struct.Trace.html "struct tower_http::trace::Trace") you
must apply the layers in this order:

    
    
    use tower_http::{
        ServiceBuilderExt,
        trace::{TraceLayer, DefaultMakeSpan, DefaultOnResponse},
    };
    
    let svc = ServiceBuilder::new()
        // make sure to set request ids before the request reaches `TraceLayer`
        .set_x_request_id(MyMakeRequestId::default())
        // log requests and responses
        .layer(
            TraceLayer::new_for_http()
                .make_span_with(DefaultMakeSpan::new().include_headers(true))
                .on_response(DefaultOnResponse::new().include_headers(true))
        )
        // propagate the header to the response before the response reaches `TraceLayer`
        .propagate_x_request_id()
        .service(handler);

## §Doesn’t override existing headers

[`SetRequestId`](struct.SetRequestId.html "struct
tower_http::request_id::SetRequestId") and
[`PropagateRequestId`](struct.PropagateRequestId.html "struct
tower_http::request_id::PropagateRequestId") wont override request ids if its
already present on requests or responses. Among other things, this allows
other middleware to conditionally set request ids and use the middleware in
this module as a fallback.

## Structs§

[MakeRequestUuid](struct.MakeRequestUuid.html "struct
tower_http::request_id::MakeRequestUuid")

    A [`MakeRequestId`](trait.MakeRequestId.html "trait tower_http::request_id::MakeRequestId") that generates `UUID`s.
[PropagateRequestId](struct.PropagateRequestId.html "struct
tower_http::request_id::PropagateRequestId")

    Propagate request ids from requests to responses.
[PropagateRequestIdLayer](struct.PropagateRequestIdLayer.html "struct
tower_http::request_id::PropagateRequestIdLayer")

    Propagate request ids from requests to responses.
[PropagateRequestIdResponseFuture](struct.PropagateRequestIdResponseFuture.html
"struct tower_http::request_id::PropagateRequestIdResponseFuture")

    Response future for [`PropagateRequestId`](struct.PropagateRequestId.html "struct tower_http::request_id::PropagateRequestId").
[RequestId](struct.RequestId.html "struct tower_http::request_id::RequestId")

    An identifier for a request.
[SetRequestId](struct.SetRequestId.html "struct
tower_http::request_id::SetRequestId")

    Set request id headers and extensions on requests.
[SetRequestIdLayer](struct.SetRequestIdLayer.html "struct
tower_http::request_id::SetRequestIdLayer")

    Set request id headers and extensions on requests.

## Traits§

[MakeRequestId](trait.MakeRequestId.html "trait
tower_http::request_id::MakeRequestId")

    Trait for producing [`RequestId`](struct.RequestId.html "struct tower_http::request_id::RequestId")s.

