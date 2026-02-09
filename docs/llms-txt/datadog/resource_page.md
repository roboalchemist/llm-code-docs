# Source: https://docs.datadoghq.com/tracing/services/resource_page.md

---
title: Resource Page
description: >-
  Analyze resource performance with health metrics, dependency maps, span
  summaries, and frontend impact data.
breadcrumbs: Docs > APM > Service Observability > Resource Page
---

# Resource Page

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/resource-page-cropped.a5877c3f9c9be325fd36758c0ac40af5.png?auto=format"
   alt="The APM resource page, showing monitor status and trends for key metrics" /%}

A resource is a particular action for a given [service](https://docs.datadoghq.com/tracing/glossary/#services) (typically an individual endpoint or query). Read more about resources in [Getting Started with APM](https://docs.datadoghq.com/tracing/glossary/). For each resource, APM automatically generates a dashboard page covering:

- Key health metrics
- Monitor status for all monitors associated with this service
- List of metrics for all resources associated with this service

## Out-of-the-box graphs{% #out-of-the-box-graphs %}

Datadog provides out-of-the-box graphs for any given resource. Use the dropdown above each graph to change the displayed information.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/resource_otb_graphs.e96a628ef132c72a8bc6d76646a807c9.png?auto=format"
   alt="Out-of-the-box resource graphs showing requests per second, latency, total errors, and percent time spent per service" /%}

### Requests and Errors{% #requests-and-errors %}

The **Requests and Errors** graph displays the total number of requests (hits) and errors over time. Using the dropdown menu, you can also view:

- **Requests by Version**: Breakdown of requests across different service versions.
- **Requests per Second by Version**: The rate of requests for each version.
- **Requests and Errors Per Second**: The rate of requests (hits) and errors per second.

### Errors{% #errors %}

The **Errors** graph displays the total count of errors over time. Using the dropdown menu, you can also view:

- **Errors by Version**: The error counts for each service version side by side.
- **Errors per Second by Version**: The error rate (errors per second) for each service version over time.
- **Errors per Second**: The overall error rate for the service, per second.
- **% Error Rate by Version**: The percentage of requests resulting in errors for each service version.
- **% Error Rate**: The overall error rate for the service, as a percentage.

### Latency{% #latency %}

The **Latency** graph displays the latency percentiles as a timeseries. Using the dropdown menu, you can also view:

- **Latency by Version**: Latency broken down by service version.
- **Historical Latency**: Comparison of the current latency distribution with the previous day and week.
- **Latency Distribution**: The distribution of latencies over the selected time frame.
- **Latency by Error**: The latency of requests over time, segmented by whether the requests resulted in errors.
- **Apdex** (Application Performance Index): The [Apdex](https://docs.datadoghq.com/tracing/guide/configure_an_apdex_for_your_traces_with_datadog_apm/) score over time.

### Avg Time per Request{% #avg-time-per-request %}

For services involving multiple downstream services, a fourth graph breaks down the average [execution time](https://docs.datadoghq.com/glossary/#execution-time) spent per request. This graph is built on sampled trace data, unlike the other top graphs which use unsampled data sources.

Using the dropdown menu, you can also view:

- **Total Time Spent**: The cumulative time spent in each downstream service over time.
- **% of Time Spent**: The percentage of time spent in each downstream service relative to the total time.

For services like Postgres or Redis, which are final operations that do not call other services, there is no sub-services graph. [Watchdog](https://docs.datadoghq.com/watchdog/) performs automatic anomaly detection on the Requests, Latency, and Error graphs. If an anomaly is detected, an overlay appears on the graph. Clicking the Watchdog icon provides more details in a side panel.

### Export to dashboard{% #export-to-dashboard %}

On the upper-right corner of each graph, click on the up arrow in order to export your graph into a pre-existing [Dashboard](https://docs.datadoghq.com/dashboards/).

### Latency distribution{% #latency-distribution %}

The resource page also displays a resource latency distribution graph:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/resource_latency_distribution.e871f9c047bdcc4dd62e30a2ade4baf1.png?auto=format"
   alt="A latency distribution graph showing a distribution of the time taken per resource request" /%}

Use the top right percentile selectors to zoom into a given percentile, or hover over the sidebar to view percentile markers.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/service/latency_distribution_sidebar.0f612dbd09d5f47743733f9e553f172f.png?auto=format"
   alt="A close-up of the latency distribution graph sidebar which allows filtering on percentiles" /%}

## Dependency Map{% #dependency-map %}

Use the Dependency Map to view a flow graph of all of a resource's upstream and downstream service dependencies. The map is scoped to the requests flowing through the selected service and resource (endpoint, database query, etc.) you're focused on.

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.datadoghq.com, ap2.datadoghq.com

[Inferred service dependencies](https://docs.datadoghq.com/tracing/services/inferred_services/) like databases, queues or third-party services are represented with a purple background node.
{% /callout %}

Click on a downstream or upstream service node to see which resources are invoked in the request flow. To focus on a particular request path, select a node an click `set as start/end`. This filters the map to focus on the requests that also flow through this upstream or downstream dependency.

**Note**: This map is based on a sample of ingested spans. Request rates are then upscaled based on applied sampling rates to represent actual application/service traffic.

The dependency map is only available for service-entry span resources.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/dependency_map.9225e6c183da96b6fb69fb78b01beead.png?auto=format"
   alt="Resource page dependency map" /%}

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.datadoghq.com, ap2.datadoghq.com

**Note**: [Service overrides](https://docs.datadoghq.com/tracing/guide/service_overrides/) are represented as part of the edge of the dependency map to keep visibility over the actual remote service, database or queue the service is interacting with.
{% /callout %}

### Frontend Impact{% #frontend-impact %}

Datadog provides you visibility into how a web resource impacts your frontend applications. You can understand what frontend view is sending requests to the resource and identify views that are experiencing high latency or errors from the resource.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/resource_frontend_impact.3f6859fd4a90ac9b0a83bad19d39b256.png?auto=format"
   alt="A table showing several key metrics for a list of views sending requests to a particular resource" /%}

Isolate requests and errors over time for a specific frontend view by hovering over a RUM View Name in the table and clicking on **Isolate this View**. From here, you can explore sampled traces originating from the frontend views by clicking on **View Traces** at the top right of the panel. You can also investigate the sampled RUM sessions for each view by clicking on the context menu for a frontend view in the table.

The frontend impact panel is only available if you use Real User Monitoring (RUM) and the resource belongs to a web service. Unlike the requests, errors, and latency graphs which use unsampled data sources, the frontend impact metrics are built on indexed trace data from the past 1 hour:

{% dl %}

{% dt %}
`RUM View Name:`
{% /dt %}

{% dd %}
Name of the frontend view
{% /dd %}

{% dt %}
`App Name:`
{% /dt %}

{% dd %}
Name of application that contains the frontend view
{% /dd %}

{% dt %}
`Sessions:`
{% /dt %}

{% dd %}
Number of sessions for the frontend view
{% /dd %}

{% dt %}
`Error Rate Per Sessions:`
{% /dt %}

{% dd %}
Number of sessions that included the frontend view
{% /dd %}

{% dt %}
`P95 Latency`
{% /dt %}

{% dd %}
P95 latency for requests originating from the frontend view
{% /dd %}

{% dt %}
`Requests`
{% /dt %}

{% dd %}
Number of requests originating from the frontend view
{% /dd %}

{% /dl %}

## Span summary{% #span-summary %}

For a given resource, Datadog provides you a [span](https://docs.datadoghq.com/tracing/glossary/#spans) analysis breakdown of all matching traces:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/span_stats.e929640d13304fb26ca58f24ea4f5489.png?auto=format"
   alt="A table showing several key metrics for a list of the spans associated with a particular resource" /%}

The displayed metrics represent, per span:

{% dl %}

{% dt %}
`Avg Spans/trace`
{% /dt %}

{% dd %}
Average number of occurrences of the span, for traces including the current resource, where the span is present at least once.
{% /dd %}

{% dt %}
`% of Traces`
{% /dt %}

{% dd %}
Percentage of traces including the current resource where the span is present at least once.
{% /dd %}

{% dt %}
`Avg Duration`
{% /dt %}

{% dd %}
Average duration of the span, for traces including the current resource, where the span is present at least once.
{% /dd %}

{% dt %}
`Avg % Exec Time`
{% /dt %}

{% dd %}
Average ratio of execution time for which the span was active, for traces including the current resource, where the span is present at least once.
{% /dd %}

{% /dl %}

**Note**: A span is considered active when it's not waiting for a child span to complete. The active spans at a given time, for a given trace, are all the leaf spans (in other words, spans without children).

The span summary table is only available for resources containing service entry spans.

## Traces{% #traces %}

Consult the list of [traces](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/) associated with this resource in the [Trace search](https://docs.datadoghq.com/tracing/search/) modal already filtered on your environment, service, operation, and resource name:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/resource/traces_list.29fcb0e7075964290ebfce3c30135175.png?auto=format"
   alt="A list of traces associated with a particular resource that shows the timestamp, duration, status, and latency breakdown of each trace" /%}

## Endpoint definition{% #endpoint-definition %}

An endpoint is an HTTP resource exposed by a service at a specific URL path.

If a resource represents an endpoint, a new **Definition** section is added to the resource page.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/software_catalog/definition-section.4cce3e10db1e2293c92395c8c0d0c31b.png?auto=format"
   alt="Resource side panel showing endpoint Definition section." /%}

## Further Reading{% #further-reading %}

- [Pinpoint performance issues in downstream services with the Dependency Map Navigator](https://www.datadoghq.com/blog/dependency-map-navigator/)
- [Learn how to setup APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page/)
- [Understand how to read a Datadog Trace](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/)
