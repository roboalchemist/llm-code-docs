# Source: https://developers.notion.com/reference/property-item-object.md

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

# Page property items

## Overview

A `property_item` object describes the identifier, type, and value of a page property. It's returned from the [Retrieve a page property item](/reference/retrieve-a-page-property) API.

Generally, the details on this page are the same as those in [Page properties](/reference/page-property-values), but with tweaks and additional information specific to the retrieve page property item endpoint, such as [value pagination](#paginated-property-values).

## Common fields

Each page property item object contains the following keys. In addition, it will contain a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `object` | `"property_item"` | Always `"property_item"`. | `"property_item"` |
| `id` | `string` | Underlying identifier for the property. This identifier is guaranteed to remain constant when the property name changes. It may be a UUID, but is often a short random string. The `id` may be used in place of `name` when creating or updating pages. | `"f%5C%5C%3Ap"` |
| `type` | `string` (enum) | Type of the property. Possible values are `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"date"`, `"formula"`, `"relation"`, `"rollup"`, `"title"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, and `"last_edited_by"`. | `"rich_text"` |

## Paginated values

The [`title`](/reference/retrieve-a-page-property#paginated-properties), `rich_text`, `relation` and `people` property items of are returned as a paginated `list` object of individual `property_item` objects in the results. An abridged set of the the properties found in the `list` object are found below; see the [Pagination](/reference/pagination) documentation for additional information.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `object` | `"list"` | Always `"list"`. | `"list"` |
| `type` | `"property_item"` | Always `"property_item"`. | `"property_item"` |
| `results` | `list` | List of `property_item` objects. | ```
[{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]
``` |
| `property_item` | `object` | A `property_item` object that describes the property. | ```
{"id": "title", "next_url": null, "type": "title", "title": {}}
``` |
| `next_url` | `string` or `null` | The URL the user can request to get the next page of results. | `"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"` |

## Title

Title property value objects contain an array of [rich text objects](/reference/rich-text) within the `title` property.

```json
{
  "Name": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "title",
        "type": "title",
        "title": {
          "type": "text",
          "text": {
            "content": "The title",
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
          "plain_text": "The title",
          "href": null
        }
      }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "property_item",
    "property_item": {
      "id": "title",
      "next_url": null,
      "type": "title",
      "title": {}
    }
  }
}
```

## Rich text

Rich text property value objects contain an array of [rich text objects](/reference/rich-text) within the `rich_text` property.

```json
{
  "Details": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "NVv%5E",
        "type": "rich_text",
        "rich_text": {
          "type": "text",
          "text": {
            "content": "Some more text with ",
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
          "plain_text": "Some more text with ",
          "href": null
        }
      },
      {
        "object": "property_item",
        "id": "NVv%5E",
        "type": "rich_text",
        "rich_text": {
          "type": "text",
          "text": {
            "content": "fun formatting",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": true,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "fun formatting",
          "href": null
        }
      }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "property_item",
    "property_item": {
      "id": "rich_text",
      "next_url": null,
      "type": "rich_text",
      "rich_text": {}
    }
  }
}
```
```

# Number

Number property value objects contain a number within the `number` property.

```json
{
  "Quantity": {
    "object": "property_item",
    "id": "XpXf",
    "type": "number",
    "number": 1234
  }
}
```

## Select

Select property value objects contain the following data within the `select` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` (UUIDv4) | ID of the option.<br/>When updating a select property, you can use either `name` or `id`. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"` |
| `name` | `string` | Name of the option as it appears in Notion.<br/>If the select [database property](/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.<br/>Note: Commas (",") are not valid for select values. | `"Fruit"` |
| `color` | `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`. Not currently editable. | `"red"` |

```json
{
  "Option": {
    "object": "property_item",
    "id": "%7CtzR",
    "type": "select",
    "select": {
      "id": "64190ec9-e963-47cb-bc37-6a71d6b71206",
      "name": "Option 1",
      "color": "orange"
    }
  }
}
```

## Multi-select

Multi-select property value objects contain an array of multi-select option values within the `multi_select` property.

### Option values

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` (UUIDv4) | ID of the option.<br/>When updating a multi-select property, you can use either `name` or `id`. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"` |
| `name` | `string` | Name of the option as it appears in Notion.<br/>If the multi-select [database property](/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.<br/>Note: Commas (",") are not valid for select values. | `"Fruit"` |
| `color` | `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`. Not currently editable. | `"red"` |

```json
{
  "Tags": {
    "object": "property_item",
    "id": "z%7D%5C%3C",
    "type": "multi_select",
    "multi_select": [
      {
        "id": "91e6959e-7690-4f55-b8dd-d3da9debac45",
        "name": "A",
        "color": "orange"
      },
      {
        "id": "2f998e2d-7b1c-485b-ba6b-5e6a815ec8f5",
        "name": "B",
        "color": "purple"
      }
    ]
  }
}
```

# Date

Date property value objects contain the following data within the `date` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `start` | string ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | An ISO 8601 format date, with optional time. | `"2020-12-08T12:00:00Z"` |
| `end` | string (optional, [ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | An ISO 8601 formatted date, with optional time. Represents the end of a date range.<br/>If `null`, this property's date value is not a range. | `"2020-12-08T12:00:00Z"` |
| `time_zone` | string (optional, enum) | Time zone information for `start` and `end`. Possible values are extracted from the [IANA database](https://www.iana.org/time-zones) and they are based on the time zones from [Moment.js](https://momentjs.com/timezone/).<br/>When time zone is provided, `start` and `end` should not have any [UTC offset](https://en.wikipedia.org/wiki/UTC_offset). In addition, when time zone is provided, `start` and `end` cannot be dates without time information.<br/>If `null`, time zone information will be contained in [UTC offset](https://en.wikipedia.org/wiki/UTC_offset)s in `start` and `end`. | `"America/Los_Angeles"` |

```json
{
  "Shipment Time": {
    "object": "property_item",
    "id": "i%3Ahj",
    "type": "date",
    "date": {
      "start": "2021-05-11T11:00:00.000-04:00",
      "end": null,
      "time_zone": null
    }
  }
}
```

# Formula

Formula property value objects represent the result of evaluating a formula described in the [database's properties](/reference/property-object). These objects contain a `type` key and a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` (enum) | The type of the formula result. Possible values are `"string"`, `"number"`, `"boolean"`, and `"date"`. |

### String formula

String formula property values contain an optional string within the `string` property.

### Number formula

Number formula property values contain an optional number within the `number` property.

### Boolean formula

Boolean formula property values contain a boolean within the `boolean` property.

### Date formula

Date formula property values contain a date within the `date` property.

```json
{
  "Shipment Time": {
    "object": "property_item",
    "type": "date",
    "date": "2021-05-11T11:00:00.000-04:00"
  }
}
```

# Date Formula Property Values

Date formula property values contain an optional [date property value](#date-property-values) within the `date` property.

```json
{
  "Formula": {
    "object": "property_item",
    "id": "KpQq",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 1234
    }
  }
}
```

## Relation

Relation property value objects contain an array of `relation` property items with page references within the `relation` property. A page reference is an object with an `id` property which is a string value (UUIDv4) corresponding to a page ID in another database.

```json
{
  "Project": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "vYdV",
        "type": "relation",
        "relation": {
          "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"
        }
      }
    ],
    "next_cursor": null,
    "has_more": true,
    "type": "property_item",
    "property_item": {
      "id": "vYdV",
      "next_url": null,
      "type": "relation",
      "relation": {}
    }
  }
}
```

## Rollup

Rollup property value objects represent the result of evaluating a rollup described in the [data source's properties](/reference/property-object). The property is returned as a `list` object of type `property_item` with a list of `relation` items used to compute the rollup under `results`.

A `rollup` property item is also returned under the `property_type` key that describes the rollup aggregation and computed result.

In order to avoid timeouts, if the rollup has a large number of aggregations or properties, the endpoint returns a `next_cursor` value that is used to determine the aggregation value _so far_ for the subset of relations that have been paginated through.

Once `has_more` is `false`, then the final rollup value is returned. See the [Pagination documentation](/reference/pagination) for more information on pagination in the Notion API.

Computing the values of following aggregations are _not_ supported. Instead the endpoint returns a list of `property_item` objects for the rollup:

- `show_unique` (Show unique values)
- `unique` (Count unique values)
- `median`(Median)

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` (enum) | The type of rollup. Possible values are `"number"`, `"date"`, `"array"`, `"unsupported"` and `"incomplete"`. |
| `function` | `string` (enum) | Describes the aggregation used. Possible values include: `count`, `count_values`, `empty`, `not_empty`, `unique`, `show_unique`, `percent_empty`, `percent_not_empty`, `sum`, `average`, `median`, `min`, `max`, `range`, `earliest_date`, `latest_date`, `date_range`, `checked`, `unchecked`, `percent_checked`, `percent_unchecked`, `count_per_group`, `percent_per_group`, `show_original` |

### Number Rollup

Number rollup property values contain a number within the `number` property.

### Date Rollup

Date rollup property values contain a [date property value](#date-property-values) within the `date` property.

### Array Rollup

Array rollup property values contain an array of `property_item` objects within the `results` property.

### Incomplete Rollup

Rollups with an aggregation with more than one page of aggregated results will return a `rollup` object of type `"incomplete"`. To obtain the final value, paginate through the next values in the rollup using the `next_cursor` or `next_url` property.

```json
{
  "Rollup": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "vYdV",
        "type": "relation",
        "relation": {
          "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"
        }
      }...
    ],
    "next_cursor": "1QaTunT5",
    "has_more": true,
    "type": "property_item",
    "property_item": {
      "id": "y}~p",
      "next_url": "http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/y%7D~p?start_cursor=1QaTunT5&page_size=25",
      "type": "rollup",
      "rollup": {
        "function": "sum",
        "type": "incomplete",
        "incomplete": {}
      }
    }
  }
}
```

## People

People property value objects contain an array of user objects within the `people` property.

```json
{
  "Owners": {
    "object": "property_item",
    "id": "KpQq",
    "type": "people",
    "people": [
      {
        "object": "user",
        "id": "285e5768-3fdc-4742-ab9e-125f9050f3b8",
        "name": "Example Avo",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "[email protected]"
        }
      }
    ]
  }
}
```

## Files

File property value objects contain an array of file references within the `files` property. A file reference is an object with a File Object and `name` property, with a string value corresponding to a filename of the original file upload (e.g. `"Whole_Earth_Catalog.jpg"`).

```json
{
  "Files": {
    "object": "property_item",
    "id": "KpQq",
    "type": "files",
    "files": [
      {
        "type": "external",
        "name": "Space Wallpaper",
        "external": "https://website.domain/images/space.png"
      }
    ]
  }
}
```

## Checkbox

Checkbox property value objects contain a boolean within the `checkbox` property.

```json
{
  "Done?": {
    "object": "property_item",
    "id": "KpQq",
    "type": "checkbox",
    "checkbox": true
  }
}
```

## URL

URL property value objects contain a non-empty string within the `url` property. The string describes a web address (i.e. `"http://worrydream.com/EarlyHistoryOfSmalltalk/"`).

```json
{
  "Website": {
    "object": "property_item",
    "id": "KpQq",
    "type": "url",
    "url": "https://notion.so/notiondevs"
  }
}
```

## Email

Email property value objects contain a string within the `email` property. The string describes an email address (i.e. `"[email protected]"`).
```

# Shipper's No.

The Shipper's No. property value object contains a string within the `shipper_no` property. No structure is enforced.

```json
{
  "Shipper's No.": {
    "object": "property_item",
    "id": "KpQq",
    "type": "shipper_no",
    "shipper_no": "415-000-1111"
  }
}
```

# Created time

Created time property value objects contain a string within the `created_time` property. The string contains the date and time when this page was created. It is formatted as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date time string (i.e. `"2020-03-17T19:10:04.968Z"`).

```json
{
  "Created Time": {
    "object": "property_item",
    "id": "KpQq",
    "type": "create_time",
    "created_time": "2020-03-17T19:10:04.968Z"
  }
}
```

# Created by

Created by property value objects contain a [user object](/reference/user) within the `created_by` property. The user object describes the user who created this page.

```json
{
  "Created By": {
    "created_by": {
      "object": "user",
      "id": "23345d4f-cf71-4a70-89a5-226c95a6eaae",
      "name": "Test User",
      "type": "person",
      "person": {
        "email": "[email protected]"
      }
    }
  }
}
```

```json
{
  "dsEa": {
    "created_by": {
      "object": "user",
      "id": "71e95936-2737-4e11-b03d-f174f6f13087"
    }
  }
}
```

# Last edited time

Last edited time property value objects contain a string within the `last_edited_time` property. The string contains the date and time when this page was last updated. It is formatted as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date time string (i.e. `"2020-03-17T19:10:04.968Z"`).

```json
{
  "Last Edited Time": {
    "last_edited_time": "2020-03-17T19:10:04.968Z"
  }
}
```

```json
{
  "as0w": {
    "last_edited_time": "2020-03-17T19:10:04.968Z"
  }
}
```

# Last edited by

Last edited by property value objects contain a [user object](/reference/user) within the `last_edited_by` property. The user object describes the user who last updated this page.

```json
{
  "Last Edited By": {
    "last_edited_by": {
      "object": "user",
      "id": "23345d4f-cf71-4a70-89a5-226c95a6eaae",
      "name": "Test User",
      "type": "person",
      "person": {
        "email": "[email protected]"
      }
    }
  }
}
```

```json
{
  "as12": {
    "last_edited_by": {
      "object": "user",
      "id": "71e95936-2737-4e11-b03d-f174f6f13087"
    }
  }
}
```
```