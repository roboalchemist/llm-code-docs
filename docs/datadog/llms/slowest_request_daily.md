# Source: https://docs.datadoghq.com/tracing/guide/slowest_request_daily.md

---
title: Debug the slowest trace on the slowest endpoint of a web service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Debug the slowest trace on the slowest endpoint
  of a web service
---

# Debug the slowest trace on the slowest endpoint of a web service

*3 minutes to complete*

{% video
   url="https://datadog-docs.imgix.net/images/tracing/guide/slowest_request_daily/slowest_trace_1_cropped.mp4" /%}

With Datadog APM, you can investigate the performance of your endpoints, identify slow requests, and investigate the root cause of latency issues. This example shows the slowest [trace](https://docs.datadoghq.com/tracing/glossary/#trace) of the day for an e-commerce checkout endpoint and how it slows down because of high CPU usage.

1. **Open the [Software Catalog](https://app.datadoghq.com/services)**.

This page contains a list of all services sending data to Datadog. Note you can search for keywords, filter by `env-tag`, and set the time frame.

1. **Search for a relevant and active web service and open the Service Page**.

The `web-store` service is used in this example because it is the primary server in the tech stack and it controls most calls to third party services.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/slowest_request_daily/slowest_trace_2_cropped.47a1b1e4b9c93fe8b1beeea26fa3af20.png?auto=format"
      alt="Identifying the slowest trace and finding the bottleneck causing it" /%}

In addition to throughput, latency, and error rate information, the service details page contains a list of Resources (major operations like API endpoints, SQL queries, and web requests) identified for the service.

1. **Sort the Resource table by p99 latency** and click into the slowest resource. **Note**: If you cannot see a p99 latency column, you can click on the cog icon `Change Columns` and flip the switch for `p99`.

The [Resource](https://docs.datadoghq.com/tracing/glossary/#resources) page contains high-level metrics about this resource like throughput, latency, error rate, and a breakdown of the time spent on each downstream service from the resource. In addition, it contains the specific [traces](https://docs.datadoghq.com/tracing/glossary/#trace) that pass through the resource and an aggregate view of the [spans](https://docs.datadoghq.com/tracing/glossary/#spans) that make up these traces.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/slowest_request_daily/slowest_trace_3_cropped.dcd8e6b693937da26c98339924236dc5.png?auto=format"
      alt="Identifying the slowest trace and finding the bottleneck causing it" /%}

1. Set the time filter to `1d One Day`. Scroll down to the Traces table and **sort it by duration**, hover over the top trace in the table and **click View Trace**

This is the flame graph and associated information. Here you can see the duration of each step in the trace and whether it is erroneous. This is useful in identifying slow components and error-prone ones. The flame graph can be zoomed, scrolled, and explored naturally. Under the flame graph you can see associated metadata, Logs, and Host information.

The flame graph is a great way of identifying the precise piece of your stack that is erroneous or latent. Errors are marked with red highlights and duration is represented by the horizontal length of the span, meaning long spans are the slowest ones. Learn more about using the flame graph in the [Trace View guide](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/?tab=spanmetadata).

Under the flame graph you can see all of the tags (including [custom ones](https://docs.datadoghq.com/tracing/guide/adding_metadata_to_spans/)). From here you can also see associated logs (if you [connected Logs to your Traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/)), see host-level information such as CPU and memory usage.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/guide/slowest_request_daily/slowest_trace_4_cropped.fd5e7eb6dc89f873558e1ee966d07c70.png?auto=format"
      alt="Identifying the slowest trace and finding the bottleneck causing it" /%}

1. **Click into the Host tab**, observe the CPU and memory performance of the underlying host while the request was hitting it.

1. **Click Open Host Dashboard** to view all relevant data about the host

Datadog APM seamlessly integrates with the other Datadog metrics and information - like infrastructure metrics and Logs. Using the flame graph, this information is available to you as well as any [custom metadata](https://docs.datadoghq.com/tracing/guide/adding_metadata_to_spans/) you are sending with your traces.

## Further Reading{% #further-reading %}

- [Alert on anomalous p99 latency of a database service](https://docs.datadoghq.com/tracing/guide/alert_anomalies_p99_database/)
- [Compare a service's latency to the previous week](https://docs.datadoghq.com/tracing/guide/week_over_week_p50_comparison/)
- [Create a Dashboard to track and correlate APM metrics](https://docs.datadoghq.com/tracing/guide/apm_dashboard/)
- [All guides](https://docs.datadoghq.com/tracing/guide/)
