# Source: https://docs.datadoghq.com/tracing/trace_explorer/trace_view.md

---
title: Trace View
description: >-
  Visualize and analyze individual traces using flame graphs, span lists,
  waterfalls, and maps with detailed span information.
breadcrumbs: Docs > APM > Trace Explorer > Trace View
---

# Trace View

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/trace_view.6cc4349832a248528c2367a5527b692e.png?auto=format"
   alt="Trace View" /%}

## Overview{% #overview %}

View an individual [trace](https://docs.datadoghq.com/tracing/glossary/#trace) to see all of its [spans](https://docs.datadoghq.com/tracing/glossary/#spans) and associated metadata. Each trace can be visualized as either a Flame Graph, Span List, Waterfall, or Map.

The trace header displays critical trace information, including the root span's service name, resource name, trace ID, end-to-end trace duration, and the trace start time. To get a permalink to the trace, click **Open Full Page** and save the URL.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/trace_header.33677dca771ce05dee63f60ccfa63d96.png?auto=format"
   alt="Trace header" /%}

## Trace visualizations{% #trace-visualizations %}

{% tab title="Flame Graph" %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/flamegraph.ecb4e6e9bed640d1e44ed9469d8f6e9a.png?auto=format"
   alt="Flame Graph" /%}

The Flame Graph is the default visualization that displays all the color-coded spans from a trace on a timeline. This is useful for understanding the execution path of a request and where time was spent over a trace.

To navigate the graph, scroll to zoom, click and drag to move around, and use the minimap to zoom into the selected span or zoom out to the full trace.

The legend details the color coding of the flame graph. Group spans by either **Service** (default), **[Base service](https://docs.datadoghq.com/tracing/guide/service_overrides#base-service)** (service from which the span is emitted), **Host**, or **Container**. Choose to display either the percentage of trace execution time (**% Exec Time**) or span count (**Spans**) by group. If errors exist on spans in the trace, highlight them in the flame graph by selecting the **Errors** checkbox under **Filter Spans**.

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com, ap2.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.datadoghq.com

Spans from [inferred services](https://docs.datadoghq.com/tracing/services/inferred_services) are represented with a dashed outline.
{% /callout %}

{% video
   url="https://datadog-docs.imgix.net/images/tracing/trace_view/flamegraph_legend.mp4" /%}

{% /tab %}

{% tab title="Span List" %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/spanlist.458cfcd54f92cce5fce015ec8e240ffb.png?auto=format"
   alt="Trace View" /%}

Displays [resources](https://docs.datadoghq.com/tracing/glossary/#resources) by group ([service](https://docs.datadoghq.com/tracing/glossary/#services) by default) and sorts them according to their count of spans. This visualization is useful for scanning latency information by resource or grouping.

Filter resources by type or naming information using the corresponding buttons and text-based search.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/spanlist_headers.1b6dcee1410d86d1ad1c2d0a379e9a0d.png?auto=format"
   alt="Span List headers" /%}

Groups can be sorted by clicking on the corresponding column header: **RESOURCE**, **SPANS**, average duration (**AVG DURATION**), execution time (**EXEC TIME**), or percentage of trace execution time (**% EXEC TIME**).
{% /tab %}

{% tab title="Waterfall" %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/waterfall2.60f2d29b352bdffe1f161e3a184409a3.png?auto=format"
   alt="Waterfall" /%}

Displays all spans for a trace on a timeline where each row corresponds to a span. This visualization is useful for isolating and focusing on relevant parts of a trace.

Each row (span) indicates the following:

- **Relative span duration**: The length of the color-coded bar corresponds to the percentage of total trace duration.
- **Absolute span duration**: The absolute time in milliseconds (ms).
- **Span details**: The corresponding service name and resource name are displayed.
- **Statuses**: When applicable, an HTTP status code is displayed.
- **Color coding**: Spans are color-coded by service (default), host, or container. To change how spans are color-coded, use the **Color by** dropdown.

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com, ap2.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.datadoghq.com

Spans from [inferred services](https://docs.datadoghq.com/tracing/services/inferred_services) are represented with a dashed underline.
{% /callout %}

To expand or collapse span descendants, click the chevron (>) icon on a row. To expand or collapse all spans, click the **Expand all** (+) or **Collapse all** (-) buttons.
{% /tab %}

{% tab title="Map" %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/trace-map.c02fd2dd23eb6523ba558d44bab77adf.png?auto=format"
   alt="Trace map" /%}

Trace map displays a representation of all services involved in a single trace. It provides an overview of the transaction lifecycle at the service level and shows service dependencies.

Each node on the map represents a service in the transaction lifecycle. To prevent cyclic dependencies on the map, services that call another service that had already been invoked by the original service, are represented by duplicated nodes. [Inferred services](https://docs.datadoghq.com/tracing/services/inferred_services) are represented with a dashed outline and a purple background.

Service nodes explicitly show the percentage of the **total execution time**, which shows the trace duration breakdown at the service level.

If a [service entry span](https://docs.datadoghq.com/glossary/#service-entry-span) is in an error state, the corresponding service node is marked with a red border to highlight a faulty services. If an error occurs in a service exit span, the edge indicating the call to the next service is also highlighted in red.

To view additional information about the service entry spans for each node, hover over the error state. The tooltip displays details about the service entry span's operation and resource name, along with any error messages. To further investigation, click **View Entry Span** to switch to the Waterfall view.
{% /tab %}

### Trace preview{% #trace-preview %}

When a trace size exceeds 100MB, it cannot be fully visualized using the default trace side panel. In such cases, Trace Preview mode is enabled. This mode returns only the most critical spans to help you continue your investigation. These include:

- Service entry level spans
- Error spans
- Long-running spans
- Spans linked to other spans or traces

The available visualization options for large traces are limited to the Waterfall and Map views. In Preview mode, the Waterfall view provides additional an option to fetch spans that are not included by default. These spans are grouped and represented using numbered pills. Each pill displays the total number of spans available in that group. You can click on a number pill to expand and view all spans within that group.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/trace/trace-preview.548e76d6bce3ba149424f835226a3488.png?auto=format"
   alt="Trace preview" /%}

## Span search{% #span-search %}

In the Waterfall and Flamegraph visualizations, the search option allows you to find the spans that meet specific queries. Spans that match the search query are highlighted in the trace view and you can navigate between these matches using the arrows next to the search bar.

**Note**: When the `Error` checkbox is selected, the search results return spans that match the query and are in an error state.

The search query on the trace side panel supports the following options:

- **Free text search:** Free-form text search allows filtering by service, resource, or operation name. It highlights the spans containing the specified text within these categories. Example: `web`
- **Key-value search:** Use key:value expression to filter spans with specific key-value pairs. Example: `service:web-ui`

**Note**: Wildcards are not supported in the Trace search bar.

**Supported expressions:**

- Group expression: `language:(go OR python)`
- Boolean expression: `service:event-query OR terminator`
- Range expression: `duration:>200ms`

**Note**: Numerical values support `<`, `>`, `<=`, and `>=` expressions.

## More information{% #more-information %}

The height-adjustable bottom of the Trace View shows selected span and trace information.

The span header contains service, operation, and resource names of the selected span as well as latency information. Pivot to other parts of the platform or narrow down your [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer) search by clicking on the naming pill.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/span_header.6f436463f55d6c2a7097bddf6b6ac46c.png?auto=format"
   alt="Span header" /%}

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com, ap2.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.datadoghq.com



When the span represents a client call from an instrumented service to a database, a queue, or a third-party service, the span header shows the service and the inferred entity.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/span_header_inferred.52c1ca6ad938da41d4a09f25b264aa04.png?auto=format"
   alt="Span header inferred" /%}


{% /callout %}

{% tab title="Span Info" %}
See all span metadata, including custom tags. Click on a span tag to update the search query in the Trace Explorer or copy the tag's value to the clipboard.

Other information may be displayed under various conditions:

- Error message and stack trace (on error span)

- SQL Query markup (on database spans)

- RUM Context and Metadata (on RUM spans)

- Spark Metrics (on Spark job spans)

- A git warning message (when git information is missing on a CI Test)

  {% image
     source="https://datadog-docs.imgix.net/images/tracing/trace_view/info_tab.b91da221f6d21cd671287ee7a2c6dc85.png?auto=format"
     alt="Span Info tab" /%}

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com, ap2.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, app.datadoghq.com



When the service name is an override from the base service name, the top of the info section shows the:

- **[Base service](https://docs.datadoghq.com/tracing/guide/service_overrides#base-service)**: service from which the span is emitted, identified by the `@base_service` attribute.

- **[Service override](https://docs.datadoghq.com/tracing/guide/service_overrides)**: service name, different from the base service name, set automatically in Datadog integrations or changed via the programmatic API. The service override is identified by the `service` reserved attribute.

- **[Inferred service](https://docs.datadoghq.com/tracing/services/inferred_services)** (*when applicable*): name of the inferred entity being called by the base service, identified by one of the [peer attributes](https://docs.datadoghq.com/tracing/services/inferred_services#peer-tags).

  {% image
     source="https://datadog-docs.imgix.net/images/tracing/trace_view/base_override_inferred_service.b6c08234b9b89553addd7e3978d6ec74.png?auto=format"
     alt="Base, Override, and inferred service" /%}


{% /callout %}

{% /tab %}

{% tab title="Infrastructure" %}
Toggle between host-level and container-level (when available) infrastructure information for the selected span.

See associated tags, as well as critical host/container metrics graphs including CPU, Memory, and I/O with an overlay of when the trace occurred.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/infrastructure_tab.447e1bbcd8951c341ce012aad4b59629.png?auto=format"
   alt="Infrastructure tab" /%}

{% /tab %}

{% tab title="Logs" %}
See logs related to your service at the time of the trace. When you hover over a log, a line showing its timestamp is displayed on the trace flame graph. Clicking on the log brings you to the [Log Explorer search](https://docs.datadoghq.com/logs/explorer/search/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/connect_logs_and_traces/logs-trace-correlation.3fa4d93210758779eeb24beaf35e5da4.png?auto=format"
   alt="Logs in Traces" /%}

{% /tab %}

{% tab title="Processes" %}
Click on a service's span to see the processes running on its underlying infrastructure. A service's span processes are correlated with the hosts or pods on which the service runs at the time of the request. You can analyze process metrics such as CPU and RSS memory alongside code-level errors to distinguish between application-specific and wider infrastructure issues. Clicking on a process will bring you to the [Live Processes page](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows). To view span-specific processes, enable [process collection](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows#installation). Related processes are not currently supported for serverless and browser traces.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/processes_tab.cc8568299897e3c060043fa6f1a43b4b.png?auto=format"
   alt="Processes tab" /%}

{% /tab %}

{% tab title="Network" %}
Click on a service's span to see network dependencies of the service making the request. Use key network performance metrics such as volume, errors (TCP retransmits), and network latency (TCP round-trip time) to differentiate between application-specific and network-wide issues, especially when no code errors have been generated. For instance, you can use network telemetry to determine if high request latency is due to traffic overloading of the relevant application, or faulty dependencies with a downstream pod, security group, or any other tagged endpoint. Clicking on a process brings you to the [Network Analytics](https://docs.datadoghq.com/network_monitoring/performance/network_analytics) page. To view span-specific processes, enable [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/performance/setup).

**Note**: Related network telemetry is not currently supported for serverless traces.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/network_tab.f4c877db1fd55669dececbcc950e3fd2.png?auto=format"
   alt="Network tab" /%}

{% /tab %}

{% tab title="Security" %}
See attack attempts that target the services of the distributed trace. You can see the pattern used by the attacker, the rule that detects the attack, and whether the attacker found a vulnerability in your service.

Click **View in AAP** to investigate further using [Datadog App and API Protection](https://docs.datadoghq.com/security/application_security/how-it-works/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_view/security_tab.f75a880a1b4ff76453492a144da4e698.png?auto=format"
   alt="Security tab" /%}

{% /tab %}

{% tab title="Profiles" %}
View [Profiles](https://docs.datadoghq.com/profiler/connect_traces_and_profiles/#identify-code-hotspots-in-slow-traces) to identify lines of code related to performance issues. The values on the left side represent the time spent in each method call during the selected span.

{% image
   source="https://datadog-docs.imgix.net/images/profiler/profiles_tab.0e581f4836c2c600a56470f30a4c1ecf.png?auto=format"
   alt="Profiles tab showing time spent in each method for a selected span" /%}

{% /tab %}

{% tab title="Span Links" %}
[Span links](https://docs.datadoghq.com/tracing/trace_collection/span_links/) correlate one or more spans together that are causally related but don't have a typical parent-child relationship.

Click a span in the flame graph to display spans connected with span links:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/span_links/span_links_tab_2.3e7409ef1ab88eb6d387aff1190b4ca0.png?auto=format"
   alt="Span Links tab" /%}

**Note**: Span links only display when the corresponding spans are ingested and indexed, for example, with a [retention filter](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/).

To learn more about span links and how to add them with custom instrumentation, read [Span Links](https://docs.datadoghq.com/tracing/trace_collection/span_links/).
{% /tab %}

## Further Reading{% #further-reading %}

- [From performance to impact: Bridging frontend teams through shared context](https://www.datadoghq.com/blog/rum-product-analytics-bridging-teams)
- [Learn how to setup APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page/)
- [Dive into your resource performance and traces](https://docs.datadoghq.com/tracing/services/resource_page/)
- [Understand how to read a Datadog Trace](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/)
