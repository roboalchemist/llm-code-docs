# Source: https://docs.datadoghq.com/tracing/metrics.md

---
title: APM Metrics
description: Learn about useful metrics you can generate from APM data.
breadcrumbs: Docs > APM > APM Metrics
---

# APM Metrics

## Trace metrics{% #trace-metrics %}

[Tracing application metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/) are collected after enabling trace collection and instrumenting your application. These metrics are available for dashboards and monitors. These metrics capture **request** counts, **error** counts, and **latency** measures. They are calculated based on 100% of the application's traffic, regardless of any [trace ingestion sampling](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms) configuration.

By default, these metrics are calculated in the Datadog Agent based on the traces sent from an instrumented application to the Agent.

Ingested span and traces are kept for 15 minutes. Indexed spans and traces that retention filters keep are stored in Datadog for 15 days. But if you generate custom metrics from ingested data, the metrics are retained for 15 months.

## Runtime metrics{% #runtime-metrics %}

Enable [runtime metrics collection](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/) in supported tracing libraries to gain insights into an application's performance. These metrics are sent to the Datadog Agent over the configured DogStatsD port.

## Next steps{% #next-steps %}

- [Create a Dashboard to track and correlate APM metrics](https://docs.datadoghq.com/tracing/guide/apm_dashboard)
- [Create APM Monitors that alert and notify you when something is unexpected](https://docs.datadoghq.com/monitors/create/types/apm/)

## Further Reading{% #further-reading %}

- [Customize trace ingestion and retain important traces.](https://docs.datadoghq.com/tracing/trace_pipeline/)
- [Instrument your services and set up trace data collection in the Agent](https://docs.datadoghq.com/tracing/trace_collection/)
- [Create and manage monitors to notify your teams when it matters.](https://docs.datadoghq.com/monitors/)
