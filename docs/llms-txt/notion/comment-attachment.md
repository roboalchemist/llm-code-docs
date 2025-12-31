# Source: https://developers.notion.com/reference/comment-attachment.md

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

# Comment Attachment

The Comment Attachment object represents [files](/reference/file-object) that have been attached to a [Comment](/reference/comment-object).

> **📘**
> Comments can currently support up to 3 attachments.

## Request format (input)

### Object properties

After following the [Working with files and media](/docs/working-with-files-and-media) guide, provide an array of objects under the `attachments` parameter in the [Create comment](/reference/create-a-comment) API, each containing the following properties:

| Parameter | Type | Description | Example value |
| --- | --- | --- | --- |
| `file_upload_id` | `string` (UUID) | ID of a [File Upload](/reference/file-upload) with a status of `"uploaded"` | `"2e2cdb8b-9897-4a6c-a935-82922b1cfb87"` |
| `type` | `string` (optional) | Possible type values are: `"file_upload"` | `"file_upload"` |

**Example Create Comment request:**

```json
{
  "parent": {
    "page_id": "d0a1ffaf-a4d8-4acf-a1ed-abae6e110418"
  },
  "rich_text": [
    {
      "text": {
        "content": "Thanks for the helpful page!"
      }
    }
  ],
  "attachments": {
    "file_upload_id": "2e2cdb8b-9897-4a6c-a935-82922b1cfb87"
  }
}
```

In the Notion app, when viewing a comment uploaded using the API, the user experience is automatically customized based on the detected category of the file upload. For example, uploading a `.png` file displays your attachment as an inline image instead of a regular file download block.

## Response format (output)

### Object properties

The response of Comment APIs like [Create comment](/reference/create-a-comment) contains `attachments` with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `category` | `string` (enum) | The category of this attachment. Possible type values are: `"audio"`, `"image"`, `"pdf"`, `"productivity"`, and `"video"` | `"audio"` |
| `file` | `object` | A [file object](/reference/file-object#notion-hosted-files-type-file) containing type-specific configuration. | `{"url": "<https://s3.us-west-2.amazonaws.com/...>", "expiry_time": "2025-06-10T21:26:03.070Z"}` |

**Example attachment object in Create Comment response:**

```json
{
  "category": "video",
  "file": {
    "url": "https://s3.us-west-2.amazonaws.com/...",
    "expiry_time": "2025-06-10T21:26:03.070Z"
  }
}
```

The `file.url` is a temporary download link generated at the time of retrieving a comment. See the guide on [Retrieving existing files](/docs/retrieving-files) to learn more about accessing the files you upload.
```