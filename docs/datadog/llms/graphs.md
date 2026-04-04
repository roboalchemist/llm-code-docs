# Source: https://docs.datadoghq.com/dashboards/sharing/graphs.md

---
title: Share Graphs
description: >-
  Generate embed codes for individual graphs and manage sharing permissions with
  revocation and IP restrictions.
breadcrumbs: Docs > Dashboards > Sharing > Share Graphs
---

# Share Graphs

To share a graph:

1. From the graph you want to share, click the pencil icon in the upper right corner.
1. Under the *Graph your data* section, select the **Share** tab.
1. Pick a timeframe for your graph.
1. Pick a graph size.
1. Choose to include the legend or not.
1. Get the embed code with the **Generate embed code** button.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/sharing/graph_share_tab.8281a1263dda99b5e019b5bdfeac1cee.png?auto=format"
   alt="Share tab in a graphing editor" /%}

All shared graphs are listed in the [Public Sharing Settings page](https://app.datadoghq.com/organization-settings/public-sharing). You can also revoke individual shared graphs or disable all shared graphs from this page.

## Revoke{% #revoke %}

To revoke the keys used to share individual (embedded) graphs:

1. Navigate to [**Organization Settings > Public Sharing > Shared Graphs**](https://app.datadoghq.com/organization-settings/public-sharing/shared-graphs) to see a list of all shared graphs.
1. Find your graph by using the search bar or by sorting the table columns.
1. Click on the **Revoke** button next to the graph you want to stop sharing.

## Applying restrictions{% #applying-restrictions %}

You can restrict access on an IP address basis to your dashboard. Email [Datadog support](https://docs.datadoghq.com/help/) to enable the IP address include listing feature that allows administrators to provide a list of IP addresses that have access to shared dashboards. After it's enabled, manage your restrictions on your organization's [Public Sharing](https://app.datadoghq.com/organization-settings/public-sharing/settings) page.

## API{% #api %}

Datadog has a [dedicated API](https://docs.datadoghq.com/api/latest/embeddable-graphs/) allowing you to interact with your shared graphs (embeds):

| Endpoint                                                                                          | Description                                                             |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Get all embeds](https://docs.datadoghq.com/api/latest/embeddable-graphs/#get-all-embeds)         | Get a list of previously created embeddable graphs.                     |
| [Create embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#create-embed)             | Creates a new embeddable graph.                                         |
| [Get specific embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#get-specific-embed) | Get the HTML fragment for a previously generated embed with `embed_id`. |
| [Enable embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#enable-embed)             | Enable the specified embed.                                             |
| [Revoke embed](https://docs.datadoghq.com/api/latest/embeddable-graphs/#revoke-embed)             | Revoke the specified embed.                                             |

## Further Reading{% #further-reading %}

- [Share dashboards securely with anyone outside of your organization](https://www.datadoghq.com/blog/dashboard-sharing/)
- [Create Dashboards in Datadog](https://docs.datadoghq.com/dashboards/)
- [Embeddable Graphs with Template Variables](https://docs.datadoghq.com/dashboards/guide/embeddable-graphs-with-template-variables/)
- [Discover Widgets for your Dashboard](https://docs.datadoghq.com/dashboards/widgets/)
