# Source: https://docs.datadoghq.com/dashboards/widgets/alert_graph.md

---
title: Alert Graph Widget
description: Graph the current status of any monitor defined on your system.
breadcrumbs: Docs > Dashboards > Widgets > Alert Graph Widget
---

# Alert Graph Widget

Alert graphs are timeseries graphs showing the current status of most monitors defined on your system:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/alert_graph/alert_graph.0ddfb73f548355b8adbe31723dff1dd3.png?auto=format"
   alt="Alert Graph" /%}

This widget is supported in default scheduled query alert monitors such as metric, anomaly, outlier, forecast, APM metrics, and integration.

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Choose a previously created monitor to graph.
1. Select a timeframe.
1. Select your visualization:
   - Timeseries
   - Top list

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptionalert_id [*required*]stringID of the alert to use in the widget. time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringThe title of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the alert graph widget. Allowed enum values: `alert_graph`
default: `alert_graph`
viz_type [*required*]enumWhether to display the Alert Graph as a timeseries or a top list. Allowed enum values: `timeseries,toplist`
{% /tab %}

{% tab title="example" %}

```json
{
  "alert_id": "",
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "alert_graph",
  "viz_type": "timeseries"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
