# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listboxfilemetadatainstances.md

# ListBoxFileMetadataInstances 2025.10.9.21

## Bundle

org.apache.nifi | nifi-box-nar

## Description

Retrieves all metadata instances associated with a Box file.

## Tags

box, instances, metadata, storage, templates

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Box Client Service | Controller Service used to obtain a Box API connection. |
| File ID | The ID of the file for which to fetch metadata. |

## Relationships

| Name | Description |
| --- | --- |
| failure | A FlowFile will be routed here if there is an error fetching metadata instances from the file. |
| not found | FlowFiles for which the specified Box file was not found will be routed to this relationship. |
| success | A FlowFile containing the metadata instances records will be routed to this relationship upon successful processing. |

## Writes attributes

| Name | Description |
| --- | --- |
| box.id | The ID of the file from which metadata was fetched |
| record.count | The number of records in the FlowFile |
| mime.type | The MIME Type specified by the Record Writer |
| box.metadata.instances.names | Comma-separated list of instances names |
| box.metadata.instances.count | Number of metadata instances found |
| error.code | The error code returned by Box |
| error.message | The error message returned by Box |

## See also

* [org.apache.nifi.processors.box.FetchBoxFile](fetchboxfile.md)
* [org.apache.nifi.processors.box.FetchBoxFileInfo](fetchboxfileinfo.md)
* [org.apache.nifi.processors.box.ListBoxFile](listboxfile.md)
