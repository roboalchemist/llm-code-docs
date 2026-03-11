# Source: https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-metrics-perspective.md

# Metrics perspective

The Metrics Perspective shows metrics for the selected resource.

![Metrics perspective](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-37c5b6e03a0b2a7027f4d62db67885b05ac21694%2Fk8s-metrics-perspective.png?alt=media)

## Charts

Charts show metrics data for the selected components in near real-time - data is fetched every 30 seconds. If a process is stopped and no more data is received, the process will eventually leave the chart as the data shifts left at least every 30 seconds. If more data arrives during the 30-second interval, it will be pushed to a chart.

## Ordering

Metric charts are ordered on priority and name. Both are configured on the [metric binding](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts).
