# Source: https://configcat.com/docs/advanced/proxy/grpc.md

# gRPC

Copy page

The ConfigCat Proxy can communicate over [gRPC](https://grpc.io), an open-source, high-performance RPC framework with client support in several languages.

To establish gRPC connections, you'll need the protobuf and the gRPC [service definition](https://github.com/configcat/configcat-proxy/blob/main/grpc/proto/flag_service.proto). It's required to generate clients with [`protoc`](https://protobuf.dev/downloads/) for your [desired platform](https://protobuf.dev/reference/).

flag\_service.proto

```protobuf
syntax = "proto3";

option go_package = "github.com/configcat/configcat-proxy/grpc/proto";

package configcat;

import "google/protobuf/empty.proto";
import "google/protobuf/timestamp.proto";

// Service that contains feature flag evaluation procedures.
service FlagService {
  // Stream for getting notified when a feature flag's value changes.
  rpc EvalFlagStream(EvalRequest) returns (stream EvalResponse) {}
  // Stream for getting notified when any feature flag's value changes.
  rpc EvalAllFlagsStream(EvalRequest) returns (stream EvalAllResponse) {}

  // Evaluates a feature flag.
  rpc EvalFlag(EvalRequest) returns (EvalResponse) {}
  // Evaluates each feature flag.
  rpc EvalAllFlags(EvalRequest) returns (EvalAllResponse) {}
  // Requests the keys of each feature flag.
  rpc GetKeys(KeysRequest) returns (KeysResponse) {}
  // Commands the underlying SDK to refresh its evaluation data.
  rpc Refresh(RefreshRequest) returns (google.protobuf.Empty) {}
}

// Feature flag evaluation request message.
message EvalRequest {
  // The SDK identifier. Deprecated, the field `target` should be used instead for SDK identification.
  string sdk_id = 1 [ deprecated = true ];
  // The feature flag's key to evaluate.
  string key = 2;
  // The user object.
  map<string, UserValue> user = 3;
  // The evaluation request's target.
  Target target = 4;
}

// Feature flag evaluation response message.
message EvalResponse {
  // The evaluated value.
  oneof value {
    int32 int_value = 1;
    double double_value = 2;
    string string_value = 3;
    bool bool_value = 4;
  }
  // The variation ID.
  string variation_id = 5;
}

// Response message that contains the evaluation result of each feature flag.
message EvalAllResponse {
  // The evaluated value of each feature flag.
  map<string, EvalResponse> values = 1;
}

// Request message for getting each available feature flag's key.
message KeysRequest {
  // The SDK identifier. Deprecated, the field `target` should be used instead for SDK identification.
  string sdk_id = 1 [ deprecated = true ];
  // The request's target.
  Target target = 2;
}

// Response message that contains each available feature flag's key.
message KeysResponse {
  // The keys of each feature flag.
  repeated string keys = 1;
}

// Request message for the given SDK to refresh its evaluation data.
message RefreshRequest {
  // The SDK identifier. Deprecated, the field `target` should be used instead for SDK identification.
  string sdk_id = 1 [ deprecated = true ];
  // The request's target.
  Target target = 2;
}

// Defines the possible values that can be set in the `user` map.
message UserValue {
  oneof value {
    double number_value = 1;
    string string_value = 2;
    google.protobuf.Timestamp time_value = 3;
    StringList string_list_value = 4;
  }
}

// Identifies the target of evaluation requests by either an SDK Id or an SDK Key.
message Target {
  oneof identifier {
    // The SDK Id.
    string sdk_id = 1;
    // The SDK key.
    string sdk_key = 2;
  }
}

// Represents a list of strings.
message StringList {
  repeated string values = 1;
}

```

info

In order to secure the gRPC communication with the Proxy, set up [TLS](https://configcat.com/docs/advanced/proxy/proxy-overview.md#tls).

## Client Usage[​](#client-usage "Direct link to Client Usage")

The following example uses a generated Go client, but gRPC clients generated for other languages are working as well.

example.go

```go
conn, err := grpc.NewClient("localhost:50051",
    grpc.WithTransportCredentials(credentials.NewTLS(&tls.Config{
      // Any TLS options
    })))
if err != nil {
    panic(err)
}

defer func() {
    _ = conn.Close()
}()

client := proto.NewFlagServiceClient(conn)

ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

resp, err := client.EvalFlag(ctx, &proto.EvalRequest{
    Target: &proto.Target{Identifier: &proto.Target_SdkKey{SdkKey: "#YOUR-SDK-KEY#"}},
    // Or with SDK identifier
    // Target: &proto.Target{Identifier: &proto.Target_SdkId{SdkId: "#SDK-IDENTIFIER#"}},
    Key: "<flag-key>",
    User: map[string]*proto.UserValue{"Identifier": {Value: &proto.UserValue_StringValue{StringValue: "<user-id>"}}},
})
if err != nil {
    panic(err)
}

fmt.Printf("Evaluation result: %v", resp.GetBoolValue())

```

## Health Check[​](#health-check "Direct link to Health Check")

The Proxy exposes health information over a [standardized health RPC service](https://github.com/grpc/grpc-proto/blob/master/grpc/health/v1/health.proto).

Clients can set `""` as the `service` parameter (or skip specifying it) to get the health status of the gRPC server. Exposing the health check service is configurable and turned on by default.

For more details about gRPC health checking, check out the [official documentation](https://grpc.io/docs/guides/health-checking/).

## Server Reflection[​](#server-reflection "Direct link to Server Reflection")

The Proxy can expose its protobuf-defined feature flag evaluation API over a [standardized reflection RPC service](https://github.com/grpc/grpc-proto/blob/master/grpc/reflection/v1/reflection.proto), including all types referenced by the request and response messages. Exposing the reflection service is configurable and turned off by default.

For more details about gRPC server reflection, check out the [official documentation](https://grpc.io/docs/guides/reflection/).

## Available Options[​](#available-options "Direct link to Available Options")

The following gRPC related options are available:

* YAML
* Environment variables

options.yml

```yaml
grpc:
  enabled: <true|false>
  port: 50051
  server_reflection_enabled: <true|false>
  health_check_enabled: <true|false>
  keep_alive:
    max_connection_idle: 15
    max_connection_age: 30
    max_connection_age_grace: 5
    time: 5
    timeout: 1
  log:
    level: "<error|warn|info|debug>"

```

```shell
CONFIGCAT_GRPC_ENABLED=<true|false>
CONFIGCAT_GRPC_PORT=50051
CONFIGCAT_GRPC_HEALTH_CHECK_ENABLED=<true|false>
CONFIGCAT_GRPC_SERVER_REFLECTION_ENABLED=<true|false>
CONFIGCAT_GRPC_KEEP_ALIVE_MAX_CONNECTION_IDLE=15
CONFIGCAT_GRPC_KEEP_ALIVE_MAX_CONNECTION_AGE=30
CONFIGCAT_GRPC_KEEP_ALIVE_MAX_CONNECTION_AGE_GRACE=5
CONFIGCAT_GRPC_KEEP_ALIVE_TIME=5
CONFIGCAT_GRPC_KEEP_ALIVE_TIMEOUT=1
CONFIGCAT_GRPC_LOG_LEVEL="<error|warn|info|debug>"

```

Here's the explanation for each option:

| Option                                                                                                                                                       | Default              | Description                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - YAML<br />- Environment variable```yaml
grpc:
  enabled: <true|false>

``````shell
CONFIGCAT_GRPC_ENABLED=<true|false>

```                                       | `true`               | Turns the ability to communicate with the Proxy through gRPC on/off.                                                                                                                                                               |
| - YAML<br />- Environment variable```yaml
grpc:
  port: 50051

``````shell
CONFIGCAT_GRPC_PORT=50051

```                                                           | `50051`              | The port used for gRPC communication.                                                                                                                                                                                              |
| - YAML<br />- Environment variable```yaml
grpc:
  health_check_enabled: <true|false>

``````shell
CONFIGCAT_GRPC_HEALTH_CHECK_ENABLED=<true|false>

```             | `true`               | Turns the [gRPC health check service](https://grpc.io/docs/guides/health-checking/) on/off.                                                                                                                                        |
| - YAML<br />- Environment variable```yaml
grpc:
  server_reflection_enabled: <true|false>

``````shell
CONFIGCAT_GRPC_SERVER_REFLECTION_ENABLED=<true|false>

```   | `false`              | Turns the [gRPC server reflection](https://grpc.io/docs/guides/reflection/) on/off.                                                                                                                                                |
| - YAML<br />- Environment variable```yaml
grpc:
  keep_alive:
    max_connection_idle: 15

``````shell
CONFIGCAT_GRPC_KEEP_ALIVE_MAX_CONNECTION_IDLE=15

```         | `INT_MAX (Infinite)` | Maximum time in seconds that a channel may have no outstanding rpcs, after which the server will close the connection. [More about the gRPC keep-alive](https://grpc.io/docs/guides/keepalive/).                                   |
| - YAML<br />- Environment variable```yaml
grpc:
  keep_alive:
    max_connection_age: 30

``````shell
CONFIGCAT_GRPC_KEEP_ALIVE_MAX_CONNECTION_AGE=30

```           | `INT_MAX (Infinite)` | Maximum time in seconds that a channel may exist. [More about the gRPC keep-alive](https://grpc.io/docs/guides/keepalive/).                                                                                                        |
| - YAML<br />- Environment variable```yaml
grpc:
  keep_alive:
    max_connection_age_grace: 5

``````shell
CONFIGCAT_GRPC_KEEP_ALIVE_MAX_CONNECTION_AGE_GRACE=5

``` | `INT_MAX (Infinite)` | Grace period in seconds after the channel reaches its max age. [More about the gRPC keep-alive](https://grpc.io/docs/guides/keepalive/).                                                                                           |
| - YAML<br />- Environment variable```yaml
grpc:
  keep_alive:
    time: 5

``````shell
CONFIGCAT_GRPC_KEEP_ALIVE_TIME=5

```                                         | `7200`               | The interval in seconds between PING frames. [More about the gRPC keep-alive](https://grpc.io/docs/guides/keepalive/).                                                                                                             |
| - YAML<br />- Environment variable```yaml
grpc:
  keep_alive:
    timeout: 1

``````shell
CONFIGCAT_GRPC_KEEP_ALIVE_TIMEOUT=1

```                                   | `20`                 | The timeout in seconds for a PING frame to be acknowledged. If sender does not receive an acknowledgment within this time, it will close the connection. [More about the gRPC keep-alive](https://grpc.io/docs/guides/keepalive/). |
| - YAML<br />- Environment variable```yaml
grpc:
  log:
    level: "<error|warn|info|debug>"

``````shell
CONFIGCAT_GRPC_LOG_LEVEL="<error|warn|info|debug>"

```     | `warn`               | The verbosity of the gRPC related logs.<br />Possible values: `error`, `warn`, `info` or `debug`.<br />When `debug` is set, the Proxy will log each RPC with additional details.                                                   |
