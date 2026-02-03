# Source: https://docs.datadoghq.com/dashboards/widgets/topology_map.md

---
title: Topology Map Widget
description: >-
  Displays a map of a service to all of the services that call it, and all of
  the services that it calls.
breadcrumbs: Docs > Dashboards > Widgets > Topology Map Widget
---

# Topology Map Widget

The Topology Map widget displays a visualization of data sources and their relationships to help understand how data flows through your architecture.

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Choose the data to graph:

   - Service Map: The node in the center of the widget represents the mapped service. Services that call the mapped service are shown with arrows from the caller to the service. To learn more about the Service Map, reference the [Service Map feature of APM](https://docs.datadoghq.com/tracing/services/services_map/).

1. Enter a title for your graph.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescription custom_links[object]List of custom links.is_hiddenbooleanThe flag for toggling context menu link visibility.labelstringThe label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.linkstringThe URL of the custom link. URL must include `http` or `https`. A relative URL must start with `/`.override_labelstringThe label ID that refers to a context menu link. Can be `logs`, `hosts`, `traces`, `profiles`, `processes`, `containers`, or `rum`. requests [*required*][object]One or more Topology requests. queryobjectQuery to service-based topology data sources like the service map or data streams.data_sourceenumName of the data source Allowed enum values: `data_streams,service_map`filters[string]Your environment and primary tag (or * if enabled for your account).servicestringName of the servicerequest_typeenumWidget request type. Allowed enum values: `topology`titlestringTitle of your widget.title_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`title_sizestringSize of the title.type [*required*]enumType of the topology map widget. Allowed enum values: `topology_map`
default: `topology_map`
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
  "requests": [
    {
      "query": {
        "data_source": "string",
        "filters": [
          "env:prod",
          "az:us-east"
        ],
        "service": "myService"
      },
      "request_type": "string"
    }
  ],
  "title": "string",
  "title_align": "string",
  "title_size": "string",
  "type": "topology_map"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
- [Service Map](https://docs.datadoghq.com/tracing/services/services_map/)
