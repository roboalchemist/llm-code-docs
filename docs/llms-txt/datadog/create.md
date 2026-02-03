# Source: https://docs.datadoghq.com/actions/datastores/create.md

---
title: Create and Manage Datastores
description: >-
  Create datastores with primary keys, seed initial data, and manage datastore
  contents through manual editing or file uploads.
breadcrumbs: Docs > Datastores > Create and Manage Datastores
---

# Create and Manage Datastores

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

You can create and manage datastores from the [Datastore page](https://app.datadoghq.com/actions/datastores).

## Create a datastore{% #create-a-datastore %}

To create a datastore:

1. Navigate to the [Datastores page](https://app.datadoghq.com/actions/datastores).

1. Click **+ New Datastore**.

1. Enter a **Name** for your datastore.

1. Enter a **Primary Key** or toggle the option to **Autogenerate a Primary Key** if a primary key is not essential to your use case.

   - If you choose to enter a primary key, the key must be a column name in your data where each key has a unique value.
   - Choosing to Autogenerate a key removes your ability to provide your own keys for new items in the datastore, but you can still update existing items by specifying their keys.

1. Optionally, enter a **Description** for your datastore.

1. *Optionally*, you can seed your datastore with initial data from a JSON or CSV file. Use one of the following methods to upload the contents of the file:

   - Drag and drop the file into the UI.
   - Click **browse files** to browse and select a file from your computer.
   - Copy a CSV file on your computer and use `Ctrl`/`Cmd` + `V` to paste it.

The CSV or JSON file must include a header row with a column that matches your Primary Key.

1. Click **Create**. A confirmation pop-up window appears with options to [create a workflow or app](https://docs.datadoghq.com/actions/datastore/use#create-workflow-app) from your datastore, or view the datastore.

### Create from an app or workflow{% #create-from-an-app-or-workflow %}

You can create a datastore from an app or workflow by clicking the **Datastore ID** button in a datastore action and selecting **New Datastore**.

{% image
   source="https://datadog-docs.imgix.net/images/actions/datastore/datastore-create.ca7dc6bde4ea1fbfcdda62b878c796e5.png?auto=format"
   alt="Create a workflow from a workflow by clicking New Datastore" /%}

## Edit a datastore{% #edit-a-datastore %}

### Manually edit your data{% #manually-edit-your-data %}

To manually edit a row in your datastore:

1. On the [Datastores page](https://app.datadoghq.com/actions/datastores), locate your datastore and click to open it.
1. Hover over the row you want to change and click the **Edit**  icon.
1. Use the **JSON** or **Raw text** tabs to edit keys in the row.

**Note:** You cannot manually edit the primary key in a row. If you need to edit a primary key, delete the row and re-add it or re-upload the data from a file.

### Update using a file{% #update-using-a-file %}

To update a datastore using a file:

1. On the [Datastores page](https://app.datadoghq.com/actions/datastores), locate your datastore and click to open it.
1. Click **Add Data**.
1. Select an option for how your data should be handled.
   - **Overwrite** replaces existing rows in your table with the data for your file.
   - **Append** adds the rows in your file to the existing dataset. The append option does not allow you to add duplicate entries to your dataset.
1. Click **Add**.

## View a datastore{% #view-a-datastore %}

To view a datastore, locate your datastore on the [Datastores page](https://app.datadoghq.com/actions/datastores) and click to open it.

After you've opened a datastore, you can:

- Export the dataset to a JSON or CSV file.
- Click **Columns** to show or hide table columns.
- Click **Create** to [create a workflow or app](https://docs.datadoghq.com/actions/datastore/use#create-workflow-app) from the datastore.
- Click **Add data** to add data from a CSV or JSON file.

The **Table Options** button allows you to:

- Edit the [datastore permissions](https://docs.datadoghq.com/actions/datastore/auth/).
- Copy the datastore UUID, which is useful for [apps with multiple datastore references](https://docs.datadoghq.com/actions/datastore/use#multiple-datastores).
- Clone the datastore.
- Delete the datastore.

## Limitations{% #limitations %}

Datastores have the following limitations:

- Your organization can have up to 50 datastores.
- A datastore can contain up to 5,000 rows.
- A primary key column of type `string` is required and must uniquely identify each row.
- Each row can be up to 100 KB in size.
- The primary-key value is immutable, it cannot be changed after the row is created.

Reach out to [support](https://docs.datadoghq.com/help/) if you have a use case that exceeds these limits.

## Further reading{% #further-reading %}

- [Build Apps](https://docs.datadoghq.com/service_management/app_builder/build)
- [Build Workflows](https://docs.datadoghq.com/service_management/workflows/build)
- [Enhance your automated workflows and apps with Datastore](https://www.datadoghq.com/blog/datadog-datastore/)
