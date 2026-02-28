# Source: https://docs.datadoghq.com/tracing/troubleshooting.md

---
title: APM Troubleshooting
description: >-
  Comprehensive troubleshooting guide for APM issues including trace retention,
  service configuration, and connection errors.
breadcrumbs: Docs > APM > APM Troubleshooting
---

If you experience unexpected behavior while using Datadog APM, read the information on this page to help resolve the issue. Datadog recommends regularly updating to the latest version of the Datadog tracing libraries you use, as each release contains improvements and fixes. If you continue to experience issues, reach out to [Datadog support](https://docs.datadoghq.com/help/).

The following components are involved in sending APM data to Datadog:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/troubleshooting_pipeline_info_1.6c310c1a0ac8ef715126997180b64a3a.png?auto=format"
   alt="APM Troubleshooting Pipeline" /%}

For more information, see Additional support.

## Trace retention{% #trace-retention %}

This section addresses issues related to trace data retention and filtering across Datadog.

{% collapsible-section %}
#### There are more spans in the Trace Explorer than on the Monitors page

If you haven't set up [custom retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#create-your-own-retention-filter), this is expected behavior. Here's why:

The [Trace Explorer](https://app.datadoghq.com/apm/traces) page allows you to search all ingested or indexed spans using any tag. Here, you can query any of your traces.

By default, after spans have been ingested, they are retained by the [Datadog intelligent filter](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#datadog-intelligent-retention-filter). Datadog also has other [retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#retention-filters) that are enabled by default to give you visibility over your services, endpoints, errors, and high-latency traces.

However, to use these traces in your monitors, you must set [custom retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#create-your-own-retention-filter).

Custom retention filters allow you to decide which spans are indexed and [retained](https://docs.datadoghq.com/data_security/data_retention_periods/) by creating, modifying, and disabling additional filters based on tags. You can also set a percentage of spans matching each filter to be retained. These indexed traces can then be used in your monitors.

| PRODUCT                                  | SPAN SOURCE                                                      |
| ---------------------------------------- | ---------------------------------------------------------------- |
| Monitors                                 | Spans from custom retention filters                              |
| Other products(Dashboard, Notebook etc.) | Spans from custom retention filters + Datadog intelligent filter |

{% /collapsible-section %}

## Trace metrics{% #trace-metrics %}

This section covers troubleshooting discrepancies and inconsistencies with trace metrics.

{% collapsible-section %}
#### Trace metrics and custom span-based metrics have different values

Trace metrics and custom span-based metrics can have different values because they are calculated based on different datasets:

- [Trace metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/) are calculated based on 100% of the application's traffic, regardless of your [trace ingestion sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/?tab=java) configuration. The trace metrics namespace follows this format: `trace.<SPAN_NAME>.<METRIC_SUFFIX>`.
- [Custom span-based metrics](https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/) are generated based on your ingested spans, which depend on your [trace ingestion sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/?tab=java). For example, if you are ingesting 50% of your traces, your custom span-based metrics are based on the 50% ingested spans.

To ensure that your trace metrics and custom span-based metrics have the same value, configure a 100% ingestion rate for your application or service.

{% alert level="info" %}
Metric names must follow the [metric naming convention](https://docs.datadoghq.com/metrics/custom_metrics/#naming-custom-metrics). Metric names that start with `trace.*` are not permitted and are not saved.
{% /alert %}

{% /collapsible-section %}

## Services{% #services %}

This section covers strategies to troubleshoot service-related issues.

{% collapsible-section %}
#### One service is showing up as multiple services in Datadog

This can happen when the service name is not consistent across all spans.

For example, you might have a single service such as `service:test` showing multiple services in the Datadog:

- `service:test`
- `service:test-mongodb`
- `service:test-postgresdb`

You can use [Inferred Service dependencies (Preview)](https://docs.datadoghq.com/tracing/services/inferred_services). Inferred external APIs use the default naming scheme `net.peer.name`. For example: `api.stripe.com`, `api.twilio.com`, and `us6.api.mailchimp.com`. Inferred databases use the default naming `scheme db.instance`.

Or, you can merge the service names using an environment variable such as `DD_SERVICE_MAPPING` or `DD_TRACE_SERVICE_MAPPING`, depending on the language.

For more information, see [Configure the Datadog Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/library_config/) or choose your language here:

{% tab title="Java" %}

{% dl %}

{% dt %}
`dd.service.mapping`
{% /dt %}

{% dd %}
**Environment Variable**: `DD_SERVICE_MAPPING`**Default**: `null`**Example**: `mysql:my-mysql-service-name-db, postgresql:my-postgres-service-name-db`Dynamically rename services with configuration. Useful for making databases have distinct names across different services.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Python" %}

{% dl %}

{% dt %}
`DD_SERVICE_MAPPING`
{% /dt %}

{% dd %}
Define service name mappings to allow renaming services in traces, for example: `postgres:postgresql,defaultdb:postgresql`. Available in version 0.47+.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Go" %}

{% dl %}

{% dt %}
`DD_SERVICE_MAPPING`
{% /dt %}

{% dd %}
**Default**: `null`Dynamically rename services through configuration. Services can be separated by commas or spaces, for example: `mysql:mysql-service-name,postgres:postgres-service-name`, `mysql:mysql-service-name postgres:postgres-service-name`.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Node.js" %}

{% dl %}

{% dt %}
`DD_SERVICE_MAPPING`
{% /dt %}

{% dd %}
**Configuration**: `serviceMapping`**Default**: N/A**Example**: `mysql:my-mysql-service-name-db,pg:my-pg-service-name-db`Provide service names for each plugin. Accepts comma separated `plugin:service-name` pairs, with or without spaces.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title=".NET" %}

{% dl %}

{% dt %}
`DD_TRACE_SERVICE_MAPPING`
{% /dt %}

{% dd %}
Rename services using configuration. Accepts a comma-separated list of key-value pairs of service name keys to rename, and the name to use instead, in the format `[from-key]:[to-name]`.**Example**: `mysql:main-mysql-db, mongodb:offsite-mongodb-service`The `from-key` value is specific to the integration type, and should exclude the application name prefix. For example, to rename `my-application-sql-server` to `main-db`, use `sql-server:main-db`. Added in version 1.23.0
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="PHP" %}

{% dl %}

{% dt %}
`DD_SERVICE_MAPPING`
{% /dt %}

{% dd %}
**INI**: `datadog.service_mapping`**Default**: `null`Change the default name of an APM integration. Rename one or more integrations at a time, for example: `DD_SERVICE_MAPPING=pdo:payments-db,mysqli:orders-db` (see [Integration names](https://docs.datadoghq.com/tracing/trace_collection/library_config/php#integration-names)).
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Ruby" %}
Ruby does not support `DD_SERVICE_MAPPING` or `DD_TRACE_SERVICE_MAPPING`. See [Additional Ruby configuration](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/ruby/#advanced-configuration) for code options to change the service name.
{% /tab %}

{% /collapsible-section %}

{% collapsible-section %}
#### There is an unexpected increase in ingested/indexed spans on the Plan and Usage page

Spikes in data ingestion and indexing can be caused by various factors. To investigate the cause of an increase, use the [APM Traces Estimated Usage metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics/#apm-traces-estimated-usage-dashboard):

| USAGE TYPE         | METRIC                                       | DESCRIPTION                                                   |
| ------------------ | -------------------------------------------- | ------------------------------------------------------------- |
| APM Indexed Spans  | `datadog.estimated_usage.apm.indexed_spans`  | Total number of spans indexed by tag-based retention filters. |
| APM Ingested Spans | `datadog.estimated_usage.apm.ingested_spans` | Total number of ingested spans.                               |

The [APM Traces Usage dashboard](https://app.datadoghq.com/dash/integration/apm_estimated_usage) contains several widget groups displaying high-level KPIs and additional usage information.
{% /collapsible-section %}

{% collapsible-section %}
#### Missing error message and stack trace

In some traces with an error status, the **Errors** tab shows `Missing error message and stack trace` rather than exception details.

A span can show this message for two possible reasons:

- The span contains an unhandled exception.
- An HTTP response within the span returned an HTTP status code between 400 and 599.

When an exception is handled in a try/catch block, `error.message`, `error.type`, and `error.stack` span tags are not populated. To populate the detailed error span tags, use [Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/?tab=datadogapi) code.
{% /collapsible-section %}

## Data volume guidelines{% #data-volume-guidelines %}

If you encounter any of the following issues, you may be exceeding [Datadog's volume guidelines](https://docs.datadoghq.com/tracing/troubleshooting/#data-volume-guidelines):

- Your trace metrics are not reporting as you would expect in the Datadog platform.
- You are missing some of your resources that you expected to see in the Datadog platform.
- You are seeing traces from your service but are not able to find this service on the [Software Catalog page](https://app.datadoghq.com/services).

{% collapsible-section %}
#### Data volume guidelines

Your instrumented application can submit spans with timestamps up to 18 hours in the past and two hours in the future from the current time.

Datadog accepts the following combinations for a given 40-minute interval:

- 5000 unique `environments` and `service` combinations
- 100 unique `primary tag values` per additional primary tag
- 100 unique `operation names` per environment and service
- 1000 unique `resources` per environment, service, and operation name
- 30 unique `versions` per environment and service

If you need to accommodate larger volumes, contact [Datadog support](https://docs.datadoghq.com/help/) with your use case.

Datadog truncates the following strings if they exceed the indicated number of characters:

| Name                                                               | Characters |
| ------------------------------------------------------------------ | ---------- |
| [service](https://docs.datadoghq.com/tracing/glossary/#services)   | 100        |
| operation                                                          | 100        |
| type                                                               | 100        |
| [resource](https://docs.datadoghq.com/tracing/glossary/#resources) | 5000       |
| [tag key](https://docs.datadoghq.com/glossary/#span-tag)           | 200        |
| [tag value](https://docs.datadoghq.com/glossary/#span-tag)         | 25000      |

Additionally, the number of [span tags](https://docs.datadoghq.com/glossary/#span-tag) present on any span cannot exceed 1024.
{% /collapsible-section %}

{% collapsible-section %}
#### The number of services exceeds what is specified in the data volume guidelines

If the number of services exceeds what is specified in the data volume guidelines, try following these best practices for service naming conventions.

### Exclude environment tag values from service names{% #exclude-environment-tag-values-from-service-names %}

By default, the environment (`env`) is the primary tag for [Datadog APM](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/troubleshooting-service-naming-convention-issues-3.bd31e7f9068f78d4df132c05fb9bfd8b.png?auto=format"
   alt="Environment is the default primary tag" /%}

A service is typically deployed in multiple environments, such as `prod`, `staging`, and `dev`. Performance metrics like request counts, latency, and error rate differ across various environments. The environment dropdown in the Software Catalog allows you to scope the data in the **Performance** tab to a specific environment.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/troubleshooting-service-naming-convention-issues-2.aaf7387b8df8570a6af7f337e07a9003.png?auto=format"
   alt="Choose a specific environment using the `env` dropdown in the Software Catalog" /%}

One pattern that often leads to issues with an overwhelming number of services is including the environment value in service names. For example, you might have two unique services instead of one since they are operating in two separate environments: `prod-web-store` and `dev-web-store`.

Datadog recommends tuning your instrumentation by renaming your services.

Trace metrics are unsampled, which means your instrumented application shows all data instead of subsections of them. The volume guidelines are also applied.

### Use additional primary tags instead of putting metric partitions or grouping variables into service names{% #use-additional-primary-tags-instead-of-putting-metric-partitions-or-grouping-variables-into-service-names %}

You can use additional primary tags to group and aggregate your trace metrics. Use the dropdown to scope the performance data to a given cluster name or data center value.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/troubleshooting-service-naming-convention-issues-1.64ac28d2f419d94b92ea6977a14df26b.png?auto=format"
   alt="Use the dropdown menu to select a specific cluster or data center value" /%}

Including metric partitions or grouping variables in service names instead of applying additional primary tags unnecessarily inflates the number of unique services in an account and results in potential delay or data loss.

For example, instead of the service `web-store`, you might decide to name different instances of a service `web-store-us-1`, `web-store-eu-1`, and `web-store-eu-2` to see performance metrics for these partitions side-by-side. Datadog recommends implementing the **region value** (`us-1`, `eu-1`, `eu-2`) as a primary tag.
{% /collapsible-section %}

## Connection errors{% #connection-errors %}

This section provides guidance on diagnosing and resolving connection and communication issues between your applications and the Datadog Agent

{% collapsible-section %}
#### Your instrumented application isn't communicating with the Datadog Agent

Read about how to find and fix these problems in [Connection Errors](https://docs.datadoghq.com/tracing/troubleshooting/connection_errors/).
{% /collapsible-section %}

## Resource usage{% #resource-usage %}

This section contains information on troubleshooting performance issues related to resource utilization.

{% collapsible-section %}
#### Out of memory errors

Read about detecting trace collection CPU usage and about calculating adequate resource limits for the Agent in [Agent Resource Usage](https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_resource_usage/).
{% /collapsible-section %}

{% collapsible-section %}
#### Rate limit or max event error messages

Within Datadog Agent logs, if you see error messages about rate limits or max events per second, you can change these limits by following [these instructions](https://docs.datadoghq.com/tracing/troubleshooting/agent_rate_limits). If you have questions, before you change the limits, consult with the Datadog [support team](https://docs.datadoghq.com/help/).
{% /collapsible-section %}

## Security{% #security %}

This section covers approaches for addressing security concerns in APM, including protecting sensitive data and managing traffic.

{% collapsible-section %}
#### Modifying, discarding, or obfuscating spans

There are several configuration options available to scrub sensitive data or discard traces corresponding to health checks or other unwanted traffic that can be configured within the Datadog Agent, or in some languages the tracing client. For details on the options available, see [Security and Agent Customization](https://docs.datadoghq.com/tracing/custom_instrumentation/agent_customization). While this offers representative examples, if you require assistance applying these options to your environment, reach out to [Datadog Support](https://docs.datadoghq.com/help/).
{% /collapsible-section %}

## Debugging and logging{% #debugging-and-logging %}

This section explains how to use debug and startup logs to identify and resolve issues with your Datadog tracer.

{% collapsible-section %}
#### Debug logs

To capture full details on the Datadog tracer, enable debug mode on your tracer by using the `DD_TRACE_DEBUG` environment variable. You might enable it for your own investigation or if Datadog support has recommended it for triage purposes. However, be sure to disable debug logging when you are finished testing to avoid the logging overhead it introduces.

These logs can surface instrumentation errors or integration-specific errors. For details on enabling and capturing these debug logs, see the [debug mode troubleshooting page](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/).
{% /collapsible-section %}

{% collapsible-section %}
#### Startup logs

During startup, Datadog tracing libraries emit logs that reflect the configurations applied in a JSON object, as well as any errors encountered, including if the Agent can be reached in languages where this is possible. Some languages require these startup logs to be enabled with the environment variable `DD_TRACE_STARTUP_LOGS=true`. For more information, see the [Startup logs](https://docs.datadoghq.com/tracing/troubleshooting/tracer_startup_logs/).
{% /collapsible-section %}

{% collapsible-section %}
#### SDK configurations

Configuration values are automatically reported by the SDKs and can be viewed in the UI. This can be used to troubleshoot instrumentation issues caused by misconfiguration. For details, see the [SDK configurations page](https://docs.datadoghq.com/tracing/troubleshooting/sdk_configurations/).
{% /collapsible-section %}

## Additional support{% #additional-support %}

If you still need additional support, open a ticket with Datadog Support.

{% collapsible-section %}
#### Open a Datadog Support ticket

When you open a [support ticket](https://docs.datadoghq.com/help/), the Datadog support team may ask for the following types of information:

1. **Links to a trace or screenshots of the issue**: This helps reproduce your issues for troubleshooting purposes.

1. **Tracer startup logs**: Startup logs help identify tracer misconfiguration or communication issues between the tracer and the Datadog Agent. By comparing the tracer's configuration with the application or container settings, support teams can pinpoint improperly applied settings.

1. **Tracer debug logs**: Tracer debug logs provide deeper insights than startup logs, revealing:

   - Proper integration instrumentation during application traffic flow
   - Contents of spans created by the tracer
   - Connection errors when sending spans to the Agent

1. **Datadog Agent flare**: [Datadog Agent flares](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/?tab=agentv6v7) enable you to see what is happening within the Datadog Agent, for example, if traces are being rejected or malformed. This does not help if traces are not reaching the Datadog Agent, but does help identify the source of an issue, or any metric discrepancies.

1. **A description of your environment**: Understanding your application's deployment configuration helps the Support team identify potential tracer-Agent communication issues and identify misconfigurations. For complex problems, support may request Kubernetes manifests, ECS task definitions, or similar deployment configuration files.

1. **Custom tracing code**: Custom instrumentation, configuration, and adding span tags can significantly impact trace visualizations in Datadog.

1. **Version information**: Knowing what language, framework, Datadog Agent, and Datadog tracer versions you are using allows Support to verify [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/), check for known issues, or recommend a version upgrades. For example:

{% /collapsible-section %}

## Further reading{% #further-reading %}

- [Connection Errors](https://docs.datadoghq.com/tracing/troubleshooting/connection_errors)
- [Datadog tracer startup logs](https://docs.datadoghq.com/tracing/troubleshooting/tracer_startup_logs/)
- [Datadog tracer debug logs](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/)
- [APM metrics sent by the Datadog Agent](https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_metrics/)
- [Custom retention filter](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#create-your-own-retention-filter)
- [Trace Ingestion Sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/?tab=java)
- [Data volume guidelines](https://docs.datadoghq.com/tracing/troubleshooting/#data-volume-guidelines)
- [Datadog's full list of integrations](https://docs.datadoghq.com/integrations/)
- [Inferred Service dependencies](https://docs.datadoghq.com/tracing/services/inferred_services)
- [Troubleshooting APM Instrumentation on a Host](https://learn.datadoghq.com/courses/troubleshooting-apm-instrumentation-on-a-host)
