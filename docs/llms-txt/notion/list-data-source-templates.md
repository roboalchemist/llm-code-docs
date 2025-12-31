# Source: https://developers.notion.com/reference/list-data-source-templates.md

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
- [Data source properties](/reference/data-source)

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

# List data source templates

[post](https://docs.rapidapi.com/reference/list-data-source-templates)

## Main Menu

*   [Create a database](https://docs.rapidapi.com/reference/database-create)
    *   [Update a database](https://docs.rapidapi.com/reference/database-update)
    *   [Retrieve a database](https://docs.rapidapi.com/reference/database-retrieve)
*   [Data sources](https://docs.rapidapi.com/reference/create-a-data-source)
    *   [Create a data source](https://docs.rapidapi.com/reference/create-a-data-source)
    *   [Update a data source](https://docs.rapidapi.com/reference/update-a-data-source)
        *   [Update data source properties](https://docs.rapidapi.com/reference/update-data-source-properties)
    *   [Retrieve a data source](https://docs.rapidapi.com/reference/retrieve-a-data-source)
    *   [Query a data source](https://docs.rapidapi.com/reference/query-a-data-source)
        *   [Filter data source entries](https://docs.rapidapi.com/reference/filter-data-source-entries)
        *   [Sort data source entries](https://docs.rapidapi.com/reference/sort-data-source-entries)
    *   [List data source templates](https://docs.rapidapi.com/reference/list-data-source-templates)
*   [Databases (deprecated)](https://docs.rapidapi.com/reference/create-a-database)
    *   [Create a database](https://docs.rapidapi.com/reference/create-a-database)
    *   [Query a database](https://docs.rapidapi.com/reference/post-database-query)
        *   [Filter database entries](https://docs.rapidapi.com/reference/post-database-query-filter)
        *   [Sort database entries](https://docs.rapidapi.com/reference/post-database-query-sort)
    *   [Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database)
    *   [Update a database](https://docs.rapidapi.com/reference/update-a-database)
        *   [Update database properties](https://docs.rapidapi.com/reference/update-property-schema-object)
    *   [List databases (deprecated)](https://docs.rapidapi.com/reference/get-databases)
*   [Comments](https://docs.rapidapi.com/reference/create-a-comment)
    *   [Create comment](https://docs.rapidapi.com/reference/create-a-comment)
    *   [Retrieve a comment](https://docs.rapidapi.com/reference/retrieve-comment)
    *   [List comments](https://docs.rapidapi.com/reference/list-comments)
*   [File Uploads](https://docs.rapidapi.com/reference/create-a-file-upload)
    *   [Create a file upload](https://docs.rapidapi.com/reference/create-a-file-upload)
    *   [Send a file upload](https://docs.rapidapi.com/reference/send-a-file-upload)
    *   [Complete a file upload](https://docs.rapidapi.com/reference/complete-a-file-upload)
    *   [Retrieve a file upload](https://docs.rapidapi.com/reference/retrieve-a-file-upload)
    *   [List file uploads](https://docs.rapidapi.com/reference/list-file-uploads)
*   [Search](https://docs.rapidapi.com/reference/post-search)
```

# List data source templates

Use this API to retrieve details of all page templates available for a data source.

The response object contains an array `page_size` results (up to 100) under the `templates` key. Each element of the array is a JSON object with the following attributes:

| Key | Data Type | Meaning |
| --- | --- | --- |
| `id` | `String` (UUIDv4 format) | The ID of the template. |
| `name` | `String` | The display name of the template. |
| `is_default` | `Boolean` | Whether that template is the data source's default. |

**Pagination**: When there are more templates than the current API response contains, the `has_more` boolean field is set to `true`, and the `next_cursor` is set to the ID of the next template to use as the `start_cursor` of your next API request.

Only templates under the data source identified by the `data_source_id` in the URL are returned. Also, the bot must have access to the template for it to appear in this API. However, in most cases, as long as the bot is connected to the data source's parent database (check the "Connections" list under the 3-dot menu), this access also extends to all of the child templates.

Templates are also valid Notion pages, so you can retrieve a template's full properties and content using the [Retrieve a page](/reference/retrieve-a-page) API. This also means that opening a template in the Notion app and copying its URL is an alternative way to get its ID.
```