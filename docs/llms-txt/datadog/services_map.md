# Source: https://docs.datadoghq.com/tracing/services/services_map.md

---
title: Service Map
description: The Service Map visualizes data that is being collected by Datadog APM.
breadcrumbs: Docs > APM > Service Observability > Service Map
source_url: https://docs.datadoghq.com/services/services_map/index.html
---

# Service Map

The Service Map decomposes your application into all its component [services](https://docs.datadoghq.com/tracing/glossary/#services) and draws the observed dependencies between these services in real time, so you can identify bottlenecks and understand how data flows through your architecture.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/service_map_overview_3.3b80f55bde2fa4baefdb2bdbdb92d7fb.png?auto=format"
   alt="Service Map Overview" /%}

## Setup{% #setup %}

The Service Map visualizes data collected by Datadog APM and RUM. Setup is not required to view [services](https://docs.datadoghq.com/tracing/glossary/#services).

## Ways to use it{% #ways-to-use-it %}

The Service Map provides an overview of your services and their health. This cuts through the noise and isolates problem areas. Also, you can access other telemetry collected by Datadog directly from this view.

## Identifying a service's dependencies{% #identifying-a-services-dependencies %}

The service map provides a complete picture of a service's dependencies, including those in different environments. For example, even if your service is only deployed in environment `prod`, the map reveals its connections to services in `staging` (and other environments).

## Grouping by Team or Application{% #grouping-by-team-or-application %}

The Service Map can be grouped by team or application to create a clear picture of service ownership and application dependencies. This is particularly useful as it enables visualization of complex microservice architecture on a more granular level to help organizations quickly reach the information they need.

## Filtering versus changing scopes{% #filtering-versus-changing-scopes %}

The Service Map can be filtered using facets or a fuzzy string match on service names. Facets are tags that Datadog automatically applies to service data, and include service type (for example, web server, database, cache), last deploy time, or monitor status. Filtering is particularly useful in a microservices environment with hundreds or thousands of nodes. Services can also be filtered by incident status to identify those involved in an ongoing or resolved incident and extract key information from the associated Service Page including incident data, resources, and Datadog Teams information. In addition, you can scope the Service Map to a specific time range, which helps keep track of your evolving architecture.

Services are also scoped by `env`, and optionally a [Second Primary Tag](https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog). Using the dropdowns to select a different scope draws an entirely different map consisting of the services within that scope. These services cannot call or be called by services in other environments.

## Inspection{% #inspection %}

Mousing over a service highlights it and shows its request traffic as animated lines to better emphasize directionality.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/servicemap-anim.mp4" /%}

Clicking a service offers you the option to inspect that service. This isolates the service, displays the source of requests from other services, and the requests for data sent by this service to other services. Generally, the services on the left are closer to your customers, and the ones on the right are more likely root causes.

On the inspection page, each node can be inspected allowing you to pivot around the Service Map one dependency at a time.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/servicemap.6eb19f8710f9ba56d10c67e639e5ea96.png?auto=format"
   alt="Service Map" /%}

A node is collapsed when there are two services in the filter (applied through the search bar or facets) that are connected by one or more services which are not in the filter.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/service_map_collapsed.378cf4863db825f89c2c1951718ce83b.png?auto=format"
   alt="Service Map Collapsed Node" /%}

## The "service" tag{% #the-service-tag %}

Clicking on a service reveals further filtering options:

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/service_map_inspect_menu_2.159fcc7d809336fd9e8f8f15c6e128b3.png?auto=format"
   alt="Service Map tag" /%}

The service tag has a special meaning in Datadog, and is used both to identify APM services and to link them to other parts of the product.

The following screenshot shows a dashboard query for `service:fse-auto-process`. This is tagged automatically by APM.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/servicedash.e66aad42b24e92cbff20406fe09a16a4.png?auto=format"
   alt="Service Map dashboard" /%}

Using this tag on your Host Map or logs with the same key allows Datadog to join applications to logs, infrastructure, or custom business metrics. On the visualization menu shown above, each option pivots to the appropriate view of the collected data scoped to your `service`.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/servicemaptags.41b299c55429d6e5695bddba1e939c78.png?auto=format"
   alt="Service Map tags" /%}

Additionally, monitors can be tagged by service in the **Say what's happening** section. This allows you to associate monitors for any metric, including custom business metrics, with your services. The status of monitors is exposed directly on the Service Map.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/servicemon.a4f931f76be4d92e431e44778e4fbcd5.png?auto=format"
   alt="Service Map monitor" /%}

## Data freshness and meaning{% #data-freshness-and-meaning %}

### Nodes and edges{% #nodes-and-edges %}

Nodes represent services exactly as instrumented in APM and match those in your [Software Catalog](https://app.datadoghq.com/services). Edges represent aggregate calls from one service to another. These interactions are shown on the flame graph for each individual [trace](https://docs.datadoghq.com/tracing/glossary/#trace).

New services or connections appear within moments of being instrumented and automatically age out if no corresponding traces are seen for 30 days. You can query any service map to view nodes that have data within the last 30 days. Nodes only appear in the graph if they have data within the selected time frame.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/visualization/services_map/servicenodes.mp4" /%}

### Color{% #color %}

Service node borders are colored with red or yellow depending on their respective Service Health state. [Service Health](https://docs.datadoghq.com/tracing/services/service_page/#service-health) consolidates signals across Watchdog anomalies, paging monitors, and incidents into one single health state for each service. Use Service Health to quickly identify services that require immediate attention.

### Availability{% #availability %}

The Service Map is rendered based on complete traces that include the root spans. When some spans are missing during the query window you specify, the map view may be unavailable for that time period. This may happen when [APM connection errors](https://docs.datadoghq.com/tracing/troubleshooting/connection_errors) occur and spans get dropped.

## Further Reading{% #further-reading %}

- [Learn how to setup APM tracing with your application](https://docs.datadoghq.com/tracing/trace_collection/)
- [Introducing the Service Map in Datadog](https://www.datadoghq.com/blog/service-map/)
- [Creating context with service maps (Datadog + Airbnb)](https://www.datadoghq.com/videos/dash-keynote-creating-context-with-service-maps/)
