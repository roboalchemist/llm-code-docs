# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/follow_redirect/
# Path: follow_redirect/

[tower_http](../index.html)

# Module follow_redirect Copy item path

[Source](../../src/tower_http/follow_redirect/mod.rs.html#1-476)

Available on **crate feature`follow-redirect`** only.

Expand description

Middleware for following redirections.

## §Overview

The [`FollowRedirect`](struct.FollowRedirect.html "struct
tower_http::follow_redirect::FollowRedirect") middleware retries requests with
the inner [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-
linux-gnu/tower_service/trait.Service.html "trait tower_service::Service") to
follow HTTP redirections.

The middleware tries to clone the original
[`Request`](https://docs.rs/http/1.1.0/x86_64-unknown-linux-
gnu/http/request/struct.Request.html "struct http::request::Request") when
making a redirected request. However, since
[`Extensions`](https://docs.rs/http/1.1.0/x86_64-unknown-linux-
gnu/http/extensions/struct.Extensions.html "struct
http::extensions::Extensions") are `!Clone`, any extensions set by outer
middleware will be discarded. Also, the request body cannot always be cloned.
When the original body is known to be empty by
[`Body::size_hint`](https://docs.rs/http-body/1.0.1/x86_64-unknown-linux-
gnu/http_body/trait.Body.html#method.size_hint "method
http_body::Body::size_hint"), the middleware uses `Default` implementation of
the body type to create a new request body. If you know that the body can be
cloned in some way, you can tell the middleware to clone it by configuring a
[`policy`](policy/index.html "mod tower_http::follow_redirect::policy").

## §Examples

### §Basic usage

    
    
    use http::{Request, Response};
    use bytes::Bytes;
    use http_body_util::Full;
    use tower::{Service, ServiceBuilder, ServiceExt};
    use tower_http::follow_redirect::{FollowRedirectLayer, RequestUri};
    
    let mut client = ServiceBuilder::new()
        .layer(FollowRedirectLayer::new())
        .service(http_client);
    
    let request = Request::builder()
        .uri("https://rust-lang.org/")
        .body(Full::<Bytes>::default())
        .unwrap();
    
    let response = client.ready().await?.call(request).await?;
    // Get the final request URI.
    assert_eq!(response.extensions().get::<RequestUri>().unwrap().0, "https://www.rust-lang.org/");

### §Customizing the `Policy`

You can use a [`Policy`](policy/trait.Policy.html "trait
tower_http::follow_redirect::policy::Policy") value to customize how the
middleware handles redirections.

    
    
    use http::{Request, Response};
    use http_body_util::Full;
    use bytes::Bytes;
    use tower::{Service, ServiceBuilder, ServiceExt};
    use tower_http::follow_redirect::{
        policy::{self, PolicyExt},
        FollowRedirectLayer,
    };
    
    #[derive(Debug)]
    enum MyError {
        TooManyRedirects,
        Other(tower::BoxError),
    }
    
    let policy = policy::Limited::new(10) // Set the maximum number of redirections to 10.
        // Return an error when the limit was reached.
        .or::<_, (), _>(policy::redirect_fn(|_| Err(MyError::TooManyRedirects)))
        // Do not follow cross-origin redirections, and return the redirection responses as-is.
        .and::<_, (), _>(policy::SameOrigin::new());
    
    let mut client = ServiceBuilder::new()
        .layer(FollowRedirectLayer::with_policy(policy))
        .map_err(MyError::Other)
        .service(http_client);
    
    // ...

## Modules§

[policy](policy/index.html "mod tower_http::follow_redirect::policy")

    Tools for customizing the behavior of a [`FollowRedirect`](struct.FollowRedirect.html "struct tower_http::follow_redirect::FollowRedirect") middleware.

## Structs§

[FollowRedirect](struct.FollowRedirect.html "struct
tower_http::follow_redirect::FollowRedirect")

    Middleware that retries requests with a [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service") to follow redirection responses.
[FollowRedirectLayer](struct.FollowRedirectLayer.html "struct
tower_http::follow_redirect::FollowRedirectLayer")

    [`Layer`](https://docs.rs/tower-layer/0.3.3/x86_64-unknown-linux-gnu/tower_layer/trait.Layer.html "trait tower_layer::Layer") for retrying requests with a [`Service`](https://docs.rs/tower-service/0.3.3/x86_64-unknown-linux-gnu/tower_service/trait.Service.html "trait tower_service::Service") to follow redirection responses.
[RequestUri](struct.RequestUri.html "struct
tower_http::follow_redirect::RequestUri")

    Response [`Extensions`](https://docs.rs/http/1.1.0/x86_64-unknown-linux-gnu/http/extensions/struct.Extensions.html "struct http::extensions::Extensions") value that represents the effective request URI of a response returned by a [`FollowRedirect`](struct.FollowRedirect.html "struct tower_http::follow_redirect::FollowRedirect") middleware.
[ResponseFuture](struct.ResponseFuture.html "struct
tower_http::follow_redirect::ResponseFuture")

    Response future for [`FollowRedirect`](struct.FollowRedirect.html "struct tower_http::follow_redirect::FollowRedirect").

