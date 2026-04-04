# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getsharepointsitegroupmembers.md

# GetSharepointSiteGroupMembers 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-sharepoint-rest-nar

## Description

Retrieves all members of a SharePoint site group.

## Tags

groups, membership, microsoft, openflow, sharepoint

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Group ID | The ID of the SharePoint group. |
| OAuth2 Access Token Provider | Enables managed retrieval of OAuth2 Bearer Token. |
| Site URL | The URL of the SharePoint site. |
| Web Client Service | The Web Client Service to use for communicating with Sharepoint. |

## Relationships

| Name | Description |
| --- | --- |
| comms.failure | A FlowFile is routed here if the processor failed to communicate with Sharepoint. Can be retried |
| failure | A FlowFile is routed here if the group members could not be fetched |
| success | A FlowFile is routed here if the group members were successfully retrieved |

## Writes attributes

| Name | Description |
| --- | --- |
| sharepoint.group.user.ids | The IDs of the users in the SharePoint site group. |
| sharepoint.group.user.emails | The emails of the users in the SharePoint site group. |

## See also

* [com.snowflake.openflow.runtime.processors.sharepoint.rest.ListSharepointSiteGroups](listsharepointsitegroups.md)
