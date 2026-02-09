# Source: https://docs.datadoghq.com/dashboards/widgets/run_workflow.md

---
title: Run Workflow Widget
description: >-
  Trigger automated workflows directly from dashboards to resolve issues and
  maintain system health quickly.
breadcrumbs: Docs > Dashboards > Widgets > Run Workflow Widget
---

# Run Workflow Widget

## Overview{% #overview %}

The Run Workflow widget allows you to automate critical tasks from dashboards. Trigger your workflows from a dashboard at the point you become aware of an issue affecting the health of your system. This keeps your systems up and running by improving the time to resolution and reducing the possibility of errors.

## Configuration{% #configuration %}

1. Under **Select the workflow**, find your workflow in the dropdown menu.
1. Map dashboard template variables to workflow input parameters. This allows the values of your dashboard template variables to be mapped directly to the input parameters when you run the workflow.
1. Enter a title for the widget and click **Save**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/workflows/trigger-from-dashboard2.f01a0e070983d6c8eda0db457d982ff8.png?auto=format"
   alt="Click Run Workflow to trigger a workflow from Dashboard widget." /%}

To run the workflow:

1. Click **Run Workflow** on your dashboard widget.
1. Under **Execution parameters**, any template variables you mapped to workflow inputs are automatically populated. Enter the values for any unmapped execution parameters, or edit the existing values if needed.
1. Click **Run** to run the workflow.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescription custom_links[object]List of custom links.is_hiddenbooleanThe flag for toggling context menu link visibility.labelstringThe label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.linkstringThe URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.override_labelstringThe label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`. inputs[object]Array of workflow inputs to map to dashboard template variables.name [*required*]stringName of the workflow input.value [*required*]stringDashboard template variable. Can be suffixed with '.value' or '.key'. time <oneOf>Time setting for the widget. Option 1objectWrapper for live spanhide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.live_spanenumThe available timeframes depend on the widget you are using. Allowed enum values: `1m,5m,10m,15m,30m,1h,4h,1d,2d,1w,1mo,3mo,6mo,week_to_date,month_to_date,1y,alert` Option 2objectUsed for arbitrary live span times, such as 17 minutes or 6 hours.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.type [*required*]enumType "live" denotes a live span in the new format. Allowed enum values: `live`unit [*required*]enumUnit of the time span. Allowed enum values: `minute,hour,day,week,month,year`value [*required*]int64Value of the time span. Option 3objectUsed for fixed span times, such as 'March 1 to March 7'.from [*required*]int64Start time in seconds since epoch.hide_incomplete_cost_databooleanWhether to hide incomplete cost data in the widget.to [*required*]int64End time in seconds since epoch.type [*required*]enumType "fixed" denotes a fixed span. Allowed enum values: `fixed`titlestringTitle of your widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the run workflow widget. Allowed enum values: `run_workflow`
default: `run_workflow`
workflow_id [*required*]stringWorkflow id.
{% /tab %}

{% tab title="example" %}

```json
{
  "custom_links": [
    {
      "is_hidden": false,
      "label": "Search logs for {{host}}",
      "link": "https://app.datadoghq.com/logs?query={{host}}",
      "override_label": "logs"
    }
  ],
  "inputs": [
    {
      "name": "Environment",
      "value": "$env.value"
    }
  ],
  "time": {
    "hide_incomplete_cost_data": false,
    "live_span": "5m"
  },
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "run_workflow",
  "workflow_id": "<workflow_id>"
}
```

{% /tab %}

{% /tab %}

## Further reading{% #further-reading %}

- [Workflow Automation](https://docs.datadoghq.com/service_management/workflows/)
