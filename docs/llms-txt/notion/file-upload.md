# Source: https://developers.notion.com/reference/file-upload.md

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

# API Reference

## Database Operations

- [Create a database](https://docs.nestbase.com/reference/database-create)
- [Update a database](https://docs.nestbase.com/reference/database-update)
- [Retrieve a database](https://docs.nestbase.com/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.nestbase.com/reference/create-a-data-source)
- [Update a data source](https://docs.nestbase.com/reference/update-a-data-source)
  - [Update data source properties](https://docs.nestbase.com/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.nestbase.com/reference/retrieve-a-data-source)
- [Query a data source](https://docs.nestbase.com/reference/query-a-data-source)
  - [Filter data source entries](https://docs.nestbase.com/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.nestbase.com/reference/sort-data-source-entries)
- [List data source templates](https://docs.nestbase.com/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.nestbase.com/reference/create-a-database)
- [Query a database](https://docs.nestbase.com/reference/post-database-query)
  - [Filter database entries](https://docs.nestbase.com/reference/post-database-query-filter)
  - [Sort database entries](https://docs.nestbase.com/reference/post-database-query-sort)
- [Retrieve a database](https://docs.nestbase.com/reference/retrieve-a-database)
- [Update a database](https://docs.nestbase.com/reference/update-a-database)
  - [Update database properties](https://docs.nestbase.com/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.nestbase.com/reference/get-databases)

### Comments

- [Create comment](https://docs.nestbase.com/reference/create-a-comment)
- [Retrieve a comment](https://docs.nestbase.com/reference/retrieve-comment)
- [List comments](https://docs.nestbase.com/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.nestbase.com/reference/create-a-file-upload)
- [Send a file upload](https://docs.nestbase.com/reference/send-a-file-upload)
- [Complete a file upload](https://docs.nestbase.com/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.nestbase.com/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.nestbase.com/reference/list-file-uploads)

### Search

- [Search](https://docs.nestbase.com/reference/post-search)
```

# File Upload

The [File Upload object](#object-properties) tracks the lifecycle of a file uploaded to Notion in the API.

> **📘 Getting started**
> View [Working with files and media](/docs/working-with-files-and-media) for a comprehensive, end-to-end guide to uploading and attaching files.

Once a file upload has a `status` of `"uploaded"`, pass its ID in a [file object](/reference/file-object#files-uploaded-in-the-api-type-file_upload) with a `type` of `file_upload` to the API to attach it to blocks, pages, and databases in a Notion workspace.

## Object properties

The response of File Upload APIs like [Retrieve a file upload](/reference/retrieve-a-file-upload) contains `FileUpload` objects with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `object` | `"file_upload"` |  |
| `id` | UUID | ID of the FileUpload. |
| `created_time` | String | ISO 8601 timestamp when the FileUpload was created. |
| `last_edited_time` | String | ISO 8601 timestamp when the FileUpload was last modified. |
| `expiry_time` | String | Nullable. ISO 8601 timestamp when the FileUpload will expire, if the API integration that created it doesn't complete the upload and attach to at least one block or other object in a workspace. |
| `status` | One of:<br/>- `"pending"`<br/>- `"uploaded"`<br/>- `"expired"`<br/>- `"failed"` | Enum status of the file upload.<br/>- `pending` status means awaiting upload or completion of an upload.<br/>- `uploaded` status means file contents have been sent. If the `expiry_time` is `null`, that means the file upload has already been attached to a block or other object.<br/>- `expired` and `failed` file uploads can no longer be used. `failed` is only used for FileUploads with `mode=external_url` when the import was unsuccessful. |
| `filename` | String | Nullable. Name of the file, provided during the [Create a file upload](/reference/create-a-file-upload) step, or, for `single_part` uploads, can be determined from the provided filename in the form data passed to the [Send a file upload](/reference/send-a-file-upload) step.<br/>A file extension is automatically added based on the `content_type` if the filename doesn't already have one. |
| `content_type` | String | Nullable. The MIME content type of the uploaded file. Must be provided explicitly or inferred from a `filename` that includes an extension.<br/>For `single_part` uploads, the content type can remain `null` until the [Send a file upload](/reference/send-a-file-upload) step and inferred from the `file` parameter's content type. |
| `content_length` | Integer | Nullable. The total size of the file, in bytes. For pending `multi_part` uploads, this field is a running total based on the file segments uploaded so far and recalculated at the end during the [Complete a file upload](/reference/complete-a-file-upload) step. |
| `upload_url` | String | Field only included for `pending` file uploads.<br>This is the URL to use for [sending file contents](/reference/send-a-file-upload). |
| `complete_url` | String | Field only included for `pending` file uploads created with a `mode` of `multi_part`.<br>This is the URL to use to [complete a multi-part file upload](/reference/complete-a-file-upload). |
| `file_import_result` | String | Field only included for a `failed` or `uploaded` file upload created with a `mode` of `external_url`.<br>Provides details on the success or failure of importing a file into Notion using an external URL. |

```