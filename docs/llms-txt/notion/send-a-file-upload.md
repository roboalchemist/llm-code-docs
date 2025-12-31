# Source: https://developers.notion.com/reference/send-a-file-upload.md

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

# Send a file upload

[Post](https://docs.rapidapi.com/reference/post-search)

## Request Body

| Field | Description |
| --- | --- |
| `body` | The file content as a Base64 encoded string. |

## Response

| Field | Description |
| --- | --- |
| `id` | The unique identifier for the uploaded file. |
| `name` | The name of the uploaded file. |
| `size` | The size of the uploaded file in bytes. |
| `type` | The type of the uploaded file. |

## Example

```json
{
  "body": "YWJvdXQgTWFuYWdlciBNb2xlY3VsYXIgUmVzb3VyY2Vz"
}
```

# Send a file upload

Use this API to transmit file contents to Notion for a [file upload](/reference/file-upload).

For this endpoint, use a `Content-Type` of `multipart/form-data`, and provide your file contents under the `file` key.

> The use of multipart form data is unique to this endpoint. Other Notion APIs, including [Create a file upload](/reference/create-a-file-upload) and [Complete a file upload](/reference/complete-a-file-upload), use JSON parameters.
> 
> Include a `boundary` with the `Content-Type` header of your request as per [RFC 2388](https://datatracker.ietf.org/doc/html/rfc2388). Most request libraries (e.g., `fetch`, `ky`) automatically handle this as long as you provide a form data object but don't overwrite the `Content-Type` explicitly.
> 
> For more tips and examples, view the [file upload guide](/reference/uploading-small-files#step-2-upload-file-contents).

When `mode=multi_part`, each part must include a form field `part_number` to indicate which part is being sent. Parts may be sent concurrently up to standard Notion API [rate limits](/reference/request-limits), and may be sent out of order as long as all parts (1, ..., `part_number`) are successfully sent before calling the [complete file upload API](/reference/complete-a-file-upload).

The maximum allowed length of a file name is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](/reference/list-file-uploads) API.
```