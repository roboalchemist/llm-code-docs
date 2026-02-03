# Source: https://docs.datadoghq.com/dashboards/guide/graphing_json.md

---
title: Graphing with JSON
description: >-
  Create and configure dashboard widgets programmatically using JSON syntax with
  the Datadog API.
breadcrumbs: Docs > Dashboards > Graphing Guides > Graphing with JSON
---

# Graphing with JSON

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/graphing_json/json_editor.77a875ca97e2d6a63a3a29e5bb67f060.png?auto=format"
   alt="Configure a timeseries widget with the JSON editor" /%}

In addition to the [GUI graph editor](https://docs.datadoghq.com/dashboards/querying/#graphing-editor), you can use the JSON editor in your dashboard widgets to configure your visualizations. The schema displayed in the JSON editor mirrors the request body schema of the Dashboard API. For more information on the JSON parameters and required fields see the [Dashboard API documentation](https://docs.datadoghq.com/api/v1/dashboards/).

## Widget JSON schema{% #widget-json-schema %}

Find the widget type you want to add to your dashboard and apply the JSON fields listed in the respective documentation. For a full list of widget types, see the [Widget index](https://docs.datadoghq.com/dashboards/widgets/).

### Y-Axis schema{% #y-axis-schema %}

The Datadog y-axis controls allow you to:

- Clip the y-axis to specific ranges
- Filter series either by specifying a percentage or an absolute value
- Change the y-axis scale from linear to log, sqrt, or power scale

### Markers schema{% #markers-schema %}

Markers allow you to add visual conditional formatting for your graphs. For example, ALERT, WARNING, or OK.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/graphing_json/markers.8c4ff28ed530559957009d2c51b39c61.png?auto=format"
   alt="Markers" /%}

## Template variable schema{% #template-variable-schema %}

Dashboard template variables apply a new scope to one or more graphs on your dashboard. This allows you to dynamically explore metrics across different sets of tags by using variables instead of specific tags. Learn more about [template variable in the Datadog UI](https://docs.datadoghq.com/dashboards/template_variables/).

## Further Reading{% #further-reading %}

- [Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)
- [Widgets](https://docs.datadoghq.com/dashboards/widgets/)
