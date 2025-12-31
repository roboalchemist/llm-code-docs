# Source: https://developers.notion.com/reference/update-a-data-source.md

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

# Update a Database

[Create a database](/reference/database-create) - POST

[Update a database](/reference/database-update) - PATCH

[Retrieve a database](/reference/database-retrieve) - GET

## Data Sources

### Create a Data Source

[Create a data source](/reference/create-a-data-source) - POST

### Update a Data Source

#### Update Data Source Properties

[Update data source properties](/reference/update-data-source-properties)

#### Retrieve a Data Source

[Retrieve a data source](/reference/retrieve-a-data-source) - GET

### Query a Data Source

#### Filter Data Source Entries

[Filter data source entries](/reference/filter-data-source-entries)

#### Sort Data Source Entries

[Sort data source entries](/reference/sort-data-source-entries)

#### List Data Source Templates

[List data source templates](/reference/list-data-source-templates) - GET

### Databases (Deprecated)

#### Create a Database

[Create a database](/reference/create-a-database) - POST

#### Query a Database

##### Filter Database Entries

[Filter database entries](/reference/post-database-query-filter)

##### Sort Database Entries

[Sort database entries](/reference/post-database-query-sort)

#### Retrieve a Database

[Retrieve a database](/reference/retrieve-a-database) - GET

#### Update a Database

##### Update Database Properties

[Update database properties](/reference/update-property-schema-object)

#### List Databases (Deprecated)

[List databases (deprecated)](/reference/get-databases) - GET

### Comments

#### Create Comment

[Create comment](/reference/create-a-comment) - POST

#### Retrieve a Comment

[Retrieve a comment](/reference/retrieve-comment) - GET

#### List Comments

[List comments](/reference/list-comments) - GET

### File Uploads

#### Create a File Upload

[Create a file upload](/reference/create-a-file-upload) - POST

#### Send a File Upload

[Send a file upload](/reference/send-a-file-upload) - POST

#### Complete a File Upload

[Complete a file upload](/reference/complete-a-file-upload) - POST

#### Retrieve a File Upload

[Retrieve a file upload](/reference/retrieve-a-file-upload) - GET

#### List File Uploads

[List file uploads](/reference/list-file-uploads) - GET

### Search

[Search](/reference/post-search) - POST
```

# Update a data source

Updates the [data source](/reference/data-source) object — the properties, title, description, or whether it's in the trash — of a specified data source under a database.

Returns the updated data source object.

Use the `parent` parameter to move the data source to a different `database_id`. If you do so, any existing views that refer to the data source in the current database continue to exist, but become _linked_ views. A new standard "table" view for the moved data source is created under the new (destination) database. Use the Notion app to make any further changes to the views; managing views using the API is not currently supported.

Data source properties represent the columns (or schema) of a data source. To update the properties of a data source, use the `properties` [body param](/reference/update-data-source-properties) with this endpoint. Learn more about data source properties in the [data source properties](/reference/property-object) and [Update data source properties](/reference/update-data-source-properties) docs.

To update a `relation` data source property, share the related database with the integration. Learn more about relations in the [data source properties](/reference/property-object#relation) page.

For an overview of how to use the REST API with databases, refer to the [Working with databases](/docs/working-with-databases) guide.

## How data sources property type changes work

All properties in pages are stored as rich text. Notion will convert that rich text based on the types defined in a data source's schema. When a type is changed using the API, the data will continue to be available, it is just presented differently.

For example, a multi select property value is represented as a comma-separated list of strings (eg. "1, 2, 3") and a people property value is represented as a comma-separated list of IDs. These are compatible and the type can be converted.

Note: Not all type changes work. In some cases data will no longer be returned, such as people type → file type.

## Interacting with data source rows

This endpoint cannot be used to update data source rows.

To update the properties of a data source row — rather than a column — use the [Update page properties](/reference/patch-page) endpoint. To add a new row to a database, use the [Create a page](/reference/post-page) endpoint.

## Recommended data source schema size limit

Developers are encouraged to keep their data source schema size to a maximum of **50KB**. To stay within this schema size limit, the number of properties (or columns) added to a data source should be managed.

Data source schema updates that are too large will be blocked by the REST API to help developers keep their data source queries performant.

## Errors

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

> 🚧 The following data source properties cannot be updated via the API:
> 
> - `formula`
> - `status`
> - [Synced content](https://www.notion.so/help/guides/synced-databases-bridge-different-tools)
> - `place`

> 📘 Data source relations must be shared with your integration
> 
> To update a data source [relation](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation) property, the related database must also be shared with your integration.
```