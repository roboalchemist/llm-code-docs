# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/gethubspotschema.md

# GetHubSpotSchema 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-hubspot-processors-nar

## Description

Retrieves schema information for HubSpot object types including field names, types, and labels. Outputs detailed field metadata as JSON for schema discovery and mapping purposes.

## Tags

Preview, crm, hubspot, metadata, schema

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| HubSpot Service | HubSpot Client Service. |
| Object Type | HubSpot object type |

## Relationships

| Name | Description |
| --- | --- |
| failure | HubSpot fail relationship |
| retry | HubSpot retry relationship. FlowFiles that failed to process due to a server timeout or rate limit related error. FlowFiles routed here should be routed back into the processor. |
| success | HubSpot success relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| hubspot.object.type | The HubSpot object type |
| hubspot.field.count | Number of fields retrieved |
| mime.type | MIME type of the output (application/json) |

## See also

* [com.snowflake.openflow.runtime.processors.hubspot.GetHubSpotObject](gethubspotobject.md)
* [com.snowflake.openflow.runtime.processors.hubspot.ListArchivedHubSpotData](listarchivedhubspotdata.md)
* [com.snowflake.openflow.runtime.processors.hubspot.ListHubSpotObjects](listhubspotobjects.md)
* [com.snowflake.openflow.runtime.processors.hubspot.PutHubSpot](puthubspot.md)
