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

# Reference

## Database Operations

*   [Create a database](https://docs.rapidapi.com/reference/database-create)
*   [Update a database](https://docs.rapidapi.com/reference/database-update)
*   [Retrieve a database](https://docs.rapidapi.com/reference/database-retrieve)

## Data Sources

*   [Create a data source](https://docs.rapidapi.com/reference/create-a-data-source)
*   [Update a data source](https://docs.rapidapi.com/reference/update-a-data-source)
    *   [Update data source properties](https://docs.rapidapi.com/reference/update-data-source-properties)
*   [Retrieve a data source](https://docs.rapidapi.com/reference/retrieve-a-data-source)
*   [Query a data source](https://docs.rapidapi.com/reference/query-a-data-source)
    *   [Filter data source entries](https://docs.rapidapi.com/reference/filter-data-source-entries)
    *   [Sort data source entries](https://docs.rapidapi.com/reference/sort-data-source-entries)
*   [List data source templates](https://docs.rapidapi.com/reference/list-data-source-templates)

## Deprecated Databases

*   [Create a database](https://docs.rapidapi.com/reference/create-a-database)
*   [Query a database](https://docs.rapidapi.com/reference/post-database-query)
    *   [Filter database entries](https://docs.rapidapi.com/reference/post-database-query-filter)
    *   [Sort database entries](https://docs.rapidapi.com/reference/post-database-query-sort)
*   [Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database)
*   [Update a database](https://docs.rapidapi.com/reference/update-a-database)
    *   [Update database properties](https://docs.rapidapi.com/reference/update-property-schema-object)
*   [List databases (deprecated)](https://docs.rapidapi.com/reference/get-databases)

## Comments

*   [Create comment](https://docs.rapidapi.com/reference/create-a-comment)
*   [Retrieve a comment](https://docs.rapidapi.com/reference/retrieve-comment)
*   [List comments](https://docs.rapidapi.com/reference/list-comments)

## File Uploads

*   [Create a file upload](https://docs.rapidapi.com/reference/create-a-file-upload)
*   [Send a file upload](https://docs.rapidapi.com/reference/send-a-file-upload)
*   [Complete a file upload](https://docs.rapidapi.com/reference/complete-a-file-upload)
*   [Retrieve a file upload](https://docs.rapidapi.com/reference/retrieve-a-file-upload)
*   [List file uploads](https://docs.rapidapi.com/reference/list-file-uploads)

## Search

```

# Update a database

Updates the attributes — the title, description, icon, or cover, etc. — of a specified database.

Returns the updated [database object](/reference/database).

To update the `properties` of the [data sources](/reference/data-source) under a database, use the [Update a data source](/reference/update-a-data-source) API starting from API version `2025-09-03`.

For an overview of how to use the REST API with databases, refer to the [Working with databases](/docs/working-with-databases) guide.

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
```