# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getconfluencepagecontent.md

# GetConfluencePageContent 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-atlassian-processors-nar

## Description

Processor downloading Confluence pages.

## Tags

Preview, atlassian, confluence, content, fetch, page

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Body Format | Format in which body of the Confluence Page will be fetched |
| Confluence Client Service | Controller service for managing connections to Confluence |
| Confluence Page ID | Identifier of the Confluence Page |

## Relationships

| Name | Description |
| --- | --- |
| failure | Failed to fetch Confluence page |
| not found | Confluence page not found |
| removed | Confluence page was removed |
| retry | Retryable failure occurred, e.g. rate limiting |
| success | Successfully fetched Confluence page |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | text/html |
| confluence.page.version | Version of the Confluence page. |
| confluence.page.last.modification.date | Last modification date of the Confluence page. |
| confluence.page.change.type | Informs about status change for the searched page. |
