# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/fetchboxfile.md

# FetchBoxFile 2025.10.9.21

## Bundle

org.apache.nifi | nifi-box-nar

## Description

Fetches files from a Box Folder. Designed to be used in tandem with ListBoxFile.

## Tags

box, fetch, storage

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Box Client Service | Controller Service used to obtain a Box API connection. |
| File ID | The ID of the File to fetch |

## Relationships

| Name | Description |
| --- | --- |
| failure | A FlowFile will be routed here for each File for which fetch was attempted but failed. |
| success | A FlowFile will be routed here for each successfully fetched File. |

## Writes attributes

| Name | Description |
| --- | --- |
| box.id | The id of the file |
| filename | The name of the file |
| path | The folder path where the file is located |
| box.size | The size of the file |
| box.timestamp | The last modified time of the file |
| error.code | The error code returned by Box |
| error.message | The error message returned by Box |

## See also

* [org.apache.nifi.processors.box.ListBoxFile](listboxfile.md)
* [org.apache.nifi.processors.box.PutBoxFile](putboxfile.md)
