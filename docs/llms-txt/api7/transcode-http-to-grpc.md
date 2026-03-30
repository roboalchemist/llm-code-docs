# Source: https://docs.api7.ai/apisix/how-to-guide/transformation/transcode-http-to-grpc.md

# Transcode HTTP to gRPC

[gRPC](https://grpc.io/) is an open-source high-performance Remote Procedure Call (RPC) framework based on HTTP/2 protocol. It uses [protocol buffers (protobuf)](https://protobuf.dev/) as the interface description language (IDL).

This guide will show you how to use the `grpc-transcode` plugin with the [proto object](https://docs.api7.ai/apisix/key-concepts/protos.md) to transform between RESTful HTTP requests and gRPC requests, as well as their corresponding responses.

<br />

![REST to gRPC Diagram](https://static.api7.ai/uploads/2023/05/06/omYvTUSm_transform-grpc.jpg)

<br />

note

Ingress Controller currently does not support proto resource.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to APISIX for validation.
* Install [gRPCurl](https://github.com/fullstorydev/grpcurl) to send requests to gRPC services for validation.
* Follow the [Getting Started tutorial](https://docs.api7.ai/apisix/getting-started/.md) to start a new APISIX instance in Docker.

## Deploy an Example gRPC Server[â](#deploy-an-example-grpc-server "Direct link to Deploy an Example gRPC Server")

Start an [example gRPC server](https://github.com/api7/grpc_server_example) Docker instance `quickstart-grpc-example` on port `50051`:

```
docker run -d \
  --name quickstart-grpc-example \
  --network=apisix-quickstart-net \
  -p 50051:50051 \
  api7/grpc-server-example:1.0.2
```

This example gRPC server holds several services, such as `echo.EchoService`:

echo.proto

```
syntax = "proto3";

package echo;

service EchoService {
  rpc Echo (EchoMsg) returns (EchoMsg);
}

message EchoMsg {
  string msg = 1;
}
```

In this example, `Echo` is a method in `EchoService` that accepts a parameter of type `EchoMsg`.

Test the gRPC method `echo.EchoService.Echo` using gRPCurl:

```
grpcurl -plaintext -d '{"msg": "Hello"}' "127.0.0.1:50051" "echo.EchoService/Echo"
```

A response similar to the following verifies that the gRPC service is working:

```
{
  "msg": "Hello"
}
```

## Create a Proto Object to Store Protobuf File[â](#create-a-proto-object-to-store-protobuf-file "Direct link to Create a Proto Object to Store Protobuf File")

Store the protobuf file `echo.proto` as a proto object in APISIX with the ID `quickstart-proto`:

```
curl -i "http://127.0.0.1:9180/apisix/admin/protos" -X PUT -d '
{
  "id": "quickstart-proto",
  "content": "syntax = \"proto3\";

  package echo;

  service EchoService {
    rpc Echo (EchoMsg) returns (EchoMsg);
  }

  message EchoMsg {
    string msg = 1;
  }"
}'
```

An `HTTP/1.1 201 Created` response verifies that the proto object is created successfully.

## Enable `grpc-transcode` Plugin[â](#enable-grpc-transcode-plugin "Direct link to enable-grpc-transcode-plugin")

Create a route with ID `quickstart-grpc` and enable the plugin `grpc-transcode`:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "quickstart-grpc",
  "methods": ["GET"],
  "uri": "/echo",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "quickstart-proto",
      "service": "echo.EchoService",
      "method": "Echo"
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "quickstart-grpc-example:50051": 1
    }
  }
}'
```

â¶ `proto_id`: the proto object which defines gRPC services

â· `service`: gRPC service `echo.EchoService` in use

â¸ `method`: gRPC method `Echo` in use

An `HTTP/1.1 201 Created` response verifies that the route is created and the plugin `grpc-transcode` is enabled successfully.

APISIX now transcodes the RESTful HTTP requests received at `/echo` route to gRPC requests and forwards them to the upstream gRPC server `quickstart-grpc-example` to invoke the method `echo.EchoService/Echo`. Once the gRPC server responds, APISIX transcodes the gRPC responses back to RESTful HTTP responses for clients.

## Test gRPC Services in a RESTful Way[â](#test-grpc-services-in-a-restful-way "Direct link to Test gRPC Services in a RESTful Way")

Send an HTTP request to `/echo` with parameters defined in `EchoMsg`:

```
curl -i "http://127.0.0.1:9080/echo?msg=Hello"
```

A valid response similar to the following verifies that the plugin `grpc-transcode` works:

```
{"msg":"Hello"}
```

## Next Steps[â](#next-steps "Direct link to Next Steps")

See the `grpc-transcode` [plugin doc](https://docs.api7.ai/hub/grpc-transcode.md) for more configuration options and examples.

In addition to transcoding HTTP requests to gRPC requests, APISIX also supports [gRPC-Web](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md), a variation of the [native gRPC protocol](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md), with the APISIX plugin `grpc-web`.
