# Source: https://www.apollographql.com/docs/graphos/connectors/requests/grpc-json-bridge.md

# Connecting gRPC services using a JSON Bridge

[gRPC](https://grpc.io/) is a high-performance, language-agnostic Remote Procedure Call (RPC) framework for building APIs.
Apollo Connectors can communicate with gRPC services through a gRPC-to-JSON bridge that handles protocol conversion.

## gRPC-JSON transcoding

gRPC-JSON transcoding allows HTTP clients to send JSON/HTTP requests that are transparently mapped to gRPC method calls. It handles:

* Calling gRPC methods with an HTTP POST request to a path like `/com.example.ProductService/GetProduct`
* Converting JSON request bodies to Protocol Buffer request messages
* Converting Protocol Buffers response messages to JSON

### Transcoding solutions

Several tools support gRPC-JSON transcoding:

* **[Envoy Proxy](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/grpc_json_transcoder_filter)**: An open-source proxy with built-in support via the `grpc_json_transcoder` HTTP filter.
* **[Google Cloud Endpoints](https://cloud.google.com/endpoints/docs/grpc/transcoding)**: A managed solution using ESP (Extensible Service Proxy).
* **Custom gRPC gateways**: You can build one using libraries like [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) (for Go) or your own logic.

## Connecting transcoded gRPC APIs

After setting up your gRPC JSON bridge, you can call it using Connectors just like any other HTTP API:

```graphql
type Query {
  product(id: ID!): Product
    @connect(
      source: "productService"
      http: {
        POST: "/com.example.ProductService/GetProduct"
        body: "productId: $args.id"
      }
      selection: """
        sku
        title
        description
      """
    )
}
```

## Limitations

When using gRPC-JSON transcoding, there's an important limitation to keep in mind:
**Field names become part of your public API.** Unlike regular gRPC clients that use field numbers for encoding—allowing you to change field names safely—JSON bridges rely directly on field names. This means you cannot change field names in your protobuf definitions without breaking existing clients that consume the JSON API.
