# Source: https://developers.notion.com/reference/filter-data-source-entries.md

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
- [Update page](/reference/update-page)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (POST)
- [List databases](/reference/list-databases) (GET)
- [Delete a database](/reference/delete-database) (DEL)
```

# Filter data source entries

## Main Content

### Navigation Links

- [Create a database](/reference/database-create)
- [Update a database](/reference/database-update)
- [Retrieve a database](/reference/database-retrieve)

### Data Sources

#### Create a data source
- [Create a data source](/reference/create-a-data-source)

#### Update a data source
- [Update data source properties](/reference/update-data-source-properties)
- [Update a data source](/reference/retrieve-a-data-source)

#### Query a data source
- [Query a data source](/reference/query-a-data-source)
  - [Filter data source entries](/reference/filter-data-source-entries)
  - [Sort data source entries](/reference/sort-data-source-entries)
- [List data source templates](/reference/list-data-source-templates)

#### Databases (deprecated)
- [Create a database](/reference/create-a-database)
- [Query a database](/reference/post-database-query)
  - [Filter database entries](/reference/post-database-query-filter)
  - [Sort database entries](/reference/post-database-query-sort)
- [Retrieve a database](/reference/retrieve-a-database)
- [Update a database](/reference/update-a-database)
  - [Update database properties](/reference/update-property-schema-object)
- [List databases (deprecated)](/reference/get-databases)

#### Comments
- [Create comment](/reference/create-a-comment)
- [Retrieve a comment](/reference/retrieve-comment)
- [List comments](/reference/list-comments)

#### File Uploads
- [Create a file upload](/reference/create-a-file-upload)
- [Send a file upload](/reference/send-a-file-upload)
- [Complete a file upload](/reference/complete-a-file-upload)
- [Retrieve a file upload](/reference/retrieve-a-file-upload)
- [List file uploads](/reference/list-file-uploads)

#### Search
- [Search](/reference/post-search)
```

# Filter data source entries

When you [query a data source](/reference/query-a-data-source), you can send a `filter` object in the body of the request that limits the returned entries based on the specified criteria.

For example, the below query limits the response to entries where the `"Task completed"` checkbox property value is `true`:

```bash
curl -X POST 'https://api.notion.com/v1/data_sources/897e5a76ae524b489fdfe71f5945d1af/query' \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H 'Notion-Version: 2025-09-03' \
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
// replace with your own data source ID
const dataSourceId = 'd9824bdc-8445-4327-be8b-5b47500af6ce';

const filteredRows = async () => {
	const response = await notion.databases.query({
	  data_source_id: dataSourceId,
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

Filters can be chained with the `and` and `or` keys so that multiple filters are applied at the same time. (See [Query a data source](/reference/query-a-data-source) for additional examples.)

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

If no filter is provided, all the pages in the data source will be returned with pagination.

## The filter object

Each `filter` object contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `property` | `string` | The name of the property as it appears in the data source, or the property ID. | `"Task completed"` |
| `checkbox` | `string` | The type-specific filter condition for the query. Only types listed in the Field column of this table are supported. Refer to [type-specific filter conditions](#type-specific-filter-conditions) for details on corresponding object values. | `"checkbox": { "equals": true }` |

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

> The filter object mimics the data source [filter option in the Notion UI](https://www.notion.so/help/views-filters-and-sorts).

## Type-specific filter conditions

### Checkbox

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `boolean` | Whether a checkbox property value matches the provided value exactly. Returns or excludes all data source entries with an exact value match. | `false` |
| `does_not_equal` | `boolean` | Whether a checkbox property value differs from the provided value. Returns or excludes all data source entries with a difference in values. | `true` |

### Date

> For the `after`, `before`, `equals, on_or_before`, and `on_or_after` fields, if a date string with a time is provided, then the comparison is done with millisecond precision. If no timezone is provided, then the timezone defaults to UTC.

A date filter condition can be used to limit `date` property value types and the [timestamp](#timestamp) property types `created_time` and `last_edited_time`.

The condition contains the below fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `after` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against. Returns data source entries where the date property value is after the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `before` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against. Returns data source entries where the date property value is before the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `equals` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against. Returns data source entries where the date property value is equal to the provided date. | `"2021-05-10"` |

### Example checkbox filter condition

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
| `is_empty` | `true` | The value to compare the date property value against.<br/>Returns data source entries where the date property value contains no data. | `true` |
| `is_not_empty` | `true` | The value to compare the date property value against.<br/>Returns data source entries where the date property value is not empty. | `true` |
| `next_month` | `object` (empty) | A filter that limits the results to data source entries where the date property value is within the next month. | `{}` |
| `next_week` | `object` (empty) | A filter that limits the results to data source entries where the date property value is within the next week. | `{}` |
| `next_year` | `object` (empty) | A filter that limits the results to data source entries where the date property value is within the next year. | `{}` |
| `on_or_after` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.<br/>Returns data source entries where the date property value is on or after the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `on_or_before` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.<br/>Returns data source entries where the date property value is on or before the provided date. | `"2021-05-10"`<br>`"2021-05-10T12:00:00"`<br>`"2021-10-15T12:00:00-07:00"` |
| `past_month` | `object` (empty) | A filter that limits the results to data source entries where the date property value is within the past month. | `{}` |
| `past_week` | `object` (empty) | A filter that limits the results to data source entries where the date property value is within the past week. | `{}` |
| `past_year` | `object` (empty) | A filter that limits the results to data source entries where the date property value is within the past year. | `{}` |
| `this_week` | `object` (empty) | A filter that limits the results to data source entries where the date property value is this week. | `{}` |

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

## Files

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `is_empty` | `true` | Whether the files property value does not contain any data.<br/>Returns all data source entries with an empty `files` property value. | `true` |
| `is_not_empty` | `true` | Whether the `files` property value contains data.<br/>Returns all entries with a populated `files` property value. | `true` |

## Formula

The primary field of the `formula` filter condition object matches the type of the formula’s result. For example, to filter a formula property that computes a `checkbox`, use a `formula` filter condition object with a `checkbox` field containing a checkbox filter condition as its value.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `checkbox` | `object` | A [checkbox](#checkbox) filter condition to compare the formula result against.<br/>Returns data source entries where the formula result matches the provided condition. | Refer to the [checkbox](#checkbox) filter condition. |
| `date` | `object` | A [date](#date) filter condition to compare the formula result against.<br/>Returns data source entries where the formula result matches the provided condition. | Refer to the [date](#date) filter condition. |
| `number` | `object` | A [number](#number) filter condition to compare the formula result against.<br/>Returns data source entries where the formula result matches the provided condition. | Refer to the [number](#number) filter condition. |
| `string` | `object` | A [rich text](#rich-text) filter condition to compare the formula result against.<br/>Returns data source entries where the formula result matches the provided condition. | Refer to the [rich text](#rich-text) filter condition. |

## Example formula filter condition

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

## Multi-select

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` | The value to compare the multi-select property value against.<br/>Returns data source entries where the multi-select value matches the provided string. | `"Marketing"` |
| `does_not_contain` | `string` | The value to compare the multi-select property value against.<br/>Returns data source entries where the multi-select value does not match the provided string. | `"Engineering"` |
| `is_empty` | `true` | Whether the multi-select property value is empty.<br/>Returns data source entries where the multi-select value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the multi-select property value is not empty.<br/>Returns data source entries where the multi-select value does contains data. | `true` |

## Example multi-select filter condition

```json
{
  "filter": {
    "property": "Programming language",
    "multi_select": {
      "contains": "TypeScript"
    }
  }
}
```

## Number

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `is_empty` | `true` | Whether the number property value does not contain any data.<br/>Returns all data source entries with an empty `number` property value. | `true` |
| `is_not_empty` | `true` | Whether the `number` property value contains data.<br/>Returns all entries with a populated `number` property value. | `true` |

```

# Data Source Filter Conditions

## Example number filter condition

```json
{
  "filter": {
    "property": "Estimated working days",
    "number": {
      "less_than_or_equal_to": 5
    }
  }
}
```

## People

You can apply a people filter condition to `people`, `created_by`, and `last_edited_by` data source property types.

The people filter condition contains the following fields:

| Field | Type (UUIDv4) | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` | The value to compare the people property value against. Returns data source entries where the people property value contains the provided string. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `does_not_contain` | `string` (UUIDv4) | The value to compare the people property value against. Returns data source entries where the people property value does not contain the provided string. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `is_empty` | `true` | Whether the people property value does not contain any data. Returns data source entries where the people property value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the people property value contains data. Returns data source entries where the people property value is not empty. | `true` |

## Example people filter condition

```json
{
  "filter": {
    "property": "Last edited by",
    "people": {
      "contains": "c2f20311-9e54-4d11-8c79-7398424ae41e"
    }
  }
}
```

## Relation

| Field | Type (UUIDv4) | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` (UUIDv4) | The value to compare the relation property value against. Returns data source entries where the relation property value contains the provided string. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `does_not_contain` | `string` (UUIDv4) | The value to compare the relation property value against. Returns entries where the relation property value does not contain the provided string. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `is_empty` | `true` | Whether the relation property value does not contain data. Returns data source entries where the relation property value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the relation property value contains data. Returns data source entries where the property value is not empty. | `true` |

## Example relation filter condition

```json
{
  "filter": {
    "property": "✔️ Task List",
    "relation": {
      "contains": "0c1f7cb280904f18924ed92965055e32"
    }
  }
}
```

## Rich text

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` | The `string` to compare the text property value against. Returns data source entries with a text property value that includes the provided string. | `"Moved to Q2"` |
| `does_not_contain` | `string` | The `string` to compare the text property value against. Returns data source entries with a text property value that does not include the provided string. | `"Moved to Q2"` |
| `does_not_equal` | `string` | The `string` to compare the text property value against. Returns data source entries with a text property value that does not match the provided string. | `"Moved to Q2"` |
| `ends_with` | `string` | The `string` to compare the text property value against. Returns data source entries with a text property value that ends with the provided string. | `"Q2"` |
| `equals` | `string` | The `string` to compare the text property value against. | `"Moved to Q2"` |

```

# Data Source Filters

Data source filters allow you to apply constraints to the data returned from your data sources before they are sent to the web app.

## General Syntax

```
{ "filter": { "property": "value", "filter_condition": "..." } }
```

### Property

The property name that the filter condition will be applied to.

| Property | Type | Description |
| --- | --- | --- |
| `string` | `string` | The text property name to filter. |
| `boolean` | `boolean` | Whether the property should be evaluated as true or false. |
| `number` | `number` | The numeric property name to filter. |
| `integer` | `integer` | The integer property name to filter. |
| `date` | `date` | The date property name to filter. |
| `timestamp` | `timestamp` | The timestamp property name to filter. |

### Filter Condition

The filter condition that will be applied to the filtered data.

| Filter Condition | Type | Description |
| --- | --- | --- |
| `equals` | `string` | The string to compare the value against. |
| `does_not_equal` | `string` | The string to compare the value against. |
| `is_empty` | `boolean` | Whether the value does not contain any data. |
| `is_not_empty` | `boolean` | Whether the value contains any data. |
| `starts_with` | `string` | The string to compare the value against. |
| `in_range` | `number` | The inclusive range to filter the value against. |
| `not_in_range` | `number` | The exclusive range to filter the value against. |
| `between` | `number` | The start and end range to filter the value against. |
| `not_between` | `number` | The start and end range to filter the value against. |
| `is_between` | `number` | The start and end range to filter the value against. |
| `is_not_between` | `number` | The start and end range to filter the value against. |
| `is_regex` | `string` | A regular expression to match the value against. |
| `not_regex` | `string` | A regular expression to do not match the value against. |
| `is_in_list` | `array` | The list of values to filter the value against. |
| `not_in_list` | `array` | The list of values to do not filter the value against. |
| `is_in_rollup` | `object` | The rollup property name to filter the value against. |
| `is_not_in_rollup` | `object` | The rollup property name to do not filter the value against. |
| `is_in_sublist` | `array` | The sublist of values to filter the value against. |
| `is_not_in_sublist` | `array` | The sublist of values to do not filter the value against. |
| `is_in_table` | `object` | The table property name to filter the value against. |
| `is_not_in_table` | `object` | The table property name to do not filter the value against. |
| `is_in_column` | `object` | The column property name to filter the value against. |
| `is_not_in_column` | `object` | The column property name to do not filter the value against. |
| `is_in_property` | `object` | The property property name to filter the value against. |
| `is_not_in_property` | `object` | The property property name to do not filter the value against. |
| `is_in_tableau` | `object` | The tableau property name to filter the value against. |
| `is_not_in_tableau` | `object` | The tableau property name to do not filter the value against. |
| `is_in_chart` | `object` | The chart property name to filter the value against. |
| `is_not_in_chart` | `object` | The chart property name to do not filter the value against. |
| `is_in_dataframe` | `object` | The dataframe property name to filter the value against. |
| `is_not_in_dataframe` | `object` | The dataframe property name to do not filter the value against. |
| `is_in_dataset` | `object` | The dataset property name to filter the value against. |
| `is_not_in_dataset` | `object` | The dataset property name to do not filter the value against. |
| `is_in_collection` | `object` | The collection property name to filter the value against. |
| `is_not_in_collection` | `object` | The collection property name to do not filter the value against. |
| `is_in_user` | `object` | The user property name to filter the value against. |
| `is_not_in_user` | `object` | The user property name to do not filter the value against. |
| `is_in_org` | `object` | The organization property name to filter the value against. |
| `is_not_in_org` | `object` | The organization property name to do not filter the value against. |
| `is_in_project` | `object` | The project property name to filter the value against. |
| `is_not_in_project` | `object` | The project property name to do not filter the value against. |
| `is_in_task` | `object` | The task property name to filter the value against. |
| `is_not_in_task` | `object` | The task property name to do not filter the value against. |
| `is_in_issue` | `object` | The issue property name to filter the value against. |
| `is_not_in_issue` | `object` | The issue property name to do not filter the value against. |
| `is_in_comment` | `object` | The comment property name to filter the value against. |
| `is_not_in_comment` | `object` | The comment property name to do not filter the value against. |
| `is_in_activity` | `object` | The activity property name to filter the value against. |
| `is_not_in_activity` | `object` | The activity property name to do not filter the value against. |
| `is_in_notification` | `object` | The notification property name to filter the value against. |
| `is_not_in_notification` | `object` | The notification property name to do not filter the value against. |
| `is_in_comment_reply` | `object` | The comment reply property name to filter the value against. |
| `is_not_in_comment_reply` | `object` | The comment reply property name to do not filter the value against. |
| `is_in_note` | `object` | The note property name to filter the value against. |
| `is_not_in_note` | `object` | The note property name to do not filter the value against. |
| `is_in_tag` | `object` | The tag property name to filter the value against. |
| `is_not_in_tag` | `object` | The tag property name to do not filter the value against. |
| `is_in_field` | `object` | The field property name to filter the value against. |
| `is_not_in_field` | `object` | The field property name to do not filter the value against. |
| `is_in_custom_field` | `object` | The custom field property name to filter the value against. |
| `is_not_in_custom_field` | `object` | The custom field property name to do not filter the value against. |
| `is_in_custom_metadata` | `object` | The custom metadata property name to filter the value against. |
| `is_not_in_custom_metadata` | `object` | The custom metadata property name to do not filter the value against. |
| `is_in_custom_metadata_field` | `object` | The custom metadata field property name to filter the value against. |
| `is_not_in_custom_metadata_field` | `object` | The custom metadata field property name to do not filter the value against. |
| `is_in_custom_metadata_value` | `object` | The custom metadata value property name to filter the value against. |
| `is_not_in_custom_metadata_value` | `object` | The custom metadata value property name to do not filter the value against. |
| `is_in_custom_metadata_list` | `object` | The custom metadata list property name to filter the value against. |
| `is_not_in_custom_metadata_list` | `object` | The custom metadata list property name to do not filter the value against. |
| `is_in_custom_metadata_value_list` | `object` | The custom metadata value list property name to filter the value against. |
| `is_not_in_custom_metadata_value_list` | `object` | The custom metadata value list property name to do not filter the value against. |
| `is_in_custom_metadata_object` | `object` | The custom metadata object property name to filter the value against. |
| `is_not_in_custom_metadata_object` | `object` | The custom metadata object property name to do not filter the value against. |
| `is_in_custom_metadata_key` | `object` | The custom metadata key property name to filter the value against. |
| `is_not_in_custom_metadata_key` | `object` | The custom metadata key property name to do not filter the value against. |
| `is_in_custom_metadata_value_key` | `object` | The custom metadata value key property name to filter the value against. |
| `is_not_in_custom_metadata_value_key` | `object` | The custom metadata value key property name to do not filter the value against. |
| `is_in_custom_metadata_list_key` | `object` | The custom metadata list key property name to filter the value against. |
| `is_not_in_custom_metadata_list_key` | `object` | The custom metadata list key property name to do not filter the value against. |
| `is_in_custom_metadata_value_list_key` | `object` | The custom metadata value list key property name to filter the value against. |
| `is_not_in_custom_metadata_value_list_key` | `object` | The custom metadata value list key property name to do not filter the value against. |
| `is_in_custom_metadata_object_key` | `object` | The custom metadata object key property name to filter the value against. |
| `is_not_in_custom_metadata_object_key` | `object` | The custom metadata object key property name to do not filter the value against. |
| `is_in_custom_metadata_value_key_list` | `object` | The custom metadata value key list property name to filter the value against. |
| `is_not_in_custom_metadata_value_key_list` | `object` | The custom metadata value key list property name to do not filter the value against. |
| `is_in_custom_metadata_value_list_key_list` | `object` | The custom metadata value list key list property name to filter the value against. |
| `is_not_in_custom_metadata_value_list_key_list` | `object` | The custom metadata value list key list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list` | `object` | The custom metadata list key list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list` | `object` | The custom metadata list key list property name to do not filter the value against. |
| `is_in_custom_metadata_value_list_key_list` | `object` | The custom metadata value list key list property name to filter the value against. |
| `is_not_in_custom_metadata_value_list_key_list` | `object` | The custom metadata value list key list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list` | `object` | The custom metadata list key list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list` | `object` | The custom metadata list key list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list` | `object` | The custom metadata list key list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list` | `object` | The custom metadata list key list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list` | `object` | The custom metadata list key list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list` | `object` | The custom metadata list key list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list` | `object` | The custom metadata list key list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list` | `object` | The custom metadata list key list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to do not filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_not_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list` | `object` | The custom metadata list key list list list list list list list property name to filter the value against. |
| `is_in_custom_metadata_list_key_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list

# Data Source Query Filters

Data source queries can be filtered using one of two methods:

1. **Using a filter object**: This method allows you to specify multiple conditions using the `filter` object, which can then be applied to the data source.
2. **Using a filter chain**: This method involves creating a series of filter conditions that are chained together using the `and` or `or` keyword.

## The filter object

The `filter` object is used to specify multiple conditions that must be met for a data source entry to be included in the results. It can contain properties such as `checkbox`, `number`, `rich_text`, `select`, `status`, `timestamp`, `verification`, `id`, and `relation`.

### Example filter object

```json
{
  "filter": {
    "property": "Name",
    "rich_text": {
      "equals": "John Doe"
    },
    "number": {
      "greater_than": 10
    }
  }
}
```

This filter will return all data source entries where the `Name` property equals "John Doe" and the `Number` property is greater than 10.

### Type-specific filter conditions

#### Checkbox

The `checkbox` field is used to check if a specific condition must be met. For example, to filter data source entries where a person has completed a task, you would use:

```json
{
  "filter": {
    "property": "Completed",
    "checkbox": {
      "equals": true
    }
  }
}
```

#### Date

The `date` field can be used to filter data source entries based on a specific date range. For example, to filter data source entries from January 1, 2023, to December 31, 2023, you would use:

```json
{
  "filter": {
    "property": "Created At",
    "date": {
      "greater_than_or_equal_to": "2023-01-01T00:00:00Z",
      "less_than_or_equal_to": "2023-12-31T23:59:59Z"
    }
  }
}
```

#### Files

The `files` field allows you to filter data source entries based on the presence of specific file types or file IDs. For example, to filter data source entries that contain a PDF file, you would use:

```json
{
  "filter": {
    "property": "Files",
    "files": {
      "equals": "file1.pdf"
    }
  }
}
```

#### Formula

The `formula` field allows you to filter data source entries based on a complex logical expression. For example, to filter data source entries where a person's salary is greater than their department's average salary, you would use:

```json
{
  "filter": {
    "property": "Salary",
    "formula": {
      "equals": {
        "and": [
          {
            "property": "Department Name",
            "richText": {
              "contains": "Finance"
            }
          },
          {
            "property": "Average Salary",
            "number": {
              "greater_than": 50000
            }
          }
        ]
      }
    }
  }
}
```

#### Multi-select

The `multiselect` field allows you to filter data source entries based on multiple selected options. For example, to filter data source entries where a person has selected both "Apple" and "Google", you would use:

```json
{
  "filter": {
    "property": "Selected Brands",
    "multiselect": {
      "equals": [
        "Apple",
        "Google"
      ]
    }
  }
}
```

#### Number

The `number` field allows you to filter data source entries based on a specific number. For example, to filter data source entries where a person's age is 25, you would use:

```json
{
  "filter": {
    "property": "Age",
    "number": {
      "equal_to": 25
    }
  }
}
```

#### People

The `people` field allows you to filter data source entries based on a specific person's ID. For example, to filter data source entries where a person's ID is "person123", you would use:

```json
{
  "filter": {
    "property": "People",
    "people": {
      "equals": "person123"
    }
  }
}
```

#### Relation

The `relation` field allows you to filter data source entries based on a specific relation. For example, to filter data source entries where a person has a relationship with another person named "John Doe", you would use:

```json
{
  "filter": {
    "property": "Relationships",
    "relation": {
      "equals": "person123"
    }
  }
}
```

#### Rich text

The `richText` field allows you to filter data source entries based on a specific rich text string. For example, to filter data source entries where a person's description contains the word "happy", you would use:

```json
{
  "filter": {
    "property": "Description",
    "richText": {
      "contains": "happy"
    }
  }
}
```

#### Rollup

The `rollup` field allows you to filter data source entries based on a specific rollup level. For example, to filter data source entries where a person has a total bill payment of $1000 or more, you would use:

```json
{
  "filter": {
    "property": "Total Bill Payment",
    "rollup": {
      "equals": 1000
    }
  }
}
```

#### Select

The `select` field allows you to filter data source entries based on a specific selection. For example, to filter data source entries where a person has selected "Yes" for a question, you would use:

```json
{
  "filter": {
    "property": "Questions",
    "select": {
      "equals": "Yes"
    }
  }
}
```

#### Status

The `status` field allows you to filter data source entries based on a specific status. For example, to filter data source entries where a person's ticket status is "open", you would use:

```json
{
  "filter": {
    "property": "Ticket Status",
    "status": {
      "equals": "open"
    }
  }
}
```

#### Timestamp

The `timestamp` field allows you to filter data source entries based on a specific timestamp. For example, to filter data source entries from 10 AM to 2 PM on Monday, you would use:

```json
{
  "filter": {
    "property": "Created At",
    "timestamp": {
      "greater_than_or_equal_to": "2023-08-01T10:00:00Z",
      "less_than_or_equal_to": "2023-08-02T14:00:00Z"
    }
  }
}
```

#### Verification

The `verification` field allows you to filter data source entries based on a specific verification status. For example, to filter data source entries where a person's identity has been verified, you would use:

```json
{
  "filter": {
    "property": "Verification",
    "verification": {
      "equals": "verified"
    }
  }
}
```

#### ID

The `id` field allows you to filter data source entries based on a specific ID. For example, to filter data source entries where a person's ID is "person123", you would use:

```json
{
  "filter": {
    "property": "Id",
    "id": {
      "equals": "person123"
    }
  }
}
```

## Compound filter conditions

You can use a compound filter condition to limit the results of a data source query based on multiple conditions. This mimics filter chaining in the Notion UI.

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
        "property": "Working Days",
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
        "richText": {
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
            "property": "Priority Goal",
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