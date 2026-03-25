# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listsharepointdrives.md

# ListSharepointDrives 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-msgraph-nar

## Description

Emits a FlowFile for each Drive present in the specified Sharepoint Site.

## Tags

document, graph, microsoft, openflow, sharepoint, unstructured

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Authentication Service | The service that provides authentication for the SharePoint API. |
| Site URL | The URL of the Sharepoint Site. |

## Relationships

| Name | Description |
| --- | --- |
| success | FlowFiles for each Drive are routed to this relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| sharepoint.site.url | The URL of the Sharepoint Site. |
| sharepoint.site.id | The ID of the Sharepoint Site. |
| sharepoint.drive.name | The name of the Sharepoint Drive. |
| sharepoint.drive.id | The ID of the Sharepoint Drive. |

## See also

* [com.snowflake.openflow.runtime.processors.sharepoint.FetchSharepointFile](fetchsharepointfile.md)
* [com.snowflake.openflow.runtime.processors.sharepoint.FindSharepointDriveItem](findsharepointdriveitem.md)
