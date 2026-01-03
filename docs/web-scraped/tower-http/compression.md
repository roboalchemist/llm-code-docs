# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/compression/
# Path: compression/

[tower_http](../index.html)

# Module compression Copy item path

[Source](../../src/tower_http/compression/mod.rs.html#1-511)

Available on **crate features`compression-br` or `compression-deflate` or
`compression-gzip` or `compression-zstd`** only.

Expand description

Middleware that compresses response bodies.

## §Example

Example showing how to respond with the compressed contents of a file.

    
    
    use bytes::{Bytes, BytesMut};
    use http::{Request, Response, header::ACCEPT_ENCODING};
    use http_body_util::{Full, BodyExt, StreamBody, combinators::UnsyncBoxBody};
    use http_body::Frame;
    use std::convert::Infallible;
    use tokio::fs::{self, File};
    use tokio_util::io::ReaderStream;
    use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
    use tower_http::{compression::CompressionLayer, BoxError};
    use futures_util::TryStreamExt;
    
    type BoxBody = UnsyncBoxBody<Bytes, std::io::Error>;
    
    async fn handle(req: Request<Full<Bytes>>) -> Result<Response<BoxBody>, Infallible> {
        // Open the file.
        let file = File::open("Cargo.toml").await.expect("file missing");
        // Convert the file into a `Stream` of `Bytes`.
        let stream = ReaderStream::new(file);
        // Convert the stream into a stream of data `Frame`s.
        let stream = stream.map_ok(Frame::data);
        // Convert the `Stream` into a `Body`.
        let body = StreamBody::new(stream);
        // Erase the type because its very hard to name in the function signature.
        let body = body.boxed_unsync();
        // Create response.
        Ok(Response::new(body))
    }
    
    let mut service = ServiceBuilder::new()
        // Compress responses based on the `Accept-Encoding` header.
        .layer(CompressionLayer::new())
        .service_fn(handle);
    
    // Call the service.
    let request = Request::builder()
        .header(ACCEPT_ENCODING, "gzip")
        .body(Full::<Bytes>::default())?;
    
    let response = service
        .ready()
        .await?
        .call(request)
        .await?;
    
    assert_eq!(response.headers()["content-encoding"], "gzip");
    
    // Read the body
    let bytes = response
        .into_body()
        .collect()
        .await?
        .to_bytes();
    
    // The compressed body should be smaller 🤞
    let uncompressed_len = fs::read_to_string("Cargo.toml").await?.len();
    assert!(bytes.len() < uncompressed_len);

## Modules§

[predicate](predicate/index.html "mod tower_http::compression::predicate")

    Predicates for disabling compression of responses.

## Structs§

[Compression](struct.Compression.html "struct
tower_http::compression::Compression")

    Compress response bodies of the underlying service.
[CompressionBody](struct.CompressionBody.html "struct
tower_http::compression::CompressionBody")

    Response body of [`Compression`](struct.Compression.html "struct tower_http::compression::Compression").
[CompressionLayer](struct.CompressionLayer.html "struct
tower_http::compression::CompressionLayer")

    Compress response bodies of the underlying service.
[DefaultPredicate](struct.DefaultPredicate.html "struct
tower_http::compression::DefaultPredicate")

    The default predicate used by [`Compression`](struct.Compression.html "struct tower_http::compression::Compression") and [`CompressionLayer`](struct.CompressionLayer.html "struct tower_http::compression::CompressionLayer").
[ResponseFuture](struct.ResponseFuture.html "struct
tower_http::compression::ResponseFuture")

    Response future of [`Compression`](struct.Compression.html "struct tower_http::compression::Compression").

## Enums§

[CompressionLevel](enum.CompressionLevel.html "enum
tower_http::compression::CompressionLevel")

    Level of compression data should be compressed with.

## Traits§

[Predicate](trait.Predicate.html "trait tower_http::compression::Predicate")

    Predicate used to determine if a response should be compressed or not.

