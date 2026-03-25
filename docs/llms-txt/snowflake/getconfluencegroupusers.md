# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getconfluencegroupusers.md

# GetConfluenceGroupUsers 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-atlassian-processors-nar

## Description

Processor that downloads information about users belonging to a given Confluence group

## Tags

Preview, atlassian, confluence, groups, users

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Confluence Client Service | Controller service for managing connections to Confluence |
| Confluence Group ID | Identifier of the Confluence Group |

## Relationships

| Name | Description |
| --- | --- |
| failure | Failed to fetch Confluence group users |
| retry | Retryable failure occurred, e.g. rate limiting |
| success | Successfully fetched Confluence group users |

## Writes attributes

| Name | Description |
| --- | --- |
| confluence.group.user.ids | Identifiers of the Confluence group users. |
| confluence.group.user.emails | Emails of the Confluence group users. |
