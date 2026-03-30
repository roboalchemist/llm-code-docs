# Source: https://docs.airbyte.com/platform/using-airbyte/sync-files-and-records.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/sync-files-and-records.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/sync-files-and-records.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/sync-files-and-records.md

# Sync files and records together

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte supports moving files and records together in the same connection. Some sources are a mix of structured data and unstructured attachments. The combination of structured and unstructured data drives more robust knowledge systems with more context, something critical to successful AI systems.

## How it works[​](#how-it-works "Direct link to How it works")

The process to move files and records depends on whether your data source is structured with unstructured attachments, or is unstructured/file-based.

* **Structured sources with unstructured attachments**: Files are a stream. When you set up your connection, you select and deselect this stream as you normally would. This stream includes structured metadata describing those files. The columns you choose in the stream are the metadata Airbyte syncs to your destination.

* **Unstructured/file-based sources**: Files and records aren't synced together and you must choose to copy files. When you set up the source, choose the **Copy raw files** delivery method. Airbyte syncs your raw files and includes structured metadata describing those files. When you set up your connection, the columns you choose in the stream represent the metadata Airbyte adds to that file.

## Which connectors support file transfers[​](#which-connectors-support-file-transfers "Direct link to Which connectors support file transfers")

Connectors that support file transfers have `supportsFileTransfer: true` in their metadata. Airbyte's UI doesn't currently make this obvious, but the following sources support file transfers.

* Zendesk Support
* S3
* Sharepoint
* Google Drive
* SFTP Bulk

The following destination supports file transfers.

* S3

## Unstructured/file-based sources[​](#unstructuredfile-based-sources "Direct link to Unstructured/file-based sources")

For file-based sources, use the [copy raw files](/platform/1.7/using-airbyte/delivery-methods.md#copy-raw-files) delivery method to move files with structured metadata.

## Structured/mixed sources[​](#structuredmixed-sources "Direct link to Structured/mixed sources")

In the case of structured data sources with unstructured attachments, you sync your files the same way you sync your data.

1. Add your [source](/platform/1.7/using-airbyte/getting-started/add-a-source.md), if you haven't already.

2. Add your [destination](/platform/1.7/using-airbyte/getting-started/add-a-destination.md), if you haven't already. While configuring the destination connector, choose the file format of your log by setting the **Output Format** option. For help, see [Change the metadata format](#metadata-format) below.

3. Add your [connection](/platform/1.7/using-airbyte/getting-started/set-up-a-connection.md), if you haven't already. In the schema, enable the stream(s) containing the files you want to sync, and select which fields you want in your metadata. For help, see [Change what's in the metadata](#metadata-content), below.

## Configure file metadata[​](#configure-file-metadata "Direct link to Configure file metadata")

Two elements of the metadata are configurable: file format and what's in the file. You configure each of these in difference places in Airbyte.

### Change the metadata format[​](#metadata-format "Direct link to Change the metadata format")

To change the format of the metadata, change the output format on the Destination connector.

1. In the left navigation, click **Destinations**.

2. Choose your destination connector from the list, or [create a new one](/platform/1.7/using-airbyte/getting-started/add-a-destination.md).

3. Under **Output Format**, choose the file format you want. You can also choose whether you want to compress the file, or if you want to flatten it.

   ![Choosing JSON Lines format as the Output Format on the Destinaton configuration for the S3 destination](/assets/images/output-format-747a9ba68560c0d5324d45075948b135.png)

4. Click **Test and save**. Next time you sync, your metadata has the chosen format.

### Change what's in the metadata[​](#metadata-content "Direct link to Change what's in the metadata")

You choose what appears in your metadata when setting up your connection.

1. In the left navigation, click **Connections**.

2. Choose your connection from the list, or [create a new one](/platform/1.7/using-airbyte/getting-started/set-up-a-connection.md).

3. Click the **Schema** tab.

4. Open the stream that contains your files.

5. Select and deselect fields as needed.

   ![article\_attachments stream with various fields selected and deselected](/assets/images/file-metadata-choice-7f687806c4a0c31bad7401ad179405a6.png)

6. Click **Save changes**. Next time you sync data, your metadata in your destination updates.

### Metadata sample[​](#metadata-sample "Direct link to Metadata sample")

Here is a sample of metadata in `.jsonl` format, describing a single Word document.

```
{
    "_airbyte_raw_id": "9e089a10-b347-4acf-abc8-f093b93b84bb",
    "_airbyte_extracted_at": 1748991118573,
    "_airbyte_meta": {
        "sync_id": 38401084,
        "changes": []
    },
    "_airbyte_generation_id": 2,
    "_airbyte_data": {
        "folder": "",
        "file_name": "Test Plan.docx",
        "bytes": 7838,
        "source_uri": "https://example.com",
        "id": "1i3cTG1UPQx-ZHft-78neonQ9tDNjkZ-E4bK46eGShFk",
        "created_at": "2025-03-04T14:30:28.000000Z",
        "updated_at": "2025-03-04T14:31:11.253000Z",
        "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "_airbyte_file_path": "/Files/2025_06_03_1748991116728_/Test Plan.docx"
    }
}
```
