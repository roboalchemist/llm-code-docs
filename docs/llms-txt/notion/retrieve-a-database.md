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

# Retrieve a Database

[Create a database](https://docs.rapidapi.com/reference/database-create) - POST

[Update a database](https://docs.rapidapi.com/reference/database-update) - PATCH

[Retrieve a database](https://docs.rapidapi.com/reference/database-retrieve) - GET

## Data Sources

### Create a Data Source

[Create a data source](https://docs.rapidapi.com/reference/create-a-data-source) - POST

### Update a Data Source

#### Update Data Source Properties

[Update data source properties](https://docs.rapidapi.com/reference/update-data-source-properties)

### Retrieve a Data Source

[Retrieve a data source](https://docs.rapidapi.com/reference/retrieve-a-data-source) - GET

### Query a Data Source

#### Filter Data Source Entries

[Filter data source entries](https://docs.rapidapi.com/reference/filter-data-source-entries)

#### Sort Data Source Entries

[Sort data source entries](https://docs.rapidapi.com/reference/sort-data-source-entries)

### List Data Source Templates

[List data source templates](https://docs.rapidapi.com/reference/list-data-source-templates) - GET

## Databases (deprecated)

### Create a Database

[Create a database](https://docs.rapidapi.com/reference/create-a-database) - POST

### Query a Database

#### Filter Database Entries

[Filter database entries](https://docs.rapidapi.com/reference/post-database-query-filter)

#### Sort Database Entries

[Sort database entries](https://docs.rapidapi.com/reference/post-database-query-sort)

### Retrieve a Database

[Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database) - GET

### Update a Database

#### Update Database Properties

[Update database properties](https://docs.rapidapi.com/reference/update-property-schema-object)

### List Databases (deprecated)

[List databases (deprecated)](https://docs.rapidapi.com/reference/get-databases) - GET

## Comments

### Create Comment

[Create comment](https://docs.rapidapi.com/reference/create-a-comment) - POST

### Retrieve a Comment

[Retrieve a comment](https://docs.rapidapi.com/reference/retrieve-comment) - GET

### List Comments

[List comments](https://docs.rapidapi.com/reference/list-comments) - GET

## File Uploads

### Create a File Upload

[Create a file upload](https://docs.rapidapi.com/reference/create-a-file-upload) - POST

### Send a File Upload

[Send a file upload](https://docs.rapidapi.com/reference/send-a-file-upload) - POST

### Complete a File Upload

[Complete a file upload](https://docs.rapidapi.com/reference/complete-a-file-upload) - POST

### Retrieve a File Upload

[Retrieve a file upload](https://docs.rapidapi.com/reference/retrieve-a-file-upload) - GET

### List File Uploads

[List file uploads](https://docs.rapidapi.com/reference/list-file-uploads) - GET

## Search

[Search](https://docs.rapidapi.com/reference/post-search) - POST
```

# Retrieve a database

> ❗️Deprecated as of version 2025-09-03
> 
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
> 
> Refer to the new APIs instead:
> 
> - [Retrieve a database](/reference/database-retrieve)
> - [Retrieve a data source](/reference/retrieve-a-data-source)

Retrieves a [database object](/reference/database) — information that describes the structure and columns of a database — for a provided database ID. The response adheres to any limits to an integration’s capabilities.

To fetch database rows rather than columns, use the [Query a database](/reference/post-database-query) endpoint.

To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.

![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)

Notion database ID

Refer to the [Build your first integration guide](/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

## Additional resources

- [How to share a database with your integration](/docs/create-a-notion-integration#give-your-integration-page-permissions)
- [Working with databases guide](/docs/working-with-databases)

> 📘Database relations must be shared with your integration
> 
> To retrieve database properties from [database relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.

> 🚧The Notion API does not support retrieving linked databases.
> 
> To fetch the information in a [linked database](https://www.notion.so/help/guides/using-linked-databases), share the original source database with your Notion integration.
```