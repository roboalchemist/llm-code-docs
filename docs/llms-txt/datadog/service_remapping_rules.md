# Source: https://docs.datadoghq.com/tracing/services/service_remapping_rules.md

---
title: Service remapping rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > APM > Service Observability > Service remapping rules
source_url: https://docs.datadoghq.com/services/service_remapping_rules/index.html
---

# Service remapping rules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Service remapping rules are in Preview.

[Request Access](https://www.datadoghq.com/product-preview/service-remapping-rules/)
{% /callout %}

## Overview{% #overview %}

Update how your services appear across Datadog without changing tracer configuration or redeploying code. Service remapping rules allow you to rename, merge, or split services; or create new services based on infrastructure tags from the Datadog UI. You can also create remapping rules for other entity types, such as datastores and queues.

{% alert level="info" %}
Each organization can contain up to 100 remapping rules.
{% /alert %}

## Prerequisites{% #prerequisites %}

You must have the `apm_service_renaming_write` permission to create remapping rules. See [Permissions](https://docs.datadoghq.com/account_management/rbac/permissions) for details on Datadog role-based access control.

### Tracer version requirements{% #tracer-version-requirements %}

You can create service remapping rules only for services instrumented with supported tracer versions. If a service is reporting from an older tracer version, upgrade the tracer before creating remapping rules for that service.

| Language   | Minimum supported tracer version                                        |
| ---------- | ----------------------------------------------------------------------- |
| Dotnet     | [3.4.0](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v3.4.0) |
| Go         | [1.55.0](https://github.com/DataDog/dd-trace-go/releases/tag/v1.55.0)   |
| Java       | [1.20.0](https://github.com/DataDog/dd-trace-java/releases/tag/v1.20.0) |
| JavaScript | [4.16.0](https://github.com/DataDog/dd-trace-js/releases/tag/v4.16.0)   |
| PHP        | [0.94.1](https://github.com/DataDog/dd-trace-php/releases/tag/0.94.1)   |
| Python     | [1.19.0](https://github.com/DataDog/dd-trace-py/releases/tag/v1.19.0)   |
| Ruby       | [1.15.0](https://github.com/DataDog/dd-trace-rb/releases/tag/v1.15.0)   |

## Create a service remapping rule{% #create-a-service-remapping-rule %}

### Step 1: Select remapping action and entities to target{% #step-1-select-remapping-action-and-entities-to-target %}

1. In Datadog, navigate to **APM** > **Software Catalog** > **Manage** > [**Manage Renaming Rules**](https://app.datadoghq.com/software/settings/service-rename) and click **+ Add Rule**.

Alternatively, navigate to **APM** > [**Software Catalog**](https://app.datadoghq.com/software) and click on a service to open the service side panel. From there, click **Service Page** > **Service Renaming**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/services/renaming_rules/service-side-panel.41c140a9d03535155d3a75b1f54f3a85.png?auto=format"
      alt="The side panel for a service, showing the Service Page dropdown menu with a Service Remapping option" /%}



1. Choose a remapping action to perform for your new remapping rule.

   - You can select to split a single entity, rename an entity, merge multiple entities together, or rename several entities.
   - You can also choose to identify a service based on infrastructure tags.

1. Use the search bar to select the entities you want to rename.

   - You can select one or more entities, but all must be of the same type (service, datastore, or queue).
   - As you select entities, a span query is built in the background. To edit the query, select **Build Advanced Query**.
   - If you're correlating a service with infrastructure tags, you can only select *one* service.

### Step 2: Specify new entity name{% #step-2-specify-new-entity-name %}

In the text box, enter a unique name for the selected entity (or entities). Alternatively, use tag values with the `{{tagName}}` syntax to rename based on an entity's tags.

1. If tag values follow a pattern, apply a regular expression to extract only the portion you want in the name.
1. If you're correlating a service with infrastructure tags, choose one of the suggested infrastructure tags for the selected service.

### Step 3: Name your rule and review{% #step-3-name-your-rule-and-review %}

1. Optionally, enter a descriptive name for the remapping rule so you can identify it later.
1. Review and save your remapping rule.

## Remapping rules behavior{% #remapping-rules-behavior %}

Services with remapping rules appear with consistent names across [APM](https://docs.datadoghq.com/tracing/services/), [Software Catalog](https://docs.datadoghq.com/internal_developer_portal/software_catalog/), [Logs](https://docs.datadoghq.com/logs/explorer/), and [Metrics](https://docs.datadoghq.com/metrics/explorer/).

- **Historical data:** Changes made by remapping rules affect only telemetry ingested while a rule is active, and past data is not updated retroactively. Deleting or modifying a rule stops it from applying to new data, but does not revert names on previously ingested data.
- **Logs service remapper:** Service remapping rules occur before logs pipelines. If the logs service remapper and remapping rules are both applied to a service, the remapping rules take precedence.
- **Dashboards and monitors:** Existing queries that reference old service names are not automatically updated. Review and update these manually.
- **Service overrides:** Remapping rules apply to base services; service overrides are not renamed.
