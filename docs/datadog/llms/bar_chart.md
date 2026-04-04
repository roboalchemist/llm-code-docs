# Source: https://docs.datadoghq.com/dashboards/widgets/bar_chart.md

---
title: Bar Chart Widget
description: >-
  Display aggregated data in vertical or horizontal bars to compare metrics
  across different categories.
breadcrumbs: Docs > Dashboards > Widgets > Bar Chart Widget
---

# Bar Chart Widget

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/bar_chart/bar_chart.734c6c962b626fe57daa187317d36370.png?auto=format"
   alt="Bar chart widget example visualization" /%}

The bar chart widget is part of the same data family as the top list, treemap, and pie chart widgets, using categorical axes rather than temporal axes like timeseries bar graphs. It displays categorical data using vertical bars, allowing you to compare values across different categories or groups. Unlike the horizontal top list widget, the bar chart uses a vertical orientation which is particularly useful for dashboards with wide and short aspect ratios, or when you want to focus on value comparison rather than ranking.

Use the bar chart when visual comparison across categories matters more than reading exact tag values. Use the top list to prioritize label readability (such as long tag names) or need a ranked list format.

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Select from the available data sources.
1. Configure the query. See the following resources for more information:
   - Metrics: See the [querying ](https://docs.datadoghq.com/dashboards/querying)documentation to configure a metric query.
   - Events: See the [log search](https://docs.datadoghq.com/logs/explorer/search_syntax/) documentation to configure a log event query.
1. (Optional) Modify the query with a [formula](https://docs.datadoghq.com/dashboards/functions/).
1. Customize your graph.

### Options{% #options %}

#### Display mode{% #display-mode %}

The bar chart widget supports multiple levels of grouping with stacked visualization, enabling you to break down data by multiple dimensions.

- **Stacked mode**: Shows grouped data as layered bars within each category.
- **Flat mode**: Displays individual bars for each group.
- **Relative mode**: Shows values as percentages of the total (only for scalar data).
- **Absolute mode**: Shows raw count values.

## Further reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
- [Top List Widget](https://docs.datadoghq.com/dashboards/widgets/top_list)
- [Treemap Widget](https://docs.datadoghq.com/dashboards/widgets/treemap)
- [Pie Chart Widget](https://docs.datadoghq.com/dashboards/widgets/pie_chart)
- [Context Links](https://docs.datadoghq.com/dashboards/guide/context-links/#overview/)
