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
- [Create a token](/reference/create-a-token) (POST)
- [Introspect token](/reference/introspect-token) (POST)
- [Revoke token](/reference/revoke-token) (POST)
- [Refresh a token](/reference/refresh-a-token) (POST)

### Blocks
- [Append block children](/reference/append-block-children) (PATCH)
- [Retrieve a block](/reference/retrieve-a-block) (GET)
- [Retrieve block children](/reference/retrieve-block-children) (GET)
- [Update a block](/reference/update-a-block) (PATCH)
- [Delete a block](/reference/delete-a-block) (DEL)

### Pages
- [Create a page](/reference/create-a-page) (POST)
- [Retrieve a page](/reference/retrieve-a-page) (GET)
- [Retrieve a page property item](/reference/retrieve-a-page-property) (GET)
- [Update page](/reference/update-page) (PATCH)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (POST)
- [List databases](/reference/list-databases) (GET)
- [Delete a database](/reference/delete-database) (DEL)
```

# Post a Database Query Filter

[Post](https://docs.rapidapi.com/reference/post-database-query-filter)

## Request Method
POST

## Path Parameters
- `databaseId` (string): The ID of the database to query.

## Response
The response will contain a list of entries that match the query criteria.

## Example Request

```http
POST https://example.com/api/database/query
Content-Type: application/json
Authorization: Bearer API_KEY

{
  "databaseId": "your_database_id",
  "filter": {
    "field": "title",
    "operator": "==",
    "value": "my_query"
  }
}
```

## Example Response

```json
[
  {
    "id": 1,
    "title": "My Query",
    "content": "This is my query result."
  },
  {
    "id": 2,
    "title": "Another Query",
    "content": "This is another query result."
  }
]
```

# Filter database entries

> ❗️Deprecated as of version 2025-09-03
> 
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
> 
> Refer to the new page instead:
> 
> *   [Filter data source entries](/reference/filter-data-source-entries)

When you [query a database](/reference/post-database-query), you can send a `filter` object in the body of the request that limits the returned entries based on the specified criteria.

For example, the below query limits the response to entries where the `"Task completed"` checkbox property value is `true`:

```bash
curl -X POST 'https://api.notion.com/v1/databases/897e5a76ae524b489fdfe71f5945d1af/query' \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H 'Notion-Version: 2022-06-28' \
  -H "Content-Type: application/json" \
--data '{
  "filter": {
    "property": "Task completed",
    "checkbox": {
        "equals": true
   }
  }
}'
```

Here is the same query using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js):

```javascript
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });
// replace with your own database ID
const databaseId = 'd9824bdc-8445-4327-be8b-5b47500af6ce';

const filteredRows = async () => {
	const response = await notion.databases.query({
	  database_id: databaseId,
	  filter: {
	    property: "Task completed",
	    checkbox: {
	      equals: true
	    }
	  },
	});
  return response;
}
```

Filters can be chained with the `and` and `or` keys so that multiple filters are applied at the same time. (See [Query a database](/reference/post-database-query) for additional examples.)

```json
{
  "and": [
    {
      "property": "Done",
      "checkbox": {
        "equals": true
      }
    }, 
    {
      "or": [
        {
          "property": "Tags",
          "contains": "A"
        },
        {
          "property": "Tags",
          "contains": "B"
        }
      ]
    }
  ]
}
```

If no filter is provided, all the pages in the database will be returned with pagination.

## The filter object

Each `filter` object contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `property` | `string` | The name of the property as it appears in the database, or the property ID. | `"Task completed"` |
| `checkbox` | `string` | The type of checkbox filter. Valid values are `equals`, `does_not_equal`, `date`, `file`, `formula`, `multi_select`, `number`, `people`, `phone_number`, `relation`, `rich_text`, `select`, `status`, `timestamp`, `verification`, `ID`. | `object` |
|  | `boolean` | Whether a checkbox property value matches the provided value exactly. Returns or excludes all database entries with an exact value match. | `false` |
|  | `boolean` | Whether a checkbox property value differs from the provided value. Returns or excludes all database entries with a difference in values. | `true` |

### Example checkbox filter object

```json
{
  "filter": {
    "property": "Task completed",
    "checkbox": {
      "equals": true
    }
  }
}
```

> 👍The filter object mimics the database [filter option in the Notion UI](https://www.notion.so/help/views-filters-and-sorts).

## Type-specific filter conditions

### Checkbox

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `boolean` | Whether a checkbox property value matches the provided value exactly. Returns or excludes all database entries with an exact value match. | `false` |
| `does_not_equal` | `boolean` | Whether a checkbox property value differs from the provided value. Returns or excludes all database entries with a difference in values. | `true` |

### Date

> 📘For the `after`, `before`, `equals`, `on_or_before`, and `on_or_after` fields, if a date string with a time is provided, then the comparison is done with millisecond precision.
> 
> If no timezone is provided, then the timezone defaults to UTC.

A date filter condition can be used to limit `date` property value types and the [timestamp](#timestamp) property types `created_time` and `last_edited_time`.

The condition contains the below fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `after` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against. Returns database entries where the date property value is after the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `before` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against. Returns database entries where the date property value is before the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |

```json
{
  "filter": {
    "property": "Task completed",
    "checkbox": {
      "does_not_equal": true
    }
  }
}
```
```

# Date Filters

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.<br/>Returns database entries where the date property value is the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `is_empty` | `true` | The value to compare the date property value against.<br/>Returns database entries where the date property value contains no data. | `true` |
| `is_not_empty` | `true` | The value to compare the date property value against.<br/>Returns database entries where the date property value is not empty. | `true` |
| `next_month` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the next month. | `{}` |
| `next_week` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the next week. | `{}` |
| `next_year` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the next year. | `{}` |
| `on_or_after` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.<br/>Returns database entries where the date property value is on or after the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `on_or_before` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.<br/>Returns database entries where the date property value is on or before the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `past_month` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the past month. | `{}` |
| `past_week` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the past week. | `{}` |
| `past_year` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the past year. | `{}` |
| `this_week` | `object` (empty) | A filter that limits the results to database entries where the date property value is this week. | `{}` |

## Example date filter condition

```json
{
  "filter": {
    "property": "Due date",
    "date": {
      "on_or_after": "2023-02-08"
    }
  }
}
```

### Files

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `is_empty` | `true` | Whether the files property value does not contain any data.<br/>Returns all database entries with an empty `files` property value. | `true` |
| `is_not_empty` | `true` | Whether the `files` property value contains data.<br/>Returns all entries with a populated `files` property value. | `true` |

### Example files filter condition

```json
{
  "filter": {
    "property": "Blueprint",
    "files": {
      "is_not_empty": true
    }
  }
}
```

### Formula

The primary field of the `formula` filter condition object matches the type of the formula’s result. For example, to filter a formula property that computes a `checkbox`, use a `formula` filter condition object with a `checkbox` field containing a checkbox filter condition as its value.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `checkbox` | `object` | A [checkbox](#checkbox) filter condition to compare the formula result against.<br/>Returns database entries where the formula result matches the provided condition. | Refer to the [checkbox](#checkbox) filter condition. |
| `date` | `object` | A [date](#date) filter condition to compare the formula result against.<br/>Returns database entries where the formula result matches the provided condition. | Refer to the [date](#date) filter condition. |
| `number` | `object` | A [number](#number) filter condition to compare the formula result against.<br/>Returns database entries where the formula result matches the provided condition. | Refer to the [number](#number) filter condition. |
| `string` | `object` | A [rich text](#rich-text) filter condition to compare the formula result against.<br/>Returns database entries where the formula result matches the provided condition. | Refer to the [rich text](#rich-text) filter condition. |

### Example formula filter condition

```json
{
  "filter": {
    "property": "One month deadline",
    "formula": {
      "date": {
          "after": "2021-05-10"
      }
    }
  }
}
```

### Multi-select

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` | The value to compare the multi-select property value against.<br/>Returns database entries where the multi-select value matches the provided string. | `"Marketing"` |
| `does_not_contain` | `string` | The value to compare the multi-select property value against.<br/>Returns database entries where the multi-select value does not match the provided string. | `"Engineering"` |
| `is_empty` | `true` | Whether the multi-select property value is empty.<br/>Returns database entries where the multi-select value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the multi-select property value is not empty.<br/>Returns database entries where the multi-select value does contains data. | `true` |

### Example multi-select filter condition

```json
{
  "filter": {
    "property": "Product Line",
    "contains": "Marketing"
  }
}
```

# Filter Conditions

## Boolean

### `and`

The `and` filter condition combines multiple filters, ensuring that all conditions must be met for an entry to be included.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `false` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `not_in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `or`

The `or` filter condition combines multiple filters, allowing for at least one condition to be met for an entry to be included.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is in the list of values. | `true` |

### `not_in`

The `not_in` filter condition excludes values from the list of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the provided value. | `true` |
| `not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not the same as the provided value. | `true` |
| `in` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is not in the list of values. | `true` |

### `between`

The `between` filter condition specifies a range of values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `boolean` | The boolean value to compare the value against. Returns database entries where the value differs from the provided value. | `true` |
| `equals` | `boolean` | The boolean value to compare the value against. Returns database entries where the value is the same as the

# Database Property Filters

## General Syntax

To apply a filter condition to a database property, use the following syntax:

```json
{
  "filter": {
    "property": "property_name",
    "value": "value_to_compare"
  }
}
```

### Example

```json
{
  "filter": {
    "property": "Description",
    "value": "cross-team"
  }
}
```

## Type-Specific Filter Conditions

### String

- **`equals`**: Compares the property value to a specific string.
- **`is_empty`**: Checks if the property value is empty.
- **`is_not_empty`**: Checks if the property value is not empty.
- **`starts_with`**: Compares the property value to a specific string.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `string` | The string to compare the property value against. Returns database entries with a property value matching the provided string. | `"Moved to Q2"` |
| `is_empty` | `true` | Whether the property value does not contain any data. Returns database entries with a property value that is empty. | `true` |
| `is_not_empty` | `true` | Whether the property value contains any data. Returns database entries with a property value that contains data. | `true` |
| `starts_with` | `string` | The string to compare the property value against. Returns database entries with a property value starting with the provided string. | `"Moved"` |

### Array

- **`any`**: Compares the property value to a list of objects, using any of the defined comparison operators (`equals`, `is_empty`, `is_not_empty`, or `starts_with`).
- **`every`**: Compares the property value to a list of objects, using all of the defined comparison operators (`equals`, `is_empty`, `is_not_empty`, or `starts_with`).
- **`none`**: Compares the property value to a list of objects, using none of the defined comparison operators (`equals`, `is_empty`, `is_not_empty`, or `starts_with`).

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `any` | `object` | The value to compare each array element against. Can be a filter condition for any other type. Returns database entries where the array element matches the provided criteria. | `"rich_text": {"contains": "Take Fig on a walk"}` |
| `every` | `object` | The value to compare each array element against. Can be a filter condition for any other type. Returns database entries where all array elements match the provided criteria. | `"rich_text": {"contains": "Take Fig on a walk"}` |
| `none` | `object` | The value to compare each array element against. Can be a filter condition for any other type. Returns database entries where none of the array elements match the provided criteria. | `"rich_text": {"contains": "Take Fig on a walk"}` |

### Date

- **`date`**: A date filter condition to compare the array element against a date. Returns database entries where the array element matches the provided date.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `date` | `object` | A date filter condition to compare the array element against a date. Returns database entries where the array element matches the provided date. | Refer to the date filter condition. |

### Number

- **`number`**: A number filter condition to compare the array element against a number. Returns database entries where the array element matches the provided number.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `number` | `object` | A number filter condition to compare the array element against a number. Returns database entries where the array element matches the provided number. | Refer to the number filter condition. |

### Rollup

A rollup database property can evaluate to an array, date, or number value. The filter condition for the rollup property contains a `rollup` key and a corresponding object value that depends on the computed value type.

#### Filter Conditions for Array Rollup Values

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `any` | `object` | The value to compare each rollup property value against. Can be a filter condition for any other type. Returns database entries where the rollup property value matches the provided criteria. | `"rich_text": {"contains": "Take Fig on a walk"}` |
| `every` | `object` | The value to compare each rollup property value against. Can be a filter condition for any other type. Returns database entries where every rollup property value matches the provided criteria. | `"rich_text": {"contains": "Take Fig on a walk"}` |
| `none` | `object` | The value to compare each rollup property value against. Can be a filter condition for any other type. Returns database entries where no rollup property value matches the provided criteria. | `"rich_text": {"contains": "Take Fig on a walk"}` |

#### Filter Conditions for Date Rollup Values

A rollup value is stored as a `date` only if the "Earliest date", "Latest date", or "Date range" computation is selected for the property in the Notion UI.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `date` | `object` | A date filter condition to compare the rollup value against. Returns database entries where the rollup value matches the provided condition. | Refer to the date filter condition. |

#### Filter Conditions for Number Rollup Values

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `number` | `object` | A number filter condition to compare the rollup value against. Returns database entries where the rollup value matches the provided condition. | Refer to the number filter condition. |

### Select

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `string` | The string to compare the select property value against. Returns database entries where the select property value matches the provided string. | `"This week"` |
| `does_not_equal` | `string` | The string to compare the select property value against. Returns database entries where the select property value does not match the provided string. | `"Backlog"` |
| `is_empty` | `true` | Whether the select property value does not contain data. Returns database entries where the select property value is empty. | `true` |
| `is_not_empty` | `true` | Whether the select property value contains data. Returns database entries where the select property value is not empty. | `true` |

### Status

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `string` | The string to compare the status property value against. Returns database entries where the status property value matches the provided string. | `"This week"` |
| `does_not_equal` | `string` | The string to compare the status property value against. Returns database entries where the status property value does not match the provided string. | `"Backlog"` |
| `is_empty` | `true` | Whether the status property value does not contain data. Returns database entries where the status property value is empty. | `true` |
| `is_not_empty` | `true` | Whether the status property value contains data. Returns database entries where the status property value is not empty. | `true` |

### Timestamp

Use a timestamp filter condition to filter results based on `created_time` or `last_edited_time` values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `timestamp` | `created_time last_edited_time` | A constant string representing the type of timestamp to use as a filter. | `"created_time"` |
| `created_time` | `object` | A date filter condition used to filter the specified timestamp. | Refer to the date filter condition. |

#### Example Timestamp Filter Condition for Created Time

```json
{
  "filter": {
    "timestamp": "created_time",
    "created_time": {
      "on_or_before": "2022-10-13"
    }
  }
}
```

> The `timestamp` filter condition does not require a property name. The API throws an error if you provide one.

### Verification

The `timestamp` filter condition does not require a property name. The API throws an error if you provide one.
```

# Database Query Filters

## The filter object

A database query filter is a JSON object that specifies one or more fields to search for values that match. You can use any combination of filters to create complex queries.

### Example filter object

```json
{
  "filter": {
    "field1": {
      "type": "string",
      "value": "example value"
    },
    "field2": {
      "type": "number",
      "value": 123
    }
  }
}
```

### Type-specific filter conditions

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `number` | The value to compare the field value against. Returns database entries where the field value differs from the provided value. | `42` |
| `equals` | `number` | The value to compare the field value against. Returns database entries where the field value is the same as the provided value. | `42` |
| `greater_than` | `number` | The value to compare the field value against. Returns database entries where the field value exceeds the provided value. | `42` |
| `greater_than_or_equal_to` | `number` | The value to compare the field value against. Returns database entries where the field value is equal to or exceeds the provided value. | `42` |
| `less_than` | `number` | The value to compare the field value against. Returns database entries where the field value is less than the provided value. | `42` |
| `less_than_or_equal_to` | `number` | The value to compare the field value against. Returns database entries where the field value is equal to or is less than the provided value. | `42` |

### Example filter object with multiple fields

```json
{
  "filter": {
    "field1": {
      "type": "string",
      "value": "example value"
    },
    "field2": {
      "type": "number",
      "value": 123
    },
    "field3": {
      "type": "boolean",
      "value": true
    }
  }
}
```

## Type-specific filter conditions

### Checkbox

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `checkbox` | `boolean` | Whether the field value matches the specified value. | `true` |
| `equals` | `boolean` | Whether the field value matches the specified value. | `true` |

### Date

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `date` | `string` | A date string in YYYY-MM-DD format. | `"2023-09-16"` |
| `date_between` | `string` | A date range string in YYYY-MM-DD format. | `"2023-09-15 00:00:00"`, `"2023-09-17 00:00:00"` |
| `date_before` | `string` | A date string in YYYY-MM-DD format before which the field value should match. | `"2023-09-15"` |
| `date_after` | `string` | A date string in YYYY-MM-DD format after which the field value should match. | `"2023-09-17"` |

### Files

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `file` | `object` | A file object containing properties like `name`, `url`, `size`, etc. | `{"name": "file1.pdf", "url": "https://example.com/file1.pdf", "size": 1024}` |
| `file_in_folder` | `string` | A folder ID that the file belongs to. | `"folder1"` |

### Formula

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `formula` | `string` | A complex expression using operators and functions. | `"A + B * C / D"` |

### Multi-select

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `select` | `array` | An array of select options. | `["option1", "option2"]` |
| `select_in` | `string` | A folder ID that the select option belongs to. | `"folder1"` |

### Number

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `number` | `string` | A number string in decimal format. | `"123.45"` |
| `number_between` | `string` | A number range string in decimal format. | `"123.45 00:00:00"` |
| `number_before` | `string` | A number string in decimal format before which the value should match. | `"123.45"` |
| `number_after` | `string` | A number string in decimal format after which the value should match. | `"123.45"` |

### People

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `person` | `object` | A person object containing properties like `name`, `title`, `department`, etc. | `{"name": "John Doe", "title": "Manager", "department": "Sales"}` |
| `person_in` | `string` | A folder ID that the person belongs to. | `"folder1"` |

### Relation

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `relation` | `string` | A relation ID that the object belongs to. | `"relation1"` |

### Rich text

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `rich_text` | `string` | A rich text string. | `"This is a rich text string."` |

### Rollup

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `rollup` | `string` | A rollup ID that the object belongs to. | `"rollup1"` |

### Select

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `select` | `string` | A select option. | `"option1"` |

### Status

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `status` | `string` | The verification status being queried. Valid options are: `verified`, `expired`, `none`. | `"verified"` |

### Timestamp

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `timestamp` | `string` | A timestamp string in YYYY-MM-DD HH:mm:ss format. | `"2023-09-16 14:30:00"` |

### Verification

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `verification` | `object` | A verification object containing properties like `status`, `expires_at`, etc. | `{"status": "verified", "expires_at": "2023-09-17 00:00:00"}` |

### ID

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `number` | The value to compare the ID property value against. Returns database entries where the ID property value differs from the provided value. | `42` |
| `equals` | `number` | The value to compare the ID property value against. Returns database entries where the ID property value is the same as the provided value. | `42` |
| `greater_than` | `number` | The value to compare the ID property value against. Returns database entries where the ID property value exceeds the provided value. | `42` |
| `greater_than_or_equal_to` | `number` | The value to compare the ID property value against. Returns database entries where the ID property value is equal to or exceeds the provided value. | `42` |
| `less_than` | `number` | The value to compare the ID property value against. Returns database entries where the ID property value is less than the provided value. | `42` |
| `less_than_or_equal_to` | `number` | The value to compare the ID property value against. Returns database entries where the ID property value is equal to or is less than the provided value. | `42` |

### Example verification filter condition for getting verified pages

```json
{
  "filter": {
    "property": "verification",
    "verification": {
      "status": "verified"
    }
  }
}
```

### Example ID filter condition

```json
{
  "filter": {
    "and": [
      {
        "property": "ID",
        "unique_id": {
          "greater_than": 1
        }
      },
      {
        "property": "ID",
        "unique_id": {
          "less_than": 3
        }
      }
    ]
  }
}
```

## Compound filter conditions

You can use a compound filter condition to limit the results of a database query based on multiple conditions. This mimics filter chaining in the Notion UI.

### Example filter chain in the Notion UI

![1340](https://files.readme.io/14ec7e8-Untitled.png)

The above filters in the Notion UI are equivalent to the following compound filter condition via the API:

```json
{
  "and": [
    {
      "property": "Done",
      "checkbox": {
        "equals": true
      }
    },
    {
      "or": [
        {
          "property": "Tags",
          "contains": "A"
        },
        {
          "property": "Tags",
          "contains": "B"
        }
      ]
    }
  ]
}
```

A compound filter condition contains an `and` or `or` key with a value that is an array of filter objects or nested compound filter objects. Nesting is supported up to two levels deep.

### Example compound filter conditions

#### Example compound filter condition for a checkbox and number property value

```json
{
  "filter": {
    "and": [
      {
        "property": "Complete",
        "checkbox": {
          "equals": true
        }
      },
      {
        "property": "Working days",
        "number": {
          "greater_than": 10
        }
      }
    ]
  }
}
```

#### Example nested filter condition

```json
{
  "filter": {
    "or": [
      {
        "property": "Description",
        "rich_text": {
          "contains": "2023"
        }
      },
      {
        "and": [
          {
            "property": "Department",
            "select": {
              "equals": "Engineering"
            }
          },
          {
            "property": "Priority goal",
            "checkbox": {
              "equals": true
            }
          }
        ]
      }
    ]
  }
}
```
```