# Source: https://developers.notion.com/reference/emoji-object.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Emoji

> An emoji object contains information about an emoji character. It is most often used to represent an emoji that is rendered as a page icon in the Notion UI.

<CodeGroup>
  ```json Example emoji object theme={null}
  {
    "type": "emoji",
    "emoji": "😻"
  }
  ```
</CodeGroup>

The object contains the following fields:

|         | Type      | Description                                                    | Example value |
| :------ | :-------- | :------------------------------------------------------------- | :------------ |
| `type`  | `"emoji"` | The constant string `"emoji"` that represents the object type. | `"emoji"`     |
| `emoji` | `string`  | The emoji character.                                           | `"😻"`        |

To use the Notion API to render an emoji object as a page icon, set a page’s icon [property field](/reference/page) to an emoji object.

### Example: set a page icon via the [Create a page](/reference/post-page) endpoint

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.notion.com/v1/pages' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
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
</CodeGroup>

### Example: set a page icon via the [Update page](/reference/patch-page) endpoint

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7 \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
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
</CodeGroup>

## Custom emoji

Custom emojis are icons uploaded and managed in your own workspace.

The object contains the following fields:

|                | Type             | Description                                                    | Example value                                                                                                                                                                                      |
| :------------- | :--------------- | :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`         | `"custom_emoji"` | The constant string `"emoji"` that represents the object type. | `"emoji"`                                                                                                                                                                                          |
| `custom_emoji` | `object`         | Custom emoji object, containing id, name, url                  | `{ "id": "45ce454c-d427-4f53-9489-e5d0f3d1db6b", "name": "bufo", "url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png" }` |

### Example: custom emoji in page icon response:

<CodeGroup>
  ```json Example emoji object theme={null}
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
</CodeGroup>

### Example: inline custom emoji response

<CodeGroup>
  ```json Example emoji object theme={null}
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
</CodeGroup>

### Example: set page icon to a custom emoji

Provide the custom emoji ID to preserve/set custom emoji

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7 \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
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
</CodeGroup>
