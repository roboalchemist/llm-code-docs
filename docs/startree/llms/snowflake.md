# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/batch/snowflake.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Snowflake

> Create a connection to load batch data from Snowflake into StarTree Cloud.

## Step 1: In the Data Portal, click Tables and then click Create Table

## Step 2: Select Snowflake as the Data Source

## Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection.

## Step 4: Configure Connection Parameters

### Connecting to Snowflake Using Basic Authentication

Use the following JSON configuration when Snowflake is set up with **basic authentication** using **user** and **password**.

```json  theme={null}
{
  "sql.snowflake.account": "my_snowflake_account",
  "sql.snowflake.db": "my_database_name",
  "sql.snowflake.schema": "my_schema_name",
  "authentication.type": "basic",
  "sql.snowflake.user": "my_username",
  "sql.snowflake.password": "my_secure_password"
}
```

#### Property Descriptions

| Property                 | Required | Description                                                                                          |
| ------------------------ | -------- | ---------------------------------------------------------------------------------------------------- |
| `sql.snowflake.account`  | Yes      | The name of the Snowflake account. Found in your Snowflake URL (e.g., `xyz.snowflakecomputing.com`). |
| `sql.snowflake.db`       | Yes      | The name of the database where the data resides.                                                     |
| `sql.snowflake.schema`   | Yes      | The name of the schema where the data resides.                                                       |
| `sql.snowflake.user`     | Yes      | The username for authenticating with Snowflake. Ensure the user has appropriate read access.         |
| `sql.snowflake.password` | Yes      | The password for authenticating with Snowflake.                                                      |

### Connecting to Snowflake Using Key Pair Authentication

Use the following JSON configuration when Snowflake is set up with Key Pair based authentication.

```json  theme={null}
{
  "sql.snowflake.account": "my_snowflake_account",
  "sql.snowflake.db": "my_snowflake_db",
  "sql.snowflake.schema": "PUBLIC",
  "sql.snowflake.user": "my_username",
  "authentication.type": "key_pair",
  "sql.snowflake.privateKey": "BASE64_ENCODED_PRIVATE_KEY",
  "sql.snowflake.privateKeyPassword": "BASE64_ENCODED_PASSWORD"
}
```

#### Property Descriptions

| Parameter                          | Required | Description                                                                                          |
| ---------------------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| `sql.snowflake.account`            | Yes      | The name of the Snowflake account. Found in your Snowflake URL (e.g., `xyz.snowflakecomputing.com`). |
| `sql.snowflake.db`                 | Yes      | The name of the database where the data resides.                                                     |
| `sql.snowflake.schema`             | Yes      | The name of the schema where the data resides.                                                       |
| `sql.snowflake.user`               | Yes      | The username for authenticating with Snowflake. Ensure the user has appropriate read access.         |
| `sql.snowflake.privateKey`         | Yes      | Make sure the private key is Base64-encoded for secure authentication.                               |
| `sql.snowflake.privateKeyPassword` | Yes      | Make sure the password for the private key is Base64-encoded for secure authentication.              |

For more details, please refer to the [Snowflake official documentation here](https://docs.snowflake.com/en/developer-guide/jdbc/jdbc-configure#using-key-pair-authentication-and-key-rotation)

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

| Property               | Required | Description                                                                                                                                                |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sql.queryTemplate`    | Yes      | The SQL query template for fetching data from Snowflake.                                                                                                   |
| `sql.timeColumnName`   | Yes      | The time column used for filtering data while ingesting.                                                                                                   |
| `sql.timeColumnFormat` | Yes      | The datetime format of the time column used for filtering.                                                                                                 |
| `sql.startTime`        | Yes      | The start time for data extraction. Dynamically used in the `$START` placeholder of `sql.queryTemplate`. It should match the mentioned time column format. |
| `sql.endTime`          | Yes      | The end time for data extraction. Dynamically used in the `$END` placeholder of `sql.queryTemplate`. It should match the mentioned time column format.     |

### Additional Optional Parameters

Use the following JSON for optional configurations:

```json  theme={null}
{
  "sql.bufferTimePeriod": "0d",
  "sql.numBucketsToLookBack": "0",
  "sql.bucketTimePeriod": "1d"
}
```

### Optional Configuration Properties

| Property                   | Required | Description                                                                                                                 |
| -------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `sql.bufferTimePeriod`     | No       | The buffer time period before fetching data. Default value: `0d`. Defines additional time to consider before fetching data. |
| `sql.bucketTimePeriod`     | No       | The time period granularity for each data bucket. Default value: `1d`.                                                      |
| `sql.numBucketsToLookBack` | No       | The number of time buckets to look back when fetching data. Default value: `0`. Used for incremental data fetching.         |

## Step 6: Preview the Data

Click Show Sample Data to preview the source data before finalizing the configuration.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
