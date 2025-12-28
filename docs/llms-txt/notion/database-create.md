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

# RESTful API Reference

## Database Operations

- [Create a database](https://docs.apimatic.io/reference/database-create)
  - POST
- [Update a database](https://docs.apimatic.io/reference/database-update)
  - PATCH
- [Retrieve a database](https://docs.apimatic.io/reference/database-retrieve)
  - GET

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.apimatic.io/reference/create-a-data-source)
  - POST

### Update a Data Source

#### Update Data Source Properties

- [Update data source properties](https://docs.apimatic.io/reference/update-data-source-properties)

### Retrieve a Data Source

- [Retrieve a data source](https://docs.apimatic.io/reference/retrieve-a-data-source)
  - GET

### Query a Data Source

#### Filter Data Source Entries

- [Filter data source entries](https://docs.apimatic.io/reference/filter-data-source-entries)

#### Sort Data Source Entries

- [Sort data source entries](https://docs.apimatic.io/reference/sort-data-source-entries)

### List Data Source Templates

- [List data source templates](https://docs.apimatic.io/reference/list-data-source-templates)
  - GET

## Databases (Deprecated)

### Create a Database

- [Create a database](https://docs.apimatic.io/reference/create-a-database)
  - POST

### Query a Database

#### Filter Database Entries

- [Filter database entries](https://docs.apimatic.io/reference/post-database-query-filter)

#### Sort Database Entries

- [Sort database entries](https://docs.apimatic.io/reference/post-database-query-sort)

### Retrieve a Database

- [Retrieve a database](https://docs.apimatic.io/reference/retrieve-a-database)
  - GET

### Update a Database

#### Update Database Properties

- [Update database properties](https://docs.apimatic.io/reference/update-property-schema-object)

### List Databases (Deprecated)

- [List databases (deprecated)](https://docs.apimatic.io/reference/get-databases)
  - GET

## Comments

### Create Comment

- [Create comment](https://docs.apimatic.io/reference/create-a-comment)
  - POST

### Retrieve a Comment

- [Retrieve a comment](https://docs.apimatic.io/reference/retrieve-comment)
  - GET

### List Comments

- [List comments](https://docs.apimatic.io/reference/list-comments)
  - GET

## File Uploads

### Create a File Upload

- [Create a file upload](https://docs.apimatic.io/reference/create-a-file-upload)
  - POST

### Send a File Upload

- [Send a file upload](https://docs.apimatic.io/reference/send-a-file-upload)
  - POST

### Complete a File Upload

- [Complete a file upload](https://docs.apimatic.io/reference/complete-a-file-upload)
  - POST

### Retrieve a File Upload

- [Retrieve a file upload](https://docs.apimatic.io/reference/retrieve-a-file-upload)
  - GET

### List File Uploads

- [List file uploads](https://docs.apimatic.io/reference/list-file-uploads)
  - GET

## Search

- [Search](https://docs.apimatic.io/reference/post-search)
  - POST
```

# Create a database

Create a database and its initial data source.

**Endpoint:**  
[https://api.notion.com/v1/databases](https://api.notion.com/v1/databases)

## Properties

Create a database and its initial data source. Currently, the `parent` of a new database must be a Notion page (`page_id` type) or a [wiki database](https://www.notion.so/help/wikis-and-verified-pages).

Use this endpoint to create a database, its first [data source](/reference/data-source), and its first table view, all in one API call. Then, if you want to add a second data source, use the [Create a data source](/reference/create-a-data-source) API with a version of at least `2025-09-03`, and provide the `database_id` as the `id` returned by the database create response.

For a complete reference on what properties are available, see [Data source properties](/reference/property-object). After creating the database, to update one of its child data sources' properties, use the [Update a data source](/reference/update-a-data-source) API.

> **📘 Integration capabilities**
> 
> This endpoint requires an integration to have insert content capabilities. Attempting to call this API without insert content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

> **🚧 Limitations**
> 
> Creating new `status` database properties is currently not supported.

### Errors

Returns a 404 if the specified parent page does not exist, or if the integration does not have access to the parent page.

Returns a 400 if the request is incorrectly formatted, or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

_Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information._
```