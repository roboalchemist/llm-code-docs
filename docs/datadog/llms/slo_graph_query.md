# Source: https://docs.datadoghq.com/dashboards/guide/slo_graph_query.md

---
title: Scope metric-based SLO queries
description: >-
  Configure scoping and filtering for metric-based SLO queries using compatible
  semantic tags in dashboard widgets.
breadcrumbs: Docs > Dashboards > Graphing Guides > Scope metric-based SLO queries
---

# Scope metric-based SLO queries

{% alert level="info" %}
This feature is only available for **metric-based** SLO queries.
{% /alert %}

## Overview{% #overview %}

The [SLO widget](https://docs.datadoghq.com/dashboards/widgets/slo/) supports advanced metric query filtering, including the use of template variables to dynamically scope results displayed.

## Walk through of an SLO query{% #walk-through-of-an-slo-query %}

### Metric-based SLO query{% #metric-based-slo-query %}

First, create a [metric-based SLO](https://docs.datadoghq.com/service_level_objectives/metric/). This example uses APM trace metrics to measure the availability of an example service called `web-store`.

##### Good events (numerator){% #good-events-numerator %}

`sum:trace.rack.request.hits{service:web-store} by {resource_name}.as_count()``sum:trace.rack.request.errors{service:web-store} by {resource_name}.as_count()`

##### Total events (denominator){% #total-events-denominator %}

`sum:trace.rack.request.hits{service:web-store} by {resource_name}.as_count()`

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_graph_query/trace_metrics_slo.4d0ee168249fb6b14773f87fa1a1c43f.png?auto=format"
   alt="SLO configuration showing example trace metrics" /%}

### SLO widget{% #slo-widget %}

Select the SLO in the [SLO widget editor](https://docs.datadoghq.com/dashboards/widgets/slo/). You can apply additional filters in the widget configuration to further scope the results displayed. This does not modify the original definition of the SLO. In the example, we add the `$env` and `$availability-zone` tags to the **filter by** field of the widget.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/service_level_objectives/slo_graph_query/slo_filter_by.52464b7b1de0be3e365dbe0c09caa8fe.png?auto=format"
   alt="SLO Summary editor with dynamic tags for $env and $availability-zone" /%}

With this configuration, what happens when the [Dashboard template variable](https://docs.datadoghq.com/dashboards/template_variables/) is changed to `env:prod` and `availability-zone:northcentralus`?

The SLO widget filters the SLO metric queries by those additional tags for your visualization purposes:

##### Good events (numerator){% #good-events-numerator-1 %}

`sum:trace.rack.request.hits{service:web-store, env:prod, availability-zone:northcentralus} by {resource_name}.as_count()``sum:trace.rack.request.errors{service:web-store, env:prod, availability-zone:northcentralus} by {resource_name}.as_count()`

##### Total events (denominator){% #total-events-denominator-1 %}

`sum:trace.rack.request.hits{service:web-store, env:prod, availability-zone:northcentralus} by {resource_name}.as_count()`

## Further reading{% #further-reading %}

- [SLO Widget](https://docs.datadoghq.com/dashboards/widgets/slo/)
