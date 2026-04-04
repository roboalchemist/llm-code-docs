# Source: https://docs.datadoghq.com/dashboards/widgets/monitor_summary.md

---
title: Monitor Summary Widget
description: >-
  Display a summary view of all your Datadog monitors, or a subset based on a
  query.
breadcrumbs: Docs > Dashboards > Widgets > Monitor Summary Widget
---

# Monitor Summary Widget

The monitor summary widget displays a summary view of all your Datadog monitors, or a subset based on a query.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/monitor-summary-overview.e794756ebd3ffc9824e4dc44cee812da.png?auto=format"
   alt="monitor summary" /%}

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Select one of the three summary types: `Monitor`, `Group` or `Combined`

   - The `Monitor` summary type lists statuses and names of monitors matching the [monitor query](https://docs.datadoghq.com/monitors/manage/). Multi alert monitors have only one row in the results list and their status is the multi alert monitor's overall status. The Status Counts are the number of matching monitors with each status type.

   {% image
      source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/monitor_summary_type.a79f29eba5333907525c8f6fe4359845.png?auto=format"
      alt="monitor summary type" /%}

   - The `Group` summary type lists statuses, names, and groups of monitors matching the monitor query. Multi alert monitors are broken into several rows in the results list and correspond to each group and that group's specific status in the multi alert monitor. The `Group` summary type also supports `group` and `group_status` facets in its monitor query similar to the [Triggered Monitors](https://docs.datadoghq.com/monitors/manage/#grouped-results) page. The Status Counts are the number of matching monitor groups with each status type.

   {% image
      source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/group_summary_type.eba9ea8ffb168990c56486ec08893989.png?auto=format"
      alt="group summary type" /%}

   - The `Combined` summary type lists the number of group statuses and names of the monitors matching the monitor query. Multi alert monitors have only one row in the results list like in the `Monitor` summary type but the groups column displays the number of groups in each status type instead of the monitor's overall status. Similar to the `Group` summary type, the `Combined` summary type also supports the `group` and `group_status` facets in its monitor query. The Status Counts still show the count of overall monitor statuses like in the `Monitor` summary type.

   {% image
      source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/combined_summary_type.00863aad5ce08595a8d0eee50bc79df3.png?auto=format"
      alt="combined summary type" /%}

1. Enter a monitor query to display the monitor summary widget over a subset of your monitors.

**Note** In addition to the facets listed in the link above, the `Group` and `Combined` summary types also support the `group` and `group_status` facets for group-level searching, similar to the [Triggered Monitors](https://docs.datadoghq.com/monitors/manage/#grouped-results) page.

#### Template variables{% #template-variables %}

To use template variables created in your dashboard in the monitor summary search query, follow the same query format as the Manage Monitor page.

**Example**

1. Filtering on Monitor `scope` with a `$service` template variable.

To leverage `scope` in the manage or triggered monitor page, you have to do `scope:service:web-store`. Therefore in the widget you have to do `scope:$service` to then apply the template variable value to the widget.

   {% image
      source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/templatevariable-example-scope.20daa41603be2494efaebe2f1c7755c6.png?auto=format"
      alt="Scope Template variable" /%}

1. Filtering on Monitor `group` with a `$env` template variable.

To leverage `group` in the manage or triggered monitor page, you have to do `group:env:prod`. Therefore in the widget you have to do `group:$env` to then apply the template variable value to the widget.

   {% image
      source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/templatevariable-example-group.b1e9c37877a0c191e38ba020bfb4bf7a.png?auto=format"
      alt="Group Template variable" /%}

## Options{% #options %}

#### Display preferences{% #display-preferences %}

Choose to show only the `Count` of monitors per monitor status type, a `List` of monitors, or `Both`. The `Text` and `Background` options specify whether the status colors should be applied to the text or background of the Status Counts. The `Hide empty Status Counts` option, when enabled, only shows the Status Counts for statuses that have more than zero monitors in the result list.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/display-preferences.676f563d0301d5fd431f1fa9b9310cb8.png?auto=format"
   alt="display preferences" /%}

Selecting the `Show triggered column` option filters the results to monitors or monitor groups that are in a triggered state (`Alert`, `Warn`, or `No Data`) and sorts them from most recently triggered to least recently triggered. An additional column is added indicating the amount of time that has elapsed since the monitor/group last triggered.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/monitor_summary/monitor-summary.f8dac95a3372eea0ab8c7bbc821e1c66.png?auto=format"
   alt="display preferences" /%}

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptioncolor_preferenceenumWhich color to use on the widget. Allowed enum values: `background,text`countint64**DEPRECATED**: The number of monitors to display.display_formatenumWhat to display on the widget. Allowed enum values: `counts,countsAndList,list`hide_zero_countsbooleanWhether to show counts of 0 or not.query [*required*]stringQuery to filter the monitors with.show_last_triggeredbooleanWhether to show the time that has elapsed since the monitor/group triggered.show_prioritybooleanWhether to show the priorities column.sortenumWidget sorting methods. Allowed enum values: `name,group,status,tags,triggered,group,asc,group,desc,name,asc,name,desc,status,asc,status,desc,tags,asc,tags,desc,triggered,asc,triggered,desc,priority,asc,priority,desc`startint64**DEPRECATED**: The start of the list. Typically 0.summary_typeenumWhich summary type should be used. Allowed enum values: `monitors,groups,combined`titlestringTitle of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the monitor summary widget. Allowed enum values: `manage_status`
default: `manage_status`
{% /tab %}

{% tab title="example" %}

```json
{
  "color_preference": "string",
  "count": "integer",
  "display_format": "string",
  "hide_zero_counts": false,
  "query": "",
  "show_last_triggered": false,
  "show_priority": false,
  "sort": "name,asc",
  "start": "integer",
  "summary_type": "string",
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "manage_status"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
