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

# Emoji

An emoji object contains information about an emoji character. It is most often used to represent an emoji that is rendered as a page icon in the Notion UI.

```json
{
  "type": "emoji",
  "emoji": "😻"
}
```

The object contains the following fields:

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `type` | `"emoji"` | The constant string `"emoji"` that represents the object type. | `"emoji"` |
| `emoji` | `string` | The emoji character. | `"😻"` |

To use the Notion API to render an emoji object as a page icon, set a page’s icon [property field](/reference/page) to an emoji object.

## Example: set a page icon via the [Create a page](/reference/post-page) endpoint

### cURL

```curl
curl 'https://api.notion.com/v1/pages' \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  --data '{
  "parent": {
    "page_id": "13d6da822f9343fa8ec14c89b8184d5a"
  },
  "properties": {
    "title": [
      {
        "type": "text",
        "text": {
          "content": "A page with an avocado icon",
          "link": null
        }
      }
    ]
  },
  "icon": {
    "type": "emoji",
    "emoji": "🥑"
  }
}'
```

## Example: set a page icon via the [Update page](/reference/patch-page) endpoint

### cURL

```curl
curl https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7 \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -X PATCH \
  --data '{
  "icon": {
	  "type": "emoji", 
	  "emoji": "🥨"
    }
}'
```

## Custom emoji

Custom emojis are icons uploaded and managed in your own workspace.

The object contains the following fields:

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `type` | `"custom_emoji"` | The constant string `"emoji"` that represents the object type. | `"emoji"` |
| `custom_emoji` | `object` | Custom emoji object, containing id, name, url | ```
{       "id": "45ce454c-d427-4f53-9489-e5d0f3d1db6b",       "name": "bufo",       "url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png"    } ``` |

### Example: custom emoji in page icon response

```json
{
  "icon": {
    "type": "custom_emoji",
    "custom_emoji": {
      "id": "45ce454c-d427-4f53-9489-e5d0f3d1db6b",
      "name": "bufo",
      "url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png"
    }
  }
}
```

### Example: inline custom emoji response

```json
{
  "type": "mention",
  "mention": {
    "type": "custom_emoji",
    "custom_emoji": {
      "id": "45ce454c-d427-4f53-9489-e5d0f3d1db6b",
      "name": "bufo",
      "url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png"
    }
  }
  ...
}
```

### Example: set page icon to a custom emoji

Provide the custom emoji ID to preserve/set custom emoji

```curl
curl https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7 \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -X PATCH \
  --data '{
  "icon": {
    "type": "custom_emoji",
    "custom_emoji": {
      "id": "45ce454c-d427-4f53-9489-e5d0f3d1db6b"
    }
  }
}'
```
```