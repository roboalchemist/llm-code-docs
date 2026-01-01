# Source: https://docs.rs/tower-http/latest/tower_http/add_extension/

[tower_http](../index.html)
# Module add_extension Copy item path

[Source](../../src/tower_http/add_extension.rs.html#1-167)
Available on
**crate feature add-extension**
only.
Expand description
Middleware that clones a value into each request’s extensions.

## §Example

```
use tower_http::add_extension::AddExtensionLayer;
use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
use http::{Request, Response};
use bytes::Bytes;
use http_body_util::Full;
use std::{sync::Arc, convert::Infallible};

// Shared state across all request handlers --- in this case, a pool of database connections.
struct State {
    pool: DatabaseConnectionPool,
}

async fn handle(req: Request<Full<Bytes>>) -> Result<Response<Full<Bytes>>, Infallible> {
    // Grab the state from the request extensions.
    let state = req.extensions().get::<Arc<State>>().unwrap();

    Ok(Response::new(Full::default()))
}

// Construct the shared state.
let state = State {
    pool: DatabaseConnectionPool::new(),
};

let mut service = ServiceBuilder::new()
    // Share an `Arc<State>` with all requests.
    .layer(AddExtensionLayer::new(Arc::new(state)))
    .service_fn(handle);

// Call the service.
let response = service
    .ready()
    .await?
    .call(Request::new(Full::default()))
    .await?;
```

## Structs§

[AddExtension](struct.AddExtension.html)
Middleware for adding some shareable value to
[request extensions](https://docs.rs/http/latest/http/struct.Extensions.html)
.
[AddExtensionLayer](struct.AddExtensionLayer.html)
[Layer](https://docs.rs/tower-layer/0.3.3/x86_64-unknown-linux-gnu/tower_layer/trait.Layer.html)
for adding some shareable value to
[request extensions](https://docs.rs/http/latest/http/struct.Extensions.html)
.