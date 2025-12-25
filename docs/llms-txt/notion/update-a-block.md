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
- [Create a token](/reference/create-a-token) (POST)
- [Introspect token](/reference/introspect-token) (POST)
- [Revoke token](/reference/revoke-token) (POST)
- [Refresh a token](/reference/refresh-a-token) (POST)

### Blocks
- [Append block children](/reference/append-block-children) (PATCH)
- [Retrieve a block](/reference/retrieve-a-block) (GET)
- [Retrieve block children](/reference/retrieve-block-children) (GET)
- [Update a block](/reference/update-a-block) (PATCH)
- [Delete a block](/reference/delete-a-block) (DEL)

### Pages
- [Create a page](/reference/create-a-page) (POST)
- [Retrieve a page](/reference/retrieve-a-page) (GET)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (GET)
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (POST)
```

# RESTful API Reference

## Database Operations

- [Create a database](https://docs.apimatic.io/reference/database-create)
- [Update a database](https://docs.apimatic.io/reference/database-update)
- [Retrieve a database](https://docs.apimatic.io/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.apimatic.io/reference/create-a-data-source)
- [Update a data source](https://docs.apimatic.io/reference/update-a-data-source)
  - [Update data source properties](https://docs.apimatic.io/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.apimatic.io/reference/retrieve-a-data-source)
- [Query a data source](https://docs.apimatic.io/reference/query-a-data-source)
  - [Filter data source entries](https://docs.apimatic.io/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.apimatic.io/reference/sort-data-source-entries)
- [List data source templates](https://docs.apimatic.io/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.apimatic.io/reference/create-a-database)
- [Query a database](https://docs.apimatic.io/reference/post-database-query)
  - [Filter database entries](https://docs.apimatic.io/reference/post-database-query-filter)
  - [Sort database entries](https://docs.apimatic.io/reference/post-database-query-sort)
- [Retrieve a database](https://docs.apimatic.io/reference/retrieve-a-database)
- [Update a database](https://docs.apimatic.io/reference/update-a-database)
  - [Update database properties](https://docs.apimatic.io/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.apimatic.io/reference/get-databases)

### Comments

- [Create comment](https://docs.apimatic.io/reference/create-a-comment)
- [Retrieve a comment](https://docs.apimatic.io/reference/retrieve-comment)
- [List comments](https://docs.apimatic.io/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.apimatic.io/reference/create-a-file-upload)
- [Send a file upload](https://docs.apimatic.io/reference/send-a-file-upload)
- [Complete a file upload](https://docs.apimatic.io/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.apimatic.io/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.apimatic.io/reference/list-file-uploads)

### Search

- [Search](https://docs.apimatic.io/reference/post-search)
```

# Update a block

Updates the content for the specified `block_id` based on the block type. Supported fields based on the block object type (see [Block object](/reference/block#block-type-object) for available fields and the expected input for each field).

**Note**: The update replaces the _entire_ value for a given field. If a field is omitted (ex: omitting `checked` when updating a `to_do` block), the value will not be changed.

> **📘**
> 
> **Updating `child_page` blocks**
> 
> To update `child_page` type blocks, use the [Update page](/reference/patch-page) endpoint. Updating the page's `title` updates the text displayed in the associated `child_page` block.

> **📘**
> 
> **Updating `child_database` blocks**
> 
> To update `child_database` type blocks, use the [Update database](/reference/update-a-database) endpoint. Updating the page's `title` updates the text displayed in the associated `child_database` block.

> **📘**
> 
> **Updating `children`**
> 
> A block's children _CANNOT_ be directly updated with this endpoint. Instead use [Append block children](/reference/patch-block-children) to add children.

> **📘**
> 
> **Updating `heading` blocks**
> 
> To update the toggle of a `heading` block, you can include the optional `is_toggleable` property in the request. Toggle can be added and removed from a `heading` block. However, you cannot remove toggle from a `heading` block if it has children. All children _MUST_ be removed before revoking toggle from a `heading` block.

## Success

Returns a 200 HTTP response containing the updated [block object](/reference/block) on success.

> **📘**
> 
> **Integration capabilities**
> 
> This endpoint requires an integration to have update content capabilities. Attempting to call this API without update content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

## Errors

Returns a 404 HTTP response if the block doesn't exist, has been archived, or if the integration doesn't have access to the page.

Returns a 400 if the `type` for the block is incorrect or the input is incorrect for a given field.

Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

_Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information._
```