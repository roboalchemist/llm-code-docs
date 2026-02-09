# Source: https://docs.datadoghq.com/watchdog/insights.md

---
title: Watchdog Insights
description: >-
  View anomalies and outliers that match your search query with Watchdog
  Insights.
breadcrumbs: Docs > Datadog Watchdogâ¢ > Watchdog Insights
---

# Watchdog Insights

## Overview{% #overview %}

Investigating an incident requires trial and error. Drawing from their experience, engineers familiar with a particular area know where to first look for potential problems. Using Watchdog Insights allows all engineers, including less experienced ones, to pay attention to the most important data and accelerate their incident investigations.

Throughout most of Datadog, Watchdog returns two types of insights:

- **Anomalies**: All the pre-calculated [Watchdog alerts](https://docs.datadoghq.com/watchdog/#overview) matching the active search query that Watchdog found by scanning your organization's data. Access the full list in the [Watchdog Alert explorer](https://app.datadoghq.com/watchdog).
- **Outliers**: Tags that appear too frequently in some event types (for example, errors) or drive some continuous metrics upwards (for example, latency). Outliers are dynamically calculated on the data matching the active query and the time frame.

{% image
   source="https://datadog-docs.imgix.net/images/logs/explorer/watchdog_insights/insights-for-log-explorer.aea00acf4cce10aaacc1f780dceae245.png?auto=format"
   alt="The log explorer showing the Watchdog Insights banner with five log anomalies" /%}

## Explore insights{% #explore-insights %}

The Watchdog Insights carousel sits near the top of the following product pages:

- [Log explorer](https://app.datadoghq.com/logs)
- APM:
  - [Trace Explorer](https://app.datadoghq.com/apm/traces)
  - [Service Page](https://docs.datadoghq.com/tracing/services/service_page/)
  - [Resource Page](https://docs.datadoghq.com/tracing/services/resource_page/)
  - [Database Explorer](https://app.datadoghq.com/databases/list)
  - [Profile Explorer](https://app.datadoghq.com/profiling/explorer)
- Infrastructure:
  - [Processes Explorer](https://app.datadoghq.com/process)
  - [Serverless Explorer](https://app.datadoghq.com/functions)
  - [Kubernetes Explorer](https://app.datadoghq.com/orchestration/overview/pod)
  - [Real User Monitoring (RUM) Explorer](https://app.datadoghq.com/rum/sessions?query=%40type%3Aview)
  - [Synthetic Monitoring & Testing Explorer](https://app.datadoghq.com/synthetics/explorer)
  - [Error Tracking issue side panel](https://app.datadoghq.com/rum/error-tracking)

Expand the carousel for an overview. The highest priority insights (based on `Insight type`, `State`, `Status`, `Start time`, `Anomaly type`) appear on the left.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/log_explorer_watchdog_insights.2d89bfd74399bd3e6cfb9575d50b475f.png?auto=format"
   alt="The Watchdog Insights carousel on the Log Explorer, showing three anomalies: new error logs in the web-store service, a spike in error logs in the product-recommendation service, and another spike in error logs in the product-recommendation service" /%}

Click **View all** to expand the panel. A side panel opens from the right, containing a vertical list of Watchdog Insights. Each entry shows a detailed view, with more information than the summary card.

Every outlier comes with embedded interactions and a side panel with troubleshooting information. Each Insight's interactions and side panel vary based on the Watchdog Insight type.

### Filter on Insight query{% #filter-on-insight-query %}

To refine your current view to match a Watchdog Insight, hover over the top right corner of an Insight summary card. Two icons appear. Click on the inverted triangle icon with the tooltip **Filter on Insight**. The page refreshes to show a list of entries corresponding to the insight. **Note**: Filtering on Watchdog Insights automatically changes the scope you're looking at. As a result, if you select an outlier insight, it is no longer visible, as it is treated as the baseline.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/filter_on_insight.f90729411539c28c4bf977ea645679bb.png?auto=format"
   alt="Filtering the explorer on the insight context" /%}

### Share an outlier{% #share-an-outlier %}

To share a given outlier, click on it in the insight panel to open the details side panel. Click the **Copy Link** button at the top of the details panel:

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/share-outlier.8007fc2d6ffd36524308d3e0a0aeccde.png?auto=format"
   alt="Outlier side panel showing how to copy the link" /%}

The link to the outlier expires with the retention of the underlying data. For instance, if the logs used to build the outlier are retained for 15 days, the link to the outlier expires with the logs after 15 days.

## Explore graph insights with Watchdog explains{% #explore-graph-insights-with-watchdog-explains %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/graph_insights/watchdog_explains/graph_filter_tag.ba837d8e39c98021e6f069188047449e.png?auto=format"
   alt="Filter out the offending tag, in this case researcher-query, to compare the original against what the graph would look like without the offending tag" /%}

Datadog collects various types of data to provide insights into application performance, including metrics, traces, and logs, which tell you what, how, and why something is happening. Watchdog Explains analyzes high-level trends such as latency, error rates, or request count evolution to detect critical signals. Upon observing a spike in these graphs, Watchdog Explains helps you investigate the immediate questions:

- What is the source of the spike?
- Does this anomaly affect everyone or is an isolated incident?

For more information, see the [Watchdog Explains](https://docs.datadoghq.com/dashboards/graph_insights/watchdog_explains) documentation.

## Outlier types{% #outlier-types %}

{% tab title="Log Management" %}
### Error outliers{% #error-outliers %}

Error outliers display fields such as [faceted tags or attributes](https://docs.datadoghq.com/logs/explorer/facets/) containing characteristics of errors that match the current query. Statistically overrepresented `key:value` pairs among errors provide hints into the root causes of problems.

Typical examples of error outliers include `env:staging`, `docker_image:acme:3.1`, and `http.useragent_details.browser.family:curl`.

In the banner card view, you can see:

- The field name
- The proportion of errors and overall logs that the field contributes to

{% image
   source="https://datadog-docs.imgix.net/images/logs/explorer/watchdog_insights/error_outlier_s_card.2d48225813493400ae713155c4e3a992.png?auto=format"
   alt="The error outlier card showing a red bar with 73.3% of total errors and a blue bar with 8.31% of total errors" /%}

In the full side panel view, you can see:

- The timeseries of error logs that contain the field
- Tags that are often associated with the error logs
- A comprehensive list of [log patterns](https://docs.datadoghq.com/logs/explorer/analytics/patterns)

{% image
   source="https://datadog-docs.imgix.net/images/logs/explorer/watchdog_insights/error_outlier_side_panel.aff0751da0bbf40eb477f3e732bb09b1.png?auto=format"
   alt="Error Outlier side panel" /%}

{% /tab %}

{% tab title="APM" %}
APM outliers are available on all APM pages where the Watchdog Insights carousel is available:

- [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/?tab=listview)
- [Service Page](https://docs.datadoghq.com/tracing/services/service_page/)
- [Resource Page](https://docs.datadoghq.com/tracing/services/resource_page/)

### Error outliers{% #error-outliers %}

Error outliers display fields such as tags containing characteristics of errors that match the current query. Statistically overrepresented `key:value` pairs among errors provide hints into the root cause of problems.

Typical examples of error outliers include `env:staging`, `availability_zone:us-east-1a`, `cluster_name:chinook`, and `version:v123456`.

In the banner card view, you can see:

- The field name
- The proportion of errors and overall traces that the field contributes to

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/watchdog_insights/error_outlier_s_card.4b392e8562103c19c5c6bb5493c6cbfb.png?auto=format"
   alt="The error outlier card showing a red bar with 24.2% of total errors and a blue bar with 12.1% of total errors" /%}

In the full side panel view, you can see:

- The timeseries of error traces that contain the field
- Tags that are often associated with the error traces
- A comprehensive list of related Error Tracking Issues and failing spans

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/watchdog_insights/error_outlier_side_panel.4c36c832b636fd2fd4e16519b016823c.png?auto=format"
   alt="Error Outlier side panel" /%}

### Latency outliers{% #latency-outliers %}

Latency outliers display fields such as tags that are associated with performance bottlenecks that match the current search query. `key:value` pairs with worse performance than the baseline can provide hints into the performance bottlenecks among a subset of APM spans.

Latency outliers are computed for the span duration.

In the banner card view, you can see:

- The field name

- The latency distribution for spans containing the tag and the baseline for the rest of the data

- A percentile of interest latency value for the outlier tag and the difference with the baseline for the rest of the data

  {% image
     source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/watchdog_insights/latency_outliers_s_card.00b81a9ea3cd66d43ae01a6654c28d63.png?auto=format"
     alt="Latency Outlier banner card" /%}

In the full side panel, you can see a latency distribution graph for the tag and the baseline. The X axis has increments of `p50`, `p75`, `p99`, and `max`, along with a list of APM events that contain the field.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/trace_explorer/watchdog_insights/latency_outlier_side_panel.848d7b993e0a9d7a067550e3a1b7c05b.png?auto=format"
   alt="Latency Outlier full side panel view" /%}

{% /tab %}

{% tab title="Profiling" %}
### Lock contention outlier{% #lock-contention-outlier %}

In the banner card view, you can see:

- The name of the impacted service
- The number of threads impacted
- The potential CPU savings (and estimated cost savings)

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/small_card_profiling_lock_pressure.aeb32f105fcf9a1574f3f891f03dd2a7.png?auto=format"
   alt="Profiling insight on Lock Contention" /%}

In the full side panel, you can see instructions on how to resolve the lock contention:

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/side_panel_profiling_lock_pressure.d870fcb80ef8452a43bed7a8881fe94e.png?auto=format"
   alt="Side panel with all the information on how to address the Lock Contention outlier" /%}

### Garbage collection outlier{% #garbage-collection-outlier %}

In the banner card view, you can see:

- The name of the impacted service
- The amount of CPU time used to perform garbage collection

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/small_card_profiling_garbage_collection.f74738fab09c0b12446d2183cf119301.png?auto=format"
   alt="Profiling insight on Garbage Collection" /%}

In the full side panel, you can see instructions on how to better configure garbage collection to free up some CPU time:

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/side_panel_profiling_garbage_collection.aac266e99fee4f9d4891e26d5c31c89b.png?auto=format"
   alt="Side panel with all the information on how to address the Garbage Collection outlier" /%}

### Regex compilation outlier{% #regex-compilation-outlier %}

In the banner card view, you can see:

- The name of the impacted service
- The amount of CPU time spent on compiling regexes

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/small_card_profiling_regex_compilation.db8a1bfcfcf21cdf9fdfc3b2e2dbbcd8.png?auto=format"
   alt="Profiling insight on Regex Compilation" /%}

In the full side panel, you can see instructions on how to improve regex compilation time, as well as examples of functions within your code that could be improved:

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/side_panel_profiling_regex_compilation.3ceb76b372ba8ffeae8e40a81a27e69b.png?auto=format"
   alt="Side panel with all the information on how to address the Regex Compilation outlier" /%}

{% /tab %}

{% tab title="Databases" %}
For Database Monitoring, Watchdog surfaces insights on the following metrics:

- `CPU`
- `Commits`
- `IO`
- `Background`
- `Concurrency`
- `Idle`

Find the databases impacted by one or multiple outliers by using the Insight carousel.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/side_panel_dbm_insights.21f4839001ba1f46b8fd68c07a2104f4.png?auto=format"
   alt="Carousel to filter the Databases with Insights" /%}

An overlay is then set on the databases, with pink pills highlighting the different Insights and giving more information about what happened.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/overlay_database_insight.a28f46fedcfc4f30ce937d12ae650d58.png?auto=format"
   alt="Watchdog insight overlay on the database to highlight what is happening" /%}

{% /tab %}

{% tab title="RUM" %}
### Error outlier{% #error-outlier %}

Error outliers display fields such as [faceted tags or attributes](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/monitoring_page_performance/#monitoring-single-page-applications-spa) that contain characteristics of errors that match the current search query. Statistically overrepresented `key:value` pairs among errors can provide hints into the root causes of issues. Typical examples of error outliers include `env:staging`, `version:1234`, and `browser.name:Chrome`.

In the banner card view, you can see:

- The field name
- The proportion of total errors and overall RUM events that the field contributes to
- Related tags

In the full side panel, you can see a timeseries graph about the total number of RUM errors with the field, along with impact pie charts and a list of RUM events that contain the field.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/explorer/watchdog_insights/error_outlier_side_panel-1.6552e4fcb2cba8372d5c560179200b6d.png?auto=format"
   alt="Error Outlier full side panel" /%}

### Latency outlier{% #latency-outlier %}

Latency outliers display fields such as [faceted tags or attributes](https://docs.datadoghq.com/real_user_monitoring/explorer/search/#facets) that are associated with performance bottlenecks that match the current search query. `key:value` pairs with worse performance than the baseline can provide hints into the performance bottlenecks among a subset of real users.

Latency outliers are computed for [Core Web Vitals](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/monitoring_page_performance/#event-timings-and-core-web-vitals) such as First Contentful Paint, First Input Delay, Cumulative Layout Shift, and [Loading Time](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/monitoring_page_performance/#monitoring-single-page-applications-spa). For more information, see [Monitoring Page Performance](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/monitoring_page_performance/#event-timings-and-core-web-vitals).

In the banner card view, you can see:

- The field name
- The performance metric value containing the field and the baseline for the rest of the data

In the full side panel, you can see a timeseries graph about the performance metric. The X axis has increments of `p50`, `p75`, `p99`, and `max`, along with a list of RUM events that contain the field.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/explorer/watchdog_insights/latency_outlier_side_panel-1.b4f87685d6b69ced2e3d2dfeb76d14f7.png?auto=format"
   alt="Latency Outlier full side panel view" /%}

{% /tab %}

{% tab title="Synthetic Monitoring" %}
### Error outliers{% #error-outliers %}

Error outliers in Synthetic Monitoring display unexpected behaviors and performance deviations. These anomalies provide insights into the reliability issues in your [Synthetic Browser Tests](https://docs.datadoghq.com/synthetics/browser_tests). Identifying these error outliers helps you troubleshoot errors in failed test runs, enhancing debugging and reducing Mean Time To Resolution (MTTR).

When reviewing failed test runs, you can see the number of error outliers on the failed test:

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/synthetics_watchdog_outlier.c4628b907b6f435962034ff61dec4948.png?auto=format"
   alt="An overview of a failed browser test run with test step details and the error message which was identified as an error outlier for a failing test step by Watchdog" /%}

To view the error outlier message, click on the outlier. Then, on the test step side panel, click the **Errors & Warnings** tab.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/outlier_step_error_2.9fc120d0a7dbe44ae9267ace748c4a6d.png?auto=format"
   alt="An error message which was identified as an error outlier for a failing test step by Watchdog" /%}

{% /tab %}

{% tab title="Serverless" %}
For serverless infrastructures, Watchdog surfaces the following insights:

- `Cold Start Ratio Up/Down`
- `Error Invocation Ratio Up/Down`
- `Memory Usage Up/Down`
- `OOM Ratio Up/Down`
- `Estimated Cost Up/Down`
- `Init Duration Up/Down`
- `Runtime Duration Up/Down`

Find the serverless functions impacted by one or multiple outliers by using the Insights carousel.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/side_panel_serverless_facet_insights.a2cfe97027d391f8ca7844959a6a143c.png?auto=format"
   alt="Facet to filter the Serverless Functions with insights" /%}

An overlay is then set on the function, with pink pills highlighting the different insights and giving more information about what happened.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/overlay_serverless_insight.485754ca550e153cfd8b4244ea6c4b5f.png?auto=format"
   alt="Watchdog insight overlay on the function to highlight what is happening" /%}

{% /tab %}

{% tab title="Processes" %}
For Process Explorer, the Watchdog Insight carousel reflects [all Process anomalies](https://app.datadoghq.com/process) for the current context of the Process Explorer.
{% /tab %}

{% tab title="Kubernetes" %}
For Kubernetes Explorer, the Watchdog Insight carousel reflects [all the Kubernetes anomalies](https://app.datadoghq.com/orchestration/overview/pod) for the current context of the Kubernetes Explorer.
{% /tab %}

## Further reading{% #further-reading %}

- [Watchdog Insights for Logs](https://docs.datadoghq.com/logs/explorer/watchdog_insights/)
- [Watchdog Insights for RUM](https://docs.datadoghq.com/real_user_monitoring/explorer/watchdog_insights/)
- [Augmented troubleshooting with Watchdog Insights](https://www.datadoghq.com/blog/datadog-watchdog-insights-log-management/)
- [Automatically detect error and latency patterns with Watchdog Insights for APM](https://www.datadoghq.com/blog/watchdog-insights-apm/)
