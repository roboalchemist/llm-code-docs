# Source: https://developers.notion.com/reference/parent-object.md

# Notion API

## Objects

### Block
- [Rich text](/reference/rich-text)

### Page
- [Page properties](/reference/page-property-values)
  - [Page property items](/reference/property-item-object)

### Database
- [Database](/reference/database)

### Data source
- [Data source properties](/reference/property-object)

### Comment
- [Comment attachment](/reference/comment-attachment)
- [Comment display name](/reference/comment-display-name)

### File
- [File Upload](/reference/file-upload)

### User
- [User](/reference/user)

### Parent
- [Parent](/reference/parent-object)

### Emoji
- [Emoji](/reference/emoji-object)

### Unfurl attribute (Link Previews)
- [Unfurl attribute (Link Previews)](/reference/unfurl-attribute-object)

## Endpoints

### Authentication
- [Create a token](/reference/create-a-token) (post)
- [Introspect token](/reference/introspect-token) (post)
- [Revoke token](/reference/revoke-token) (post)
- [Refresh a token](/reference/refresh-a-token) (post)

### Blocks
- [Append block children](/reference/append-block-children) (patch)
- [Retrieve a block](/reference/retrieve-a-block) (get)
- [Retrieve block children](/reference/retrieve-block-children) (get)
- [Update a block](/reference/update-a-block) (patch)
- [Delete a block](/reference/delete-a-block) (del)

### Pages
- [Create a page](/reference/create-a-page) (post)
- [Retrieve a page](/reference/retrieve-a-page) (get)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (get)
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (post)
- [List databases](/reference/list-databases) (get)
- [Delete a database](/reference/delete-database) (del)
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

# Parent

Learn more about different parent objects that link together a workspace's entities in Notion's API.

[Pages](/reference/page), [databases](/reference/database), [data sources](/reference/data-source), [comments](/reference/comment-object), and [blocks](/reference/block) are either located inside other pages, databases, data sources, and blocks, or are located at the top level of a workspace. This location is known as the "parent". Parent information is represented by a consistent `parent` object throughout the API.

## General Parenting Rules

### Pages Can Be Parented By Other Pages, Data Sources, Blocks, Or The Whole Workspace

*   Prior to [API version 2025-09-03](/docs/upgrade-guide-2025-09-03), page parents were databases, not data sources.

### Blocks Can Be Parented By Pages, Data Sources, Or Blocks

### Databases Can Be Parented By Pages, Blocks, Or The Whole Workspace

*   For wikis, databases can also have a data source parent.

### Data Sources Are Parented By Databases

*   Linked or externally synced external data sources may have data source parents, but aren't thoroughly supported in Notion's API.

> **Exceptions Apply**
> 
> These parenting rules reflect the possible response you may receive when retrieving information about pages, databases, and blocks via Notion’s REST API in the latest API version.
> 
> If you are creating new pages, databases, or blocks via Notion’s public REST API, the parenting rules may vary. For example, the parent of a database currently must be a page if it is [created](/reference/create-a-database) via the API.
> 
> Refer to the API reference documentation for creating [pages](/reference/post-page), [databases](/reference/database-create), [data sources](/reference/create-a-data-source), and [blocks](/reference/patch-block-children) for more information on current parenting rules.

## Database Parent

Database parents most commonly show up for [Data source](/reference/data-source) objects.

| Property | Type | Description | Example values |
| --- | --- | --- | --- |
| `type` | `string` | Always `"database_id"`. | `"database_id"` |
| `database_id` | `string` (UUIDv4) | The ID of the [database](/reference/database) that this page belongs to. | `"b8595b75-abd1-4cad-8dfe-f935a8ef57cb"` |

### Database Parent Example

```json
{
  "type": "database_id",
  "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
}
```

## Data Source Parent

Data source parents most commonly show up for [Page](/reference/page) objects.

| Property | Type | Description | Example values |
| --- | --- | --- | --- |
| `type` | `string` | Always `"data_source_id"`. | `"data_source_id"` |
| `data_source_id` | `string` (UUIDv4) | The ID of the [data source](/reference/data-source) that this page belongs to. | `"1a44be12-0953-4631-b498-9e5817518db8"` |
| `database_id` | `string` (UUIDv4) | The ID of the [database](/reference/database) that the data source belongs to, provided in the API response for convenience. | `"b8595b75-abd1-4cad-8dfe-f935a8ef57cb"` |

### Data Source Parent Example

```json
{
  "type": "data_source_id",
  "data_source_id": "1a44be12-0953-4631-b498-9e5817518db8",
  "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
}
```

## Page Parent

| Property | Type | Description | Example values |
| --- | --- | --- | --- |
| `type` | `string` | Always `"page_id"`. | `"page_id"` |
| `page_id` | `string` (UUIDv4) | The ID of the [page](/reference/page) that this page belongs to. | `"59833787-2cf9-4fdf-8782-e53db20768a5"` |

### Page Parent Example

```json
{
  "type": "page_id",
  "page_id": "59833787-2cf9-4fdf-8782-e53db20768a5"
}
```

## Workspace Parent

A page or database with a workspace parent is a top-level page within a Notion workspace. Team-level pages are also currently represented as having a workspace parent in the API.

The workspace `parent` object contains the following keys:

| Property | Type | Description | Example values |
| --- | --- | --- | --- |
| `type` | `type` | Always `"workspace"`. | `"workspace"` |
| `workspace` | `boolean` | Always `true`. | `true` |

### Workspace Parent Example

```json
{
  "type": "workspace",
  "workspace": true
}
```

## Block Parent

A page may have a block parent if it is created inline in a chunk of text, or is located beneath another block like a toggle or bullet block. The `parent` property is an object containing the following keys:

| Property | Type | Description | Example values |
| --- | --- | --- | --- |
| `type` | `type` | Always `"block_id"`. | `"block_id"` |
| `block_id` | `string` (UUIDv4) | The ID of the [page](/reference/page) that this page belongs to. | `"ea29285f-7282-4b00-b80c-32bdbab50261"` |

### Block Parent Example

```json
{
  "type": "block_id",
  "block_id": "7d50a184-5bbe-4d90-8f29-6bec57ed817b"
}
```
```

# Navigation

## Table of Contents

- [Database parent](#database-parent)
- [Data source parent](#data-source-parent)
- [Page parent](#page-parent)
- [Workspace parent](#workspace-parent)
- [Block parent](#block-parent)

---

## Database parent

- [Create a database](/docs/10.4/user-guide/sql-reference/data-types/database.html#create-database)
- [Use a database](/docs/10.4/user-guide/sql-reference/data-types/database.html#use-database)
- [Describe a database](/docs/10.4/user-guide/sql-reference/data-types/database.html#describe-database)
- [Alter a database](/docs/10.4/user-guide/sql-reference/data-types/database.html#alter-database)
- [Drop a database](/docs/10.4/user-guide/sql-reference/data-types/database.html#drop-database)

## Data source parent

- [Create a data source](/docs/10.4/user-guide/sql-reference/data-types/data-source.html#create-data-source)
- [Use a data source](/docs/10.4/user-guide/sql-reference/data-types/data-source.html#use-data-source)
- [Describe a data source](/docs/10.4/user-guide/sql-reference/data-types/data-source.html#describe-data-source)
- [Alter a data source](/docs/10.4/user-guide/sql-reference/data-types/data-source.html#alter-data-source)
- [Drop a data source](/docs/10.4/user-guide/sql-reference/data-types/data-source.html#drop-data-source)

## Page parent

- [Create a page](/docs/10.4/user-guide/sql-reference/data-types/page.html#create-page)
- [Use a page](/docs/10.4/user-guide/sql-reference/data-types/page.html#use-page)
- [Describe a page](/docs/10.4/user-guide/sql-reference/data-types/page.html#describe-page)
- [Alter a page](/docs/10.4/user-guide/sql-reference/data-types/page.html#alter-page)
- [Drop a page](/docs/10.4/user-guide/sql-reference/data-types/page.html#drop-page)

## Workspace parent

- [Create a workspace](/docs/10.4/user-guide/sql-reference/data-types/workspace.html#create-workspace)
- [Use a workspace](/docs/10.4/user-guide/sql-reference/data-types/workspace.html#use-workspace)
- [Describe a workspace](/docs/10.4/user-guide/sql-reference/data-types/workspace.html#describe-workspace)
- [Alter a workspace](/docs/10.4/user-guide/sql-reference/data-types/workspace.html#alter-workspace)
- [Drop a workspace](/docs/10.4/user-guide/sql-reference/data-types/workspace.html#drop-workspace)

## Block parent

- [Create a block](/docs/10.4/user-guide/sql-reference/data-types/block.html#create-block)
- [Use a block](/docs/10.4/user-guide/sql-reference/data-types/block.html#use-block)
- [Describe a block](/docs/10.4/user-guide/sql-reference/data-types/block.html#describe-block)
- [Alter a block](/docs/10.4/user-guide/sql-reference/data-types/block.html#alter-block)
- [Drop a block](/docs/10.4/user-guide/sql-reference/data-types/block.html#drop-block)
```