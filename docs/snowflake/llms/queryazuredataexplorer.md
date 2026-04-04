# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/queryazuredataexplorer.md

# QueryAzureDataExplorer 2025.10.9.21

## Bundle

org.apache.nifi | nifi-azure-nar

## Description

Query Azure Data Explorer and stream JSON results to output FlowFiles

## Tags

ADX, Azure, Data, Explorer, Kusto

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Database Name | Azure Data Explorer Database Name for querying |
| Kusto Query Service | Azure Data Explorer Kusto Query Service |
| Query | Query to be run against Azure Data Explorer |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles containing original input associated with a failed Query |
| success | FlowFiles containing results of a successful Query |

## Writes attributes

| Name | Description |
| --- | --- |
| query.error.message | Azure Data Explorer query error message on failures |
| query.executed | Azure Data Explorer query executed |
| mime.type | Content Type set to application/json |
