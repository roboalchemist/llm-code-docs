# Source: https://developers.notion.com/reference/database-retrieve.md

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

# Retrieve a database

[Create a database](/reference/database-create) - POST

[Update a database](/reference/database-update) - PATCH

## Main Content

### Create a database
[Create a database](/reference/database-create) - POST

### Update a database
[Update a database](/reference/database-update) - PATCH

### Retrieve a database
[Retrieve a database](/reference/database-retrieve) - GET
```

# Retrieve a database

Retrieves a [database object](/reference/database) — a container for one or more [data sources](/reference/data-source) — for a provided database ID. The response adheres to any limits to an integration’s capabilities.

The most important fields in the database object response to highlight:

- `data_sources`: An array of JSON objects with the `id` and `name` of every data source under the database
  - These data source IDs can be used with the [Retrieve a data source](/reference/retrieve-a-data-source), [Update a data source](/reference/update-a-data-source), and [Query a data source](/reference/query-a-data-source) APIs
- `parent`: The direct parent of the database; generally a `page_id` or `workspace: true`

To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.

![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)

Notion database ID

Refer to the [Build your first integration guide](/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

## Additional resources

- [How to share a database with your integration](/docs/create-a-notion-integration#give-your-integration-page-permissions)
- [Working with databases guide](/docs/working-with-databases)
```