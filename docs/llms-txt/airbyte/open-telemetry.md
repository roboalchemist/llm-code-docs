# Source: https://docs.airbyte.com/platform/operator-guides/open-telemetry.md

# Source: https://docs.airbyte.com/platform/2.0/operator-guides/open-telemetry.md

# Source: https://docs.airbyte.com/platform/1.8/operator-guides/open-telemetry.md

# OpenTelemetry metrics monitoring

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte Self-Managed Enterprise generates a number of crucial metrics about syncs and volumes of data moved. You can configure Airbyte to send telemetry data to an OpenTelemetry collector endpoint so you can consume these metrics in your downstream monitoring tool of choice. Airbyte doesn't send traces and logs.

Airbyte sends specific metrics to provide you with health insight in the following areas.

* Resource provisioning: Monitor API requests and sync attempts to ensure your deployment has adequate resources

* Sync performance: Track sync duration and data volume moved to understand performance

* System health: Monitor sync status and completion rates to ensure system stability

## Example dashboard[​](#example-dashboard "Direct link to Example dashboard")

Here's an example of a dashboard in Datadog using Airbyte's OpenTelemetry metrics.

![Airbyte OpenTelemetry metrics in a dashboard in Datadog](/assets/images/otel-datadog-05b23789efcab487ffcf2945786c779a.png)

## Configure OpenTelemetry metrics[​](#configure-opentelemetry-metrics "Direct link to Configure OpenTelemetry metrics")

1. Deploy an OpenTelemetry Collector if you don't already have one. See the [OpenTelemetry documentation](https://opentelemetry.io/docs/collector/getting-started/#kubernetes) for help doing this. If you use Datadog as your monitoring tool, they have an in-depth guide to [set up a Datadog Collector and Exporter](https://docs.datadoghq.com/opentelemetry/collector_exporter/).

   1. For Airbyte to send metrics to your server, your OpenTelemetry service (collector or otherwise) must accept OpenTelemetry Protocol (OTLP) over HTTP. If you use an OpenTelemetry Collector, your configuration would need to include some variation of the below to accept OTLP over HTTP:

   ```
   receivers:
     otlp:
       protocols:
         http:
           endpoint: 0.0.0.0:4318
   ```

2. Update Airbyte's `values.yaml` file to enable OpenTelemetry.

   values.yaml

   ```
   global:
       edition: enterprise # This is an enterprise-only feature
       metrics:
           enabled: true
           otlp:
               enabled: true
               # The OpenTelemetry Collector endpoint Airbyte sends metrics to. You configure this endpoint outside of Airbyte as part of your OpenTelemetry deployment
               # This endpoint also needs to end in the metrics ingestion endpoint. For OpenTelemetry Collector users, this is /v1/metrics.
               # e.g. http://localhost:4318/v1/metrics
               collectorEndpoint: "YOUR_ENDPOINT" 
   ```

3. Redeploy Airbyte with the updated values.

Airbyte sends metrics to the collector you specified in your configuration.

## Available metrics[​](#available-metrics "Direct link to Available metrics")

The following metrics are available. They're published every minute.

| Metric                  | Tag                        | Example Value                        |
| ----------------------- | -------------------------- | ------------------------------------ |
| `airbyte.syncs`         | `connection_id`            | 653a067e-cd0b-4cab-96b5-5e5cb03f159b |
|                         | `workspace_id`             | bed3b473-1518-4461-a37f-730ea3d3a848 |
|                         | `job_id`                   | 23642492                             |
|                         | `status`                   | success, failed                      |
|                         | `attempt_count`            | 3                                    |
|                         | `source_connector_id`      | 82c7fb2d-7de1-4d4e-b12e-510b0d61e374 |
|                         | `destination_connector_id` | 3cb42982-755b-4644-9ed4-19651b53ebdd |
|                         | `version`                  | 1.5.0                                |
|                         | `service`                  | airbyte-worker                       |
| `airbyte.gb_moved`      | `connection_id`            | 653a067e-cd0b-4cab-96b5-5e5cb03f159b |
|                         | `workspace_id`             | bed3b473-1518-4461-a37f-730ea3d3a848 |
|                         | `job_id`                   | 23642492                             |
|                         | `source_connector_id`      | 82c7fb2d-7de1-4d4e-b12e-510b0d61e374 |
|                         | `destination_connector_id` | 3cb42982-755b-4644-9ed4-19651b53ebdd |
|                         | `version`                  | 1.5.0                                |
|                         | `service`                  | airbyte-worker                       |
| `airbyte.sync_duration` | `connection_id`            | 653a067e-cd0b-4cab-96b5-5e5cb03f159b |
|                         | `workspace_id`             | bed3b473-1518-4461-a37f-730ea3d3a848 |
|                         | `job_id`                   | 23642492                             |
|                         | `source_connector_id`      | 82c7fb2d-7de1-4d4e-b12e-510b0d61e374 |
|                         | `destination_connector_id` | 3cb42982-755b-4644-9ed4-19651b53ebdd |
|                         | `version`                  | 1.5.0                                |
|                         | `service`                  | airbyte-worker                       |
| `airbyte.api_requests`  | `uri`                      | /v1/applications/create              |
|                         | `status`                   | 200                                  |
|                         | `exception`                | NullPointerException                 |
|                         | `method`                   | GET, POST                            |
|                         | `version`                  | 1.5.0                                |
|                         | `service`                  | airbyte-server                       |
