# Source: https://docs.datadoghq.com/dashboards/widgets/alert_value.md

---
title: Alert Value Widget
description: >-
  Graph the current value of a metric in any simple-alert metric monitor defined
  on your system.
breadcrumbs: Docs > Dashboards > Widgets > Alert Value Widget
---

# Alert Value Widget

The Alert value widget displays the current query value from a simple-alert metric monitor. Simple-alert monitors have a metric query that is not grouped and returns one value. Use Alert value widgets in your dashboard to get an overview of your monitor behaviors and alert statuses.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/alert_value/alert_value_2023.daf5bbe7c9a5ac07df7181555b9cac61.png?auto=format"
   alt="Three alert value widgets with three different monitor statuses for disk space, high cpu and checkout error rate" /%}

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/alert_value/alert_value_setup_2023.57591a989ca2c0ace54511ac32668c14.png?auto=format"
   alt="Alert Value setup page for high cpu monitor" /%}

### Configuration{% #configuration %}

1. Choose an existing metric monitor to graph.
1. Select the formatting to display:
   - Decimal
   - Units
   - Alignment
1. Give your graph a title.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/v1/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptionalert_id [*required*]stringID of the alert to use in the widget.precisionint64Number of decimal to show. If not defined, will use the raw value.text_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`titlestringTitle of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of value in the widget.type [*required*]enumType of the alert value widget. Allowed enum values: `alert_value`
default: `alert_value`
unitstringUnit to display with the value.
{% /tab %}

{% tab title="example" %}

```json
{
  "alert_id": "",
  "precision": "integer",
  "text_align": "string",
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "alert_value",
  "unit": "string"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
