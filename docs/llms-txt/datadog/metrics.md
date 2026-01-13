# Source: https://docs.datadoghq.com/tracing/trace_pipeline/metrics.md

# Source: https://docs.datadoghq.com/tracing/metrics.md

# Source: https://docs.datadoghq.com/metrics.md

---
title: Metrics
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Metrics
source_url: https://docs.datadoghq.com/index.html
---

# Metrics

{% callout %}
##### Join an enablement webinar session

Explore and register for Foundation Enablement sessions for custom metrics. Learn how custom metrics help you track your application KPIs, such as the number of visitors, average customer basket size, request latency, or performance distribution for a custom algorithm.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Metrics)
{% /callout %}

This is an introduction to Metrics in Datadog and why they're useful. This section includes the following topics:

- [Submit Custom Metrics- Learn what custom metrics are and how to submit them.](https://docs.datadoghq.com/metrics/custom_metrics)
- [Send OpenTelemetry Metrics- Configure the Datadog Agent or OpenTelemetry Collector.](https://docs.datadoghq.com/opentelemetry/reference/otel_metrics)
- [Metrics Types- Types of metrics that can be submitted to Datadog.](https://docs.datadoghq.com/metrics/types)
- [Distribution Metrics- Learn about Distribution Metrics and globally accurate percentiles.](https://docs.datadoghq.com/metrics/distributions)
- [Metrics Units- Learn about the units that can be associated with metrics.](https://docs.datadoghq.com/metrics/units)

- [Metrics Explorer- Explore all of your metrics and perform Analytics.](https://docs.datadoghq.com/metrics/explorer)
- [Metrics Summary- Understand your actively reporting Datadog metrics.](https://docs.datadoghq.com/metrics/summary)
- [Advanced Filtering- Filter your data to narrow the scope of metrics returned.](https://docs.datadoghq.com/metrics/advanced-filtering)
- [Nested Queries- Apply additional layers of aggregation to unlock advanced querying capabilities.](https://docs.datadoghq.com/metrics/nested_queries)

- [Metrics without Limitsâ¢- Learn how to control custom metrics volumes with tag configurations using Metrics without Limitsâ¢.](https://docs.datadoghq.com/metrics/metrics-without-limits/)

## Overview{% #overview %}

### What are metrics?{% #what-are-metrics %}

Metrics are numerical values that can track anything about your environment over time, from latency to error rates to user signups.

In Datadog, metric data is ingested and stored as data points with a value and timestamp:

```text
[ 17.82,  22:11:01 ]
```

A sequence of data points is stored as a timeseries:

```text
[ 17.82,  22:11:01 ]
[  6.38,  22:11:12 ]
[  2.87,  22:11:38 ]
[  7.06,  22:12:00 ]
```

Any metrics with fractions of a second timestamps are rounded to the nearest second. If any points have the same timestamp, the latest point overwrites the previous ones.

### Why are metrics useful?{% #why-are-metrics-useful %}

Metrics provide an overall picture of your system. You can use them to assess the health of your environment at a glance. Visualize how quickly users are loading your website, or the average memory consumption of your servers, for instance. Once you identify a problem, you can use [logs](https://docs.datadoghq.com/logs) and [tracing](https://docs.datadoghq.com/tracing/) to further troubleshoot.

Metrics that track system health come automatically through Datadog's integrations with more than 1,000 services. You can also track metrics that are specific to your businessâalso known as custom metrics. You can track things such as the number of user logins or user cart sizes to the frequency of your team's code commits.

In addition, metrics can help you adjust the scale of your environment to meet the demand from your customers. Knowing exactly how much you need to consume in resources can help you save money or improve performance.

### Submitting metrics to Datadog{% #submitting-metrics-to-datadog %}

Metrics can be sent to Datadog from several places.

- [Datadog-Supported Integrations](https://docs.datadoghq.com/integrations/): Datadog's 1,000+ integrations include metrics out of the box. To access these metrics, navigate to the specific integration page for your service and follow the installation instructions there. If you need to monitor an EC2 instance, for example, you would go to the [Amazon EC2 integration documentation](https://docs.datadoghq.com/integrations/amazon_ec2/).

- You can generate metrics directly within the Datadog platform. For instance, you can count error status codes appearing in your logs and [store that as a new metric](https://docs.datadoghq.com/logs/logs_to_metrics/) in Datadog.

- Often, you'll need to track metrics related to your business (for example, number of user logins or signups). In these cases, you can create [custom metrics](https://docs.datadoghq.com/metrics/custom_metrics/). Custom metrics can be submitted through the [Agent](https://docs.datadoghq.com/agent/), [DogStatsD](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/), or the [HTTP API](https://docs.datadoghq.com/api/).

- Additionally, the [Datadog Agent](https://docs.datadoghq.com/agent/basic_agent_usage/) automatically sends several standard metrics (such as CPU and disk usage).

For a summary of all metric submission sources and methods, read the [Metrics Types documentation](https://docs.datadoghq.com/metrics/types/).

### Metric types and real-time metrics visibility{% #metric-types-and-real-time-metrics-visibility %}

#### Metric types{% #metric-types %}

Datadog supports several different metric types that serve distinct use cases: count, gauge, rate, histogram, and distribution. Metric types determine which graphs and functions are available to use with the metric in the app.

The Datadog Agent doesn't make a separate request to Datadog's servers for every single data point you send. Instead, it reports values collected over a *flush time interval*. The metric's type determines how the values collected from your host over this interval are aggregated for submission.

A ***count*** type adds up all the submitted values in a time interval. This would be suitable for a metric tracking the number of website hits, for instance.

The ***rate*** type takes the count and divides it by the length of the time interval. This is useful if you're interested in the number of hits per second.

A ***gauge*** type takes the last value reported during the interval. This type would make sense for tracking RAM or CPU usage, where taking the last value provides a representative picture of the host's behavior during the time interval. In this case, using a different type such as *count* would probably lead to inaccurate and extreme values. Choosing the correct metric type ensures accurate data.

A ***histogram*** reports five different values summarizing the submitted values: the average, count, median, 95th percentile, and max. This produces five different timeseries. This metric type is suitable for things like latency, for which it's not enough to know the average value. Histograms allow you to understand how your data was spread out without recording every single data point.

A ***distribution*** is similar to a histogram, but it summarizes values submitted during a time interval across all hosts in your environment. You can also choose to report multiple percentiles: p50, p75, p90, p95, and p99. You can learn more about this powerful feature in the [Distributions documentation](https://docs.datadoghq.com/metrics/distributions/).

See the [metrics types](https://docs.datadoghq.com/metrics/types/) documentation for more detailed examples of each metric type and submission instructions.

## Querying metrics{% #querying-metrics %}

You can visualize your metrics and create graphs throughout Datadog: in [Metrics Explorer](https://docs.datadoghq.com/metrics/explorer/), [Dashboards](https://docs.datadoghq.com/dashboards/), or [Notebooks](https://docs.datadoghq.com/notebooks/).

**Tip**: To open the Metrics Summary page from Datadog's global search, press `Cmd`/`Ctrl` + `K` and search for `metrics`.

Here's an example of a timeseries visualization:

{% image
   source="https://datadog-docs.imgix.net/images/metrics/introduction/timeseries_example.e5c8f05d164e5120ee2fbe69325a4dc8.png?auto=format"
   alt="A timeseries graph displays a latency metric represented by a single blue line with several spikes" /%}

This line graph plots latency (in milliseconds) experienced by users on the y-axis against time on the x-axis.

#### Additional visualizations{% #additional-visualizations %}

Datadog offers a variety of visualization options to help users easily graph and display their metrics.

A metric query consists of the same two evaluation steps to start: time aggregation and space aggregation. See the [anatomy of a metric query](https://docs.datadoghq.com/metrics/#anatomy-of-a-metric-query) for more information.

- [Query Value Widget- Reduces the results of those two steps into a single value.](https://docs.datadoghq.com/dashboards/widgets/query_value/)
- [Top List- Returns a single value per group.](https://docs.datadoghq.com/dashboards/widgets/top_list/)

Additionally, Datadog has many other types of graphs and widgets for visualizations. You can learn more about them in Datadog's [blog series about metric graphs](https://www.datadoghq.com/blog/timeseries-metric-graphs-101/).

The graphing experience is consistent whether you are using dashboards, notebooks, or monitors. You can create graphs by using the graphing editor UI or by directly changing the raw query string. To edit the query string, use the `</>` button on the far right.

### Anatomy of a metric query{% #anatomy-of-a-metric-query %}

A metric query in Datadog looks like this:

{% image
   source="https://datadog-docs.imgix.net/images/metrics/introduction/newanatomy.61308aa931fc6e126925be9cd094643c.jpg?auto=format"
   alt="Example query with color-coded sections" /%}

You can break this query into a few steps:

#### Metric name{% #metric-name %}

First, choose the specific metric that you'd like to graph by searching or selecting it from the dropdown next to **Metric**. If you're not sure which metric to use, start with the Metrics Explorer or a notebook. You can also see a list of actively reporting metrics on the Metrics Summary page.

#### Filter your metric{% #filter-your-metric %}

After selecting a metric, you can filter your query based on tag(s). For instance, you can use `account:prod` to *scope* your query to include only the metrics from your production hosts. For more information, read the [tagging documentation](https://docs.datadoghq.com/getting_started/tagging/using_tags/).

#### Configure time aggregation{% #configure-time-aggregation %}

Next, choose the granularity of your data using time rollup. In this example, you've defined that there is one data point for every hour (3600 seconds). You can choose how you want to aggregate the data in each time bucket. By default, *avg* is applied, but other available options are *sum*, *min*, *max*, and *count*. You can also customize how your metrics data is aggregated and bucketed with functions or in-application modifiers. For example, if you wanted to apply max and customize how your metrics data is rolled up and bucketed in time with calendar aligned queries, you would use `.rollup(max, 60)`. For more information, see the [Functions](https://docs.datadoghq.com/dashboards/functions/), [Rollup](https://docs.datadoghq.com/dashboards/functions/rollup/#rollup-with-calendar-aligned-queries), and [In-application modifiers](https://docs.datadoghq.com/metrics/custom_metrics/type_modifiers/?tab=count#in-application-modifiers) documentation.

#### Configure space aggregation{% #configure-space-aggregation %}

In Datadog, "space" refers to the way metrics are distributed over different hosts and tags. There are two different aspects of space that you can control: aggregator and grouping

*Aggregator* defines how the metrics in each group are combined. There are four aggregations available: sum, min, max, and avg.

*Grouping* defines what constitutes a line on the graph. For example, if you have hundreds of hosts spread across four regions, grouping by region allows you to graph one line for every region. This would reduce the number of timeseries to four.

#### Apply functions (optional){% #apply-functions-optional %}

You can modify your graph values with mathematical [functions](https://docs.datadoghq.com/dashboards/functions/). This can mean performing arithmetic between an integer and a metric (for example, multiplying a metric by 2). Or performing arithmetic between two metrics (for example, creating a new timeseries for the memory utilization rate like this: `jvm.heap_memory / jvm.heap_memory_max`).

### Time and space aggregation{% #time-and-space-aggregation %}

*Time aggregation* and *space aggregation* are two important components of any query. Because understanding how these aggregations work helps you avoid misinterpreting your graphs, these concepts are explained in more detail below.

#### Time aggregation{% #time-aggregation %}

Datadog stores a large volume of points, and in most cases it's not possible to display all of them on a graph. There would be more datapoints than pixels. Datadog uses time aggregation to solve this problem by combining data points into time buckets. For example, when examining four hours, data points are combined into two-minute buckets. This is called a *rollup*. As the time interval you've defined for your query increases, the granularity of your data decreases.

There are five aggregations you can apply to combine your data in each time bucket: sum, min, max, avg, and count.

It's important to remember that time aggregation is *always* applied in every query you make.

#### Space aggregation{% #space-aggregation %}

Space aggregation splits a single metric into multiple timeseries by tags such as host, container, and region. For instance, if you wanted to view the latency of your EC2 instances by region, you would need to use space aggregation's grouping by functionality to combine each region's hosts.

There are four aggregators that can be applied when using space aggregation: *sum*, *min*, *max*, and *avg*. Using the above example, say that your hosts are spread across four regions: us-east-1, us-east-2, us-west-1, and us-west-2. The hosts in each region need to be combined using an aggregator function. Using the *max* aggregator would result in the maximum latency experienced across hosts in each region, while the *avg* aggregator would yield the average latency per region.

#### Nested Queries{% #nested-queries %}

Add additional layers of aggregation on the results of existing queries in time and space with nested queries in the UI or through the [API](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products). For more information, see the [Nested Queries](https://docs.datadoghq.com/metrics/nested_queries) documentation.

### View real-time information about metrics{% #view-real-time-information-about-metrics %}

The [Metrics Summary page](https://app.datadoghq.com/metric/summary) displays a list of your metrics reported to Datadog under a specified time frame: the past hour, day, or week. Metrics can be filtered by metric name or tag.

Click on any metric name to display a details sidepanel with more detailed information. The details sidepanel displays key information for a given metric, including its metadata (type, unit, interval), number of distinct metrics, number of reporting hosts, number of tags submitted, and a table containing all tags submitted on a metric. Seeing which tags are being submitted on a metric helps you understand the number of distinct metrics reporting from it, since this number depends on your tag value combinations.

**Note:** The number of distinct metrics reported in the details sidepanel on Metrics Summary does not define your bill. See your [usage details](https://docs.datadoghq.com/account_management/plan_and_usage/usage_details/) for a precise accounting of your usage over the past month.

Read the [metrics summary documentation](https://docs.datadoghq.com/metrics/summary/) for more details.

## Further reading{% #further-reading %}

- [Advanced Filtering- Filter your data to narrow the scope of metrics returned.](https://docs.datadoghq.com/metrics/advanced-filtering)
- [Distribution metrics- Compute global percentiles across your entire dataset.](https://docs.datadoghq.com/metrics/distributions)
- [Metrics without Limitsâ¢- Learn how to control custom metrics volumes with tag configurations using Metrics without Limitsâ¢.](https://docs.datadoghq.com/metrics/metrics-without-limits/)
- [Foundation Enablement- Join an interactive session to unlock the full potential of metrics.](https://dtdg.co/fe)
