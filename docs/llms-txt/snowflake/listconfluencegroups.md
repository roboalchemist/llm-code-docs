# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listconfluencegroups.md

# ListConfluenceGroups 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-atlassian-processors-nar

## Description

Processor listing Confluence groups.

## Tags

Preview, atlassian, confluence, groups

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Confluence Client Service | Controller service for managing connections to Confluence |

## Relationships

| Name | Description |
| --- | --- |
| retry | Retryable failure occurred, e.g. rate limiting |
| success | Successfully fetched Confluence group page |

## Writes attributes

| Name | Description |
| --- | --- |
| confluence.group.ids | List of identifiers of the Confluence groups. |
