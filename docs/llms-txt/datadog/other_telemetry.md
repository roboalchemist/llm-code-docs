# Source: https://docs.datadoghq.com/tracing/other_telemetry.md

---
title: Correlate APM Data with Other Telemetry
description: >-
  Learn how to connect APM data with telemetry collected by additional Datadog
  products.
breadcrumbs: Docs > APM > Correlate APM Data with Other Telemetry
source_url: https://docs.datadoghq.com/other_telemetry/index.html
---

# Correlate APM Data with Other Telemetry

Correlating data by various Datadog products gives context to help estimate the business impact and find the root cause of an issue in a few clicks. Set up connections between incoming data to facilitate quick pivots in your explorers and dashboards.

## Correlate Database Monitoring and traces{% #correlate-database-monitoring-and-traces %}

Inject trace IDs into DBM data collection to correlate the two data sources. View database information in APM and APM information in DBM to see a comprehensive, unified view of your system's performance. See [Connect DBM and Traces](https://docs.datadoghq.com/database_monitoring/connect_dbm_and_apm/) to set it up.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_filter_by_calling_service.1abf3918d1d7f38343e666fa7b380f40.png?auto=format"
   alt="Filter your database hosts by the APM services that call them." /%}

## Correlate logs and traces{% #correlate-logs-and-traces %}

Inject trace IDs into logs, and leverage unified service tagging to find the exact logs associated with a specific service and version, or all logs correlated to an observed trace. See [Connect Logs and Traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/) to set it up.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/connect_logs_and_traces/logs-trace-correlation.3fa4d93210758779eeb24beaf35e5da4.png?auto=format"
   alt="Connect Logs And Traces" /%}

## Correlate RUM and traces{% #correlate-rum-and-traces %}

Correlate data collected in front end views with trace and spans on the back end by [Connecting RUM and Traces](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/). Pinpoint issues anywhere in your stack and understand what your users are experiencing.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/index/RumTraces.2a9dff7ac8609f6983d654248af2e46f.png?auto=format"
   alt="Connect RUM sessions and traces" /%}

## Correlate synthetic tests and traces{% #correlate-synthetic-tests-and-traces %}

Follow the data from failing synthetic tests directly through to the root causes by digging into related traces. [Connect Synthetics and Traces](https://docs.datadoghq.com/synthetics/apm/) to speed up troubleshooting your code.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/index/Synthetics.88cece79a1e3646b86b89f3bc00e63f7.png?auto=format"
   alt="Synthetic tests" /%}

## Correlate profiles and traces{% #correlate-profiles-and-traces %}

Performance data for application code that has both tracing and profiling enabled is automatically correlated, letting you move between the two types of analysis to troubleshoot and problem solve. You can move directly from span information to profiling data on the **Profiles** tab, and find specific lines of code related to performance issues. Similarly, you can debug slow and resource-consuming endpoints directly in the Profiling UI.

Read [Investigate Slow Traces or Endpoints](https://docs.datadoghq.com/profiler/connect_traces_and_profiles/) for more information.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiles_tab.0e581f4836c2c600a56470f30a4c1ecf.png?auto=format"
   alt="Profiles tab shows profiling information for a APM trace span" /%}

## Further Reading{% #further-reading %}

- [Ease troubleshooting with cross-product correlation](https://docs.datadoghq.com/logs/guide/ease-troubleshooting-with-cross-product-correlation/)
- [Seamlessly correlate DBM and APM telemetry to understand end-to-end query performance](https://www.datadoghq.com/blog/link-dbm-and-apm/)
