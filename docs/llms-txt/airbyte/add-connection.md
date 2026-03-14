# Source: https://docs.airbyte.com/platform/move-data/add-connection.md

# Source: https://docs.airbyte.com/platform/2.0/move-data/add-connection.md

# Source: https://docs.airbyte.com/platform/1.8/move-data/add-connection.md

# Add a connection

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

After you add a [source](/platform/1.8/using-airbyte/getting-started/add-a-source.md) and a [destination](/platform/1.8/using-airbyte/getting-started/add-a-destination.md), add a new connection to start syncing data from your source to your destination.

## ELT and data activation destinations are different[​](#elt-and-data-activation-destinations-are-different "Direct link to ELT and data activation destinations are different")

You configure all connections in a similar way. However, the exact process is different for [data activation](/platform/1.8/move-data/elt-data-activation.md) destinations. This page explains how to set up both.

* **ELT databases, warehouses, and lakes**: These destinations are more agnostic about schema. You can, for example, create tables with any number of columns and change those column types if you need to. This is typical of data warehouses and data lakes, and allows you more freedom to determine the structure of your data.

* **Data activation**: These destinations have stricter schemas that your connection must adhere to. For example, if you're syncing data to Salesforce, your Salesforce records have pre-existing fields for name, email, company, phone number, revenue, etc. Some of those fields may be optional, some may be required, and all expect data in a certain format. This means you need to map data from your source to your destination to ensure it arrives in the necessary format and structure. Typically, you have less freedom over the structure of data in these destinations.

The unique needs of a destination account for why setting up some connections is different than others.

## Create an ELT connection[​](#create-an-elt-connection "Direct link to Create an ELT connection")

Follow these steps to create a connection to a database, warehouse, lake, or similar type of destination.

1. Click **Connections** in the navigation.

2. Click **New connection**.

3. Click the source you want to use. If you don't have one yet, you can [add one](/platform/1.8/using-airbyte/getting-started/add-a-source.md).

4. Click the destination you want to use. If you don't have one yet, you can [add one](/platform/1.8/using-airbyte/getting-started/add-a-destination.md). Wait a moment while Airbyte fetches the schema of your data.

5. Under **Select sync mode**, select your sync mode. You can either replicate sources, which maintains an up-to-date copy of your source data in the destination, or you can append historical changes, allowing you to track changes to your data over time in your destination. Airbyte automatically selects the most appropriate sync mode for each stream based on this selection. However, you can update specific streams later.

6. In the **Schema** table, configure your schema.

   1. Choose the specific streams and fields you want to sync. You may have data you don't want to sync. For example, you might consider that data irrelevant or it might be subject to security or compliance rules. If you're unsure, you can always add it later. For help, see [Configuring schemas](/platform/1.8/using-airbyte/configuring-schema.md).

   2. Choose the sync mode for each stream. For help, see [sync modes](/platform/using-airbyte/core-concepts/sync-modes/.md).

   3. Set primary keys for each stream, if applicable. If possible, Airbyte sets this for you automatically.

7. Click **Next**.

8. Under **Configure connection**, finalize the settings for this connection.

   | Option                                                                           | Description                                                                                          |
   | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
   | Connection name                                                                  | Give your connection a more meaningful name if the default `Source -> Destination` isn't sufficient. |
   | [Tags](/platform/1.8/using-airbyte/tagging.md)                                   | Create and apply tags to organize your connections.                                                  |
   | [Schedule type](/platform/1.8/using-airbyte/core-concepts/sync-schedules.md)     | Choose if and how you want to schedule this connection.                                              |
   | [Destination namespace](/platform/1.8/using-airbyte/core-concepts/namespaces.md) | The location in the destination where you want Airbyte to write this data.                           |
   | [Stream prefix](/platform/1.8/using-airbyte/configuring-schema.md)               | If you want to prefix each stream name with a unique value.                                          |
   | [Advanced settings](/platform/1.8/using-airbyte/schema-change-management.md)     | In most cases, you don't need to change these.                                                       |

9. Click **Set up connection**. Airbyte takes you to the page for that connection, where you can manage it and initiate syncs.

## Create a data activation connection[​](#create-a-data-activation-connection "Direct link to Create a data activation connection")

info

Data activation is in **early access**. Try it today with the HubSpot and Customer.io destinations in Airbyte Cloud or Self-Managed version 1.8 and later. If you'd like to be an early adopter, chat with the team, and share feedback, [fill out this form](https://form.typeform.com/to/STc7a0jx).

Follow these steps to create a connection to a data activation destination.

### Step 1: Choose your connectors[​](#step-1-choose-your-connectors "Direct link to Step 1: Choose your connectors")

1. Click **Connections** in the navigation.

2. Click **New connection**.

3. Click the source you want to use. If you don't have one yet, you can [add one](/platform/1.8/using-airbyte/getting-started/add-a-source.md).

4. Click the destination you want to use. If you don't have one yet, you can [add one](/platform/1.8/using-airbyte/getting-started/add-a-destination.md). Wait a moment while Airbyte fetches the schema of your data. When it's done, Airbyte asks you to set up mappings.

### Step 2: Set up mappings, sync modes, and insertion methods[​](#step-2-set-up-mappings-sync-modes-and-insertion-methods "Direct link to Step 2: Set up mappings, sync modes, and insertion methods")

Data activation destinations have stricter schemas that your connection must adhere to. Some of those fields may be optional, some may be required, and all expect data in a certain format. This means you need to map data from your source to your destination to ensure it arrives in the necessary format and structure.

1. Select the first field you want to map from your source.

2. Select the sync mode and, if necessary, the cursor. For help, see [sync modes](/platform/using-airbyte/core-concepts/sync-modes/.md).

3. Select the destination field to which you want to map that field.

4. Select the insertion type. The insertion options available depend on the capabilities of the destination and its connector. Depending on your selection, Airbyte may require you to map other fields as well. In this case, it auto-populates those fields in the destination column.

5. Continue mapping source fields to destination fields until you've mapped all required fields, plus any optional fields you want to include.

### Step 3: Configure your connection[​](#step-3-configure-your-connection "Direct link to Step 3: Configure your connection")

The final step is to configure details of your connection.

| Option                                                                           | Description                                                                                          |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Connection name                                                                  | Give your connection a more meaningful name if the default `Source -> Destination` isn't sufficient. |
| [Tags](/platform/1.8/using-airbyte/tagging.md)                                   | Create and apply tags to organize your connections.                                                  |
| [Schedule type](/platform/1.8/using-airbyte/core-concepts/sync-schedules.md)     | Choose if and how you want to schedule this connection.                                              |
| [Destination namespace](/platform/1.8/using-airbyte/core-concepts/namespaces.md) | The location in the destination where you want Airbyte to write this data.                           |
| [Stream prefix](/platform/1.8/using-airbyte/configuring-schema.md)               | If you want to prefix each stream name with a unique value.                                          |
| [Advanced settings](/platform/1.8/using-airbyte/schema-change-management.md)     | In most cases, you don't need to change these.                                                       |

When you're ready to create the connection, click **Set up connection**. Airbyte takes you to the page for that connection, where you can manage it and initiate syncs.

### Step 4: Review and manage rejected records[​](#da-rejected-records "Direct link to Step 4: Review and manage rejected records")

Destinations may reject records. See [Rejected records](/platform/1.8/move-data/rejected-records.md) to learn more.
