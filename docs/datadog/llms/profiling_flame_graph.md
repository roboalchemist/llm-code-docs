# Source: https://docs.datadoghq.com/dashboards/widgets/profiling_flame_graph.md

---
title: Profiling Flame Graph Widget
description: Graph a breakdown of top consuming lines of code (CPU, Memory, ...)
breadcrumbs: Docs > Dashboards > Widgets > Profiling Flame Graph Widget
---

# Profiling Flame Graph Widget

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/profiling_flame_graph/profiling_flame_graph.f3005b9b757b81f45be34569dd5f5382.png?auto=format"
   alt="Profiling Flame Graph" /%}

The [profiling flame graph visualization](https://docs.datadoghq.com/profiler/profile_visualizations/#flame-graph) represents a breakdown of top consuming lines of code such as CPU and Memory. Add this widget to visualize stack traces of your profiled applications and accurately identify frequent resource requests.

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/profiling_flame_graph/profiling_flame_graph_config.49bf7b6a5a6da22e0534996bbd91bddc.png?auto=format"
   alt="Graph your data section in the profiling flame graph widget configuration" /%}

### Configuration{% #configuration %}

1. Scope your profiling data with tags. For example, `host`, `container_name`, `service`, `env`, or `version`.
1. To select the resource click the dropdown menu next to **Show**. Options can include `CPU Time`, `Allocated Memory`, or `Thrown Exceptions`.
1. Click the dropdown menu next to **by** and **for** to select the frame granularity and code provenance, respectively.
1. Give your graph a title or leave the box blank for the suggested title.
1. Click **Save**.

### Options{% #options %}

#### Advanced options and filtering{% #advanced-options-and-filtering %}

Click the three dot ellipsis to open Advanced options to specify coloring and resolution.

Customize your flame graph. Add graphing actions or filters in the *Filter flame graph* field.

#### Scope to endpoints{% #scope-to-endpoints %}

Filter on a specific endpoint, for total consumption (`per Minute by Endpoint`) or per request (`per Endpoint Call`).

#### Scope to functions{% #scope-to-functions %}

Filter on other criteria such as `Method`, `Package`, `Thread name` or `Trace Operation`.

#### Global time{% #global-time %}

Choose whether your widget has a custom timeframe or the dashboard's global timeframe.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/).

## Further Reading{% #further-reading %}

- [Learn about Profile visualizations](https://docs.datadoghq.com/profiler/profile_visualizations/)
- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
