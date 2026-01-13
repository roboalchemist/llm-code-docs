# Source: https://docs.datadoghq.com/tracing/glossary.md

---
title: APM Terms and Concepts
description: >-
  Learn essential APM terminology including services, resources, traces, spans,
  instrumentation, and other key concepts for distributed tracing.
breadcrumbs: Docs > APM > APM Terms and Concepts
source_url: https://docs.datadoghq.com/glossary/index.html
---

# APM Terms and Concepts

## Overview{% #overview %}

The APM UI provides many tools to troubleshoot application performance and correlate it throughout the product, enabling you to find and resolve issues in distributed systems.

For additional definitions and descriptions of important APM terms such as *spans* and *indexed*, see the [main Glossary](https://docs.datadoghq.com/glossary/).

| Concept                                                    | Description                                                                                                                                                                                                          |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service                                                    | Services are the building blocks of modern microservice architectures - broadly a service groups together endpoints, queries, or jobs for the purposes of building your application.                                 |
| Resource                                                   | Resources represent a particular domain of a customer application - they are typically an instrumented web endpoint, database query, or background job.                                                              |
| [Monitors](https://docs.datadoghq.com/monitors/types/apm/) | APM metric monitors work like regular metric monitors, but with controls tailored specifically to APM. Use these monitors to receive alerts at the service level on hits, errors, and a variety of latency measures. |
| Trace                                                      | A trace is used to track the time spent by an application processing a request and the status of this request. Each trace consists of one or more spans.                                                             |
| Trace Context Propagation                                  | The method of passing trace identifiers between services, enabling Datadog to stitch together individual spans into a complete distributed trace.                                                                    |
| Retention Filters                                          | Retention filters are tag-based controls set within the Datadog UI that determine what spans to index in Datadog for 15 days.                                                                                        |
| Ingestion Controls                                         | Ingestion controls are used to send up to 100% of traces to Datadog for live search and analytics for 15 minutes.                                                                                                    |
| Instrumentation                                            | Instrumentation is the process of adding code to your application to capture and report observability data.                                                                                                          |
| Baggage                                                    | Baggage is contextual information that is passed between traces, metrics, and logs in the form of key-value pairs.                                                                                                   |

## Services{% #services %}

After [instrumenting your application](https://docs.datadoghq.com/tracing/setup/), the [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/) is your main landing page for APM data.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/software_catalog.f0302962968f5fd79aad81bd62e8dbdb.png?auto=format"
   alt="Software Catalog" /%}

Services are the building blocks of modern microservice architectures - broadly a service groups together endpoints, queries, or jobs for the purposes of scaling instances. Some examples:

- A group of URL endpoints may be grouped together under an API service.
- A group of DB queries that are grouped together within one database service.
- A group of periodic jobs configured in the crond service.

The screenshot below is a microservice distributed system for an e-commerce site builder. There's a `web-store`, `ad-server`, `payment-db`, and `auth-service` all represented as services in APM.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/service_map.d4ec11dc6e498babe0a48df755566b89.png?auto=format"
   alt="service map" /%}

All services can be found in the [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/) and visually represented on the [Service Map](https://docs.datadoghq.com/tracing/services/services_map/). Each service has its own [Service page](https://docs.datadoghq.com/tracing/services/service_page/) where trace metrics like throughput, latency, and error rates can be viewed and inspected. Use these metrics to create dashboard widgets, create monitors, and see the performance of every resource such as a web endpoint or database query belonging to the service.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/visualization/service_page.mp4" /%}

{% alert level="info" %}
Don't see the HTTP endpoints you were expecting on the Service page? In APM, endpoints are connected to a service by more than the service name. It is also done with the `span.name` of the entry-point span of the trace. For example, on the web-store service above, `web.request` is the entry-point span. More info on this [here](https://docs.datadoghq.com/tracing/faq/resource-trace-doesn-t-show-up-under-correct-service/).
{% /alert %}

## Resources{% #resources %}

Resources represent a particular domain of a customer application. They could typically be an instrumented web endpoint, database query, or background job. For a web service, these resources can be dynamic web endpoints that are grouped by a static span name - `web.request`. In a database service, these would be database queries with the span name `db.query`. For example the `web-store` service has automatically instrumented resources - web endpoints - which handle checkouts, updating carts, adding items, and so on. A Resource name can be the HTTP method and the HTTP route, for example `GET /productpage` or `ShoppingCartController#checkout`.

Each resource has its own [Resource page](https://docs.datadoghq.com/tracing/services/resource_page/) with [trace metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/) scoped to the specific endpoint. Trace metrics can be used like any other Datadog metric - they are exportable to a dashboard or can be used to create monitors. The Resource page also shows the span summary widget with an aggregate view of [spans](https://docs.datadoghq.com/glossary/#span) for all traces, latency distribution of requests, and traces which show requests made to this endpoint.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/visualization/resource_page.mp4" /%}

## Trace{% #trace %}

A trace is used to track the time spent by an application processing a request and the status of this request. Each trace consists of one or more spans. During the lifetime of the request, you can see distributed calls across services (because a [trace-id is injected/extracted through HTTP headers](https://docs.datadoghq.com/tracing/opentracing/java/#create-a-distributed-trace-using-manual-instrumentation-with-opentracing)), [automatically instrumented libraries](https://docs.datadoghq.com/tracing/setup/), and [manual instrumentation](https://docs.datadoghq.com/tracing/manual_instrumentation/) using open-source tools like [OpenTracing](https://docs.datadoghq.com/tracing/opentracing/) in the flame graph view. In the Trace View page, each trace collects information that connects it to other parts of the platform, including [connecting logs to traces](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/), [adding tags to spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/otel_instrumentation/), and [collecting runtime metrics](https://docs.datadoghq.com/tracing/metrics/runtime_metrics/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/trace_view.dc772c4e9aae55f6497eab679edc5c59.png?auto=format"
   alt="trace view" /%}

## Trace context propagation{% #trace-context-propagation %}

Trace context propagation is the method of passing trace identifiers between services in a distributed system. It enables Datadog to stitch together individual spans from different services into a single distributed trace. Trace context propagation works by injecting identifiers, such as the trace ID and parent span ID, into HTTP headers as the request flows through the system. The downstream service then extracts these identifiers and continues the trace. This allows the Datadog to reconstruct the full path of a request across multiple services.

For more information, see the [propagating the trace context](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation) for your application's language.

## Retention filters{% #retention-filters %}

[Set tag-based filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#retention-filters) in the UI to index spans for 15 days for use with [Trace Search and Analytics](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#trace-search-and-analytics-on-indexed-spans).

## Ingestion controls{% #ingestion-controls %}

[Send 100% of traces](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/) from your services to Datadog and combine with tag-based retention filters to keep traces that matter for your business for 15 days.

## Instrumentation{% #instrumentation %}

Instrumentation is the process of adding code to your application to capture and report observability data to Datadog, such as traces, metrics, and logs. Datadog provides instrumentation libraries for various programming languages and frameworks.

You can automatically instrument your application when you install the Datadog Agent with [Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm) or when you [manually add Datadog tracing libraries](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/) to your code.

You can use custom instrumentation by embedding tracing code directly into your application code. This allows you to programmatically create, modify, or delete traces to send to Datadog.

To learn more, read [Application Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/).

## Baggage{% #baggage %}

Baggage allows you to propagate key-value pairs (also known as baggage items) across service boundaries in a distributed system. Unlike trace context, which focuses on trace identifiers, baggage allows for the transmission of business data and other contextual information alongside traces.

To learn more, read supported [propagation formats](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/#supported-formats) for your application's language.

## Further Reading{% #further-reading %}

- [Learn how to set up APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Discover and catalog the services reporting to Datadog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Learn more about services in Datadog](https://docs.datadoghq.com/tracing/services/service_page/)
- [Dive into your resource performance and traces](https://docs.datadoghq.com/tracing/services/resource_page/)
- [Learn how to read a trace in Datadog](https://docs.datadoghq.com/tracing/trace_explorer/trace_view/)
- [Learn about APM monitors](https://docs.datadoghq.com/monitors/types/apm/)
