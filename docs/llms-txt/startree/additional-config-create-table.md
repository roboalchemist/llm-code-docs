# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/additional-config-create-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Additional Configuration

> Configure advanced settings for the table in the Data Portal, including ingestion behavior and time partitioning for Apache Pinot tables. These are crucial for correct table functioning and data integrity in Apache Pinot.

This section is a key part of the table creation process in **Data Portal**, appearing after the **Data Modeling** step.

Open the StarTree Cloud console and navigate to the Data Portal section.

## Step 1: Table Details

In this step, users are required to provide core table-level metadata that governs how the table will behave in Pinot.

### Table Name

Enter a unique and meaningful name for the table. This name will be used to reference the table within Pinot and downstream tools.

### Replication Factor

Specify the number of replicas for each segment. A higher replication factor improves fault tolerance and availability but consumes more resources.

### Table Type

Select whether the table is a:

* **Fact Table**: Used for large-scale event or transactional data. Requires a **Time Column** to be selected, which helps with time-based retention, partitioning, and querying.
* **Dimension Table**: Typically used for lookups or joins. Requires the user to define a list of **Primary Key Columns**, ordered as per their significance, to uniquely identify each record.

After filling in these fields, click **Save** to confirm and move to the next step.

## Step 2: Ingestion Type Configuration

This step appears only if the data source is a streaming platform such as **Kafka**, **Kinesis**, etc. Users must define how Pinot should handle incoming records—whether to **append**, **update**, or **deduplicate** them.

### Choose Ingestion Type

You have three options:

* **Standard Table**: Default ingestion mode where records are simply appended as they arrive. No deduplication or update logic is applied.
* **Upsert Table**: Enables update capabilities where new events can replace older ones based on the primary key. Suitable for late-arriving data and event corrections.
* **Deduplication Table**: Ensures that only the most recent record for a given key is retained and drops duplicate records during ingestion. Useful in scenarios where duplicates are common in the event stream.

***

#### If “Upsert Table” is selected

You will be required to configure the following:

* **Upsert Type**: Select from the dropdown options (e.g., *Full* or *Partial*) depending on whether you want the entire row to be replaced or only specific fields updated.
* **Partial Upsert Strategy** (only if Partial Upsert is selected): Define how each upsertable column should be handled—common strategies include *overwrite*, *increment*, or *ignore*.
* **Primary Key**: Choose one or more columns that uniquely identify each row. These will be used by Pinot to determine whether incoming data should update an existing record.

***

#### If “Deduplication Table” is selected

You will be required to configure the **Dedupe Primary Key**. Select the column(s) from the dropdown that should be used to identify and eliminate duplicate records in the stream.

## Step 3: Create Table

Review the overall table configuration and create the table in the last step.

In the final step of ingestion using the Data Portal, the table schema that was configured in the previous steps is displayed. Review the configuration details. You can edit the configurations and check the sample data to see if your edits produce the required output.

Once the schema is ready, click **Create Table**.

Built with [Mintlify](https://mintlify.com).
