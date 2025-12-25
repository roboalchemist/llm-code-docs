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

[Retrieve a database](/reference/database-retrieve) - GET

## Data sources

### Create a data source

[Create a data source](/reference/create-a-data-source) - POST

### Update a data source

#### Update data source properties

[Update data source properties](/reference/update-data-source-properties)

### Retrieve a data source

[Retrieve a data source](/reference/retrieve-a-data-source) - GET

### Query a data source

#### Filter data source entries

[Filter data source entries](/reference/filter-data-source-entries)

#### Sort data source entries

[Sort data source entries](/reference/sort-data-source-entries)

### List data source templates

[List data source templates](/reference/list-data-source-templates) - GET

## Databases (deprecated)

### Create a database

[Create a database](/reference/create-a-database) - POST

### Query a database

#### Filter database entries

[Filter database entries](/reference/post-database-query-filter)

#### Sort database entries

[Sort database entries](/reference/post-database-query-sort)

### Retrieve a database

[Retrieve a database](/reference/retrieve-a-database) - GET

### Update a database

#### Update database properties

[Update database properties](/reference/update-a-database) - PATCH

### List databases (deprecated)

[List databases (deprecated)](/reference/get-databases) - GET

## Comments

### Create comment

[Create comment](/reference/create-a-comment) - POST

### Retrieve a comment

[Retrieve a comment](/reference/retrieve-comment) - GET

### List comments

[List comments](/reference/list-comments) - GET

## File Uploads

### Create a file upload

[Create a file upload](/reference/create-a-file-upload) - POST

### Send a file upload

[Send a file upload](/reference/send-a-file-upload) - POST

### Complete a file upload

[Complete a file upload](/reference/complete-a-file-upload) - POST

### Retrieve a file upload

[Retrieve a file upload](/reference/retrieve-a-file-upload) - GET

### List file uploads

[List file uploads](/reference/list-file-uploads) - GET

## Search

[Create a search](/reference/post-search) - POST
```

# Retrieve a data source

Retrieves a [data source](/reference/data-source) object — information that describes the structure and columns of a data source — for a provided data source ID. The response adheres to any limits to an integration’s capabilities and the permissions of the parent database.

To fetch data source rows (i.e., the child pages of a data source) rather than columns, use the [Query a data source](/reference/query-a-data-source) endpoint.

## Finding a data source ID

Navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32-character alphanumeric string.

![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)

Then, use the [Retrieve a database](/reference/retrieve-a-database-1-6ee911d9) API to get a list of `data_sources` for that database. There is often only one data source, but when there are multiple, you may have the ID or name of the one you want to retrieve in mind (or you can retrieve each of them). Use that data source ID with this endpoint to get its `properties`.

To get a data source ID from the Notion app directly, the settings menu for a database includes a "Copy data source ID" button under "Manage data sources":

![Screenshot of the "Manage data sources" menu for a database in Notion, with "Copy data source ID" button.](https://files.readme.io/30ed6ac31d8c25eb2ff653dd3b11bfd2e30e8af4df6a6d5e0670b4ad7a96cf73-image.png)

Refer to the [Build your first integration guide](/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

## Additional resources

- [How to share a database with your integration](/docs/create-a-notion-integration#give-your-integration-page-permissions)
- [Working with databases guide](/docs/working-with-databases)

> 📘 **Data source relations must be shared with your integration**
> 
> To retrieve data source properties from [database relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.

> 🚧 **The Notion API does not support retrieving linked data sources**
> 
> To fetch the information in a [linked data source](https://www.notion.so/help/guides/using-linked-databases), share the original source database with your Notion integration.
```