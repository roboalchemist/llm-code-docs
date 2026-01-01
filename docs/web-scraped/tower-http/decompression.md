# Tower-HTTP Documentation
# Source: https://docs.rs/tower-http/latest/tower_http/decompression/
# Path: decompression/

[tower_http](../index.html)

# Module decompression Copy item path

[Source](../../src/tower_http/decompression/mod.rs.html#1-255)

Available on **crate features`decompression-br` or `decompression-deflate` or
`decompression-gzip` or `decompression-zstd`** only.

Expand description

Middleware that decompresses request and response bodies.

## §Examples

##### §Request

    
    
    use bytes::Bytes;
    use flate2::{write::GzEncoder, Compression};
    use http::{header, HeaderValue, Request, Response};
    use http_body_util::{Full, BodyExt};
    use std::{error::Error, io::Write};
    use tower::{Service, ServiceBuilder, service_fn, ServiceExt};
    use tower_http::{BoxError, decompression::{DecompressionBody, RequestDecompressionLayer}};
    
    // A request encoded with gzip coming from some HTTP client.
    let mut encoder = GzEncoder::new(Vec::new(), Compression::default());
    encoder.write_all(b"Hello?")?;
    let request = Request::builder()
        .header(header::CONTENT_ENCODING, "gzip")
        .body(Full::from(encoder.finish()?))?;
    
    // Our HTTP server
    let mut server = ServiceBuilder::new()
        // Automatically decompress request bodies.
        .layer(RequestDecompressionLayer::new())
        .service(service_fn(handler));
    
    // Send the request, with the gzip encoded body, to our server.
    let _response = server.ready().await?.call(request).await?;
    
    // Handler receives request whose body is decoded when read
    async fn handler(
        mut req: Request<DecompressionBody<Full<Bytes>>>,
    ) -> Result<Response<Full<Bytes>>, BoxError>{
        let data = req.into_body().collect().await?.to_bytes();
        assert_eq!(&data[..], b"Hello?");
        Ok(Response::new(Full::from("Hello, World!")))
    }

##### §Response

    
    
    use bytes::Bytes;
    use http::{Request, Response};
    use http_body_util::{Full, BodyExt};
    use std::convert::Infallible;
    use tower::{Service, ServiceExt, ServiceBuilder, service_fn};
    use tower_http::{compression::Compression, decompression::DecompressionLayer, BoxError};
    
    // Some opaque service that applies compression.
    let service = Compression::new(service_fn(handle));
    
    // Our HTTP client.
    let mut client = ServiceBuilder::new()
        // Automatically decompress response bodies.
        .layer(DecompressionLayer::new())
        .service(service);
    
    // Call the service.
    //
    // `DecompressionLayer` takes care of setting `Accept-Encoding`.
    let request = Request::new(Full::<Bytes>::default());
    
    let response = client
        .ready()
        .await?
        .call(request)
        .await?;
    
    // Read the body
    let body = response.into_body();
    let bytes = body.collect().await?.to_bytes().to_vec();
    let body = String::from_utf8(bytes).map_err(Into::<BoxError>::into)?;
    
    assert_eq!(body, "Hello, World!");

## Structs§

[Decompression](struct.Decompression.html "struct
tower_http::decompression::Decompression")

    Decompresses response bodies of the underlying service.
[DecompressionBody](struct.DecompressionBody.html "struct
tower_http::decompression::DecompressionBody")

    Response body of [`RequestDecompression`](struct.RequestDecompression.html "struct tower_http::decompression::RequestDecompression") and [`Decompression`](struct.Decompression.html "struct tower_http::decompression::Decompression").
[DecompressionLayer](struct.DecompressionLayer.html "struct
tower_http::decompression::DecompressionLayer")

    Decompresses response bodies of the underlying service.
[RequestDecompression](struct.RequestDecompression.html "struct
tower_http::decompression::RequestDecompression")

    Decompresses request bodies and calls its underlying service.
[RequestDecompressionFuture](struct.RequestDecompressionFuture.html "struct
tower_http::decompression::RequestDecompressionFuture")

    Response future of [`RequestDecompression`]
[RequestDecompressionLayer](struct.RequestDecompressionLayer.html "struct
tower_http::decompression::RequestDecompressionLayer")

    Decompresses request bodies and calls its underlying service.
[ResponseFuture](struct.ResponseFuture.html "struct
tower_http::decompression::ResponseFuture")

    Response future of [`Decompression`](struct.Decompression.html "struct tower_http::decompression::Decompression").

