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

# Create a database

[post](https://docs.rapidapi.com/reference/database-create)

# Update a database

[patch](https://docs.rapidapi.com/reference/database-update)

# Retrieve a database

[get](https://docs.rapidapi.com/reference/database-retrieve)

## Data sources

### Create a data source

[post](https://docs.rapidapi.com/reference/create-a-data-source)

### Update a data source

#### Update data source properties

[update](https://docs.rapidapi.com/reference/update-data-source-properties)

### Retrieve a data source

[get](https://docs.rapidapi.com/reference/retrieve-a-data-source)

### Query a data source

#### Filter data source entries

[filter](https://docs.rapidapi.com/reference/filter-data-source-entries)

#### Sort data source entries

[sort](https://docs.rapidapi.com/reference/sort-data-source-entries)

### List data source templates

[get](https://docs.rapidapi.com/reference/list-data-source-templates)

## Databases (deprecated)

### Create a database

[post](https://docs.rapidapi.com/reference/create-a-database)

### Query a database

#### Filter database entries

[filter](https://docs.rapidapi.com/reference/post-database-query-filter)

#### Sort database entries

[sort](https://docs.rapidapi.com/reference/post-database-query-sort)

### Retrieve a database

[get](https://docs.rapidapi.com/reference/retrieve-a-database)

### Update a database

#### Update database properties

[update](https://docs.rapidapi.com/reference/update-property-schema-object)

### List databases (deprecated)

[get](https://docs.rapidapi.com/reference/get-databases)

## Comments

### Create comment

[post](https://docs.rapidapi.com/reference/create-a-comment)

### Retrieve a comment

[get](https://docs.rapidapi.com/reference/retrieve-comment)

### List comments

[get](https://docs.rapidapi.com/reference/list-comments)

## File Uploads

### Create a file upload

[post](https://docs.rapidapi.com/reference/create-a-file-upload)

### Send a file upload

[post](https://docs.rapidapi.com/reference/send-a-file-upload)

### Complete a file upload

[post](https://docs.rapidapi.com/reference/complete-a-file-upload)

### Retrieve a file upload

[get](https://docs.rapidapi.com/reference/retrieve-a-file-upload)

### List file uploads

[get](https://docs.rapidapi.com/reference/list-file-uploads)

## Search

[post](https://docs.rapidapi.com/reference/post-search)
```

# Create a data source

Use this API to add an additional [data source](/reference/data-source) to an existing [database](/reference/database). The `properties` follow the same structure as the initial schema passed to `initial_data_source[properties]` in the [Create a database](/reference/database-create6ee911d9) API, but can be managed independently of the `properties` of any sibling data sources.

A standard "table" view is created alongside the new data source. To customize database views, use the Notion app. Managing views is not currently supported in the API.
```