# Source: https://docs.datadoghq.com/dashboards/widgets/note.md

---
title: Notes and Links Widget
description: Display text in a dashboard widget.
breadcrumbs: Docs > Dashboards > Widgets > Notes and Links Widget
---

# Notes and Links Widget

The **Notes & Links** widget is similar to the [free text widget](https://docs.datadoghq.com/dashboards/widgets/free_text/) but contains more formatting and display options.

**Note**: The Notes & Links widget does not support inline HTML.

## Setup{% #setup %}

1. Enter the text you want to display. Markdown is supported.
1. Select a preset template or customize the display options.
1. Select a text size and the widget's background color.
1. To adjust the position of the text, click on the **Alignment** buttons. To not include padding, click **No Padding**.
1. To include a pointer, click **Show Pointer** and select a position from the dropdown menu.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/note/overview.3e7ce399c85f741ee477a59a5f5275b5.png?auto=format"
   alt="Adding text in the Markdown field of the Notes & Links widget editor" /%}

When you are ready to create the widget, click **Save**.

This widget supports template variables. Use the `$<VARIABLE_NAME>.value` syntax to dynamically update the widget content.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/note/template_variable.6563210acea1b90fb6f749556f5f67b2.png?auto=format"
   alt="Using template variables in the Markdown field of the Notes & Links widget editor" /%}

In this example, `$env.value` updates the value of a link to the selected environment.

**Note**: Template variables in URLs are only populated in the URL pathname (not the hostname). For example, `https://$env.value.example.com/$env.value` renders as `https://$env.value.example.com/admin`.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptionbackground_colorstringBackground color of the note.content [*required*]stringContent of the note.font_sizestringSize of the text.has_paddingbooleanWhether to add padding or not.
default: `true`
show_tickbooleanWhether to show a tick or not.text_alignenumHow to align the text on the widget. Allowed enum values: `center,left,right`tick_edgeenumDefine how you want to align the text on the widget. Allowed enum values: `bottom,left,right,top`tick_posstringWhere to position the tick on an edge.type [*required*]enumType of the note widget. Allowed enum values: `note`
default: `note`
vertical_alignenumVertical alignment. Allowed enum values: `center,top,bottom`
{% /tab %}

{% tab title="example" %}

```json
{
  "background_color": "string",
  "content": "",
  "font_size": "string",
  "has_padding": false,
  "show_tick": false,
  "text_align": "string",
  "tick_edge": "string",
  "tick_pos": "string",
  "type": "note",
  "vertical_align": "string"
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Learn how to build dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
