# Source: https://docs.datadoghq.com/tracing/guide/week_over_week_p50_comparison.md

---
title: Compare a Service's latency to the previous week
description: >-
  Learn how to create dashboards and monitors that compare service latency
  metrics week over week to identify performance trends and issues.
breadcrumbs: Docs > APM > Tracing Guides > Compare a Service's latency to the previous week
source_url: https://docs.datadoghq.com/guide/week_over_week_p50_comparison/index.html
---

# Compare a Service's latency to the previous week

*2 minutes to complete*

{% video
   url="https://datadog-docs.imgix.net/images/tracing/guide/week_over_week_p50_comparison/wow_p50_comp_3_cropped_small.mp4" /%}

Datadog can show you the latency of your application over time and how it compares to similar moments in previous time frames such as last week or month. This example shows a web server for an e-commerce platform and monitors the latency performance for the server has seen over the past month.

1. **Open the [Software Catalog](https://app.datadoghq.com/services)**.

This page contains a list of all [services](https://docs.datadoghq.com/tracing/glossary/#services) providing data to Datadog. You can search over your services by keywords, filter them by `env` tag, and set the time frame.

1. **Search and open a relevant and active service**.

This example uses the `web-store` service because it is stable. Double-check that issues have not appeared over the last month.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/week_over_week_p50_comparison/wow_p50_comp_2_cropped.86be15b175d4bf59148c219e19c35ea8.png?auto=format"
      alt="comparison 2" /%}

Click the service to see its Service page, which shows analyses of throughput, latency (including percentile distribution), and errors, a summary of the active Datadog monitors for the service, and a breakdown of the [resources](https://docs.datadoghq.com/tracing/glossary/#resources) made available by the service.

1. **Find the Latency graph** on the top of the Service page and deselect all the percentiles from the legend leaving only the p50 option, then **Expand the Latency graph** to view the full screen mode where you can conduct a more comprehensive analysis.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/week_over_week_p50_comparison/wow_p50_s3_cropped.9634e47c566f308cc29aad95fd228a57.png?auto=format"
   alt="Full view of latency chart with week-over-week display enabled" /%}

```
Datadog APM allows you to compare the different percentiles of latency for the service over time but also to view the full distribution of latencies in the Latency Distribution graph below.
```
**Add the previous week's p50 performance** by checking the `Week` option in the *Compare to Last* section on the right.
{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/week_over_week_p50_comparison/wow_p50_comp_1.35a1fd167368ff2c33df369eeca78fd4.png?auto=format"
   alt="Full view of latency chart with week-over-week display enabled" /%}

**Note**: As you conduct your analysis you can export this graph to any dashboard from the Service view, and display this data alongside any other chart generated in Datadog, including your custom metrics, host-level information, and logs.

## Further Reading{% #further-reading %}

- [Alert on anomalous p99 latency of a database service](https://docs.datadoghq.com/tracing/guide/alert_anomalies_p99_database/)
- [Create a Dashboard to track and correlate APM metrics](https://docs.datadoghq.com/tracing/guide/apm_dashboard/)
- [Debug the slowest trace on the slowest endpoint of a web service](https://docs.datadoghq.com/tracing/guide/slowest_request_daily/)
- [All guides](https://docs.datadoghq.com/tracing/guide/)
