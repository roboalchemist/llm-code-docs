# Source: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces.md

---
title: Correlate Logs and Traces
description: Connect your logs and traces to correlate them in Datadog.
breadcrumbs: >-
  Docs > APM > Correlate APM Data with Other Telemetry > Correlate Logs and
  Traces
---

# Correlate Logs and Traces

{% image
   source="https://datadog-docs.imgix.net/images/tracing/connect_logs_and_traces/logs-trace-correlation.3fa4d93210758779eeb24beaf35e5da4.png?auto=format"
   alt="Logs in Traces" /%}

The correlation between Datadog APM and Datadog Log Management is improved by the injection of trace IDs, span IDs, `env`, `service`, and `version` as attributes in your logs. With these fields you can find the exact logs associated with a specific service and version, or all logs correlated to an observed [trace](https://docs.datadoghq.com/tracing/glossary/#trace).

It is recommended to configure your application's tracer with `DD_ENV`, `DD_SERVICE`, and `DD_VERSION`. This will provide the best experience for adding `env`, `service`, and `version`. See the [unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging) documentation for more details.

Before correlating traces with logs, ensure your logs are either sent as JSON, or [parsed by the proper language level log processor](https://docs.datadoghq.com/agent/logs/#enabling-log-collection-from-integrations). Your language level logs *must* be turned into Datadog attributes in order for traces and logs correlation to work.

To learn more about automatically or manually connecting your logs to your traces, select your language below:

- [Java](java)
- [Python](python)
- [go](go)
- [Ruby](ruby)
- [Node.js](nodejs)
- [.Net](dotnet)
- [PHP](php)
- [OpenTelemetry](opentelemetry)
