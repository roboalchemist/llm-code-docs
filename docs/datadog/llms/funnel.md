# Source: https://docs.datadoghq.com/dashboards/widgets/funnel.md

---
title: Funnel Widget
description: >-
  Track conversion rates and identify bottlenecks in user workflows with funnel
  analysis visualization.
breadcrumbs: Docs > Dashboards > Widgets > Funnel Widget
---

# Funnel Widget

Funnel analysis helps you track conversion rates across key workflows to identify and address any bottlenecks in end-to-end user journeys. The funnel widget visualizes conversion rates across user workflows and end-to-end user journeys.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/funnel/funnel.876910a85b10ca3a76bcd05bbd707e84.png?auto=format"
   alt="Funnel widget visualizing drop-off rates of a user on an e-commerce site" /%}

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/funnel/funnel_setup.fea32b6e2dc0369d71b779a02310e5bb.png?auto=format"
   alt="Funnel widget setup screen" /%}

### Configuration{% #configuration %}

1. Choose the data to graph:
   - RUM: See the [Search RUM Events documentation](https://docs.datadoghq.com/real_user_monitoring/explorer/search/) to configure a RUM query.
1. Select **View** or **Action** and choose a query from the dropdown menu.
1. Click the **+** button and select another query from the dropdown menu to visualize the funnel. See the [RUM Visualize documentation](https://docs.datadoghq.com/product_analytics/journeys/funnel_analysis) for more information on visualizing Funnel analysis.

### Options{% #options %}

#### Global time{% #global-time %}

On screenboards and notebooks, choose whether your widget has a custom timeframe or uses the global timeframe.

## API{% #api %}

This widget can be used with the [Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/). See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescription requests [*required*][object]Request payload used to query items. query [*required*]objectUpdated funnel widget.data_source [*required*]enumSource from which to query items to display in the funnel. Allowed enum values: `rum`
default: `rum`
query_string [*required*]stringThe widget query. steps [*required*][object]List of funnel steps.facet [*required*]stringThe facet of the step.value [*required*]stringThe value of the step.request_type [*required*]enumWidget request type. Allowed enum values: `funnel` time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringThe title of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringThe size of the title.type [*required*]enumType of funnel widget. Allowed enum values: `funnel`
default: `funnel`
{% /tab %}

{% tab title="example" %}

```json
{
  "requests": [
    {
      "query": {
        "data_source": "rum",
        "query_string": "@browser.name:Chrome",
        "steps": [
          {
            "facet": "@view.name",
            "value": "/apm/home"
          }
        ]
      },
      "request_type": "funnel"
    }
  ],
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "funnel"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Learn more about Funnel Analysis](https://docs.datadoghq.com/product_analytics/journeys/funnel_analysis/)
- [Use funnel analysis to understand and optimize key user flows](https://www.datadoghq.com/blog/reduce-customer-friction-funnel-analysis/)
