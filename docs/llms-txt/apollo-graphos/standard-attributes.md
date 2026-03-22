# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/enabling-telemetry/standard-attributes.md

# OpenTelemetry standard attributes

[OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) define a set of **standard attributes** that can be attached to [spans](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/spans), [instruments](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/instruments) and [events](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/events). These attributes are used to filter and group data in your application performance monitor (APM).

The attributes available depend on the service of the router pipeline.

For example, set the standard attribute `http.response.status_code` on the router span:

```yaml title=router.yaml
telemetry:
  instrumentation:
    spans:
      router:
        attributes:
          # Standard attributes
          http.response.status_code: true
```

### Alias

If you don't want to use the standard name you can still create an alias and use that alias for the name, for example:

```yaml title=router.yaml
telemetry:
  instrumentation:
    spans:
      router:
        attributes:
          # Standard attributes
          http.response.status_code:
            alias: status_code # It will be named status_code instead of http.response.status_code
```

### Attribute configuration reference

A router's request lifecycle has three major services that support instrumentation:

* **Router service** - Operates within the context of an HTTP server, handling the opaque bytes of an incoming HTTP request. Does query analysis to parse the GraphQL operation and validate it against schema.
* **Supergraph service** - Handles a GraphQL request after it's been parsed and validated, and before it's sent to subgraphs. Runs the query planner to produce a query plan to execute.
* **Subgraph service** - Handles GraphQL subgraph requests that have been executed as part of a query plan. Creates HTTP client requests to subgraphs.

The router's **Execution service** that executes query plans doesn't support instrumentation.

Each service supports a unique set of standard attributes.

#### Router

Standard attributes of the `router` service:

| Attribute                   | Values | Description                                                                             |
| --------------------------- | ------ | --------------------------------------------------------------------------------------- |
| `error.type`                |        | Describes a class of error the operation ended with                                     |
| `http.request.body.size`    |        | The size of the request payload body in bytes                                           |
| `http.request.method`       |        | HTTP request method                                                                     |
| `http.response.body.size`   |        | The size of the response payload body in bytes                                          |
| `http.response.status_code` |        | HTTP response status code                                                               |
| `network.protocol.name`     |        | OSI application layer or non-OSI equivalent                                             |
| `network.protocol.version`  |        | Version of the protocol specified in network.protocol.name                              |
| `network.transport`         |        | OSI transport layer                                                                     |
| `network.type`              |        | OSI network layer or non-OSI equivalent                                                 |
| `user_agent.original`       |        | Value of the HTTP User-Agent header sent by the client                                  |
| `http.route`                |        | The matched route (path template in the format used by the respective server framework) |
| `network.local.address`     |        | Local socket address. Useful in case of a multi-IP host                                 |
| `network.local.port`        |        | Local socket port. Useful in case of a multi-port host                                  |
| `network.peer.address`      |        | Peer address of the network connection - IP address or Unix domain socket name          |
| `network.peer.port`         |        | Peer port number of the network connection                                              |
| `server.address`            |        | Name of the local HTTP server that received the request                                 |
| `server.port`               |        | Port of the local HTTP server that received the request                                 |
| `url.path`                  |        | The URI path component                                                                  |
| `url.query`                 |        | The URI query component                                                                 |
| `url.scheme`                |        | The scheme portion of the URL, such as "https" or "http"                                |

The `http.request.header.<key>` and `http.response.header.<key>` attributes are not available as standard attributes, but they can be configured using a custom attribute.

For example, to configure an attribute for `x-my-header` on `router` spans:

```yaml title=router.yaml
telemetry:
  instrumentation:
    spans:
      router:
        attributes:
          "http.request.header.x-my-header":
            request_header: "x-my-header"
```

#### Supergraph

Standard attributes of the `supergraph` service:

| Attribute                | Values                              | Description                                                                                                                                                                           |
| ------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `graphql.operation.name` |                                     | The operation name from the graphql query (need `spec_compliant` [mode](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/spans/#mode) to disable it) |
| `graphql.operation.type` | `query`\|`mutation`\|`subscription` | The operation kind from the subgraph query                                                                                                                                            |
| `graphql.document`       |                                     | The GraphQL query to the subgraph (need `spec_compliant` [mode](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/spans/#mode) to disable it)         |

OpenTelemetry vs Apollo recommendations: OpenTelemetry has experimental attributes in their [GraphQL semantic conventions](https://opentelemetry.io/docs/specs/semconv/graphql/graphql-spans/) that are currently in [Development status](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/#semantic-conventions-stability) and still evolving. Apollo does not have the same recommendations as the OpenTelemetry group and recommends using our "default" options instead.

Apollo does not recommend using the `graphql.document` attribute (marked as "Recommended" in OpenTelemetry's experimental conventions) due to significant risks:

* High cardinality: Each unique query creates a separate metric series, which can overwhelm your monitoring systems
* Security concerns: Operations may contain sensitive data in string literals that's difficult to sanitize
* Performance impact: Large operations (potentially megabytes) significantly increase telemetry overhead and storage costs

Use `graphql.operation.name` instead, which provides correlation capabilities with lower risk.

#### Subgraph

Standard attributes of the `subgraph` service:

| Attribute                         | Values                              | Description                                                                                                                                                                             |
| --------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subgraph.name`                   |                                     | The name of the subgraph (need `spec_compliant` [mode](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/spans/#mode) to disable it)                    |
| `subgraph.graphql.operation.name` |                                     | The operation name from the subgraph query  (need `spec_compliant` [mode](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/spans/#mode) to disable it) |
| `subgraph.graphql.operation.type` | `query`\|`mutation`\|`subscription` | The operation kind from the subgraph query                                                                                                                                              |
| `subgraph.graphql.document`       |                                     | The GraphQL query to the subgraph  (need `spec_compliant` [mode](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/spans/#mode) to disable it)          |
| `http.request.resend_count`       | `true`\|`false`                     | Number of retries for an http request to a subgraph                                                                                                                                     |

OpenTelemetry vs Apollo recommendations: The `subgraph.graphql.document` attribute has the same risks as the `graphql.document` attribute. While OpenTelemetry marks this as "Recommended" in their [experimental development-status semantic conventions](https://opentelemetry.io/docs/specs/semconv/graphql/graphql-spans/), Apollo does not recommend using this attribute due to high cardinality, potential sensitive data exposure, and performance impact.

#### Connector

Standard attributes of the `connector` service:

| Attribute                | Values | Description                                                      |
| ------------------------ | ------ | ---------------------------------------------------------------- |
| `subgraph.name`          |        | The name of the subgraph containing the connector                |
| `connector.source.name`  |        | The name of the `@source` associated with this connector, if any |
| `connector.http.method`  |        | The HTTP method for the connector (`GET` or `POST`, for example) |
| `connector.url.template` |        | The URL template for the connector                               |
