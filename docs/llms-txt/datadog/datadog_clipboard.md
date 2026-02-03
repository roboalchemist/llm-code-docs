# Source: https://docs.datadoghq.com/dashboards/guide/datadog_clipboard.md

---
title: Datadog Clipboard
description: Create and manage incidents
breadcrumbs: Docs > Dashboards > Graphing Guides > Datadog Clipboard
---

# Datadog Clipboard

## Overview{% #overview %}

The Datadog Clipboard is a cross-platform tool for collecting and sharing signals across contexts. It is personal to each user and stores all copied graphs alongside any saved links. Signals can be grouped and exported to a dashboard, notebook, or incident.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/clipboard-full.4ed934570a13cb7a5bdd0232b04e3a03.png?auto=format"
   alt="The main clipboard" /%}

## Cross-page exploration{% #cross-page-exploration %}

The Clipboard works on all pages in Datadog and keeps a record of all graphs copied by an individual user. The Clipboard does not automatically copy query text, event JSON, or other text-based content.

## Opening the Clipboard{% #opening-the-clipboard %}

To open the Clipboard, copy any graph and click **Open Clipboard** in the popup.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/open-clipboard.a47a6de99670205af8a73a87789ca139.png?auto=format"
   alt="Open a graph in the Clipboard" /%}

Or, click "`Cmd/Ctrl + Shift + K` to open" on the minimized Clipboard.

The Clipboard can also be opened and closed using `Cmd/Ctrl + Shift + K`. To minimize the Clipboard, click the Minimize icon. The minimized Clipboard persists on all pages of Datadog.

## Adding clips{% #adding-clips %}

To add a graph, copy it with `Cmd/Ctrl + C` or click **Copy** in the export menu. Once the Clipboard is open, copied graphs get added automatically.

To add a URL, open the Clipboard and click **Add current page**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/add-page.94e11e5335e942ce2ee2f572cf459e27.png?auto=format"
   alt="Add a dashboard to the Clipboard" /%}

## Managing clips{% #managing-clips %}

Each item in the Clipboard can be opened, cloned, or deleted; these options are available when you hover over any signal. Opening an item navigates to the link of the original signal. Open the source of any graph (like the dashboard it was clipped from) by clicking the title of the item.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/managing-clips.55ec645445940c275828ee5f964bb531.png?auto=format"
   alt="Manage your clips" /%}

The Clipboard holds a maximum of 20 signals. Remove signals by deleting them individually, or by clicking **Remove All**. If more than 20 signals are added, the oldest signals, stored furthest to the left, are removed automatically.

## Exporting{% #exporting %}

Items on the Clipboard can be exported to Dashboards, Notebooks, or Incidents using keyboard shortcuts or the export menu. To copy an individual signal, hover over it and use `Cmd/Ctrl + C` to copy, and paste it into a dashboard or notebook with `Cmd/Ctrl + V`. To copy multiple signals, use `Shift + Click` to select graphs and links, and use `Cmd/Ctrl + C` to copy them.

Alternatively, export your selection to a new or existing dashboard, notebook, or incident using the export menu. Only [supported graphs](https://docs.datadoghq.com/notebooks/#visualization) can be exported to Notebooks.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/exporting.eb6765acdb7129552a9dbdf5399ed038.png?auto=format"
   alt="Export from the Clipboard" /%}

## Further Reading{% #further-reading %}

- [Explore your data effortlessly with the Datadog Clipboard](https://www.datadoghq.com/blog/datadog-clipboard/)
