# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listboxfileinfo.md

# ListBoxFileInfo 2025.10.9.21

## Bundle

org.apache.nifi | nifi-box-nar

## Description

Fetches file metadata for each file in a Box Folder. Takes a flowFile with a folder ID attribute and outputs flowFiles with records containing all file metadata.

## Tags

box, fetch, files, folder, storage

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Box Client Service | Controller Service used to obtain a Box API connection. |
| Folder ID | The ID of the folder from which to fetch files. |
| Minimum File Age | The minimum age a file must be in order to be considered; any files younger than this will be ignored. |
| Record Writer | Specifies the Controller Service to use for writing the metadata records. Must be set. |
| Search Recursively | When ‘true’, will include files from sub-folders. Otherwise, will return only files that are within the folder defined by the ‘Folder ID’ property. |

## Relationships

| Name | Description |
| --- | --- |
| failure | A FlowFile will be routed here if there is an error fetching file metadata from the folder. |
| not.found | FlowFiles for which the specified Box folder was not found will be routed to this relationship. |
| success | A FlowFile containing the file metadata records will be routed to this relationship upon successful processing. |

## Writes attributes

| Name | Description |
| --- | --- |
| box.folder.id | The ID of the folder from which files were fetched |
| record.count | The number of records in the FlowFile |
| mime.type | The MIME Type specified by the Record Writer |
| error.code | The error code returned by Box |
| error.message | The error message returned by Box |

## See also

* [org.apache.nifi.processors.box.FetchBoxFile](fetchboxfile.md)
* [org.apache.nifi.processors.box.ListBoxFile](listboxfile.md)
* [org.apache.nifi.processors.box.PutBoxFile](putboxfile.md)
