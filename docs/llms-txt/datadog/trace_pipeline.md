# Source: https://docs.datadoghq.com/tracing/trace_pipeline.md

---
title: The Trace Pipeline
description: Learn how to control span ingestion
breadcrumbs: Docs > APM > The Trace Pipeline
---

# The Trace Pipeline

{% image
   source="https://datadog-docs.imgix.net/images/tracing/apm_lifecycle/trace_pipeline.86360aa4559de74193c0be9b40d3f2d7.png?auto=format"
   alt="Trace Pipeline" /%}

Collect traces from your instrumented applications to gain end-to-end visibility into your applications. Query and visualize distributed traces from the [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer), understand how requests flow through your microservices and easily investigate errors and performance issues.

With APM, both the **ingestion** and the **retention** of traces are fully customizable.

## Ingestion mechanisms{% #ingestion-mechanisms %}

Set up tracing to gain end-to-end visibility into your applications with fine-grained [ingestion configuration](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/). Make sure to capture complete traces, including all error and high-latency traces to never miss performance issues such as an application outage or an unresponsive service.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/service_setup.fdd1560c2e50cb491c6e843895654434.png?auto=format"
   alt="Service Setup" /%}

## Ingestion controls{% #ingestion-controls %}

The [Ingestion Control page](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls) overviews ingestion volumes and configuration settings across your services.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/ingestion_controls_page.d3ffd45f6df13587a0d142b37f2469aa.png?auto=format"
   alt="Ingestion Control Page Overview" /%}

## Generating metrics from spans{% #generating-metrics-from-spans %}

You can generate metrics from ingested spans, and use those custom metrics for queries and comparisons. Learn more in [Generating Metrics from Spans](https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/span_to_metrics/metrics_from_spans_1.6c5e7eb5734eae6013f056fbdf502d93.png?auto=format"
   alt="Graph of a span-based metric" /%}

## Trace retention{% #trace-retention %}

After spans are ingested, [Retention Filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention) determine which individual spans are indexed and stored for 15 days. The Datadog Intelligent Retention Filter automatically indexes a representative selection of spans to help you monitor application health. You can also define custom retention filters to index additional spans that are important for your organization's goals.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/retention_filters/retention_filters.ce63b8a6f88f53352e3bccbaa1a7750d.png?auto=format"
   alt="Retention Filters Page" /%}

## Trace usage metrics{% #trace-usage-metrics %}

Learn about how to track and monitor your volume of ingested and indexed data, including using the APM Estimated Usage and Ingestion Reasons dashboards, by reading [Usage Metrics](https://docs.datadoghq.com/tracing/trace_pipeline/metrics).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_indexing_and_ingestion/usage_metrics/dashboard_apm_usage.d7b33dc5f5e730ce1a6f724fd076d36f.png?auto=format"
   alt="APM Estimated Usage Dashboard" /%}
