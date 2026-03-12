# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/updatebulkjobstate.md

# UpdateBulkJobState 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-salesforce-processors-nar

## Description

Updates the status of a Salesforce Bulk Job in the shared state service for a specific object type

## Tags

bulk, preview, salesforce, state

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Object Type | Salesforce object type whose state should be updated |
| Salesforce Bulk Job State Service | Controller Service managing Bulk Jobs state |
| Status | Status to set for the object type |

## Relationships

| Name | Description |
| --- | --- |
| failure | Incoming FlowFile is routed here if update fails |
| success | Incoming FlowFile is routed here after state update |
