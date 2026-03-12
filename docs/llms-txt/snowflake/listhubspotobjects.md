# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listhubspotobjects.md

# ListHubSpotObjects 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-hubspot-processors-nar

## Description

Fetches data from HubSpot for specified object types, and generates one FlowFile per listed object with the corresponding metadata as FlowFile attributes. The object type must be searchable, which means it supports access to the /search endpoint. For more information about searchable object types, see: <https://developers.hubspot.com/docs/reference/api/crm/objects/objects#search>”)

## Tags

Preview, hubspot

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| HubSpot Service | HubSpot Client Service. |
| Object Type | HubSpot object type |
| Updated After | Filter objects updated after specified date (format: yyyy-MM-dd) |

## State management

| Scopes | Description |
| --- | --- |
| CLUSTER | Maintains pagination state and last sync timestamp to continue data retrieval from the last known position after restarts and to fetch only changed data. |

## Relationships

| Name | Description |
| --- | --- |
| failure | HubSpot fail relationship |
| original | The input Flow File is routed to the original relationship. |
| retry | HubSpot retry relationship. FlowFiles that failed to process due to a server timeout or rate limit related error. FlowFiles routed here should be routed back into the processor. |
| success | HubSpot success relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | application/json |
| statement.type | Always ‘UPSERT’ for this processor |
| hubspot.object.type | HubSpot Object Type for this fetch |
| hubspot.object.id | HubSpot Object ID for this fetch |
| hubspot.run.id | Timestamp of the start of this run. Obtained from the incoming FlowFile or current time if not available |
| hubspot.is_last | Whether this is the last paged object of the ingestion |

## Use cases

|  |
| --- |
| This processor is typically used in conjunction with a GenerateFlowFile processor |

## See also

* [com.snowflake.openflow.runtime.processors.hubspot.GetHubSpotObject](gethubspotobject.md)
* [com.snowflake.openflow.runtime.processors.hubspot.GetHubSpotSchema](gethubspotschema.md)
* [com.snowflake.openflow.runtime.processors.hubspot.ListArchivedHubSpotData](listarchivedhubspotdata.md)
* [com.snowflake.openflow.runtime.processors.hubspot.PutHubSpot](puthubspot.md)
