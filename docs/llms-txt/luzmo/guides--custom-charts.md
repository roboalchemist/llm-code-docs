# Source: https://developer.cumul.io/guide/guides--custom-charts.md

---
title: Developing custom charts
description: Create specialized data visualizations with complete flexibility using Luzmo's Custom Chart Builder. Design exactly the chart types your data needs.
url: https://developer.luzmo.com/guide/guides--custom-charts
type: guide
---

# Developing a Custom chart


## Section Index

This reference is split into separate files. **For LLM agents**: Match the user's question to the headers below and read only the relevant sub-file(s).

### [Introduction](https://developer.luzmo.com/guide/guides--custom-charts--introduction.md)


### [Quick Start](https://developer.luzmo.com/guide/guides--custom-charts--quick-start.md)

- Prerequisites
- Installation

### [Project structure](https://developer.luzmo.com/guide/guides--custom-charts--project-structure.md)


### [Creating your custom chart](https://developer.luzmo.com/guide/guides--custom-charts--creating-your-custom-chart.md)

- Key files to modify

### [Manifest configuration](https://developer.luzmo.com/guide/guides--custom-charts--manifest-configuration.md)

- Required properties
- Optional properties
- Slot options properties
- Example Manifest

### [Chart implementation](https://developer.luzmo.com/guide/guides--custom-charts--chart-implementation.md)

- Core functions
  - `render` function
  - `resize` function
  - `buildQuery` function (optional)
  - Data formatting
- Chart styling
  - Using the dashboard or chart theme
  - Styling with chart.css
- Interacting with the Dashboard
  - Filter event (setFilter)
  - Custom event (customEvent)

### [Adding third party libraries](https://developer.luzmo.com/guide/guides--custom-charts--adding-third-party-libraries.md)


### [Building and packaging](https://developer.luzmo.com/guide/guides--custom-charts--building-and-packaging.md)

- Production package
- Validation only

### [Troubleshooting](https://developer.luzmo.com/guide/guides--custom-charts--troubleshooting.md)

- Common issues
- Logs and debugging

### [Other resources](https://developer.luzmo.com/guide/guides--custom-charts--other-resources.md)



---

## Related Pages

- [Retrieving Luzmo resource IDs](https://developer.luzmo.com/guide/guides--retrieving-luzmo-resource-ids.md): Learn how to find unique identifiers for Luzmo resources like dashboards, charts, datasets, columns, connections, and collections through the UI or API.
- [Querying data](https://developer.luzmo.com/guide/guides--querying-data.md): Use the Luzmo Data API to query data from your datasets. Learn the API Query Syntax including dimensions, measures, filters, order, limit, and options.
- [Pushing data](https://developer.luzmo.com/guide/guides--pushing-data.md): Learn to programmatically store data in Luzmo's OLAP database using the Data API to create new datasets, append or replace data in existing datasets.
- [Creating a Flex chart](https://developer.luzmo.com/guide/guides--creating-a-column-flex-chart.md): Step-by-step walkthrough to create a simple Column chart using Luzmo's Flex SDK, including slots, options, filters, and interactivity features.
- [Creating an AI Chat Assistant](https://developer.luzmo.com/guide/guides--creating-an-iq-chat-component.md)


---

## Sitemap

- [Official best practices and implementation guidelines](https://developer.luzmo.com/AGENTS.md)
- [Overview of all docs pages](https://developer.luzmo.com/llms.txt)
