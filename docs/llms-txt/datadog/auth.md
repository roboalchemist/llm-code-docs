# Source: https://docs.datadoghq.com/actions/datastores/auth.md

---
title: Access and Authentication
description: Access and authentication for Datastores
breadcrumbs: Docs > Datastores > Access and Authentication
---

# Access and Authentication

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Required Datadog role permissions{% #required-datadog-role-permissions %}

To interact with Datastores, your Datadog account must have the following [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/?tab=ui#app-builder--workflow-automation), which are included in the Datadog Standard Role:

- `actions_datastore_read` - Allows read access to the data within the Actions Datastore.
- `actions_datastore_write` - Allows modification of data within the Actions Datastore, including adding, editing, and deleting records.

To use the [Datastores UI](https://app.datadoghq.com/actions/datastores), you also need the following permission, which is also included in the Datadog Standard Role:

- `actions_datastore_manage` - Allows management of the Actions Datastore, including creating, updating, and deleting the datastore itself.

## Action credentials{% #action-credentials %}

Datastores shares the Action Catalog and the connection credentials for integrations with [Datadog Workflow Automation](https://docs.datadoghq.com/actions/workflows) and [App Builder](https://docs.datadoghq.com/actions/app_builder) products. For more information on configuring credentials, see [Connections](https://docs.datadoghq.com/service_management/app_builder/connections/).

## Datastore permissions{% #datastore-permissions %}

The following permissions are available for datastores:

{% dl %}

{% dt %}
Manager
{% /dt %}

{% dd %}
Read and write access to data and can edit the datastore schema.
{% /dd %}

{% dt %}
Contributor
{% /dt %}

{% dd %}
Read and write access to the datastore.
{% /dd %}

{% dt %}
Viewer
{% /dt %}

{% dd %}
Read access to the datastore.
{% /dd %}

{% dt %}
None
{% /dt %}

{% dd %}
No access.
{% /dd %}

{% /dl %}

## Restrict access to a specific datastore{% #restrict-access-to-a-specific-datastore %}

During the datastore creation process, you're asked to set the organization access level for the datastore. You can choose either `Contributor`, `Viewer`, or `None`. Contributor is the default access level.

To restrict access to an existing datastore for either an organization or individual:

1. Hover over the datastore on the [Datastores page](https://app.datadoghq.com/actions/datastores) and click the padlock (**Permissions**) icon.
1. Use the drop-down menus to edit the permissions for a user or organization.
1. Click **Save**.

## Elevate access{% #elevate-access %}

The `user_access_manage` [permission](https://docs.datadoghq.com/account_management/rbac/permissions/?tab=ui#app-builder--workflow-automation) is required to elevate your access to datastores.

To elevate your access:

1. Hover over the datastore on the [Datastores page](https://app.datadoghq.com/actions/datastores) and click the padlock (**Permissions**) icon.
1. Click **Elevate Access**.
1. Click **Save**.

## Further reading{% #further-reading %}

- [Connections](https://docs.datadoghq.com/actions/connections)
