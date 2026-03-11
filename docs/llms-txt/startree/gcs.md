# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/batch/gcs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Google Cloud Storage (GCS)

> Create a connection to ingest files from Google Cloud Storage.

## Step 1: In the Data Portal, click Tables and then click Create Table

## Step 2: Select GCS as the Data Source

## Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection.

## Step 4: Configure Connection Parameters

Use the following JSON script to set up your service account:

```json  theme={null}
{
    "inputDirURI": "gs://my-bucket-name/directory",
    "input.fs.prop.projectId": "",
    "input.fs.prop.jsonKey": "",
    "input.fs.className": "org.apache.pinot.plugin.filesystem.GcsPinotFS"
}
```

### Property Descriptions

The following table outlines the required properties for configuring a Google Cloud Storage (GCS) connection.

| Property                  | Required | Description                                                                                                                                                                |
| ------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input.fs.prop.projectId` | Yes      | The GCP project ID. Find your project ID in the Google Cloud console.                                                                                                      |
| `input.fs.prop.jsonKey`   | Yes      | The string-encoded Google service account key. Include the appropriate format for your selected JSON key. See Google documentation on how to create a service account key. |
| `inputDirURI`             | Yes      | The path to input file(s).                                                                                                                                                 |
| `input.fs.className`      | Yes      | The class name (`org.apache.pinot.plugin.filesystem.GcsPinotFS`) for the Pinot file system.                                                                                |

## Step 5: Test the Connection and Configure Data Settings

After you have configured the connection properties, test the connection to ensure it is working.

When the connection is successful, use the following JSON to configure additional data settings:

```json  theme={null}
{
    "inputFormat": "",
    "includeFileNamePattern": "gs://*.csv"
}
```

### Property Descriptions

The following table outlines the required and optional properties for configuring data ingestion in Google Cloud Storage (GCS).

| Property                  | Required | Description                                                                                                                                                                  |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inputFormat`             | Yes      | The input file format. Supported values include **csv, json, avro, parquet**, etc.                                                                                           |
| `includeFileNamePattern`  | Optional | The glob pattern to identify which files to include for ingestion. This parameter fetches data only from the files in the `inputDirURI` path that match this pattern.        |
| `excludeFilePatternMatch` | Optional | The glob pattern to identify which files to exclude from ingestion. This parameter restricts fetching data from the files in the `inputDirURI` path that match this pattern. |

### Configure Record Reader

Configure the record reader to customize how the file format is read during ingestion.

<AccordionGroup>
  <Accordion title="CSV">
    The `CSVRecordReaderConfig` is used for handling CSV files with the following customizable options:

    * *header*: Provide a header when the input file has no headers.
    * *skipHeader*: Provide an alternate header when the input file has a corrupt header.
    * *delimiter*: Use an alternate delimiter when fields are not separated by the default delimiter comma.
    * *skipUnParseableLines*: Skip records that are not parseable instead of failing ingestion.

    **Example:** Provide a header when the input file has no headers.

    ```bash  theme={null}
    {
      "header": "colA,colB,colC"
    }
    ```

    **Example:** Provide an alternate header when the input file has a corrupt header.

    ```bash  theme={null}
    {
     "header": "colA,colB,colC",
     "skipHeader": "true"
    }
    ```

    **Example:** Use an alternate delimiter when fields are not separated by the default delimiter comma.

    ```bash  theme={null}
    {
     "delimiter": ";"
    }
    ```

    OR

    ```bash  theme={null}
    {
      "delimiter": "\\t"
    }
    ```

    **Example:** Skipping records that are not parseable instead of failing ingestion. This option to be used with caution as it can lead to data loss.

    ```bash  theme={null}
    {
      skipUnParseableLines: "true"
    }
    ```

    **Example:** Handling CSV files with no header, tab-separated fields, empty lines, and unparsable records.

    ```bash  theme={null}
    {
      "header": "colA,colB,colC",
      "delimiter": "\\t",
      "ignoreEmptyLines": "true",
      "skipUnParseableLines": "true"
    }
    ```

    For a comprehensive list of available CSV record reader configurations, see the Pinot [CSV documentation](https://docs.pinot.apache.org/basics/data-import/pinot-input-formats#csv).
  </Accordion>

  <Accordion title="AVRO">
    One configuration option `AvroRecordReaderConfig` is supported.

    * *enableLogicalTypes*: Enable logical type conversions for specific Avro logical types, such as DECIMAL, UUID, DATE, TIME\_MILLIS, TIME\_MICROS, TIMESTAMP\_MILLIS, and TIMESTAMP\_MICROS.

    ```bash  theme={null}
    {
      "enableLogicalTypes": "true"
    }
    ```

    For example, if the schema type is INT, logical type is DATE, the conversion applied is a TimeConversion, and the value is V; then a date is generated V days from epoch start.
  </Accordion>

  <Accordion title="Parquet">
    For Parquet files, Data Manager provides the ParquetRecordReaderConfig with customizable configurations in Data Manager.

    Use Parquet Avro Record Reader:

    ```bash  theme={null}
    {
        "useParquetAvroRecordReader" : "true"
    }
    ```

    When this config is used the parquet record reader used is: `org.apache.pinot.plugin.inputformat.parquet.ParquetAvroRecordReader`

    Use Parquet Native Record Reader:

    ```bash  theme={null}
    {
        "useParquetNativeRecordReader" : "true"
    }
    ```

    When this config is used the parquet record reader used is: `org.apache.pinot.plugin.inputformat.parquet.ParquetNativeRecordReader`
  </Accordion>
</AccordionGroup>

## Step 6: Sample Data

Click **Show Sample Data** to see a preview of the source data.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
