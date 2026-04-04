# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listsharepointsitegroups.md

# ListSharepointSiteGroups 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-sharepoint-rest-nar

## Description

Lists all SharePoint site groups available on a specified SharePoint site.

## Tags

groups, list, microsoft, openflow, sharepoint

## Input Requirement

ALLOWED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| OAuth2 Access Token Provider | Enables managed retrieval of OAuth2 Bearer Token. |
| Record Writer | Record writer used for writing out the records of retrieved Sharepoint Site Groups. |
| Site URL | The URL of the SharePoint site. |
| Web Client Service | The Web Client Service to use for communicating with Sharepoint. |

## Relationships

| Name | Description |
| --- | --- |
| success | Successfully listed all SharePoint site groups. Each group will be represented as a separate FlowFile. |

## Writes attributes

| Name | Description |
| --- | --- |
| record.count | The number of records (groups) returned. |
| mime.type | The MIME type for the resulting FlowFile. |

## See also

* [com.snowflake.openflow.runtime.processors.sharepoint.rest.GetSharepointSiteGroupMembers](getsharepointsitegroupmembers.md)
