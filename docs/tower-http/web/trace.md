# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/trace/
# Path: trace/

[tower_http](../index.html)

# Module trace Copy item path

[Source](../../src/tower_http/trace/mod.rs.html#1-635)

Available on **crate feature`trace`** only.

Expand description

Middleware that adds high level [tracing](https://crates.io/crates/tracing) to
a [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-
gnu/tower_service/trait.Service.html "trait tower_service::Service").

## §Example

Adding tracing to your service can be as simple as:

    
    
    use http::{Request, Response};
    use tower::{ServiceBuilder, ServiceExt, Service};
    use tower_http::trace::TraceLayer;
    use std::convert::Infallible;
    use http_body_util::Full;
    use bytes::Bytes;
    
    async fn handle(request: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
        Ok(Response::new(Full::default()))
    }
    
    // Setup tracing
    tracing_subscriber::fmt::init();
    
    let mut service = ServiceBuilder::new()
        .layer(TraceLayer::new_for_http())
        .service_fn(handle);
    
    let request = Request::new(Full::from("foo"));
    
    let response = service
        .ready()
        .await?
        .call(request)
        .await?;

If you run this application with `RUST_LOG=tower_http=trace cargo run` you
should see logs like:

    
    
    Mar 05 20:50:28.523 DEBUG request{method=GET path="/foo"}: tower_http::trace::on_request: started processing request
    Mar 05 20:50:28.524 DEBUG request{method=GET path="/foo"}: tower_http::trace::on_response: finished processing request latency=1 ms status=200

## §Customization

[`Trace`](struct.Trace.html "struct tower_http::trace::Trace") comes with good
defaults but also supports customizing many aspects of the output.

The default behaviour supports some customization:

    
    
    use http::{Request, Response, HeaderMap, StatusCode};
    use http_body_util::Full;
    use bytes::Bytes;
    use tower::ServiceBuilder;
    use tracing::Level;
    use tower_http::{
        LatencyUnit,
        trace::{TraceLayer, DefaultMakeSpan, DefaultOnRequest, DefaultOnResponse},
    };
    use std::time::Duration;
    
    let service = ServiceBuilder::new()
        .layer(
            TraceLayer::new_for_http()
                .make_span_with(
                    DefaultMakeSpan::new().include_headers(true)
                )
                .on_request(
                    DefaultOnRequest::new().level(Level::INFO)
                )
                .on_response(
                    DefaultOnResponse::new()
                        .level(Level::INFO)
                        .latency_unit(LatencyUnit::Micros)
                )
                // on so on for `on_eos`, `on_body_chunk`, and `on_failure`
        )
        .service_fn(handle);

However for maximum control you can provide callbacks:

    
    
    use http::{Request, Response, HeaderMap, StatusCode};
    use http_body_util::Full;
    use bytes::Bytes;
    use tower::ServiceBuilder;
    use tower_http::{classify::ServerErrorsFailureClass, trace::TraceLayer};
    use std::time::Duration;
    use tracing::Span;
    
    let service = ServiceBuilder::new()
        .layer(
            TraceLayer::new_for_http()
                .make_span_with(|request: &Request<Full<Bytes>>| {
                    tracing::debug_span!("http-request")
                })
                .on_request(|request: &Request<Full<Bytes>>, _span: &Span| {
                    tracing::debug!("started {} {}", request.method(), request.uri().path())
                })
                .on_response(|response: &Response<Full<Bytes>>, latency: Duration, _span: &Span| {
                    tracing::debug!("response generated in {:?}", latency)
                })
                .on_body_chunk(|chunk: &Bytes, latency: Duration, _span: &Span| {
                    tracing::debug!("sending {} bytes", chunk.len())
                })
                .on_eos(|trailers: Option<&HeaderMap>, stream_duration: Duration, _span: &Span| {
                    tracing::debug!("stream closed after {:?}", stream_duration)
                })
                .on_failure(|error: ServerErrorsFailureClass, latency: Duration, _span: &Span| {
                    tracing::debug!("something went wrong")
                })
        )
        .service_fn(handle);

### §Disabling something

Setting the behaviour to `()` will be disable that particular step:

    
    
    use http::StatusCode;
    use tower::ServiceBuilder;
    use tower_http::{classify::ServerErrorsFailureClass, trace::TraceLayer};
    use std::time::Duration;
    use tracing::Span;
    
    let service = ServiceBuilder::new()
        .layer(
            // This configuration will only emit events on failures
            TraceLayer::new_for_http()
                .on_request(())
                .on_response(())
                .on_body_chunk(())
                .on_eos(())
                .on_failure(|error: ServerErrorsFailureClass, latency: Duration, _span: &Span| {
                    tracing::debug!("something went wrong")
                })
        )
        .service_fn(handle);

## §When the callbacks are called

#### §`on_request`

The `on_request` callback is called when the request arrives at the middleware
in [`Service::call`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-
gnu/tower_service/trait.Service.html#tymethod.call "method
tower_service::Service::call") just prior to passing the request to the inner
service.

#### §`on_response`

The `on_response` callback is called when the inner service’s response future
completes with `Ok(response)` regardless if the response is classified as a
success or a failure.

For example if you’re using
[`ServerErrorsAsFailures`](../classify/struct.ServerErrorsAsFailures.html
"struct tower_http::classify::ServerErrorsAsFailures") as your classifier and
the inner service responds with `500 Internal Server Error` then the
`on_response` callback is still called. `on_failure` would _also_ be called in
this case since the response was classified as a failure.

#### §`on_body_chunk`

The `on_body_chunk` callback is called when the response body produces a new
chunk, that is when [`Body::poll_frame`](https://docs.rs/http-
body/1.0.1/x86_64-unknown-linux-
gnu/http_body/trait.Body.html#tymethod.poll_frame "method
http_body::Body::poll_frame") returns a data frame.

`on_body_chunk` is called even if the chunk is empty.

#### §`on_eos`

The `on_eos` callback is called when a streaming response body ends, that is
when [`Body::poll_frame`](https://docs.rs/http-body/1.0.1/x86_64-unknown-
linux-gnu/http_body/trait.Body.html#tymethod.poll_frame "method
http_body::Body::poll_frame") returns a trailers frame.

`on_eos` is called even if the trailers produced are `None`.

#### §`on_failure`

The `on_failure` callback is called when:

  * The inner [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service")’s response future resolves to an error.
  * A response is classified as a failure.
  * [`Body::poll_frame`](https://docs.rs/http-body/1.0.1/x86_64-unknown-linux-gnu/http_body/trait.Body.html#tymethod.poll_frame "method http_body::Body::poll_frame") returns an error.
  * An end-of-stream is classified as a failure.

## §Recording fields on the span

All callbacks receive a reference to the
[tracing](https://crates.io/crates/tracing)
[`Span`](https://docs.rs/tracing/0.1.40/x86_64-unknown-linux-
gnu/tracing/span/struct.Span.html "struct tracing::span::Span"), corresponding
to this request, produced by the closure passed to
[`TraceLayer::make_span_with`](struct.TraceLayer.html#method.make_span_with
"method tower_http::trace::TraceLayer::make_span_with"). It can be used to
[record field
values](https://docs.rs/tracing/latest/tracing/span/struct.Span.html#method.record)
that weren’t known when the span was created.

    
    
    use http::{Request, Response, HeaderMap, StatusCode};
    use http_body_util::Full;
    use bytes::Bytes;
    use tower::ServiceBuilder;
    use tower_http::trace::TraceLayer;
    use tracing::Span;
    use std::time::Duration;
    
    let service = ServiceBuilder::new()
        .layer(
            TraceLayer::new_for_http()
                .make_span_with(|request: &Request<Full<Bytes>>| {
                    tracing::debug_span!(
                        "http-request",
                        status_code = tracing::field::Empty,
                    )
                })
                .on_response(|response: &Response<Full<Bytes>>, _latency: Duration, span: &Span| {
                    span.record("status_code", &tracing::field::display(response.status()));
    
                    tracing::debug!("response generated")
                })
        )
        .service_fn(handle);

## §Providing classifiers

Tracing requires determining if a response is a success or failure.
[`MakeClassifier`](../classify/trait.MakeClassifier.html "trait
tower_http::classify::MakeClassifier") is used to create a classifier for the
incoming request. See the docs for
[`MakeClassifier`](../classify/trait.MakeClassifier.html "trait
tower_http::classify::MakeClassifier") and
[`ClassifyResponse`](../classify/trait.ClassifyResponse.html "trait
tower_http::classify::ClassifyResponse") for more details on classification.

A [`MakeClassifier`](../classify/trait.MakeClassifier.html "trait
tower_http::classify::MakeClassifier") can be provided when creating a
[`TraceLayer`](struct.TraceLayer.html "struct tower_http::trace::TraceLayer"):

    
    
    use http::{Request, Response};
    use http_body_util::Full;
    use bytes::Bytes;
    use tower::ServiceBuilder;
    use tower_http::{
        trace::TraceLayer,
        classify::{
            MakeClassifier, ClassifyResponse, ClassifiedResponse, NeverClassifyEos,
            SharedClassifier,
        },
    };
    use std::convert::Infallible;
    
    // Our `MakeClassifier` that always crates `MyClassifier` classifiers.
    #[derive(Copy, Clone)]
    struct MyMakeClassify;
    
    impl MakeClassifier for MyMakeClassify {
        type Classifier = MyClassifier;
        type FailureClass = &'static str;
        type ClassifyEos = NeverClassifyEos<&'static str>;
    
        fn make_classifier<B>(&self, req: &Request<B>) -> Self::Classifier {
            MyClassifier
        }
    }
    
    // A classifier that classifies failures as `"something went wrong..."`.
    #[derive(Copy, Clone)]
    struct MyClassifier;
    
    impl ClassifyResponse for MyClassifier {
        type FailureClass = &'static str;
        type ClassifyEos = NeverClassifyEos<&'static str>;
    
        fn classify_response<B>(
            self,
            res: &Response<B>
        ) -> ClassifiedResponse<Self::FailureClass, Self::ClassifyEos> {
            // Classify based on the status code.
            if res.status().is_server_error() {
                ClassifiedResponse::Ready(Err("something went wrong..."))
            } else {
                ClassifiedResponse::Ready(Ok(()))
            }
        }
    
        fn classify_error<E>(self, error: &E) -> Self::FailureClass
        where
            E: std::fmt::Display + 'static,
        {
            "something went wrong..."
        }
    }
    
    let service = ServiceBuilder::new()
        // Create a trace layer that uses our classifier.
        .layer(TraceLayer::new(MyMakeClassify))
        .service_fn(handle);
    
    // Since `MyClassifier` is `Clone` we can also use `SharedClassifier`
    // to avoid having to define a separate `MakeClassifier`.
    let service = ServiceBuilder::new()
        .layer(TraceLayer::new(SharedClassifier::new(MyClassifier)))
        .service_fn(handle);

[`TraceLayer`](struct.TraceLayer.html "struct tower_http::trace::TraceLayer")
comes with convenience methods for using common classifiers:

  * [`TraceLayer::new_for_http`](struct.TraceLayer.html#method.new_for_http "associated function tower_http::trace::TraceLayer::new_for_http") classifies based on the status code. It doesn’t consider streaming responses.
  * [`TraceLayer::new_for_grpc`](struct.TraceLayer.html#method.new_for_grpc "associated function tower_http::trace::TraceLayer::new_for_grpc") classifies based on the gRPC protocol and supports streaming responses.

## Structs§

[DefaultMakeSpan](struct.DefaultMakeSpan.html "struct
tower_http::trace::DefaultMakeSpan")

    The default way [`Span`](https://docs.rs/tracing/0.1.40/x86_64-unknown-linux-gnu/tracing/span/struct.Span.html "struct tracing::span::Span")s will be created for [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[DefaultOnBodyChunk](struct.DefaultOnBodyChunk.html "struct
tower_http::trace::DefaultOnBodyChunk")

    The default [`OnBodyChunk`](trait.OnBodyChunk.html "trait tower_http::trace::OnBodyChunk") implementation used by [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[DefaultOnEos](struct.DefaultOnEos.html "struct
tower_http::trace::DefaultOnEos")

    The default [`OnEos`](trait.OnEos.html "trait tower_http::trace::OnEos") implementation used by [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[DefaultOnFailure](struct.DefaultOnFailure.html "struct
tower_http::trace::DefaultOnFailure")

    The default [`OnFailure`](trait.OnFailure.html "trait tower_http::trace::OnFailure") implementation used by [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[DefaultOnRequest](struct.DefaultOnRequest.html "struct
tower_http::trace::DefaultOnRequest")

    The default [`OnRequest`](trait.OnRequest.html "trait tower_http::trace::OnRequest") implementation used by [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[DefaultOnResponse](struct.DefaultOnResponse.html "struct
tower_http::trace::DefaultOnResponse")

    The default [`OnResponse`](trait.OnResponse.html "trait tower_http::trace::OnResponse") implementation used by [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[ResponseBody](struct.ResponseBody.html "struct
tower_http::trace::ResponseBody")

    Response body for [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[ResponseFuture](struct.ResponseFuture.html "struct
tower_http::trace::ResponseFuture")

    Response future for [`Trace`](struct.Trace.html "struct tower_http::trace::Trace").
[Trace](struct.Trace.html "struct tower_http::trace::Trace")

    Middleware that adds high level [tracing](https://crates.io/crates/tracing) to a [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service").
[TraceLayer](struct.TraceLayer.html "struct tower_http::trace::TraceLayer")

    [`Layer`](https://docs.rs/tower-layer/0.3.3/x86_64-unknown-linux-gnu/tower_layer/trait.Layer.html "trait tower_layer::Layer") that adds high level [tracing](https://crates.io/crates/tracing) to a [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service").

## Traits§

[MakeSpan](trait.MakeSpan.html "trait tower_http::trace::MakeSpan")

    Trait used to generate [`Span`](https://docs.rs/tracing/0.1.40/x86_64-unknown-linux-gnu/tracing/span/struct.Span.html "struct tracing::span::Span")s from requests. [`Trace`](struct.Trace.html "struct tower_http::trace::Trace") wraps all request handling in this span.
[OnBodyChunk](trait.OnBodyChunk.html "trait tower_http::trace::OnBodyChunk")

    Trait used to tell [`Trace`](struct.Trace.html "struct tower_http::trace::Trace") what to do when a body chunk has been sent.
[OnEos](trait.OnEos.html "trait tower_http::trace::OnEos")

    Trait used to tell [`Trace`](struct.Trace.html "struct tower_http::trace::Trace") what to do when a stream closes.
[OnFailure](trait.OnFailure.html "trait tower_http::trace::OnFailure")

    Trait used to tell [`Trace`](struct.Trace.html "struct tower_http::trace::Trace") what to do when a request fails.
[OnRequest](trait.OnRequest.html "trait tower_http::trace::OnRequest")

    Trait used to tell [`Trace`](struct.Trace.html "struct tower_http::trace::Trace") what to do when a request is received.
[OnResponse](trait.OnResponse.html "trait tower_http::trace::OnResponse")

    Trait used to tell [`Trace`](struct.Trace.html "struct tower_http::trace::Trace") what to do when a response has been produced.

## Type Aliases§

[GrpcMakeClassifier](type.GrpcMakeClassifier.html "type
tower_http::trace::GrpcMakeClassifier")

    MakeClassifier for gRPC requests.
[HttpMakeClassifier](type.HttpMakeClassifier.html "type
tower_http::trace::HttpMakeClassifier")

    MakeClassifier for HTTP requests.

