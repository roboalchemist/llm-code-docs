# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getconfluencespaceids.md

# GetConfluenceSpaceIds 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-atlassian-processors-nar

## Description

Processor for retrieving Confluence space ids.

## Tags

atlassian, confluence, preview, spaces

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Confluence Client Service | Controller service for managing connections to Confluence |
| Space Keys | Comma-separated list of space keys to filter. If not specified, all spaces will be retrieved. |

## Relationships

| Name | Description |
| --- | --- |
| retry | Retryable failure occurred, e.g. rate limiting |
| success | Successfully fetched Confluence spaces |

## Writes attributes

| Name | Description |
| --- | --- |
| confluence.space.ids | List of identifiers of the Confluence spaces. |
