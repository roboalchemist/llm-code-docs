# Source: https://docs.datadoghq.com/cloud_cost_management/tags/tag_explorer.md

---
title: Tag Explorer
description: >-
  Search and manage all cost-related tags, including those from your bills, with
  insights into their sources.
breadcrumbs: Docs > Cloud Cost Management > Tags > Tag Explorer
---

# Tag Explorer

## Overview{% #overview %}

[Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/) detects the sources for all of your cost-related tags. You can search and manage tags for breaking down costs, including [Custom Costs](https://docs.datadoghq.com/cloud_cost_management/setup/custom), [Datadog costs](https://docs.datadoghq.com/cloud_cost_management/datadog_costs), and [SaaS cost integrations](https://docs.datadoghq.com/cloud_cost_management/setup/saas_costs).

Use the [Tag Explorer](https://app.datadoghq.com/cost/tags) to understand the sources and view descriptions for each tag. This includes tags managed through [Tag Pipelines](https://docs.datadoghq.com/cloud_cost_management/allocation/tag_pipelines). Tag Pipelines allow you to create and manage tag rules that fix missing or incorrect tags on your cloud bill, or create inferred tags according to your business logic.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/dropdown_1.505c1339e7c8ba4b4b11be09d210f721.png?auto=format"
   alt="Search through the list of Azure cost-related tags in the Tag Explorer and understand where the costs are coming from" /%}

## Setup{% #setup %}

To use the Tag Explorer, you must configure [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/) for AWS, Azure, Google Cloud, or Oracle Cloud.

See the respective documentation for your cloud provider:

- [aws](https://docs.datadoghq.com/cloud_cost_management/setup/aws/)
- [azure](https://docs.datadoghq.com/cloud_cost_management/setup/azure/)
- [google cloud](https://docs.datadoghq.com/cloud_cost_management/setup/google_cloud/)

## Search and manage tags{% #search-and-manage-tags %}

Navigate to [**Cloud Cost** > **Settings** > **Tag Explorer**](https://app.datadoghq.com/cost/tags) to search for tags related to your cloud provider bills, custom costs, Datadog costs, SaaS cost integrations, and tag pipelines.

{% tab title="AWS" %}
For AWS tags, select **AWS** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/aws_1.5b18fa3c369eb5368f143ebf21ebae67.png?auto=format"
   alt="Search through the list of AWS cost-related tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Azure" %}
For Azure tags, select **Azure** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/azure_1.0bdd030e0ab9dc3d63824c7af85f88f2.png?auto=format"
   alt="Search through the list of Azure cost-related tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Google" %}
For Google Cloud tags, select **Google** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/google_1.80c20cd28e7d925b785ea87ef6f65941.png?auto=format"
   alt="Search through the list of Google Cloud cost-related tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Datadog" %}

{% alert level="danger" %}
Daily Datadog costs are in Preview.
{% /alert %}

For Datadog tags, select **Datadog** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/datadog_1.1ab5c8f0f4f4404c04196a43623a6384.png?auto=format"
   alt="Search through the list of your Datadog cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Confluent Cloud" %}

{% alert level="danger" %}
Confluent Cloud costs are in Preview.
{% /alert %}

For Confluent Cloud tags, select **Confluent Cloud** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/confluent_cloud_1.d38da2074bd6d500e09d02682f016870.png?auto=format"
   alt="Search through the list of your Confluent Cloud cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Databricks" %}

{% alert level="danger" %}
Databricks costs are in Preview.
{% /alert %}

For Databricks tags, select **Databricks** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/databricks_1.b1e2fd7fe3139101c7f358a335d38ddd.png?auto=format"
   alt="Search through the list of your Databricks cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Fastly" %}

{% alert level="danger" %}
Fastly costs are in Preview.
{% /alert %}

For Fastly tags, select **Fastly** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/fastly_1.91d7ca320873465f995543433ab0b411.png?auto=format"
   alt="Search through the list of your Fastly cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Elastic Cloud" %}

{% alert level="danger" %}
Elastic Cloud costs are in Preview.
{% /alert %}

For Elastic Cloud tags, select **Elastic Cloud** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/elastic_cloud.c8ec3aa0f96a6d5b75502316695a0b22.png?auto=format"
   alt="Search through the list of your Elastic Cloud cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="MongoDB" %}

{% alert level="danger" %}
MongoDB costs are in Preview.
{% /alert %}

For MongoDB tags, select **MongoDB** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/mongodb_1.e1febafb5c694dff5a8b956fced3ad3d.png?auto=format"
   alt="Search through the list of your MongoDB cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="OpenAI" %}

{% alert level="danger" %}
OpenAI costs are in Preview.
{% /alert %}

For OpenAI tags, select **OpenAI** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/openai_1.a4caf316c70f22b60102517823b59679.png?auto=format"
   alt="Search through the list of your OpenAI cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Snowflake" %}

{% alert level="danger" %}
Snowflake costs are in Preview.
{% /alert %}

For Snowflake tags, select **Snowflake** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/snowflake_1.4e8e5fec511ef30e06ff972e3b28470d.png?auto=format"
   alt="Search through the list of your Snowflake cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

{% tab title="Twilio" %}

{% alert level="danger" %}
Twilio costs are in Preview.
{% /alert %}

For Twilio tags, select **Twilio** from the dropdown menu on the top right corner.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/twilio_1.d1f2d02fd6619ecfe976890e9e0759c7.png?auto=format"
   alt="Search through the list of your Twilio cost tags in the Tag Explorer and understand where the costs are coming from" /%}

{% /tab %}

## Set preferred tags{% #set-preferred-tags %}

You can set up to five preferred tags to highlight your organization's most important tags throughout Cloud Cost Management. These tags appear first when selecting tags in the [Explorer page](https://app.datadoghq.com/cost/explorer), [CCM Reports](https://docs.datadoghq.com/cloud_cost_management/reporting), and [Custom Allocation Rules](https://docs.datadoghq.com/cloud_cost_management/allocation/custom_allocation_rules), among other areas.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/preferred_tags_1.d1511cf0099a861cf268d48dbf606499.png?auto=format"
   alt="Preferred tags are shown throughout CCM" /%}

You can choose preferred tags from any of your existing cost data tags, including [Tag Pipelines](https://docs.datadoghq.com/cloud_cost_management/allocation/tag_pipelines). These settings apply to your entire organization.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/tag_explorer/preferred_tags_2.a40b41eb81613b58a864d820653c820c.png?auto=format"
   alt="Select your preferred tags in Tag Explorer" /%}

## Further reading{% #further-reading %}

- [Learn about Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
- [Learn about Custom Costs](https://docs.datadoghq.com/cloud_cost_management/setup/custom)
- [Learn about Datadog Costs](https://docs.datadoghq.com/cloud_cost_management/datadog_costs)
- [Learn about SaaS Cost Integrations](https://docs.datadoghq.com/cloud_cost_management/setup/saas_costs)
- [Learn about Tag Pipelines](https://docs.datadoghq.com/cloud_cost_management/allocation/tag_pipelines)
