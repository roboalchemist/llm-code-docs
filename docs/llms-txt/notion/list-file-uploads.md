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

# List file uploads

[Create a database](https://docs.rapidapi.com/reference/database-create) - POST

[Update a database](https://docs.rapidapi.com/reference/database-update) - PATCH

[Retrieve a database](https://docs.rapidapi.com/reference/database-retrieve) - GET

## Data sources

### Create a data source

[Create a data source](https://docs.rapidapi.com/reference/create-a-data-source) - POST

### Update a data source

#### Update data source properties

[Update data source properties](https://docs.rapidapi.com/reference/update-data-source-properties)

### Retrieve a data source

[Retrieve a data source](https://docs.rapidapi.com/reference/retrieve-a-data-source) - GET

### Query a data source

#### Filter data source entries

[Filter data source entries](https://docs.rapidapi.com/reference/filter-data-source-entries)

#### Sort data source entries

[Sort data source entries](https://docs.rapidapi.com/reference/sort-data-source-entries)

### List data source templates

[List data source templates](https://docs.rapidapi.com/reference/list-data-source-templates) - GET

## Databases (deprecated)

### Create a database

[Create a database](https://docs.rapidapi.com/reference/create-a-database) - POST

### Query a database

#### Filter database entries

[Filter database entries](https://docs.rapidapi.com/reference/post-database-query-filter)

#### Sort database entries

[Sort database entries](https://docs.rapidapi.com/reference/post-database-query-sort)

### Retrieve a database

[Retrieve a database](https://docs.rapidapi.com/reference/retrieve-a-database) - GET

### Update a database

#### Update database properties

[Update database properties](https://docs.rapidapi.com/reference/update-property-schema-object)

### List databases (deprecated)

[List databases (deprecated)](https://docs.rapidapi.com/reference/get-databases) - GET

## Comments

### Create comment

[Create comment](https://docs.rapidapi.com/reference/create-a-comment) - POST

### Retrieve a comment

[Retrieve a comment](https://docs.rapidapi.com/reference/retrieve-comment) - GET

### List comments

[List comments](https://docs.rapidapi.com/reference/list-comments) - GET

## File Uploads

### Create a file upload

[Create a file upload](https://docs.rapidapi.com/reference/create-a-file-upload) - POST

### Send a file upload

[Send a file upload](https://docs.rapidapi.com/reference/send-a-file-upload) - POST

### Complete a file upload

[Complete a file upload](https://docs.rapidapi.com/reference/complete-a-file-upload) - POST

### Retrieve a file upload

[Retrieve a file upload](https://docs.rapidapi.com/reference/retrieve-a-file-upload) - GET

### List file uploads

[List file uploads](https://docs.rapidapi.com/reference/list-file-uploads) - GET
```

# List file uploads

Use this API to retrieve [file uploads](/reference/file-upload) for the current bot integration, sorted by most recent first.

## Language

- Shell
- Node
- Ruby
- PHP
- Python

## Credentials

### OAuth2

**Bearer**
```