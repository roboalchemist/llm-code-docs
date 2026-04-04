# Source: https://docs.datadoghq.com/developers/dogstatsd/data_aggregation.md

---
title: DogStatsD Data Aggregation
description: >-
  Learn how the DogStatsD server aggregates your data before sending it to
  Datadog
breadcrumbs: Docs > Developers > DogStatsD > DogStatsD Data Aggregation
---

# DogStatsD Data Aggregation

Datadog DogStatsD implements the StatsD protocol [with some differences](https://docs.datadoghq.com/developers/dogstatsd/). DogStatsD enables you to send metrics and monitor your application code without blocking it. Data is transmitted from your application through UDP to the local [DogStatsD server](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/) (embedded in the Datadog Agent), which aggregates and then sends it to Datadog's API endpoint. Read more about the [DogStatsD setup](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/).

This article describes why and how the aggregation is performed over your data.

## Why aggregate metrics?{% #why-aggregate-metrics %}

Aggregation improves performance by reducing the number of API calls, each of which takes a certain amount of time.

Consider a [COUNT metric](https://docs.datadoghq.com/metrics/types/?tab=count#metric-types) that is incremented 1,000 times (+1 each time) over a short amount of time. Instead of making 1,000 separate API calls, the DogStatsD server aggregates it into a few API calls. Depending on the situation (see below), the library may submitâfor instanceâ1 datapoint with value 1,000 or X aggregate datapoints with a cumulated value of 1,000.

## How is aggregation performed with the DogStatsD server?{% #how-is-aggregation-performed-with-the-dogstatsd-server %}

[DogStatsD](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/) uses a *flush interval* of 10 seconds. Every 10 seconds, [DogStatsD](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/) checks all data received since the last flush. All values that correspond to the same metric name and the same tags are aggregated together into a single value.

To discover how tags affect aggregation, see [Getting Started with Tags](https://docs.datadoghq.com/getting_started/tagging/).

**Note**: With the StatsD protocol, the StatsD client doesn't send metrics with timestamps. The timestamp is added at the flush time. So for a flush occurring at 10:00:10, all data received by the [DogStatsD](https://docs.datadoghq.com/metrics/custom_metrics/dogstatsd_metrics_submission/) server (embedded in the Datadog Agent) between 10:00:00 and 10:00:10 is rolled up in a single datapoint that gets 10:00:00 as timestamp.

## Aggregation rules per metric type{% #aggregation-rules-per-metric-type %}

Among all values received during the same flush interval, the aggregated value send depends on the [metric type](https://docs.datadoghq.com/metrics/types/):

| Metric Type                                                                             | Aggregation performed over one flush interval                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [GAUGE](https://docs.datadoghq.com/metrics/types/?tab=gauge#metric-types)               | The latest datapoint received is sent.                                                        |
| [COUNT](https://docs.datadoghq.com/metrics/types/?tab=count#metric-types)               | The sum of all received datapoints is sent.                                                   |
| [HISTOGRAM](https://docs.datadoghq.com/metrics/types/?tab=histogram#metric-types)       | The min, max, sum, avg, 95 percentiles, count, and median of all datapoints received is sent. |
| SET                                                                                     | The number of different datapoints is sent.                                                   |
| [DISTRIBUTION](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types) | Aggregated as global distributions.                                                           |

## Further Reading{% #further-reading %}

- [Introduction to DogStatsD](https://docs.datadoghq.com/developers/dogstatsd)
- [Official and Community created API and DogStatsD client libraries](https://docs.datadoghq.com/developers/libraries)
