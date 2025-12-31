# Source: https://developers.notion.com/reference/create-a-comment.md

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

# Create a Comment

[Post](https://docs.rapidapi.com/reference/create-a-comment)

## Main Content

### Create a Database

[Create a database](https://docs.rapidapi.com/reference/database-create)

### Update a Database

[Update a database](https://docs.rapidapi.com/reference/database-update)

### Retrieve a Database

[Retrieve a database](https://docs.rapidapi.com/reference/database-retrieve)

### Data Sources

#### Create a Data Source

[Create a data source](https://docs.rapidapi.com/reference/create-a-data-source)

#### Update a Data Source

[Update a data source](https://docs.rapidapi.com/reference/update-a-data-source)

##### Update Data Source Properties

[Update data source properties](https://docs.rapidapi.com/reference/update-data-source-properties)

#### Retrieve a Data Source

[Retrieve a data source](https://docs.rapidapi.com/reference/retrieve-a-data-source)

#### Query a Data Source

[Query a data source](https://docs.rapidapi.com/reference/query-a-data-source)

##### Filter Data Source Entries

[Filter data source entries](https://docs.rapidapi.com/reference/filter-data-source-entries)

##### Sort Data Source Entries

[Sort data source entries](https://docs.rapidapi.com/reference/sort-data-source-entries)

#### List Data Source Templates

[List data source templates](https://docs.rapidapi.com/reference/list-data-source-templates)

### Databases (Deprecated)

#### Create a Database

[Create a database](https://docs.rapidapi.com/reference/create-a-database)

#### Query a Database

[Query a database](https://docs.rapidapi.com/reference/post-database-query)

##### Filter Database Entries

[Filter database entries](https://docs.rapidapi.com/reference/post-database-query-filter)

##### Sort Database Entries

[Sort database entries](https://docs.rapidapi.com/reference/post-database-query-sort)

#### Retrieve a Database

[Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database)

#### Update a Database

[Update a database](https://docs.rapidapi.com/reference/update-a-database)

##### Update Database Properties

[Update database properties](https://docs.rapidapi.com/reference/update-property-schema-object)

#### List Databases (Deprecated)

[List databases (deprecated)](https://docs.rapidapi.com/reference/get-databases)

### Comments

#### Create Comment

[Create comment](https://docs.rapidapi.com/reference/create-a-comment)

#### Retrieve a Comment

[Retrieve a comment](https://docs.rapidapi.com/reference/retrieve-comment)

#### List Comments

[List comments](https://docs.rapidapi.com/reference/list-comments)

### File Uploads

#### Create a File Upload

[Create a file upload](https://docs.rapidapi.com/reference/create-a-file-upload)

#### Send a File Upload

[Send a file upload](https://docs.rapidapi.com/reference/send-a-file-upload)

#### Complete a File Upload

[Complete a file upload](https://docs.rapidapi.com/reference/complete-a-file-upload)

#### Retrieve a File Upload

[Retrieve a file upload](https://docs.rapidapi.com/reference/retrieve-a-file-upload)

#### List File Uploads

[List file uploads](https://docs.rapidapi.com/reference/list-file-uploads)

### Search

[Search](https://docs.rapidapi.com/reference/post-search)
```

# Create comment

Creates a comment in a page, block or existing discussion thread.

Returns a [comment object](/reference/comment-object) for the created comment.

There are three locations where a new comment can be added with the public API:

1. A page
2. A block
3. An existing discussion thread

The request body will differ slightly depending on which type of comment is being added with this endpoint.

To add a new comment to a page or block, a `parent` object with a `page_id` or `block_id` must be provided in the body params.

To add a new comment to an existing discussion thread, a `discussion_id` string must be provided in the body params. (Inline comments to start a new discussion thread cannot be created via the public API.)

**Either** the `parent.page_id`, `parent.block_id` _or_ `discussion_id` parameter must be provided — ONLY one can be specified.

To see additional examples of creating a [page](/docs/working-with-comments#adding-a-comment-to-a-page) or [discussion](/docs/working-with-comments#responding-to-a-discussion-thread) comment and to learn more about comments in Notion, see the [Working with comments](/docs/working-with-comments) guide.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

> ### Reminder: Turn on integration comment capabilities
> 
> Integration capabilities for reading and inserting comments are off by default.
> 
> This endpoint requires an integration to have insert comment capabilities. Attempting to call this endpoint without insert comment capabilities will return an HTTP response with a 403 status code.
> 
> For more information on integration capabilities, see the [capabilities guide](/reference/capabilities). To update your integration settings, visit the [integration dashboard](https://www.notion.so/my-integrations).
```