# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/gethubspotobject.md

# GetHubSpotObject 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-hubspot-processors-nar

## Description

Get a HubSpot object and its associations by ID or unique value.

## Tags

Preview, hubspot

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| HubSpot Service | HubSpot Client Service. |
| Object ID Property | HubSpot property used to uniquely identify the object. |
| Object ID Value | Matching HubSpot property value to search for. |
| Object Type | HubSpot object type |

## Relationships

| Name | Description |
| --- | --- |
| failure | HubSpot fail relationship |
| missing | HubSpot object does not exist. |
| retry | HubSpot retry relationship. FlowFiles that failed to process due to a server timeout or rate limit related error. FlowFiles routed here should be routed back into the processor. |
| success | HubSpot success relationship |

## See also

* [com.snowflake.openflow.runtime.processors.hubspot.GetHubSpotSchema](gethubspotschema.md)
* [com.snowflake.openflow.runtime.processors.hubspot.ListArchivedHubSpotData](listarchivedhubspotdata.md)
* [com.snowflake.openflow.runtime.processors.hubspot.ListHubSpotObjects](listhubspotobjects.md)
* [com.snowflake.openflow.runtime.processors.hubspot.PutHubSpot](puthubspot.md)
