# Source: https://docs.datadoghq.com/tracing/metrics/metrics_namespace.md

---
title: Trace Metrics
description: >-
  Comprehensive guide to APM trace metrics including namespace, types (hits,
  errors, latency, Apdex), and how they're calculated from application traffic.
breadcrumbs: Docs > APM > APM Metrics > Trace Metrics
source_url: https://docs.datadoghq.com/metrics/metrics_namespace/index.html
---

# Trace Metrics

## Overview{% #overview %}

Tracing application metrics are collected after you [enable trace collection and instrument your application](https://docs.datadoghq.com/tracing/trace_collection/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/apm_lifecycle/trace_metrics.e33c8ad881a72575d460653a1eb614a2.png?auto=format"
   alt="Trace Metrics" /%}

These metrics capture request counts, error counts, and latency measures. They are calculated based on 100% of the application's traffic, regardless of any [trace ingestion sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms) configuration. Ensure that you have full visibility into your application's traffic by using these metrics to spot potential errors on a service or a resource, and by creating dashboards, monitors, and SLOs.

**Note**: If your applications are instrumented with OpenTelemetry libraries, and sampling is set up at the SDK level, APM metrics are calculated based on the sampled set of data. However, if sampling is set up at the OpenTelemetry Collector level and the sampler processor is upstream of the Datadog connector, APM metrics are calculated based on 100% of application traffic.

Trace metrics are generated for service entry spans and certain operations depending on integration language. For example, the Django integration produces trace metrics from spans that represent various operations (1 root span for the Django request, 1 for each middleware, and 1 for the view).

The [trace metrics](https://docs.datadoghq.com/tracing/glossary/#trace-metrics) namespace is formatted as:

- `trace.<SPAN_NAME>.<METRIC_SUFFIX>`

With the following definitions:

{% dl %}

{% dt %}
`<SPAN_NAME>`
{% /dt %}

{% dd %}
The name of the operation or `span.name` (examples: `redis.command`, `pylons.request`, `rails.request`, `mysql.query`).
{% /dd %}

{% dt %}
`<METRIC_SUFFIX>`
{% /dt %}

{% dd %}
The name of the metric (examples: `hits`, `errors`, `apdex`, `duration`). See the section below.
{% /dd %}

{% dt %}
`<TAGS>`
{% /dt %}

{% dd %}
Trace metrics tags, possible tags are: `env`, `service`, `version`, `resource`, `http.status_code`, `http.status_class`, `rpc.grpc.status_code`(requires Datadog Agent v7.65.0+) , and Datadog Agent tags (including the host and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog)).
{% /dd %}

{% dd %}
**Note:** Other tags set on spans are not available as tags on traces metrics.
{% /dd %}

{% /dl %}

## Metric suffix{% #metric-suffix %}

### Hits{% #hits %}

{% dl %}

{% dt %}
`trace.<SPAN_NAME>.hits`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for any APM service.**Description:** Represent the count of spans created with a specific name (for example, `redis.command`, `pylons.request`, `rails.request`, or `mysql.query`).**Metric type:** [COUNT](https://docs.datadoghq.com/metrics/types/?tab=count#metric-types).**Tags:** `env`, `service`, `version`, `resource`, `resource_name`, `http.status_code`, `rpc.grpc.status_code`, all host tags from the Datadog Host Agent, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% dt %}
`trace.<SPAN_NAME>.hits.by_http_status`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for HTTP/WEB APM services if http metadata exists.**Description:** Represent the count of hits for a given span break down by HTTP status code.**Metric type:** [COUNT](https://docs.datadoghq.com/metrics/types/?tab=count#metric-types).**Tags:** `env`, `service`, `version`, `resource`, `resource_name`, `http.status_class`, `http.status_code`, all host tags from the Datadog Host Agent, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% /dl %}

### Latency distribution{% #latency-distribution %}

{% dl %}

{% dt %}
`trace.<SPAN_NAME>`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for any APM service.**Description:** Represent the latency distribution for all services, resources, and versions across different environments and additional primary tags. **Recommended for all latency measurement use cases.****Metric type:** [DISTRIBUTION](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types).**Tags:** `env`, `service`,`version`, `resource`, `resource_name`, `http.status_code`, `rpc.grpc.status_code`, `synthetics`, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% /dl %}

### Errors{% #errors %}

{% dl %}

{% dt %}
`trace.<SPAN_NAME>.errors`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for any APM service.**Description:** Represent the count of errors for a given span.**Metric type:** [COUNT](https://docs.datadoghq.com/metrics/types/?tab=count#metric-types).**Tags:** `env`, `service`, `version`, `resource`, `resource_name`, `http.status_code`, `rpc.grpc.status_code`, all host tags from the Datadog Host Agent, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% dt %}
`trace.<SPAN_NAME>.errors.by_http_status`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for any APM service.**Description:** Represent the count of errors for a given span.**Metric type:** [COUNT](https://docs.datadoghq.com/metrics/types/?tab=count#metric-types).**Tags:** `env`, `service`, `version`, `resource`, `http.status_class`, `http.status_code`, all host tags from the Datadog Host Agent, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% /dl %}

### Apdex{% #apdex %}

{% dl %}

{% dt %}
`trace.<SPAN_NAME>.apdex`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for any HTTP or web-based APM service.**Description:** Measures the [Apdex](https://docs.datadoghq.com/tracing/guide/configure_an_apdex_for_your_traces_with_datadog_apm/) score for each web service.**Metric type:** [GAUGE](https://docs.datadoghq.com/metrics/types/?tab=gauge#metric-types).**Tags:** `env`, `service`, `version`, `resource` / `resource_name`, `synthetics`, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% /dl %}

## Legacy metrics{% #legacy-metrics %}

The following metrics are maintained for backward compatibility. For all latency measurement use cases, Datadog strongly recommends using Latency Distribution metrics instead.

### Duration (Legacy){% #duration-legacy %}

{% alert level="danger" %}
**Important:** Duration metrics are maintained for backward compatibility only. For all latency measurement use cases, Datadog strongly recommends using Latency Distribution metrics instead, as they provide better accuracy for percentile calculations and overall performance analysis.
{% /alert %}

{% dl %}

{% dt %}
`trace.<SPAN_NAME>.duration`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for any APM service.**Description:** Measure the total time for a collection of spans within a time interval, including child spans seen in the collecting service. For most use cases, Datadog recommends using the Latency Distribution for calculation of average latency or percentiles. To calculate the average latency with host tag filters, you can use this metric with the following formula:`sum:trace.<SPAN_NAME>.duration{<FILTER>}.rollup(sum).fill(zero) / sum:trace.<SPAN_NAME>.hits{<FILTER>}.rollup(sum).fill(zero)`This metric does not support percentile aggregations. Read the Latency Distribution section for more information.**Metric type:** [GAUGE](https://docs.datadoghq.com/metrics/types/?tab=gauge#metric-types).**Tags:** `env`, `service`, `resource`, `http.status_code`, all host tags from the Datadog Host Agent, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% /dl %}

### Duration by (Legacy){% #duration-by-legacy %}

{% alert level="danger" %}
**Important:** Duration metrics are maintained for backward compatibility only. For all latency measurement use cases, Datadog strongly recommends using Latency Distribution metrics instead, as they provide better accuracy for percentile calculations and overall performance analysis.
{% /alert %}

{% dl %}

{% dt %}
`trace.<SPAN_NAME>.duration.by_http_status`
{% /dt %}

{% dd %}
**Prerequisite:** This metric exists for HTTP/WEB APM services if http metadata exists.**Description:** Measure the total time for a collection of spans for each HTTP status. Specifically, it is the relative share of time spent by all spans over an interval and a given HTTP status - including time spent waiting on child processes.**Metric type:** [GAUGE](https://docs.datadoghq.com/metrics/types/?tab=gauge#metric-types).**Tags:** `env`, `service`, `resource`, `http.status_class`, `http.status_code`, all host tags from the Datadog Host Agent, and [additional primary tags](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-additional-primary-tags-in-datadog).
{% /dd %}

{% /dl %}

## Sampling impact on trace metrics{% #sampling-impact-on-trace-metrics %}

In most cases, trace metrics are calculated based on all application traffic. However, with certain trace ingestion sampling configurations, the metrics represent only a subset of all requests.

### Application-side sampling{% #application-side-sampling %}

Some tracing libraries support application-side sampling, which reduces the number of spans before they are sent to the Datadog Agent. For example, the Ruby tracing library offers application-side sampling to lower performance overhead. However, this can affect trace metrics, as the Datadog Agent needs all spans to calculate accurate metrics.

Very few tracing libraries support this setting, and using it is generally not recommended.

### OpenTelemetry sampling{% #opentelemetry-sampling %}

The OpenTelemetry SDK's native sampling mechanisms lower the number of spans sent to the Datadog collector, resulting in sampled and potentially inaccurate trace metrics.

### X-Ray sampling{% #x-ray-sampling %}

X-Ray spans are sampled before they are sent to Datadog, which means trace metrics might not reflect all traffic.

## Further Reading{% #further-reading %}

- [Create custom metrics from your ingested spans](https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/)
- [Learn how to setup APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page)
- [Dive into your resource performance and traces](https://docs.datadoghq.com/tracing/services/resource_page)
- [Understand how to read a Datadog Trace](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/)
