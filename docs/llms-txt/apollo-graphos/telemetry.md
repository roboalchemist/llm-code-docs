# Source: https://www.apollographql.com/docs/apollo-operator/configuration/telemetry.md

# Source: https://www.apollographql.com/docs/apollo-mcp-server/telemetry.md

# Source: https://www.apollographql.com/docs/graphos/connectors/observability/telemetry.md

# Connector Telemetry Configuration

Connector telemetry provides visibility into how your graph is interacting with your REST APIs.
Telemetry helps you monitor performance metrics, detect issues early, and gain insights into API behavior patterns.

You configure telemetry via your router. This page lists telemetry attributes, instruments, and events available for Connectors.
Refer to the [router telemetry docs](https://www.apollographql.com/docs/router/configuration/telemetry/overview) for both a telemetry overview and details.
See the Connector troubleshooting guide's [debugging section](https://www.apollographql.com/docs/graphos/schema-design/connectors/troubleshooting#adding-debug-information-to-telemetry) for information on how to add debug information to telemetry.

## Attributes

Attributes can be attached to telemetry such as [instruments](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry.md#instruments) and [events](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry.md#events). These attributes are used to filter and group data in your application performance monitor (APM).

The following standard attributes are available for Connectors:

| Attribute                | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `subgraph.name`          | The name of the subgraph containing the Connector                |
| `connector.source.name`  | The name of the `@source` associated with this Connector, if any |
| `connector.http.method`  | The HTTP method for the Connector (`GET` or `POST`, for example) |
| `connector.url.template` | The URL template for the Connector                               |

### Selectors

A *selector* is used to extract data from Connectors requests and responses and attach the data to telemetry such as [instruments](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry.md#instruments) and [events](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry.md#events).

Apollo Connectors for REST APIs make HTTP calls to the upstream HTTP API. The selectors in the following table let you extract metrics from these HTTP requests and responses.

| Selector                              | Defaultable | Values              | Description                                                       |
| ------------------------------------- | ----------- | ------------------- | ----------------------------------------------------------------- |
| `subgraph_name`                       | No          | `true`\|`false`     | The name of the subgraph containing the Connector                 |
| `connector_source `                   | No          | `name`              | The name of the `@source` associated with this Connector, if any  |
| `connector_http_request_header`       | Yes         |                     | The name of a Connector request header                            |
| `connector_http_response_header`      | Yes         |                     | The name of a Connector response header                           |
| `connector_http_response_status`      | No          | `code`\|`reason`    | The status of a Connector response                                |
| `connector_http_method`               | No          | `true`\|`false`     | The HTTP method of a Connector request                            |
| `connector_url_template`              | No          | `true`\|`false`     | The URL template of a Connector request                           |
| `connector_request_mapping_problems`  | No          | `problems`\|`count` | Any mapping problems with the Connector request                   |
| `connector_response_mapping_problems` | No          | `problems`\|`count` | Any mapping problems with the Connector response                  |
| `static`                              | No          |                     | A static string value                                             |
| `error`                               | No          | `reason`            | A string value containing error reason when it's a critical error |

## Instruments

An *instrument* in the router collects data and reports measurements to a metric backend. Supported instruments include standard instruments from OpenTelemetry, standard instruments for the router request lifecycle, and custom instruments. Supported instrument kinds are counters and histograms.

You can configure instruments in `router.yaml` with `telemetry.instrumentation.instruments`.

### OpenTelemetry standard instruments

OpenTelemetry specifies multiple [standard metric instruments](https://opentelemetry.io/docs/specs/semconv/http/http-metrics/) that are available for Connectors HTTP requests and responses:

* `http.client.request.body.size` - A histogram of request body sizes for Connectors HTTP requests.
* `http.client.request.duration` - A histogram of request durations for Connectors HTTP requests.
* `http.client.response.body.size` - A histogram of response body sizes for Connectors HTTP responses.

These instruments are configurable in `router.yaml`:

```yaml title=router.yaml
telemetry:
  instrumentation:
    instruments:
      connector:
        http.client.request.body.size: true
        http.client.request.duration: true
        http.client.response.body.size: true
```

The [`default_requirement_level` setting](https://www.apollographql.com/docs/graphos/reference/router/telemetry/instrumentation/instruments#default_requirement_level) configures whether or not these instruments are enabled by default. They can be customized by attaching or removing attributes. See [attributes](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry.md#attributes) to learn more about configuring attributes.

```yaml title=router.yaml
telemetry:
  instrumentation:
    instruments:
      connector:
        http.client.request.duration:
          attributes:
            connector.source.name: true
```

### Custom instruments

You can define custom instruments on Connectors HTTP requests and responses.

For example, the following custom instrument provides the number of 404 response statuses from a specific REST API:

```yaml title=router.yaml
telemetry:
  instrumentation:
    instruments:
      connector:
        acme.user.not.found:
          value: unit
          type: counter
          unit: count
          description: "Count of 404 responses from the user API"
          condition:
            all:
              - eq:
                  - 404
                  - connector_http_response_status: code
              - eq:
                  - "user_api"
                  - connector_source: name
```

See the [router documentation](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/instruments#instrument-configuration) for more details about configuring instruments.

## Events

An *event* is used to signal when something of note happens, such as a Connector request or response.

You can configure events for each service in `router.yaml`. Events can be standard or custom, and they can be triggered by configurable conditions.

See the [router documentation](https://www.apollographql.com/docs/router/configuration/telemetry/instrumentation/events#event-configuration) for more details about configuring events.

### Standard events

Standard events can be configured for Connectors. The following enables standard Connector HTTP response events at the `INFO` level:

```yaml title=router.yaml
events:
  connector:
    request: off
    response: info
    error: error
```

### Custom events

Custom events can also be configured for Connectors. The following example defines a custom event for each Connector HTTP response at the `INFO` level:

```yaml title=router.yaml
events:
  connector:
    connector.response:
      message: "Connector response"
      level: info
      on: response
      attributes:
        connector.http.method: true
        connector.url.template: true
        response_status:
          connector_http_response_status: code
```

If you have a `stdout` logging exporter, the router logs each Connector response with the attributes defined above:

```text
INFO  connector.http.method=GET connector.url.template=/users response_status=200 Connector response kind=connector.response
INFO  connector.http.method=GET connector.url.template=/users/{$this.id}/posts response_status=200 Connector response kind=connector.response
```
