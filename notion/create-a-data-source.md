# Source: https://developers.notion.com/reference/create-a-data-source

## Create a data source

**POST** `https://api.notion.com/v1/data_sources`

Use this API to add an additional [data source](/reference/data-source) to an existing [database](/reference/database). The `properties` follow the [same structure](/reference/property-object) as the initial schema passed to `initial_data_source[properties]` in the [Create a database](/reference/database-create6ee911d9) API, but can be managed independently of the `properties` of any sibling data sources.

A standard "table" view is created alongside the new data source. To customize database views, use the Notion app. Managing views is not currently supported in the API.

## Body Params

### parent
**object** (required)

An object specifying the parent of the new data source to be created.

### properties
**object** (required)

Property schema of the new data source.

### title
**array of objects**

Title of data source as it appears in Notion.

### icon
**object**

Icon to apply to the data source.

## Responses

### 200
Response body contains the data source object with the following structure:
- `object`: "data_source"
- `id`: string
- `created_time`: string
- `last_edited_time`: string
- `properties`: object containing property definitions
- `parent`: object with type and database_id
- `archived`: boolean (defaults to true)
- `is_inline`: boolean (defaults to true)
- `icon`: object with type and emoji
- `cover`: object with type and external url
- `title`: array of rich text objects

### 404
Response body contains error information.

## Example

### cURL Request
```bash
curl --request POST \
  --url https://api.notion.com/v1/data_sources \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '
{
  "parent": {
    "type": "database_id",
    "database_id": "6ee911d9-189c-4844-93e8-260c1438b6e4"
  },
  "properties": {
    "Title": {
      "type": "title",
      "title": {}
    },
    "Count": {
      "type": "number",
      "number": {}
    }
  },
  "title": [
    {
      "type": "text",
      "text": {"content": "New child data source"}
    }
  ]
}'
```

### Response (200)
```json
{
  "object": "data_source",
  "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
  "created_time": "2021-07-08T23:50:00.000Z",
  "last_edited_time": "2021-07-08T23:50:00.000Z",
  "properties": {
    "+1": {
      "id": "Wp%3DC",
      "name": "+1",
      "type": "people",
      "people": {}
    },
    "In stock": {
      "id": "fk%5EY",
      "name": "In stock",
      "type": "checkbox",
      "checkbox": {}
    },
    "Price": {
      "id": "evWq",
      "name": "Price",
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Description": {
      "id": "desc",
      "name": "Description",
      "type": "rich_text",
      "rich_text": {}
    },
    "Last ordered": {
      "id": "last",
      "name": "Last ordered",
      "type": "date",
      "date": {}
    },
    "Meals": {
      "id": "meals",
      "name": "Meals",
      "type": "relation",
      "relation": {}
    },
    "Number of meals": {
      "id": "num",
      "name": "Number of meals",
      "type": "rollup",
      "rollup": {}
    },
    "Store availability": {
      "id": "store",
      "name": "Store availability",
      "type": "multi_select",
      "multi_select": {}
    },
    "Photo": {
      "id": "photo",
      "name": "Photo",
      "type": "files",
      "files": {}
    },
    "Food group": {
      "id": "food",
      "name": "Food group",
      "type": "select",
      "select": {}
    },
    "Name": {
      "id": "title",
      "name": "Name",
      "type": "title",
      "title": {}
    }
  },
  "parent": {
    "type": "database_id",
    "database_id": "6ee911d9-189c-4844-93e8-260c1438b6e4"
  },
  "archived": false,
  "is_inline": true,
  "icon": {
    "type": "emoji",
    "emoji": "🥬"
  },
  "cover": {
    "type": "external",
    "external": {
      "url": "https://example.com/cover.jpg"
    }
  },
  "title": [
    {
      "type": "text",
      "text": {
        "content": "New child data source",
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
      "plain_text": "New child data source",
      "href": null
    }
  ]
}
```

---

**Updated:** 20 days ago

**Related:**
- [Retrieve a database](/reference/database-retrieve)
- [Update a data source](/reference/update-a-data-source)
