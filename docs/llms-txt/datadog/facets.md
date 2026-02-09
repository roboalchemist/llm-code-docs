# Source: https://docs.datadoghq.com/events/explorer/facets.md

# Source: https://docs.datadoghq.com/continuous_integration/explorer/facets.md

# Source: https://docs.datadoghq.com/continuous_delivery/explorer/facets.md

---
title: Deployment Execution Facets
description: Learn about facets for filtering and grouping your deployment executions.
breadcrumbs: >-
  Docs > Continuous Delivery Visibility > Explore CD Visibility Deployments >
  Deployment Execution Facets
---

# Deployment Execution Facets

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

CD Visibility is in Preview. If you're interested in this feature, complete the form to request access.

[Request Access](https://docs.google.com/forms/d/e/1FAIpQLScNhFEUOndGHwBennvUp6-XoA9luTc27XBwtSgXhycBVFM9yA/viewform?usp=sf_link)
{% /callout %}

## Overview{% #overview %}

Facets are user-defined tags and attributes from your pipelines. They are useful for both qualitative and quantitative data analysis. Facets allow you to manipulate your deployments in the search queries that appear on [dashboards](https://docs.datadoghq.com/dashboards/) and in [notebooks](https://docs.datadoghq.com/notebooks/).

Creating facets is **not required** to [search deployment executions](https://docs.datadoghq.com/continuous_delivery/explorer#deployment-executions). Autocomplete capabilities use existing facets, but also any input that matches incoming deployment executions applies.

The [Deployment Executions page](https://app.datadoghq.com/ci/deployments/executions) includes out-of-the-box facets such as `Environment`, `Deployment Status`, and `Deployment Provider`. You can use facets in the CD Visibility Explorer to:

- [Search for and filter deployment executions](https://docs.datadoghq.com/continuous_delivery/explorer#deployment-executions).
- Perform deployment or environment analytics.
- Start troubleshooting after your deployments complete.

Navigate to [**Software Delivery** > **CD Visibility** > **Executions**](https://app.datadoghq.com/ci/deployments/executions) to access the list of facets left of the deployment executions list.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/explorer/facets.97c16a5d51c577cfdff57047ace7fc11.png?auto=format"
   alt="" /%}

### Qualitative facets{% #qualitative-facets %}

Use qualitative facets when you need to:

- **Get relative insights** for values.
- **Count unique values**.
- Frequently **filter** your deployment executions against particular values. For example, use the facet on the environment tag to scope troubleshooting down to development, staging, or production environments.

**Note:** Although facets are not required to filter on tags, defining facets for tags that you use during investigations can reduce your time to resolution.

### Quantitative measures{% #quantitative-measures %}

Use quantitative measures when you need to:

- **Aggregate** values from multiple deployment executions.
- **Range filter** your deployment executions.
- **Sort** your deployment executions against that value.

#### Types{% #types %}

Measures have either a long integer or double value for equivalent capabilities.

#### Units{% #units %}

Measures support units (**time** in seconds or **size** in bytes) to handle orders of magnitude at query time and display time. The unit is a property of the measure itself, not of the field.

For example, consider a `duration` measure in nanoseconds. Suppose deployments from `env:staging` have `duration:10000000`, meaning `10 milliseconds`. Supposed deployments from `env:qa` have `duration:5000000`, meaning `5 milliseconds`. Use `duration:>2ms` to consistently query deployment execution tags from both environments at once. For more information about search queries, see [Search Syntax](https://docs.datadoghq.com/continuous_delivery/explorer/search_syntax).

## Facet panel{% #facet-panel %}

The search bar provides the most comprehensive set of interactions to filter and group your data. However, for many cases, the facet panel is a straightforward way to navigate into your data. Open a facet to see a summary of its content for the scope of the current query.

The search bar and URL automatically reflect your selections from the facet panel.

- **Facets (qualitative)** come with a top list of unique values, and a count of deployment executions matching each of them.
- **Measures (quantitative)** come with a slider indicating minimum and maximum values. Use the slider, or input numerical values, to scope the search query to different bounds.

### Grouping facets{% #grouping-facets %}

Facets are grouped into meaningful themes in the facet list. Assigning or reassigning a group for a facet only affects the facet list, and has no impact on search or analytics.

### Filtering facets{% #filtering-facets %}

Use the search facets box on the facet panel to scope the whole facet list and navigate to the facet you need to interact with. *Search facets* uses the facet display name and field name to scope results.

## Creating facets{% #creating-facets %}

Creating a facet on a deployment execution attribute or tag is not required to search for deployment executions. Facets are useful if you wish to add a meaningful description to a specific deployment execution attribute, or if you want the attribute values to appear on the Facets list.

### Creating facets from the Deployment Details side panel{% #creating-facets-from-the-deployment-details-side-panel %}

Create a facet from the Deployment Details side panel so that most of the facet details are pre-filled.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/explorer/create_facet.b00e988d8aff086a0a54c95603cf5d09.png?auto=format"
   alt="Create a facet from the Deployment Details side panel" /%}

1. Navigate to a deployment execution of interest in the [Deployment Executions page](https://app.datadoghq.com/ci/deployments/executions) that contains the field to create a facet on.

1. Open the Deployment Details side panel by selecting the deployment execution from the list.

1. Click on the desired field and create a facet from there:

   - If the field has a numerical value, you can create either a facet or a measure.
   - If the field has a string value, only facet creation is available.

### Creating facets from the facet list{% #creating-facets-from-the-facet-list %}

If finding a deployment execution that has the desired field is not an option, create a facet directly from the facet panel by clicking **+ Add**.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/explorer/add_facet.7d21517ae15ce0e731423ad040da0f64.png?auto=format"
   alt="Add a facet from the facet side panel" /%}

Define the underlying field (key) name for this facet:

- Use tag key name for environment tags.
- Use the attribute path for deployment execution attributes, with `@` prefix.

Autocomplete based on the content in deployment executions of the current views helps you to define the proper field name. But you can use virtually any value here, specifically in the case that you don't yet have matching deployment executions received by Datadog.

## Further reading{% #further-reading %}

- [Learn how to query and visualize deployments](https://docs.datadoghq.com/continuous_delivery/explorer/)
