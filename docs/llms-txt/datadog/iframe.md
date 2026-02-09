# Source: https://docs.datadoghq.com/dashboards/widgets/iframe.md

---
title: Iframe Widget
description: Include an Iframe in your Datadog dashboards.
breadcrumbs: Docs > Dashboards > Widgets > Iframe Widget
---

# Iframe Widget

An inline frame (iframe) is a HTML element that loads another HTML page within the document. The iframe widget allows you to embed a portion of any other web page on your dashboard.

## Setup{% #setup %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/iframe/iframe_setup.80a17f91231fe86773e4829938c31e8a.png?auto=format"
   alt="Iframe setup" /%}

Enter the URL of the page you want to display inside the iframe. If you do not use an HTTPS URL, you may have to configure your browser to allow non-secure content.

## API{% #api %}

This widget can be used with the **[Dashboards API](https://docs.datadoghq.com/api/latest/dashboards/)**. See the following table for the [widget JSON schema definition](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/):

{% tab %}
ModelExample
{% tab title="-model" %}
Expand AllFieldTypeDescriptiontype [*required*]enumType of the iframe widget. Allowed enum values: `iframe`
default: `iframe`
url [*required*]stringURL of the iframe.
{% /tab %}

{% tab title="example" %}

```json
{
  "type": "iframe",
  "url": ""
}
```

{% /tab %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Building Dashboards using JSON](https://docs.datadoghq.com/dashboards/graphing_json/)
