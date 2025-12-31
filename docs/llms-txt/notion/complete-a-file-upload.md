# Source: https://developers.notion.com/reference/complete-a-file-upload.md

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

# Complete a file upload

[Post](https://docs.rapidapi.com/reference/complete-a-file-upload)

## Request Parameters

| Name | Type | Description |
| --- | --- | --- |
| `databaseId` | string | The ID of the database to complete the entry in. |
| `entryId` | string | The ID of the entry to complete. |
| `templateId` | string | The ID of the template to use for the completion. |

## Response

| Name | Type | Description |
| --- | --- | --- |
| `completedEntries` | array | An array of objects containing details of completed entries. |
```

# Complete a file upload

Use this API to finalize a `mode=multi_part` [file upload](/reference/file-upload) after all of the parts have been sent successfully.

## Language

- Shell
- Node
- Ruby
- PHP
- Python
```