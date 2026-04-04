# Source: https://docs.datadoghq.com/dashboards/guide/unit-override.md

---
title: Customize your visualizations with unit override
description: >-
  Override default metric and event units to customize how data is displayed and
  formatted in dashboard visualizations.
breadcrumbs: >-
  Docs > Dashboards > Graphing Guides > Customize your visualizations with unit
  override
---

# Customize your visualizations with unit override

## Overview{% #overview %}

The unit override feature in visualizations allows you to customize how your data is labeled. This guide covers the configuration options for unit override and how these options help you analyze your graphs.

**Note**: Many of the examples in this guide use the [Table widget](https://docs.datadoghq.com/dashboards/widgets/table/), however, unit override is not exclusive to this widget.

- [Set Metrics Units](https://docs.datadoghq.com/metrics/units)
- [Set units for Event-based queries](https://docs.datadoghq.com/logs/explorer/facets/#units)

## Configuration{% #configuration %}

In your Notebooks and Dashboard widgets, find the graph editor of the cell or the widget. For Notebooks, click **More Options** and for Dashboards, find the **Graph your data** section.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/unit_override/unit_override_config.71a0e11e2371635391d1f6d9eaa9cdf7.png?auto=format"
   alt="Unit override option in the graph your data section for a Change widget" /%}

## How unit and scale attribution works{% #how-unit-and-scale-attribution-works %}

When a unit is detected, Datadog automatically chooses the most readable unit scale depending on the magnitude of your data. For example, if the source data is nanoseconds, the widget could display readable values in minutes and seconds instead of millions of nanoseconds.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/unit_override/unit_override_with_autoscale.a3e61cbea14d6f006df68b29a9907a43.png?auto=format"
   alt="Table widget showing values scaled to minutes and seconds, alongside unit override configuration with Autoscale unit enabled" /%}

With unit override, you can choose a single fixed scale to compare values. In the example below, all values are configured to scale to `minutes`. This is to directly compare values in the same scale.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/unit_override/unit_override_without_autoscale.c66aa6058d05e2af859574e1cdbe7aa7.png?auto=format"
   alt="Table widget showing values all scaled to minute, alongside unit override configuration without Autoscale unit enabled" /%}

## Assign custom units{% #assign-custom-units %}

Assign custom units to a widget to add context to unit-less metrics (like counts).

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/unit_override/custom_unit_tests.4668c4caac8cfa4828a2feeab6764cf4.png?auto=format"
   alt="Unit override configuration highlighting the Unit dropdown menu to assign custom units" /%}

Define completely custom units that are not included in the provided list of units. Instead of a generic count of events, you can specify that you are visualizing 10,000 tests, or 100 sessions. This gives you immediate context for what data you are analyzing.

**Note**: Autoscaling is not available for custom units as the unit family is not recognized.

## Further reading{% #further-reading %}

- [Metric Units](https://docs.datadoghq.com/metrics/units/)
- [Event units](https://docs.datadoghq.com/logs/explorer/facets/#units)
- [List of Widgets](https://docs.datadoghq.com/dashboards/widgets/)
