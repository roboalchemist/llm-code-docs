# Source: https://docs.datadoghq.com/dashboards/widgets/check_status.md

---
title: Check Status Widget
description: Graph the current status or number of results for any check performed.
breadcrumbs: Docs > Dashboards > Widgets > Check Status Widget
---

# Check Status Widget

Service checks monitor the up or down status of a specific service. Alerts are triggered when the monitoring Agent fails to connect to the service in a specified number of consecutive checks. The Check Status widget can visually display service degradation, service failures, cluster-wide issues, drops in throughput, or increases in latency in your dashboard. For more information, see the [Service check](https://docs.datadoghq.com/developers/service_checks) documentation.

Check status shows the current status or number of results for any check performed:

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/check_status/check_status.9ce7fab0232fdd07a1868fd7e3e45f5c.png?auto=format"
   alt="Check status widget" /%}

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Select a previously created [service check](https://docs.datadoghq.com/developers/service_checks).

1. Choose a reporting time frame. This time frame always includes up to the present, so you can choose an option such as `The past 10 minutes` or `The past 1 day` and it reports a status that includes that time frame up to the present moment. If you choose `Global Time`, the person using the dashboard can select a range using the time frame selector in the upper right, but *they must choose one that includes the present moment*, that is any `past X` time frame. Otherwise the widget is blank.

1. Choose your scope:

   - **A single check**: Select this option if your Check Status widget is for a specific element only, for example: one `host:<HOSTNAME>`, one `service:<SERVICE_NAME>`.
   - **A cluster of checks**: Select this option if your Check Status widget is for a scope of elements as in all `host`s, or all `service`s.

1. After selecting your scope, define your Check Status widget context with the **Reported by** field.

1. For the scope **A Cluster of checks**, you have the option to select a subset with the **Group by** field. **Note**: The check status does not show you the count of checks per group, it shows the count of groups running the check. For example, if you are monitoring Agent Up, grouped by `env`, the check status shows you the number of `env` that matches your scope configurations and is running the Agent, not the count of Agents in an environment.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptioncheck [*required*]stringName of the check to use in the widget.groupstringGroup reporting a single check.group_by[string]List of tag prefixes to group by in the case of a cluster check.grouping [*required*]enumThe kind of grouping to use. Allowed enum values: `check,cluster`tags[string]List of tags used to filter the groups reporting a cluster check. time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringTitle of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the check status widget. Allowed enum values: `check_status`
default: `check_status`
{% /tab %}

{% tab title="example" %}

```json
{
  "check": "",
  "group": "string",
  "group_by": [],
  "grouping": "check",
  "tags": [],
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "check_status"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Learn more about service checks](https://docs.datadoghq.com/developers/service_checks)
- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
