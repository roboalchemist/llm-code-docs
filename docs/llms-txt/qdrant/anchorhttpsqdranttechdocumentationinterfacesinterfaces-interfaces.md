# [Anchor](https://qdrant.tech/documentation/interfaces/\#interfaces) Interfaces

Qdrant supports these “official” clients.

> **Note:** If you are using a language that is not listed here, you can use the REST API directly or generate a client for your language
> using [OpenAPI](https://github.com/qdrant/qdrant/blob/master/docs/redoc/master/openapi.json)
> or [protobuf](https://github.com/qdrant/qdrant/tree/master/lib/api/src/grpc/proto) definitions.

## [Anchor](https://qdrant.tech/documentation/interfaces/\#client-libraries) Client Libraries

|  | Client Repository | Installation | Version |
| --- | --- | --- | --- |
| [![python](https://qdrant.tech/docs/misc/python.webp)](https://python-client.qdrant.tech/) | **[Python](https://github.com/qdrant/qdrant-client)** \+ **[(Client Docs)](https://python-client.qdrant.tech/)** | `pip install qdrant-client[fastembed]` | [Latest Release](https://github.com/qdrant/qdrant-client/releases) |
| ![typescript](https://qdrant.tech/docs/misc/ts.webp) | **[JavaScript / Typescript](https://github.com/qdrant/qdrant-js)** | `npm install @qdrant/js-client-rest` | [Latest Release](https://github.com/qdrant/qdrant-js/releases) |
| ![rust](https://qdrant.tech/docs/misc/rust.png) | **[Rust](https://github.com/qdrant/rust-client)** | `cargo add qdrant-client` | [Latest Release](https://github.com/qdrant/rust-client/releases) |
| ![golang](https://qdrant.tech/docs/misc/go.webp) | **[Go](https://github.com/qdrant/go-client)** | `go get github.com/qdrant/go-client` | [Latest Release](https://github.com/qdrant/go-client/releases) |
| ![.net](https://qdrant.tech/docs/misc/dotnet.webp) | **[.NET](https://github.com/qdrant/qdrant-dotnet)** | `dotnet add package Qdrant.Client` | [Latest Release](https://github.com/qdrant/qdrant-dotnet/releases) |
| ![java](https://qdrant.tech/docs/misc/java.webp) | **[Java](https://github.com/qdrant/java-client)** | [Available on Maven Central](https://central.sonatype.com/artifact/io.qdrant/client) | [Latest Release](https://github.com/qdrant/java-client/releases) |

## [Anchor](https://qdrant.tech/documentation/interfaces/\#api-reference) API Reference

All interaction with Qdrant takes place via the REST API. We recommend using REST API if you are using Qdrant for the first time or if you are working on a prototype.

| API | Documentation |
| --- | --- |
| REST API | [OpenAPI Specification](https://api.qdrant.tech/api-reference) |
| gRPC API | [gRPC Documentation](https://github.com/qdrant/qdrant/blob/master/docs/grpc/docs.md) |

### [Anchor](https://qdrant.tech/documentation/interfaces/\#grpc-interface) gRPC Interface

The gRPC methods follow the same principles as REST. For each REST endpoint, there is a corresponding gRPC method.

As per the [configuration file](https://github.com/qdrant/qdrant/blob/master/config/config.yaml), the gRPC interface is available on the specified port.

```yaml
service:
  grpc_port: 6334

```

Running the service inside of Docker will look like this:

```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant

```

**When to use gRPC:** The choice between gRPC and the REST API is a trade-off between convenience and speed. gRPC is a binary protocol and can be more challenging to debug. We recommend using gRPC if you are already familiar with Qdrant and are trying to optimize the performance of your application.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/interfaces.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/interfaces.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-9-lllmstxt|>
## single-node-speed-benchmark-2022