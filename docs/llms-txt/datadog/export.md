# Source: https://docs.datadoghq.com/continuous_integration/explorer/export.md

---
title: Export Pipeline Executions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > Continuous Integration Visibility
  Explorer > Export Pipeline Executions
source_url: https://docs.datadoghq.com/explorer/export/index.html
---

# Export Pipeline Executions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

You can use your CI Visibility search query and visualization graphs in dashboards, monitors, and notebooks, or programmatically search for events using the [Search Pipeline Events endpoint](https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/#search-pipelines-events).

## Export the search query or visualization{% #export-the-search-query-or-visualization %}

You can copy, export, or download your aggregated search query and visualization graphs in the [CI Visibility Explorer](https://app.datadoghq.com/ci/pipeline-executions).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/explorer/pipeline_export.d7df2bed1aa671a0993640a15d6dbc84.png?auto=format"
   alt="Export your pipelines view in the CI Visibility Explorer" /%}

Click the **Export** button on the right hand corner and select an option from the dropdown menu:

- Share your [saved view](https://docs.datadoghq.com/continuous_integration/explorer/saved_views/) of the [CI Visibility Explorer](https://docs.datadoghq.com/continuous_integration/explorer/).
- Export your search results to a [CI Pipeline monitor](https://docs.datadoghq.com/monitors/types/ci/) that triggers alerts on predefined thresholds.
- Export your search results to an [existing notebook](https://docs.datadoghq.com/notebooks/) for reporting or consolidation purposes.
- Download your search results as a CSV file for individual CI Visibility test or pipeline events and specific aggregations.

Options available for some visualization types are not supported in others. For example, you cannot download a distribution graph into a CSV file.

## Further reading{% #further-reading %}

- [Search for your pipelines](https://docs.datadoghq.com/continuous_integration/search/)
- [Learn about Saved Views](https://docs.datadoghq.com/continuous_integration/explorer/saved_views)
- [Learn about CI Pipeline Monitors](https://docs.datadoghq.com/monitors/types/ci)
