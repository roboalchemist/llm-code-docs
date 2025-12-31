# Source: https://developers.notion.com/reference/data-source.md

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

# Data source

**Data sources** are the individual tables of data that live under a Notion database. [Pages](/reference/page) are the items (or children) in a data source. [Page property values](/reference/page#property-value-object) must conform to the [property objects](/reference/property-object) laid out in the parent data source object.

![Diagram of the new Notion API data model: databases parent one or more data sources, each of which parents zero or more pages.](https://files.readme.io/6dc5c7eccb432e908290e2642c84579936d55ee79c6cd60a5b0807e70cdeb55a-image.png)

Diagram of the new Notion API data model.  
A database is a parent of one or more data sources, each of which parents zero or more pages.  
Previously, databases could only have one data source, so the concepts were combined in the API until 2025.

As of API version `2025-09-03`, there's a suite of APIs for managing data sources:

- [Create a data source](/reference/create-a-data-source): add an additional data source for an existing [Database](/reference/database)
- [Update a data source](/reference/update-a-data-source): update attributes, such as the `properties` of a data source
- [Retrieve a data source](/reference/retrieve-a-data-source)
- [Query a data source](/reference/query-a-data-source)

## Object fields

> Properties marked with an asterisk (\*) are available to integrations with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `object`* | `string` | Always `"data_source"`. | `"data_source"` |
| `id`* | `string` (UUID) | Unique identifier for the data source. | `"2f26ee68-df30-4251-aad4-8ddc420cba3d"` |
| `properties`* | `object` | Schema of properties for the data source as they appear in Notion. <br/> `key` string <br/> The name of the property as it appears in Notion. <br/> `value` object <br/> A [Property object](/reference/property-object). |  |
| `parent` | `object` | Information about the data source's parent database. See [Parent object](/reference/parent-object). | `{"type": "database_id", "database_id": "842a0286-cef0-46a8-abba-eac4c8ca644e"}` |
| `database_parent` | `object` | Information about the database's parent (in other words, the the data source's grandparent). See [Parent object](/reference/parent-object). | `{ "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }` |
| `created_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this data source was created. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2020-03-17T19:10:04.968Z"` |
| `created_by` | [Partial User](/reference/user) | User who created the data source. | `{"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}` |
| `last_edited_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this data source was updated. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2020-03-17T21:49:37.913Z"` |
| `last_edited_by` | [Partial User](/reference/user) | User who last edited the data source. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}` |
| `title` | array of [rich text objects](/reference/rich-text) | Name of the data source as it appears in Notion. <br/> See [rich text object](/reference/rich-text)) for a breakdown of the properties. | `[ { "type": "text", "text": { "content": "Can I create a URL property", "link": null }, "annotations": { "bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default" }, "plain_text": "Can I create a URL property", "href": null } ]` |
| `description` | array of [rich text objects](/reference/rich-text) | Description of the data source as it appears in Notion. <br/> See [rich text object](/reference/rich-text)) for a breakdown of the properties. |  |
| `icon` | [File Object](/reference/file-object) or [Emoji object](/reference/emoji-object) | Data source icon. |  |
| `archived` | `boolean` | The archived status of the data source. | `false` |
| `in_trash` | `boolean` | Whether the data source has been deleted. | `false` |

> **Maximum schema size recommendation**
> 
> Notion recommends a maximum schema size of **50KB**. Updates to database schemas that are too large will be blocked to help maintain database performance.
```