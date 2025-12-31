# Source: https://developers.notion.com/reference/create-a-database.md

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

# Create a Database

[Post](https://docs.rapidapi.com/reference/database-create)

# Update a Database

[Patch](https://docs.rapidapi.com/reference/database-update)

# Retrieve a Database

[Get](https://docs.rapidapi.com/reference/database-retrieve)

## Data Sources

### Create a Data Source

[Post](https://docs.rapidapi.com/reference/create-a-data-source)

### Update a Data Source

#### Update Data Source Properties

[Patch](https://docs.rapidapi.com/reference/update-a-data-source)

### Retrieve a Data Source

[Get](https://docs.rapidapi.com/reference/retrieve-a-data-source)

### Query a Data Source

#### Filter Data Source Entries

[Post](https://docs.rapidapi.com/reference/query-a-data-source)

#### Sort Data Source Entries

[Post](https://docs.rapidapi.com/reference/query-a-data-source)

### List Data Source Templates

[Get](https://docs.rapidapi.com/reference/list-data-source-templates)

## Databases (Deprecated)

### Create a Database

[Post](https://docs.rapidapi.com/reference/create-a-database)

### Query a Database

#### Filter Database Entries

[Post](https://docs.rapidapi.com/reference/post-database-query)

#### Sort Database Entries

[Post](https://docs.rapidapi.com/reference/post-database-query)

### Retrieve a Database

[Get](https://docs.rapidapi.com/reference/retrieve-a-database)

### Update a Database

#### Update Database Properties

[Patch](https://docs.rapidapi.com/reference/update-a-database)

### List Databases (Deprecated)

[Get](https://docs.rapidapi.com/reference/get-databases)

## Comments

### Create Comment

[Post](https://docs.rapidapi.com/reference/create-a-comment)

### Retrieve a Comment

[Get](https://docs.rapidapi.com/reference/retrieve-comment)

### List Comments

[Get](https://docs.rapidapi.com/reference/list-comments)

## File Uploads

### Create a File Upload

[Post](https://docs.rapidapi.com/reference/create-a-file-upload)

### Send a File Upload

[Post](https://docs.rapidapi.com/reference/send-a-file-upload)

### Complete a File Upload

[Post](https://docs.rapidapi.com/reference/complete-a-file-upload)

### Retrieve a File Upload

[Get](https://docs.rapidapi.com/reference/retrieve-a-file-upload)

### List File Uploads

[Get](https://docs.rapidapi.com/reference/list-file-uploads)

## Search

[Post](https://docs.rapidapi.com/reference/post-search)
```

# Create a database

> ❗️Deprecated as of version 2025-09-03
> 
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
> 
> Refer to the new APIs instead:
> 
> - [Create a database](/reference/database-create)
> - [Create a data source](/reference/create-a-data-source)

Creates a database as a subpage in the specified parent page, with the specified `properties` schema. Currently, the parent of a new database must be a Notion page or a [wiki database](https://www.notion.so/help/wikis-and-verified-pages).

> 📘Integration capabilities
> 
> This endpoint requires an integration to have insert content capabilities. Attempting to call this API without insert content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

> 🚧Limitations
> 
> Creating new `status` database properties is currently not supported.

## Errors

Returns a 404 if the specified parent page does not exist, or if the integration does not have access to the parent page.

Returns a 400 if the request is incorrectly formatted, or a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).

_Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information._
```