# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/lookupattribute.md

# LookupAttribute 2025.10.9.21

## Bundle

org.apache.nifi | nifi-standard-nar

## Description

Lookup attributes from a lookup service

## Tags

Attribute Expression Language, attributes, cache, enrich, join, lookup

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| include-empty-values | Include null or blank values for keys that are null or blank |
| lookup-service | The lookup service to use for attribute lookups |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles with failing lookups are routed to this relationship |
| matched | FlowFiles with matching lookups are routed to this relationship |
| unmatched | FlowFiles with missing lookups are routed to this relationship |
