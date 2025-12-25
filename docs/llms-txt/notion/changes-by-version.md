# Changes by version

## Introduction
[Introduction](https://docs.notion.so/reference/intro)

## Integration capabilities
[Integration capabilities](https://docs.notion.so/reference/capabilities)

## Webhooks
[Webhooks](https://docs.notion.so/reference/webhooks)
- [Event types & delivery](https://docs.notion.so/reference/webhooks-events-delivery)

## Request limits
[Request limits](https://docs.notion.so/reference/request-limits)

## Status codes
[Status codes](https://docs.notion.so/reference/status-codes)

## Versioning
[Versioning](https://docs.notion.so/reference/versioning)
- [Changes by version](https://docs.notion.so/reference/changes-by-version)
```

# API Reference

## Database Operations

- [Create a database](https://docs.nestbase.com/reference/database-create)
- [Update a database](https://docs.nestbase.com/reference/database-update)
- [Retrieve a database](https://docs.nestbase.com/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.nestbase.com/reference/create-a-data-source)
- [Update a data source](https://docs.nestbase.com/reference/update-a-data-source)
  - [Update data source properties](https://docs.nestbase.com/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.nestbase.com/reference/retrieve-a-data-source)
- [Query a data source](https://docs.nestbase.com/reference/query-a-data-source)
  - [Filter data source entries](https://docs.nestbase.com/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.nestbase.com/reference/sort-data-source-entries)
- [List data source templates](https://docs.nestbase.com/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.nestbase.com/reference/create-a-database)
- [Query a database](https://docs.nestbase.com/reference/post-database-query)
  - [Filter database entries](https://docs.nestbase.com/reference/post-database-query-filter)
  - [Sort database entries](https://docs.nestbase.com/reference/post-database-query-sort)
- [Retrieve a database](https://docs.nestbase.com/reference/retrieve-a-database)
- [Update a database](https://docs.nestbase.com/reference/update-a-database)
  - [Update database properties](https://docs.nestbase.com/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.nestbase.com/reference/get-databases)

### Comments

- [Create comment](https://docs.nestbase.com/reference/create-a-comment)
- [Retrieve a comment](https://docs.nestbase.com/reference/retrieve-comment)
- [List comments](https://docs.nestbase.com/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.nestbase.com/reference/create-a-file-upload)
- [Send a file upload](https://docs.nestbase.com/reference/send-a-file-upload)
- [Complete a file upload](https://docs.nestbase.com/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.nestbase.com/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.nestbase.com/reference/list-file-uploads)

### Search

- [Search](https://docs.nestbase.com/reference/post-search)
```

# Changes by version

| Version | Breaking changes |
| --- | --- |
| `/v1/databases` APIs are re-organized into `/v1/data_sources` (for managing individual data sources under a database container) and `/v1/databases` (for managing the database container.)<br/>Existing database IDs stay the same, but a new concept of data source IDs is introduced, and required in order to manage data source properties, to support multi-source databases (new in the Notion app as of September 2025.)<br/>See [changelog](/page/changelog) and [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03) guide for more details. |
| `2022-06-28` | Page properties must be retrieved using the page properties endpoint.<br/>Parents are now always direct parents; a parent field has been added to block.<br/>Database relations have a type of `single_property` and `dual_property`.<br/>See [changelog](/changelog/releasing-notion-version-2022-06-28) for more details. |
| `2022-02-22` | See [changelog](/changelog/releasing-notion-version-2022-02-22). |
| `2021-08-16` | The [Append block children](/reference/patch-block-children) endpoint returns a list of new [Block object](/reference/block) children instead of the parent block.<br/>Array rollup property types changed from `file`, `text` and `person` to `files`, `rich_text` and `people`.<br/>Property IDs are now encoded to be URL safe.<br/>Empty number, email, select, date, and rollup properties are now returned in page responses as `null`.<br>[More information](/changelog/notion-version-2021-08-16) |
| `2021-05-13` | Rich text property values use the type `rich_text` instead of `text`.<br>[Migration details](/changelog/unversioned-requests-no-longer-accepted) |
```