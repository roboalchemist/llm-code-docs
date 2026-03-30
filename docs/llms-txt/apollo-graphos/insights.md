# Source: https://www.apollographql.com/docs/graphos/platform/insights.md

# GraphOS Metrics and Insights

While Insights are available on all GraphOS plans, metrics retention varies by [plan](https://www.apollographql.com/pricing?referrer=docs-content).

To help analyze your supergraph's performance, GraphOS Studio can create reports with insights and visualizations about the operation metrics collected by GraphOS across the supergraph.

## Operation and field usage metrics

With your graph configured to [send operation metrics to GraphOS](https://www.apollographql.com/docs/graphos/platform/insights/sending-operation-metrics), Studio provides an Insights page per graph variant that displays various operation and field metrics. These displayed metrics include p95 service time, error percentage, request latency distribution, and [more](https://www.apollographql.com/docs/graphos/platform/insights/operation-metrics).

GraphOS also collects metrics about field usage of operations. Studio's Insights page displays field details that include field definitions, the first and last times a field received traffic, and the client that used a field. To learn more, go to [Field Usage](https://www.apollographql.com/docs/graphos/platform/insights/field-usage).

## Subgraph metrics

Subgraph and connector-level insights give your team visibility into how each service contributes to your supergraph's performance. With the Apollo Router v2.7.0 or later, you can identify top traffic sources, detect performance bottlenecks, and compare subgraphs by request volume, latency, and error rates.

Subgraph metrics help you understand which clients and operations drive the highest error and request rates, target slow operations, and analyze trends using latency heatmaps. To learn more, see [Subgraph Metrics](https://www.apollographql.com/docs/graphos/platform/insights/subgraphs).

## Error diagnostics

Studio also provides detailed error information on the Insights page. You can group and filter errors by the underlying service where the error originated, error code, and error path. Enterprise users can also see representative traces to speed error debugging. To learn more, see [Error Diagnostics](https://www.apollographql.com/docs/graphos/platform/insights/errors).

## Notifications and alerts

Because it collects metrics from across your entire supergraph, GraphOS can detect when your graph's health and performance degrade. GraphOS can notify your team whenever it detects issues with your graph.

GraphOS supports a variety of notifications, including the following:

* Daily performance reports
* Alerts when a metric exceeds a threshold
* Notifications for schema changes and updates
* Build statuses

GraphOS can send notifications to Slack, PagerDuty, and/or custom webhooks.
To learn more, go to the pages in [Notifications and Alerts](https://www.apollographql.com/docs/graphos/platform/insights/notifications).

Supported notifications differ for each [plan](https://www.apollographql.com/docs/graphos/platform/insights/notifications#plan-availability).
