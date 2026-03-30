# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/batch/adls.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to Azure Data Lake Storage (ADLS)

> Create a connection to ingest files from Azure Data Lake Storage.

## Step 1: In the Data Portal, click Tables and then click Create Table

## ​Step 2: Select ADLS as the Data Source

## ​Step 3: Create a New Connection

Click **New Connection**. If you want to use an existing connection, select the connection from the list and proceed to **Step 5**.

Enter a **Source Name** for the new connection.

Select the **Authentication Type** from the drop-down list.

## Step 4: Configure Connection Parameters

### Connecting to ADLS Using the Access Key

Use the following JSON configuration when ADLS is set up with **basic authentication** using an access key.

```json  theme={null}
{
  "input.fs.className": "org.apache.pinot.plugin.filesystem.ADLSGen2PinotFS",
  "input.fs.prop.accountName": "<account-name>",
  "authenticationType": "ACCESS_KEY",
  "input.fs.prop.accessKey": "AKIAEXAMPLEACCESSKEY",
  "input.fs.prop.fileSystemName": "<file-system-name>",
  "inputDirURI": "abfs://<file-system-name>@<account-name>.dfs.core.windows.net/<data-directory-name>/"
}
```

#### Property Descriptions

| Property                       | Required | Description                                                                       |
| ------------------------------ | -------- | --------------------------------------------------------------------------------- |
| `input.fs.className`           | Yes      | The class name of the ADLS Gen2 Pinot file system.                                |
| `input.fs.prop.accountName`    | Yes      | The Azure Storage account name used for ADLS Gen2 integration.                    |
| `authenticationType`           | Optional | Set as `ACCESS_KEY` to use an access key for authentication.                      |
| `input.fs.prop.accessKey`      | Yes      | The access key used for authentication when `authenticationType` is `ACCESS_KEY`. |
| `input.fs.prop.fileSystemName` | Yes      | The name of the file system (container) in the Azure Storage account.             |
| `inputDirURI`                  | Yes      | The URI of the input directory in ADLS Gen2 where Pinot reads data.               |

### Connecting to ADLS Using Azure Active Directory

Use the following JSON configuration when ADLS is set up with **Azure Active Directory authentication**.

```json  theme={null}
{
  "input.fs.className": "org.apache.pinot.plugin.filesystem.ADLSGen2PinotFS",
  "input.fs.prop.accountName": "Account-Name",
  "authenticationType": "AZURE_AD",
  "input.fs.prop.clientId": "Client-ID",
  "input.fs.prop.clientSecret": "SECRETKEYEXAMPLE12345",
  "input.fs.prop.tenantId": "tenant-id",
  "input.fs.prop.fileSystemName": "file-system-name",
  "inputDirURI": "abfs://my-container-name@myazure-storage-account.dfs.core.windows.net/data-directory/"
}
```

#### Property Descriptions

| Property                       | Required | Description                                                                                                                                                                                  |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input.fs.className`           | Yes      | The class name of the ADLS Gen2 Pinot file system. Must be set to `org.apache.pinot.plugin.filesystem.ADLSGen2PinotFS` for ADLS Gen2 integration.                                            |
| `input.fs.prop.accountName`    | Yes      | The name of the Azure Storage account to be used for ADLS Gen2 integration.                                                                                                                  |
| `authenticationType`           | Optional | The type of authentication used to access the ADLS storage. Set as `AZURE_AD` to use Azure Active Directory (AAD) Service Principal for authentication.                                      |
| `input.fs.prop.clientId`       | Yes      | The Client ID of the Azure Service Principal used for authentication.                                                                                                                        |
| `input.fs.prop.clientSecret`   | Yes      | The Client Secret key for the Azure Service Principal.                                                                                                                                       |
| `input.fs.prop.tenantId`       | Yes      | The Tenant ID associated with the Azure Active Directory (AAD).                                                                                                                              |
| `input.fs.prop.fileSystemName` | Yes      | The name of the file system (container) in the Azure Storage account.                                                                                                                        |
| `inputDirURI`                  | Yes      | The URI for the input directory in ADLS Gen2 where Pinot reads data. It is generally in the format: `abfs://my-container-name@myazure-storage-account.dfs.core.windows.net/data-directory/`. |

### Connecting to ADLS Using Azure Active Directory with Proxy

Use the following JSON configuration when ADLS is set up with **Azure Active Directory authentication via a proxy server**.

```json  theme={null}
{
  "input.fs.className": "org.apache.pinot.plugin.filesystem.ADLSGen2PinotFS",
  "input.fs.prop.accountName": "Account-Name",
  "authenticationType": "AZURE_AD_WITH_PROXY",
  "input.fs.prop.clientId": "Client-ID",
  "input.fs.prop.clientSecret": "SECRETKEYEXAMPLE12345",
  "input.fs.prop.tenantId": "tenant-id",
  "input.fs.prop.proxyHost": "proxy-host",
  "input.fs.prop.proxyPort": "proxy-port",
  "input.fs.prop.proxyUsername": "proxy-username",
  "input.fs.prop.proxyPassword": "proxy-password",
  "input.fs.prop.fileSystemName": "file-system-name",
  "inputDirURI": "abfs://my-container-name@myazure-storage-account.dfs.core.windows.net/data-directory/"
}
```

#### Property Descriptions

| Property                       | Required | Description                                                                                                                                                                                  |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input.fs.className`           | Yes      | The class name of the ADLS Gen2 Pinot file system. Must be set to `org.apache.pinot.plugin.filesystem.ADLSGen2PinotFS` for ADLS Gen2 integration.                                            |
| `input.fs.prop.accountName`    | Yes      | The name of the Azure Storage account to be used for ADLS Gen2 integration.                                                                                                                  |
| `authenticationType`           | Optional | The type of authentication used to access the ADLS storage. Set as `AZURE_AD_WITH_PROXY` to use Azure Active Directory (AAD) Service Principal for authentication via a proxy server.        |
| `input.fs.prop.clientId`       | Yes      | The Client ID of the Azure Service Principal used for authentication.                                                                                                                        |
| `input.fs.prop.clientSecret`   | Yes      | The Client Secret key for the Azure Service Principal.                                                                                                                                       |
| `input.fs.prop.tenantId`       | Yes      | The Tenant ID associated with the Azure Active Directory (AAD).                                                                                                                              |
| `input.fs.prop.proxyHost`      | Yes      | The hostname of the proxy server used to connect to ADLS.                                                                                                                                    |
| `input.fs.prop.proxyPort`      | Yes      | The port number of the proxy server.                                                                                                                                                         |
| `input.fs.prop.proxyUsername`  | Yes      | The username for proxy authentication.                                                                                                                                                       |
| `input.fs.prop.proxyPassword`  | Yes      | The password for proxy authentication.                                                                                                                                                       |
| `input.fs.prop.fileSystemName` | Yes      | The name of the file system (container) in the Azure Storage account.                                                                                                                        |
| `inputDirURI`                  | Yes      | The URI for the input directory in ADLS Gen2 where Pinot reads data. It is generally in the format: `abfs://my-container-name@myazure-storage-account.dfs.core.windows.net/data-directory/`. |

## Step 5: Test the Connection and Configure Data Ingestion

After you have configured the connection properties, test the connection to ensure it is working.

When the connection is successful, use the following JSON to configure additional data settings:

```json  theme={null}
{
  "inputFormat": "",
  "includeFileNamePattern": ""
}
```

### Property Descriptions

| Property                 | Required | Description                                                                                                                                                                          |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `inputFormat`            | Yes      | The format of the input files. Supported values include **csv, json, avro, parquet**, etc.                                                                                           |
| `includeFileNamePattern` | Yes      | The glob pattern to identify which files to include for ingestion. This is useful when the input directory contains a mix of files, and only specific files should be ingested.      |
| `excludeFileNamePattern` | Optional | The glob pattern to identify which files to exclude from ingestion. This is useful when the input directory contains a mix of files, and only specific files should not be ingested. |

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

## Step 6: Preview the Data

Click Show Sample Data to preview the source data before finalizing the configuration.

<Card title="Next Step" icon="forward-step" iconType="solid" href="/corecapabilities/ingestdata/dataportal/data-modeling/overview">
  Proceed with [Data Modeling](/corecapabilities/ingestdata/dataportal/data-modeling/overview).
</Card>

Built with [Mintlify](https://mintlify.com).
