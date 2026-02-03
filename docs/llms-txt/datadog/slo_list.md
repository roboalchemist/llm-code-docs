# Source: https://docs.datadoghq.com/dashboards/widgets/slo_list.md

---
title: SLO List Widget
description: Display a list of SLOs
breadcrumbs: Docs > Dashboards > Widgets > SLO List Widget
---

# SLO List Widget

SLOs (service-level objectives) are an agreed-upon target that must be achieved for each activity, function, and process to provide the best opportunity for customer success. SLOs represent the performance or health of a service.

The SLO List widget displays a subset of SLOs over their primary time window. All other configured time windows are available in the SLO's side panel on the SLO page. For more information, see the [SLO](https://docs.datadoghq.com/service_level_objectives/) documentation.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/slo_list/slo-list-widget-latest.b10683b9568a9a8fe35dd7548805cb1d.png?auto=format"
   alt="The SLO List widget displaying a list of SLOs" /%}

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/slo_list/slo-list-widget-editor-latest.876d12ff1985d4ef5a7aa936af5dac31.png?auto=format"
   alt="A search query defining the service as web-store in the SLO List widget editor" /%}

### Configuration{% #configuration %}

1. Add an SLO List widget to a dashboard.
1. Use tags to filter the list of SLOs (such as `service:foo, env:prod`). Template variables are supported.
1. Choose the maximum number of SLOs to display (the default is 100) and sort by either status or error budget.
1. Optionally, give the widget a title.

When you are ready to create the widget, click **Save**.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescription requests [*required*][object]Array of one request object to display in the widget. query [*required*]objectUpdated SLO List widget.limitint64Maximum number of results to display in the table.
default: `100`
query_string [*required*]stringWidget query. sort[object]Options for sorting results.column [*required*]stringFacet path for the columnorder [*required*]enumWidget sorting methods. Allowed enum values: `asc,desc`request_type [*required*]enumWidget request type. Allowed enum values: `slo_list`titlestringTitle of the widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the SLO List widget. Allowed enum values: `slo_list`
default: `slo_list`
{% /tab %}

{% tab title="example" %}

```json
{
  "requests": [
    {
      "query": {
        "limit": "integer",
        "query_string": "env:prod AND service:my-app",
        "sort": [
          {
            "column": "",
            "order": "desc"
          }
        ]
      },
      "request_type": "slo_list"
    }
  ],
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "slo_list"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Track the status of all your SLOs in Datadog](https://www.datadoghq.com/blog/slo-monitoring-tracking/)
- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
