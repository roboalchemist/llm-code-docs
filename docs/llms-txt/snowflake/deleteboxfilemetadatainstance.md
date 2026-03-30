# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/deleteboxfilemetadatainstance.md

# DeleteBoxFileMetadataInstance 2025.10.9.21

## Bundle

org.apache.nifi | nifi-box-nar

## Description

Deletes a metadata instance from a Box file using the specified template key

## Tags

box, delete, metadata, storage, templates

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Box Client Service | Controller Service used to obtain a Box API connection. |
| File ID | The ID of the file from which to delete metadata. |
| Template Key | The key of the metadata template instance to delete. |

## Relationships

| Name | Description |
| --- | --- |
| failure | A FlowFile is routed to this relationship if an error occurs during metadata deletion. |
| file not found | FlowFiles for which the specified Box file was not found will be routed to this relationship. |
| success | A FlowFile is routed to this relationship after metadata has been successfully deleted. |
| template not found | FlowFiles for which the specified metadata template was not found will be routed to this relationship. |

## Writes attributes

| Name | Description |
| --- | --- |
| box.id | The ID of the file from which metadata was deleted |
| box.template.key | The template key used for metadata deletion |
| error.code | The error code returned by Box |
| error.message | The error message returned by Box |

## See also

* [org.apache.nifi.processors.box.CreateBoxFileMetadataInstance](createboxfilemetadatainstance.md)
* [org.apache.nifi.processors.box.FetchBoxFileMetadataInstance](fetchboxfilemetadatainstance.md)
* [org.apache.nifi.processors.box.UpdateBoxFileMetadataInstance](updateboxfilemetadatainstance.md)
