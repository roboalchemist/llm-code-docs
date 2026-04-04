# Source: https://docs.datadoghq.com/cloud_cost_management/allocation/tag_pipelines.md

---
title: Tag Pipelines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloud Cost Management > Cost Allocation > Tag Pipelines
---

# Tag Pipelines

## Overview{% #overview %}

Tags are the foundation for all Cloud Cost Management analysis and allocation. They enable you to break down spending by service, team, project, environment, or any dimension relevant to your business. Tag Pipelines enforce the use of standardized tags across your cloud resources and ensure consistent, accurate cost attribution throughout your organization.

With [Tag Pipelines](https://app.datadoghq.com/cost/tag-pipelines), you can create tag rules to address missing or incorrect tags on your cloud bills. You can also create new inferred tags that align with specific business logic to enhance the accuracy of your cost tracking. These standardized tags power all cost analysis capabilities, including container cost allocation, custom allocation rules, and cost recommendations.

Tag Pipelines apply to Cloud Cost metrics from all providers. The rules you create affect all cost data and cost recommendations, ensuring consistency across dashboards, monitors, and allocation reports.

When tag pipelines change, the new rules are automatically applied to the most recent three months of data. It may take up to 24 hours for the historical data update to complete after rules are added or modified.

All new users have the recommended rule for [turning on tag normalization](https://docs.datadoghq.com/cloud_cost_management/tags#how-tags-are-normalized) enabled by default.

## Create a ruleset{% #create-a-ruleset %}

You can manage tag pipeline rulesets using the [API](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-tag-pipeline-ruleset), [Terraform](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/tag_pipeline_ruleset), or directly in Datadog by following the instructions below.

To create a ruleset, navigate to [**Cloud Cost > Settings > Tag Pipelines**](https://app.datadoghq.com/cost/tag-pipelines).

{% alert level="danger" %}
You can create up to 100 rules. API-based Reference Tables are not supported.
{% /alert %}

Before creating individual rules, create a ruleset (a folder for your rules) by clicking **+ New Ruleset**.

Within each ruleset, click **+ Add New Rule** and select a rule type: **Add tag**, **Alias tag keys**, or **Map multiple tags**. These rules execute in a sequential, deterministic order from top to bottom.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/pipelines-create-ruleset.533a5639e62d3d844bd0b5f07f079d39.png?auto=format"
   alt="A list of tag rules on the Tag Pipelines page displaying various categories such as team, account, service, department, business unit, and more" /%}

You can organize rules and rulesets to ensure the order of execution matches your business logic.

### Add tag{% #add-tag %}

Add a new tag (key + value) based on the presence of existing tags on your Cloud Costs data.

For example, you can create a rule to tag all resources with their business unit based on the services those resources are a part of.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/pipelines-add-tag.05f80dfea2e8acff33209b1f6ba6d977.png?auto=format"
   alt="Add new business unit tag to resources with service:process-agent or service:process-billing." /%}

Under the **Additional options** section, you have the following options:

- **Only apply if tag `{tag}` doesn't exist** - Ensures the rule only applies if the specified tag (`business-unit` in the example above) doesn't already exist.
- **Apply case-insensitive matching to resource tags** - Enables tags defined in the `To resources with tag(s)` field and tags from the cost data to be case insensitive. For example, if resource tags from the UI are: `foo:bar` and the tag from the cost data is `Foo:bar`, then the two can be matched.

### Alias tag keys{% #alias-tag-keys %}

Map existing tag values to a more standardized tag.

For example, if your organization wants to use the standard `application` tag key, but several teams have a variation of that tag (like `app`, `webapp`, or `apps`), you can alias `apps` to `application`. Each alias tag rule allows you to alias a maximum of 25 tag keys to a new tag.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/pipelines-alias-tag.4a1fab6f093ebd3ace1015f29dd2ee8a.png?auto=format"
   alt="Add application tag to resources with app, webapp, or apps tag." /%}

Add the application tag to resources with `app`, `webapp`, or `apps` tags. The rule stops executing for each resource after the first match is found. For example, if a resource already has an `app` tag, then the rule no longer attempts to identify a `webapp` or `apps` tag.

To ensure the rule only applies if the `application` tag doesn't already exist, click the toggle in the **Additional options** section.

### Map multiple tags{% #map-multiple-tags %}

Use [Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables/?tab=manualupload) to add multiple tags to cost data without creating multiple rules. This maps the values from your Reference Table's primary key column to values from cost tags. If found, the pipeline adds the selected Reference Table columns as tags to cost data.

For example, if you want to add information about which VPs, organizations, and business_units different AWS and Azure accounts fall under, you can create a table and map the tags.

{% image
   source="https://datadog-docs.imgix.net/images/cloud_cost/pipelines-map-multiple-tags.37af446ad62de977ef311b8c4d26ac0c.png?auto=format"
   alt="Add account metadata like customer_name using reference tables for tag pipelines" /%}

Similar to Alias tag keys, the rule stops executing for each resource after the first match is found. For example, if an `aws_member_account_id` is found, then the rule no longer attempts to find a `subscriptionid`.

Under the **Additional options** section, you have the following options:

- **Only apply if columns don't exist** - Ensures the defined columns are only added if they do not already exist with the associated tags from the cost data.
- **Apply case-insensitive matching for primary key values** - Enables case-insensitive matching between the primary key value from the reference table and the value of the tag in the cost data where the tag key matches the primary key. For example, if the primary key value pair from the UI is `foo:Bar` and the tag from the cost data is `foo:bar`, then the two can be matched.

## Reserved tags{% #reserved-tags %}

Certain tags such as `env` and `host` are [reserved tags](https://docs.datadoghq.com/getting_started/tagging/), and are part of [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/). The `host` tag cannot be added in Tag Pipelines.

Using tags helps correlate your metrics, traces, processes, and logs. Reserved tags like `host` provide visibility and effective monitoring across your infrastructure. For optimal correlation and actionable insights, use these reserved tags as part of your tagging strategy in Datadog.

## Delete tags{% #delete-tags %}

To delete a tag created using Tag Pipelines, delete the rule that created it. Within 24 hours, the tag is automatically removed from the most recent three months of data. To remove the tag from older data, contact [Datadog support](https://docs.datadoghq.com/help/).

## Further reading{% #further-reading %}

- [Manage and optimize your OCI costs with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/cloud-cost-management-oci)
- [Learn about Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/)
- [Getting Started with Tags](https://docs.datadoghq.com/getting_started/tagging/)
- [Learn about Reference Tables](https://docs.datadoghq.com/integrations/guide/reference-tables)
