# Source: https://docs.datadoghq.com/dashboards/widgets/sankey.md

---
title: Sankey Widget
description: >-
  Visualize user flow paths and transitions between different states or pages
  using Sankey diagram representations.
breadcrumbs: Docs > Dashboards > Widgets > Sankey Widget
---

# Sankey Widget

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
The Sankey widget is not available in the selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ().
{% /alert %}


{% /callout %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/widgets/sankey/sankey_widget.17b53a0753abcc75b6e33b9cb1b90e38.png?auto=format"
   alt="Sankey widget configuration showing an example graph" /%}

The Sankey widget shows user flow, movement, or change from one application state to another. This widget is available for Product Analytics.

## Setup{% #setup %}

### Configuration{% #configuration %}

1. Define the Sankey and select from the dropdown options to display the steps users took before or after visiting a given view.
1. Filter your data by user segment or other application tag attributes.
1. Set view options to show `N` number of views per step and customize your graph to sort by session count and display paths to other view.

## Further Reading{% #further-reading %}

- [Build Sankey Diagrams in Product Analytics](https://docs.datadoghq.com/product_analytics/journeys/sankey/)
