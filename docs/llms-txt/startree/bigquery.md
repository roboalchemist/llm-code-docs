# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/batch/bigquery.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Google BigQuery

> Create a connection to load data from Google BigQuery tables and views.

## Step 1: In the Data Portal, click Tables and then click Create Table

## ​Step 2: Select BigQuery as the Data Source

## ​Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection.

## Step 4: Configure Connection Parameters

Use the following JSON configuration:

```json  theme={null}
{
  "sql.bigquery.projectid": "project_id",
  "sql.bigquery.jsonkey": ""
}
```

### Property Descriptions

| Property                 | Required | Description                                                                                                                                       |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sql.bigquery.projectId` | Yes      | The GCP project ID. Find your project ID in the Google Cloud console.                                                                             |
| `sql.bigquery.jsonKey`   | Yes      | The string-encoded Google service account key. Ensure the correct JSON key format. See Google's documentation for creating a service account key. |

## Step 5: Test the Connection and Configure Data Ingestion

After you have configured the connection properties, test the connection to ensure it is working.

When the connection is successful, use the following JSON to configure additional data settings:

```json  theme={null}
{
  "sql.queryTemplate": "SELECT * FROM <TABLE> WHERE <TIME_COLUMN> BETWEEN $START AND $END",
  "sql.timeColumnName": "TIME_COLUMN",
  "sql.timeColumnFormat": "yyyy-MM-dd",
  "sql.startTime": "",
  "sql.endTime": ""
}
```

### Property Descriptions

| Property               | Required | Description                                                                                                                                                              |
| ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sql.queryTemplate`    | Yes      | The SQL query template for fetching data from BigQuery.                                                                                                                  |
| `sql.timeColumnName`   | Yes      | The time column used for filtering data while ingesting.                                                                                                                 |
| `sql.timeColumnFormat` | Yes      | The datetime format of the time column used for filtering.                                                                                                               |
| `sql.startTime`        | Yes      | The start time for data extraction. This value is dynamically used in the `$START` placeholder of `sql.queryTemplate`. It should match the specified time column format. |
| `sql.endTime`          | Yes      | The end time for data extraction. This value is dynamically used in the `$END` placeholder of `sql.queryTemplate`. It should match the specified time column format.     |

## Step 6: Preview the Data

Click Show Sample Data to preview the source data before finalizing the configuration.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
