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
- [Update page](/reference/update-page) (PATCH)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (POST)
- [List databases](/reference/list-databases) (GET)
- [Delete a database](/reference/delete-database) (DEL)
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

## Other Resources

- [Authentication](https://docs.apimatic.io/authentication)
- [Authorization](https://docs.apimatic.io/authorization)
- [Error Codes](https://docs.apimatic.io/error-codes)
- [HTTP Status Codes](https://docs.apimatic.io/http-status-codes)
- [API Versioning](https://docs.apimatic.io/api-versioning)
- [Terms of Service](https://docs.apimatic.io/terms-of-service)
- [Code Samples](https://docs.apimatic.io/code-samples)
- [Examples](https://docs.apimatic.io/examples)
```

# Search optimizations and limitations

## Optimizations

Search works best when the request is as specific as possible. We recommend filtering by object (such as `page` or `database`) and providing a text `query` to narrow down results.

To speed up results, try reducing the `page_size`. The default `page_size` is 100.

Our implementation of the search endpoint includes an optimization where any pages or databases that are directly shared with an integration are guaranteed to be returned. If your use case requires pages or databases to immediately be available in search without an indexing delay, we recommend that you share relevant pages/databases with your integration directly.

## Limitations

The search endpoint works best when it's being used to query for pages and databases by name. It is not optimized for the following use cases:

- **Exhaustively enumerating through all the documents that a bot has access to in a workspace.** Search is not guaranteed to return everything, and the index may change as your integration iterates through pages and databases.
- **Searching or filtering within a particular database.** This use case is much better served by finding the database ID and using the [Query a database](/reference/post-database-query) endpoint.
- **Immediate and complete results.** Search indexing is not immediate. If an integration performs a search quickly after a page is shared with the integration (such as immediately after a user performs OAuth), then the response may not contain the page.
  - When an integration needs to present a user interface that depends on search results, we recommend including a _Refresh_ button to retry the search. This will allow users to determine if the expected result is present or not, and give them a way to try again.
```