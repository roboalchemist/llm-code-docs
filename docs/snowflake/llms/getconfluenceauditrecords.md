# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getconfluenceauditrecords.md

# GetConfluenceAuditRecords 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-atlassian-processors-nar

## Description

Processor listing Confluence audit records.

## Tags

Preview, atlassian, audit log, confluence

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Audit Log Fetch Limit | How many audit logs will be fetched from Confluence API in one request |
| Confluence Client Service | Controller service for managing connections to Confluence |

## State management

| Scopes | Description |
| --- | --- |
| CLUSTER | Stores last synchronization timestamp. |

## Relationships

| Name | Description |
| --- | --- |
| failure | Failed to fetch Confluence audit records |
| original | The input Flow File is routed to the original relationship. |
| retry | Retryable failure occurred, e.g. rate limiting |
| success | Successfully fetched Confluence audit records |

## Writes attributes

| Name | Description |
| --- | --- |
| confluence.group.ids | List of identifiers of the Confluence groups. |
| confluence.page.names | List of the names of the Confluence page. |
| confluence.space.names | List of the Confluence spaces. |
| confluence.continue.fetching | Indicates whether there are more pages to fetch (true/false). |
