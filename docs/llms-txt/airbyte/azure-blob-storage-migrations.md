# Source: https://docs.airbyte.com/integrations/destinations/azure-blob-storage-migrations.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-azure-blob-storage/latest/icon.svg)

# Azure Blob Storage Migration Guide

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [1.1.6](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-azure-blob-storage)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-azure-blob-storage)(last updated a month ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `b4c5d105-31fd-4817-96b6-cb923bfc04cb`

## Upgrading to 1.0.0[​](#upgrading-to-100 "Direct link to Upgrading to 1.0.0")

### Airbyte field names[​](#airbyte-field-names "Direct link to Airbyte field names")

This version updates the Azure Blob Storage destination connector to use the [DV2 Airbyte metadata field names](/platform/understanding-airbyte/airbyte-metadata-fields.md). You should update any downstream consumers to reference the new field names. Specifically, these two fields have been renamed:

| Old field name        | New field name          |
| --------------------- | ----------------------- |
| `_airbyte_ab_id`      | `_airbyte_raw_id`       |
| `_airbyte_emitted_at` | `_airbyte_extracted_at` |

### Blob paths[​](#blob-paths "Direct link to Blob paths")

The destination connector now includes the stream namespace in the blob path. For example, if you are syncing a stream `public.users`, the connector will now put blobs into `<container_name>/public/users/**` - previously it was putting blobs into `<container_name>/users/**`.

### File extensions[​](#file-extensions "Direct link to File extensions")

The option to create blobs without a file extension has been removed. We will now always be adding a file extension based on the chosen file format.

### Split files[​](#split-files "Direct link to Split files")

The "Azure Blob Storage file spill size" option has been renamed to "file split size". It also now takes effect on CSV files, which previously ignored the option entirely.

### Required permissions[​](#required-permissions "Direct link to Required permissions")

The connector no longer attempts to create Azure blob storage containers, and therefore you no longer need to provide the `Microsoft.Storage/storageAccounts/blobServices/containers/write` permission.

### Block blobs[​](#block-blobs "Direct link to Block blobs")

The connector now writes block blobs instead of append blobs. In older versions of the connector, there was no way to recognize when a blob was "ready" for consumption, because the connector would continuously append more data to blobs throughout a sync.

With block blobs, you may now assume that as soon as a blob appears in your blob container, that blob is fully-written, and can be safely consumed by your downstream processes.
