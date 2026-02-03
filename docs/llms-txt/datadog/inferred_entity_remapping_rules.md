# Source: https://docs.datadoghq.com/tracing/services/inferred_entity_remapping_rules.md

---
title: Remapping rules for inferred entities
description: >-
  Create custom names for inferred entities like databases and queues using tags
  and regular expressions.
breadcrumbs: Docs > APM > Service Observability > Remapping rules for inferred entities
---

# Remapping rules for inferred entities

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

In Datadog, you can remap inferred entities, including datastores and queues, to make them easier to identify and manage. Remapping rules let you override the `peer.service` tag on spans with custom names, or generate names dynamically using tags and regular expressions. This functionality applies across all of APM, not only in the [Software Catalog](https://docs.datadoghq.com/internal_developer_portal/software_catalog/). After a rule is created, the updated names appear consistently in service maps, Trace Explorer, monitors, dashboards, and any other APM view.

Remapping is useful when:

- The default name does not match your preferences or conventions.
- Services that you expect to appear as one are split into multiple inferred entities.
- Multiple components are grouped under one name, but you want them represented separately.

**Note**: This page describes inferred entity remapping only. To remap your instrumented (traced) services, [Service Remapping Rules](https://docs.datadoghq.com/tracing/services/service_remapping_rules/) is available in preview.

## Prerequisites{% #prerequisites %}

You must have the `apm_service_renaming_write` permission to create remapping rules. See [Permissions](https://docs.datadoghq.com/account_management/rbac/permissions) for details on Datadog role-based access control.

## Create a remapping rule{% #create-a-remapping-rule %}

### Step 1: Select remapping action and entities to target{% #step-1-select-remapping-action-and-entities-to-target %}

1. In Datadog, navigate to **APM > Software Catalog > Manage > Manage Renaming Rules** and click **+ Add Rule**.

Alternatively, navigate to **APM > Software Catalog** and click on a service to open the service side panel. From there, click **Service Page > Service Renaming**.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/services/renaming_rules/service-side-panel.41c140a9d03535155d3a75b1f54f3a85.png?auto=format"
      alt="The side panel for a particular service, showing the Service Page dropdown menu with a Service Remapping option" /%}

1. Choose a remapping action you want to perform for your new remapping rule.

You can select to split a single entity, rename an entity, merge multiple entities together, or remap several entities.

1. Use the search bar to select the entities you want to remap.

   - You can select one or more entities, but all must be of the same type (service, datastore, or queue).
   - As you select entities, a span query is built in the background. To edit the query, select **Build Advanced Query**.

### Step 2: Specify new entity name{% #step-2-specify-new-entity-name %}

1. In the text box, enter a unique name for the selected entity (or entities). Alternatively, use tag values with the `{{tagName}}` syntax to remap based on an entity's tags.
1. If tag values follow a pattern, apply a regular expression to extract only the portion you want in the name.

### Step 3: Name your rule and review{% #step-3-name-your-rule-and-review %}

1. Optionally, enter a descriptive name for the renaming rule so you can identify it later.
1. Review and save your remapping rule.

{% alert level="info" %}

- Rules are processed at intake and applied to data as it comes in.
- Changes affect only spans ingested while a rule is active, and past data is not updated retroactively.
- Deleting or modifying a rule stops it from applying to new data, but does not revert names on previously ingested data.

{% /alert %}

## Further reading{% #further-reading %}

- [Inferred services](https://docs.datadoghq.com/tracing/services/inferred_services)
