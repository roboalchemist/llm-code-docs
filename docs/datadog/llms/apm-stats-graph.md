# Source: https://docs.datadoghq.com/dashboards/guide/apm-stats-graph.md

---
title: Configuring An APM Stats Graph
description: >-
  Configure dashboard graphs using APM statistics data with proper levels of
  detail and parameter selection.
breadcrumbs: Docs > Dashboards > Graphing Guides > Configuring An APM Stats Graph
---

# Configuring An APM Stats Graph

## Overview{% #overview %}

To configure your graph using APM stats data, follow these steps:

1. Select your visualization from the available [widgets](https://docs.datadoghq.com/dashboards/widgets/).
1. Choose your level of detail.
1. Choose your parameters.
1. Title the graph (same as for Metrics).

### Level of detail{% #level-of-detail %}

Choose what level of detail you want to see statistics for: one or more services, resources, or spans. Not all of these are available for every widget type.

### APM stats parameters{% #apm-stats-parameters %}

Select the following parameters from the graphing editor: Environment (`env`), Primary tag (`primary_tag`), Service (`service`), and Operation name (`name`).

If your level of detail is `resource` or `span`, some widget types also require you to select a Resource name (`resource`) to narrow the scope of your query.

## Further reading{% #further-reading %}

- [Learn how to query graphs](https://docs.datadoghq.com/dashboards/querying/)
