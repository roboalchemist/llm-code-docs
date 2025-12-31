# Source: https://developers.notion.com/reference/comment-object.md

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

# Comment

The Comment object represents a comment on a Notion page or block. Comments can be viewed or created by an integration that has access to the page/block and the correct capabilities. Please see the [Capabilities guide](/reference/capabilities) for more information on setting up your integration's capabilities.

When [retrieving comments](/reference/retrieve-a-comment), one or more Comment objects will be returned in the form of an array, sorted in ascending chronological order. When [adding a comment](/reference/create-a-comment) to a page or discussion, the Comment object just added will always be returned.

```json
{
  "object": "comment",
  "id": "7a793800-3e55-4d5e-8009-2261de026179",
  "parent": {
    "type": "page_id",
    "page_id": "5c6a2821-6bb1-4a7e-b6e1-c50111515c3d"
  },
  "discussion_id": "f4be6752-a539-4da2-a8a9-c3953e13bc0b",
  "created_time": "2022-07-15T21:17:00.000Z",
  "last_edited_time": "2022-07-15T21:17:00.000Z",
  "created_by": {
    "object": "user",
    "id": "e450a39e-9051-4d36-bc4e-8581611fc592"
  },
  "rich_text": [
    {
      "type": "text",
      "text": {
        "content": "Hello world",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Hello world",
      "href": null
    }
  ],
  "attachments": [
    {
      "category": "image",
      "file": {
        "url": "https://s3.us-west-2.amazonaws.com/...",
        "expiry_time": "2025-06-10T21:58:51.599Z"
      }
    }
  ],
  "display_name": {
    "type": "user",
    "resolved_name": "Avo Cado"
  }
}
```

## Reminder: Turn on integration comment capabilities

Integrations must have read comments or insert comments capabilities in order to interact with the Comment object through the API.  
For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `object` | `string` | Always `"comment"` | `"comment"` |
| `id` | `string` (UUIDv4) | Unique identifier of the comment. | `"ce18f8c6-ef2a-427f-b416-43531fc7c117"` |
| `parent` | `object` | Information about the comment's parent. See [Parent object](/reference/parent-object). Note that comments may only be parented by pages or blocks. | `{ "type": "block_id", "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c" }` |
| `discussion_id` | `string` (UUIDv4) | Unique identifier of the discussion thread that the comment is associated with. See [the guide](/docs/working-with-comments#listing-comments-for-a-page-or-block) for more information about discussion threads. | `"ce18f8c6-ef2a-427f-b416-43531fc7c117"` |
| `created_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this comment was created. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2022-07-15T21:46:00.000Z"` |
| `last_edited_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this comment was updated. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2022-07-15T21:46:00.000Z"` |
| `created_by` | [Partial User](/reference/user) | User who created the comment. | `{ "object": "user", "id": "e450a39e-9051-4d36-bc4e-8581611fc592" }` |
| `rich_text` | [Rich text object](/reference/rich-text) | Content of the comment, which supports rich text formatting, links, and mentions. | `[ { "text": { "content": "Kale", "link": { "type": "url", "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale" } } } ]` |
| `attachments` | [Comment Attachment](/reference/rich-text-copy) | File attachments on the comment | `[ { "category": "image", "file": { "url": "https://s3.us-west-2.amazonaws.com/9bc6c6e0-32b8-4d55-8c12-3ae931f43a01/meow...", "expiry_time": "2025-06-10T21:58:51.599Z" } } ]` |
| `display_name` | [Comment Display Name](/reference/comment-attachment-copy) | Custom display name on comment | `"display_name": { "type": "custom", "resolved_name": "automated response" }"` |
```