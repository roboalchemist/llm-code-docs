# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getconfluencespacepermissions.md

# GetConfluenceSpacePermissions 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-atlassian-processors-nar

## Description

Processor downloading Confluence space permissions.

## Tags

Preview, atlassian, confluence, permissions, space

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Confluence Client Service | Controller service for managing connections to Confluence |
| Confluence Space ID | Identifier of the Confluence Space. |

## Relationships

| Name | Description |
| --- | --- |
| failure | Failed to fetch and parse Confluence space permissions. |
| retry | Retryable failure occurred, e.g. rate limiting |
| space not found | Confluence space not found |
| success | Successfully fetched Confluence space permissions. |

## Writes attributes

| Name | Description |
| --- | --- |
| confluence.permissions.users | IDs of users with permissions to the Confluence space |
| confluence.permissions.emails | Emails of users with permissions to the Confluence space |
| confluence.permissions.groups | Groups with permissions to the Confluence space |
