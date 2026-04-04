# Source: https://docs.datadoghq.com/dashboards/widgets/service_summary.md

---
title: Service Summary Widget
description: Displays the graphs of a chosen service in a dashboard widget.
breadcrumbs: Docs > Dashboards > Widgets > Service Summary Widget
---

# Service Summary Widget

A service is a set of processes that do the same job, for example, a web framework or database. Datadog provides out-of-the-box graphs to display service information, as seen on the Service page. Use the service summary widget to display the graphs of a chosen [service](https://docs.datadoghq.com/tracing/services/service_page/) in your dashboard.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/service_summary/service_summary.355d60470ab741dcaee6ad47d27aa754.png?auto=format"
   alt="service summary" /%}

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Select an [environment](https://docs.datadoghq.com/tracing/send_traces/) and a [service](https://docs.datadoghq.com/tracing/services/service_page/).
1. Select a widget size.
1. Select the information to display:
   - Hits
   - Errors
   - Latency
   - Breakdown
   - Distribution
   - Resource (**Note**: You need to select the large widget size to see this option.)
1. Choose your display preference by selecting the number of columns to display your graphs across.
1. Enter a title for your graph.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptiondisplay_formatenumNumber of columns to display. Allowed enum values: `one_column,two_column,three_column`env [*required*]stringAPM environment.service [*required*]stringAPM service.show_breakdownbooleanWhether to show the latency breakdown or not.show_distributionbooleanWhether to show the latency distribution or not.show_errorsbooleanWhether to show the error metrics or not.show_hitsbooleanWhether to show the hits metrics or not.show_latencybooleanWhether to show the latency metrics or not.show_resource_listbooleanWhether to show the resource list or not.size_formatenumSize of the widget. Allowed enum values: `small,medium,large`span_name [*required*]stringAPM span name. time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringTitle of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the service summary widget. Allowed enum values: `trace_service`
default: `trace_service`
{% /tab %}

{% tab title="example" %}

```json
{
  "display_format": "string",
  "env": "",
  "service": "",
  "show_breakdown": false,
  "show_distribution": false,
  "show_errors": false,
  "show_hits": false,
  "show_latency": false,
  "show_resource_list": false,
  "size_format": "string",
  "span_name": "",
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "trace_service"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
- [Learn more about the APM Service Page](https://docs.datadoghq.com/tracing/services/service_page/)
