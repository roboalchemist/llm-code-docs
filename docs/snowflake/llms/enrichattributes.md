# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/enrichattributes.md

# EnrichAttributes 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-enrichment-nar

## Description

Looks up a value using the configured Lookup Service and adds the results to the FlowFile as one or more attributes. Frequently, this is used in conjunction with the DatabaseLookup Service in order to enrich a FlowFile by querying a database and adding the results as attributes.

## Tags

attributes, database, enrichment, json, lookup, openflow

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Attribute Name | The name of the attribute to add, whose contents will be the JSON representation of the Record returned from the Lookup Service. |
| Attribute Prefix | A prefix to apply to all attribute names that are added. |
| Flattening Strategy | When a Record is returned from the Lookup Service, this property specifies how the Record should be flattened into the FlowFile’s attributes |
| Lookup Service | The Lookup Service to use for enrichment |

## Relationships

| Name | Description |
| --- | --- |
| failure | If unable to enrich a given FlowFile for any reason, the FlowFile will be routed to this relationship. |
| matched | FlowFiles that are successfully enriched with the Record from the Lookup Service are routed to this relationship. |
| unmatched | FlowFiles for which the Lookup Service did not find a match are routed to this relationship. |

## Use cases

|  |
| --- |
| Query a database to retrieve information based on the attributes of a FlowFile |

## See also
