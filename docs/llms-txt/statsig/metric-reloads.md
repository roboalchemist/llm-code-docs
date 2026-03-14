# Source: https://docs.statsig.com/statsig-warehouse-native/features/metric-reloads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metric Reloads

Metric reloads drop all data from staging pipelines associated with a metric, and restate that data from scratch. Where this data is interconnected (e.g. ratios, funnels, etc.), related entities will be updated as well.

This is a big time saver in cases where a new metric needs to be added to an experiment, or a metric definition has changed, since you can avoid reloading N unrelated experiment metrics.


Built with [Mintlify](https://mintlify.com).