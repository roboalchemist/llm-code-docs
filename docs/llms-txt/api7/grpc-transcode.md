# Source: https://docs.api7.ai/hub/grpc-transcode.md

# grpc-transcode

The `grpc-transcode` plugin transforms between HTTP requests and gRPC requests, as well as their corresponding responses.

With this plugin enabled, APISIX accepts an HTTP request from the client, transcodes and forwards it to an upstream gRPC service. When APISIX receives the gRPC response, it will transform the response back to an HTTP response and send it to the client.

## Examples[â](#examples "Direct link to Examples")

The examples below demonstrate how you can configure the `grpc-transcode` plugin for different scenarios.

To follow along the examples, start an [example gRPC server](https://github.com/api7/grpc_server_example) in Docker:

```
docker run -d \
  --name grpc-example-server \
  -p 50051:50051 \
  api7/grpc-server-example:1.0.2
```

### Transform between HTTP and gRPC Requests[â](#transform-between-http-and-grpc-requests "Direct link to Transform between HTTP and gRPC Requests")

The following example demonstrates how to configure protobuf in APISIX and transform between HTTP and gRPC Requests using the `grpc-transcode` plugin.

Create a proto resource to store the protobuf:

```
curl "http://127.0.0.1:9180/apisix/admin/protos" -X PUT -d '
{
  "id": "echo-proto",
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

Create a route with the `grpc-transcode` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-transcode-route",
  "methods": ["GET"],
  "uri": "/echo",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "echo-proto",
      "service": "echo.EchoService",
      "method": "Echo"
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "grpc-example-server:50051": 1
    }
  }
}'
```

â¶ `proto_id`: ID of the proto object which defines gRPC services

â· `service`: gRPC service to interact with

â¸ `method`: gRPC method to use

To verify, send an HTTP request to the route with parameters defined in `EchoMsg`:

```
curl "http://127.0.0.1:9080/echo?msg=Hello"
```

You should receive the following response:

```
{"msg":"Hello"}
```

### Configure Protobuf with `.pb` File[â](#configure-protobuf-with-pb-file "Direct link to configure-protobuf-with-pb-file")

The following example demonstrates how to configure protobuf with `.pb` file in APISIX and transform between HTTP and gRPC Requests using the `grpc-transcode` plugin.

If your proto file contains imports, or if you want to combine multiple proto files, you can generate a `.pb` file using the [protoc](https://google.github.io/proto-lens/installing-protoc.html) utility and use it in APISIX, following the below steps.

Save the protocol buffer definition to a file called `echo.proto`:

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

Generate the `.pb` file with the [protoc](https://google.github.io/proto-lens/installing-protoc.html) utility and output it to a new file called `echo_proto.pb`:

```
protoc --include_imports --descriptor_set_out=echo_proto.pb echo.proto
```

Convert the `.pb` file from binary to base64 and configure it in APISIX:

```
curl "http://127.0.0.1:9180/apisix/admin/protos" -X PUT -d '
{
  "id": "echo-proto",
  "content" : "'"$(base64 -w0 /path/to/echo_proto.pb)"'"
}'
```

Create a route with the `grpc-transcode` plugin:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-transcode-route",
  "methods": ["GET"],
  "uri": "/echo",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "echo-proto",
      "service": "echo.EchoService",
      "method": "Echo"
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "grpc-example-server:50051": 1
    }
  }
}'
```

To verify, send an HTTP request to the route with parameters defined in `EchoMsg`:

```
curl "http://127.0.0.1:9080/echo?msg=Hello"
```

You should receive the following response:

```
{"msg":"Hello"}
```

### Display Error Details in Response Body[â](#display-error-details-in-response-body "Direct link to Display Error Details in Response Body")

The following example demonstrates how to configure the `grpc-transcode` plugin to include the `grpc-status-details-bin` field in the response header for error reporting, when made available by the gRPC server; and decode the message to be displayed in the response body.

Create a proto resource to store the protobuf:

```
curl "http://127.0.0.1:9180/apisix/admin/protos" -X PUT -d '
{
  "id": "hello-proto",
  "content": "syntax = \"proto3\";
  package helloworld;
  service Greeter {
    rpc GetErrResp (HelloRequest) returns (HelloReply) {}
  }
  message HelloRequest {
    string name = 1;
    repeated string items = 2;
  }
  message HelloReply {
    string message = 1;
    repeated string items = 2;
  }"
}'
```

Create a route with the `grpc-transform` plugin and set `show_status_in_body` to `true`:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-transcode-route",
  "uri": "/hello",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "hello-proto",
      "service": "helloworld.Greeter",
      "method": "GetErrResp",
      "show_status_in_body": true
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "grpc-example-server:50051": 1
    }
  }
}'
```

Send a request to the route:

```
curl -i "http://127.0.0.1:9080/hello?name=world"
```

You should see an error response similar to the following:

```
HTTP/1.1 503 Service Temporarily Unavailable
Date: Wed, 21 Feb 2024 03:08:30 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
grpc-status: 14
grpc-message: Out of service
grpc-status-details-bin: CA4SDk91dCBvZiBzZXJ2aWNlGlcKKnR5cGUuZ29vZ2xlYXBpcy5jb20vaGVsbG93b3JsZC5FcnJvckRldGFpbBIpCAESHFRoZSBzZXJ2ZXIgaXMgb3V0IG9mIHNlcnZpY2UaB3NlcnZpY2U
Server: APISIX/3.8.0

{"error":{"message":"Out of service","code":14,"details":[{"value":"\b\u0001\u0012\u001cThe server is out of service\u001a\u0007service","type_url":"type.googleapis.com/helloworld.ErrorDetail"}]}}
```

Note that certain information are not fully decoded in the error response message.

To decode the message, update the protobuf definition:

```
curl "http://127.0.0.1:9180/apisix/admin/protos" -X PUT -d '
{
  "id": "hello-proto",
  "content": "syntax = \"proto3\";
  package helloworld;
  service Greeter {
    rpc GetErrResp (HelloRequest) returns (HelloReply) {}
  }
  message HelloRequest {
    string name = 1;
    repeated string items = 2;
  }
  message HelloReply {
    string message = 1;
    repeated string items = 2;
  }
  message ErrorDetail {
    int64 code = 1;
    string message = 2;
    string type = 3;
  }"
}'
```

Configure the route with `grpc-transcode` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-transcode-route",
  "uri": "/hello",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "hello-proto",
      "service": "helloworld.Greeter",
      "method": "GetErrResp",
      "show_status_in_body": true,
      "status_detail_type": "helloworld.ErrorDetail"
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "grpc-example-server:50051": 1
    }
  }
}'
```

Send another request to the route:

```
curl -i "http://127.0.0.1:9080/hello?name=world"
```

You should see a response with error message fully decoded:

```
HTTP/1.1 503 Service Temporarily Unavailable
Date: Wed, 21 Feb 2024 03:11:43 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive
grpc-status: 14
grpc-message: Out of service
grpc-status-details-bin: CA4SDk91dCBvZiBzZXJ2aWNlGlcKKnR5cGUuZ29vZ2xlYXBpcy5jb20vaGVsbG93b3JsZC5FcnJvckRldGFpbBIpCAESHFRoZSBzZXJ2ZXIgaXMgb3V0IG9mIHNlcnZpY2UaB3NlcnZpY2U
Server: APISIX/3.8.0

{"error":{"message":"Out of service","code":14,"details":[{"message":"The server is out of service","code":1,"type":"service"}]}}
```

### Configure Encoder/Decoder Options[â](#configure-encoderdecoder-options "Direct link to Configure Encoder/Decoder Options")

The following example demonstrates how to configure encoder and decoder [options](https://github.com/starwing/lua-protobuf?tab=readme-ov-file#options) for the `grpc-transcode` plugin. Specifically, you will be applying the `int64_as_string` option to a method that performs addition operation and understand its effect.

Create a proto resource to store the protobuf:

```
curl "http://127.0.0.1:9180/apisix/admin/protos" -X PUT -d '
{
  "id": "plus-proto",
  "content": "syntax = \"proto3\";
  package helloworld;
  service Greeter {
    rpc Plus (PlusRequest) returns (PlusReply) {}
  }
  message PlusRequest {
    int64 a = 1;
    int64 b = 2;
  }
  message PlusReply {
    int64 result = 1;
  }"
}'
```

Configure the route with `grpc-transcode` plugin as such:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-transcode-route",
  "uri": "/plus",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "plus-proto",
      "service": "helloworld.Greeter",
      "method": "Plus"
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "grpc-example-server:50051": 1
    }
  }
}'
```

Send a request to the route:

```
curl "http://127.0.0.1:9080/plus?a=1237528374197491&b=1237528374197491"
```

You should see a response showing a sum of the two numbers:

```
{"result":2.475056748395e+15}
```

Update the route to use the `int64_as_string` option:

```
curl "http://127.0.0.1:9180/apisix/admin/routes" -X PUT -d '
{
  "id": "grpc-transcode-route",
  "uri": "/plus",
  "plugins": {
    "grpc-transcode": {
      "proto_id": "plus-proto",
      "service": "helloworld.Greeter",
      "method": "Plus",
      "pb_option":["int64_as_string"]
    }
  },
  "upstream": {
    "scheme": "grpc",
    "type": "roundrobin",
    "nodes": {
      "grpc-example-server:50051": 1
    }
  }
}'
```

Send another request to the route:

```
curl "http://127.0.0.1:9080/plus?a=1237528374197491&b=1237528374197491"
```

You should see a response showing a sum of the two numbers with better precision:

```
{"result":"#2475056748394982"}
```
