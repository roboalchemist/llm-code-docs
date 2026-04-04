# Source: https://docs.datadoghq.com/actions/datastores/use.md

---
title: Use Datastores with Apps and Workflows
description: >-
  Reference and perform CRUD operations on datastores within workflows and apps,
  and create workflows or apps from existing datastores.
breadcrumbs: Docs > Datastores > Use Datastores with Apps and Workflows
---

# Use Datastores with Apps and Workflows

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

You can reference and perform CRUD (Create, Read, Update, and Delete) operations on a datastore inside a workflow or an app. Additionally, you can create a workflow or app directly from an existing datastore.

## Create a workflow or app from a datastore{% #create-workflow-app %}

You can get started with a workflow or app directly from a datastore. Each time you create a datastore, Datadog asks you if you'd like to create a workflow or app, or view your datastore.

{% image
   source="https://datadog-docs.imgix.net/images/actions/datastore/datastore-toast.be44339c889e0e32a060564f9f7316f1.png?auto=format"
   alt="When you create a datastore, Datadog asks if you'd like to create a workflow or app." /%}

### Workflow Automation{% #workflow-automation %}

To create a workflow from a datastore:

1. On the [Datastores page](https://app.datadoghq.com/actions/datastores), locate your datastore in the list and click to open it.
1. Click **Create** > **Workflow from Datastore**.

Datadog creates a workflow with a **List items** workflow step prepopulated with your datastore ID. From here, follow the [Workflow Automation](https://docs.datadoghq.com/actions/workflows/build/) documentation to build your workflow. For a list of available datastore actions, see the [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/#datadog-actions-datastore).

### App Builder{% #app-builder %}

To create an app from a datastore:

1. On the [Datastores page](https://app.datadoghq.com/actions/datastores), locate your datastore in the list and click to open it.
1. Click **Create** > **App from Datastore**.

Datadog creates an app prepopulated with your datastore ID. From here, follow the [App Builder](https://docs.datadoghq.com/actions/app_builder/build/) documentation to build your app. For a list of available datastore actions, see the [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/#datadog-actions-datastore).

## Use a datastore in an app{% #use-app %}

To use a datastore in an existing app, add a datastore action:

1. Click the Data (**{ }**) icon to open the Data tab.

1. Click the plus (**+**) icon, select **Action**, and add a Datastore action to add to your app. For a list of available datastore actions, see the [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/#datadog-actions-datastore).

1. Choose an existing connection or [create one](https://docs.datadoghq.com/actions/connections/#create-a-connection).

1. From the **Datastore ID** drop-down menu, select an existing datastore, or select **New Datastore** to create one.

   {% image
      source="https://datadog-docs.imgix.net/images/actions/datastore/datastore-add-app.c8f0a1303352a75d63e4268e316be21d.png?auto=format"
      alt="Add the datastore from an App Builder action" /%}

### Use multiple datastores with a single action{% #multiple-datastores %}

In App Builder, you can use a single datastore action to reference multiple datastores. In the example below, a selector controls which datastore is displayed in the table. The app uses a single List Items datastore action.

**Note**: The datastore in this example uses pseudodata for demonstration purposes.

{% image
   source="https://datadog-docs.imgix.net/images/actions/datastore/datastore-multiple.9711c52ef7844dc3da15b531c32e9b95.png?auto=format"
   alt="You can reference multiple datastores with a single datastore action" /%}

This app uses multiple datasets by:

- Referencing each datastore's UUID as the `value` in the selector component:
  ```json
  ${[
    {
        "label": "Datastore 1",
        "value": "ae729fad-425f-4e54-b70b-f228768e66b6"
    },
    {
        "label": "Datastore 2",
        "value": "c190f470-8850-4651-9a36-781030827468"
    }
   ]}
  ```
- Using the expression `${select0?.value}` in the List Items action to list the entries from the selected datastore.

The table uses the output from the List Items action to display the data from the datastore.

### Retrieve a UUID{% #retrieve-a-uuid %}

To retrieve the UUID for a datastore:

1. On the [Datastores page](https://app.datadoghq.com/actions/datastores), locate your datastore in the list and click to open it.
1. Click **Table Options** > **Copy datastore UUID**.

## Use a datastore in a workflow{% #use-workflow %}

To use a datastore in an existing workflow, add a datastore action:

1. Click the plus (**+**) icon to add a step to your workflow.

1. Search for `datastore` and select a Datastore action to add to your workflow. For a list of available datastore actions, see the [Action Catalog](https://docs.datadoghq.com/actions/actions_catalog/#datadog-actions-datastore).

1. Click on the step in the workflow canvas.

1. From the **Datastore ID** drop-down menu, select an existing datastore, or select **New Datastore** to create one.

   {% image
      source="https://datadog-docs.imgix.net/images/actions/datastore/datastore-create.ca7dc6bde4ea1fbfcdda62b878c796e5.png?auto=format"
      alt="Add the datastore from an App Builder action" /%}

## Update a Datastore with Terraform{% #update-terraform %}

You can use a workflow to update a Datastore with Terraform by following these steps:

1. Initialize a datastore by [creating one from the UI](https://docs.datadoghq.com/actions/datastore/create/#create-a-datastore).
1. Use Terraform to define a workflow that updates the datastore.
1. Run the workflow to create or modify rows in the datastore.

## Further reading{% #further-reading %}

- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build)
- [Build Workflows](https://docs.datadoghq.com/service_management/workflows/build)
- [Enhance your automated workflows and apps with Datastore](https://www.datadoghq.com/blog/datadog-datastore/)
