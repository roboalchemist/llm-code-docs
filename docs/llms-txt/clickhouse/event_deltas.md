# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/event_deltas.md

---
slug: /use-cases/observability/clickstack/event_deltas
title: Event Deltas with ClickStack
sidebar_label: Event Deltas
pagination_prev: null
pagination_next: null
description: Event Deltas with ClickStack
doc_type: guide
keywords:

- clickstack
- event deltas
- change tracking
- logs
- observability

---

Event Deltas in ClickStack are a trace-focused feature that automatically analyzes the properties of traces to uncover what changed when performance regresses. By comparing the latency distributions of normal versus slow traces within a corpus, ClickStack highlights which attributes are most correlated with the difference - whether that's a new deployment version, a specific endpoint, or a particular user ID.

Instead of manually sifting through trace data, event deltas surface the key properties driving differences in latency between two subsets of data, making it far easier to diagnose regressions and pinpoint root causes. This feature allows you to visualize raw traces and immediately see the factors influencing performance shifts, accelerating incident response, and reducing mean time to resolution.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/410d6cfd51222ce0a6a8e6954603437299a6bc7d55d4e2e7b0bc5f60b8055591/images/use-cases/observability/hyperdx-demo/step_17.png" alt="Event Deltas"/>

## Using Event Deltas [#using-event-deltas]

Event Deltas are available directly through the **Search** panel in ClickStack when selecting a source of type `Trace`.

From the top-left **Analysis Mode** selector, choose **Event Deltas** (with a `Trace` source selected) to switch from the standard results table, which displays spans as rows.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6df442a4ce352f3737a7c147a74af7befe8dcf1839946d9d26ea7eda6884224a/images/use-cases/observability/event_deltas_no_selected.png" alt="Event Deltas not selected"/>

This view renders the distribution of spans over time, showing how latency varies alongside volume. The vertical axis represents latency, while the coloring indicates the density of traces at a given point with brighter yellow areas corresponding to a higher concentration of traces. With this visualization, users can quickly see how spans are distributed across both latency and count, making it easier to identify shifts or anomalies in performance.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6f55e8bdcb49a6c5a06e70b1173f98ef4050eb369380a100a1bda05b628bdcd8/images/use-cases/observability/event_deltas_highlighted.png" alt="Event Deltas highlighted"/>

Users can then select an area of the visualization - ideally one with higher duration spans and sufficient density, followed by **Filter by Selection**. This designates the "outliers" for analysis. Event Deltas will then identify the columns and key values most associated with those spans in this outlier subset compared to the rest of the dataset. By focusing on regions with meaningful outliers, ClickStack highlights the unique values that distinguish this subset from the overall corpus, surfacing the attributes most correlated with the observed performance differences.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/147f3631a998664bfcce405b61d6fe3d25080246edb50c80e8284eaf3f83965f/images/use-cases/observability/event_deltas_selected.png" alt="Event Deltas selected"/>

For each column, ClickStack identifies values that are heavily biased toward the selected outlier subset. In other words, when a value appears in a column, if it occurs predominantly within the outliers rather than the overall dataset (the inliers), it is highlighted as significant. Columns with the strongest bias are listed first, surfacing the attributes most strongly associated with anomalous spans and distinguishing them from baseline behavior.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c75bf9f8c0a51c0ddc9b8209fd46a1f3ef28f9569ccf1b4ed763124bc9270834/images/use-cases/observability/event_deltas_outliers.png" alt="Event Deltas outliers"/>

Consider the example above where the `SpanAttributes.app.payment.card_type` column has been surfaced. Here, the Event Deltas analysis shows that `29%` of the inliers use MasterCard, with `0%` among the outliers, while `100%` of the outliers use Visa, compared to `71%` of the inliers. This suggests that the Visa card type is strongly associated with the anomalous, higher-latency traces, whereas MasterCard appears only in the normal subset.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9c3b619f5613372d4847173059e03248024d58611837dcb8abe1bb06c6804967/images/use-cases/observability/event_deltas_issue.png" alt="Event Deltas issue"/>

Conversely, values exclusively associated with inliers can also be interesting. In the example above, the error `Visa Cash Full` appears exclusively in the inliers and is completely absent from the outlier spans. Where this occurs, latency is always less than approximately 50 milliseconds, suggesting this error is associated with low latencies.

## How Event Deltas work [#how-event-deltas-work]

Event Deltas work by issuing two queries: one for the selected outlier area and one for the inlier area. Each query is limited to the appropriate duration and time window. A sample of events from both result sets is then inspected, and columns for which a high concentration of values appears predominantly in the outliers are identified. Columns for which 100% of a value occurs only in the outlier subset are shown first, highlighting the attributes most responsible for the observed differences.

## Customizing the graph [#customizing-the-graph]

Above the graph, you'll find controls that let you customize how the heatmap is generated. As you adjust these fields, the heatmap updates in real time, allowing you to visualize and compare relationships between any measurable value and its frequency over time.

**Default Configuration**

By default, the visualization uses:

- **Y Axis**: `Duration` — displays latency values vertically
- **Color (Z Axis)**: `count()` — represents the number of requests over time (X axis)

This setup shows latency distribution across time, with color intensity indicating how many events fall within each range.

**Adjusting Parameters**

You can modify these parameters to explore different dimensions of your data:

- **Value**: Controls what is plotted on the Y axis. For example, replace `Duration` with metrics like error rate or response size.
- **Count**: Controls the color mapping. You can switch from `count()` (number of events per bucket) to other aggregation functions such as `avg()`, `sum()`, `p95()`, or even custom expressions like `countDistinct(field)`.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1eefcc437529ce62c4214f6f1563eb2c75bef504fd90190fc42c4f4d58d2cd7c/images/use-cases/observability/event_deltas_customization.png" alt="Event Deltas Customization"/>

## Recommendations [#recommendations]

Event Deltas work best when the analysis is focused on a specific service. Latency across multiple services can vary widely, making it harder to identify the columns and values most responsible for outliers. Before enabling Event Deltas, filter spans to a set where the distribution of latencies is expected to be similar. Target analyzing sets where wide latency variation is unexpected for the most useful insights, avoiding cases where it's the norm (e.g., two different services).

When selecting an area, users should aim for subsets where there is a clear distribution of slower versus faster durations, allowing the higher-latency spans to be cleanly isolated for analysis. For example, note the selected area below clearly captures a set of slower spans for analysis.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1520a7fb9741a47b211d8f0023fb852d77e02ecdf815029332fe30122a26bb33/images/use-cases/observability/event_deltas_separation.png" alt="Event Deltas Separation"/>

Conversely, the following dataset is hard to analyze in a useful way with Event Deltas.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1c4bce1d18742cc4cfcf815b6c7e8bda5c1ca227bc14ab56531fd8e5ba118399/images/use-cases/observability/event_deltas_inappropriate.png" alt="Event Deltas Poor seperation"/>
