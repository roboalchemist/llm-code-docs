# Source: https://docs.datadoghq.com/dashboards/widgets/free_text.md

---
title: Free Text Widget
description: Display text in a dashboard widget.
breadcrumbs: Docs > Dashboards > Widgets > Free Text Widget
---

# Free Text Widget

Free text is a widget that allows you to add headings to your [screenboard](https://docs.datadoghq.com/dashboards/#screenboards).

This is commonly used to state the overall purpose of the dashboard.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/free_text/free_text.9e81b9618cead0c17ac125a63073cb75.png?auto=format"
   alt="Free Text" /%}

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Enter text to display.
1. Choose your text formatting.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptioncolorstringColor of the text.font_sizestringSize of the text.text [*required*]stringText to display.text_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`type [*required*]enumType of the free text widget. Allowed enum values: `free_text`
default: `free_text`
{% /tab %}

{% tab title="example" %}

```json
{
  "color": "string",
  "font_size": "string",
  "text": "",
  "text_align": "string",
  "type": "free_text"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
