# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/converttojournalschema.md

# ConvertToJournalSchema 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-database-cdc-processors-nar

## Description

Converts the incoming database schema into the appropriate schema for a Snowflake CDC Journal table.

## Tags

Snowflake, cdc, journal

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles are routed to this relationship if the schema cannot be translated. |
| original | The original FlowFile is routed to this relationship when the schema is successfully converted. |
| success | FlowFiles are routed to this relationship after the schema has been converted. |
