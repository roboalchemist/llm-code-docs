# Source: https://developers.notion.com/reference/page-property-values.md

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

# Page properties

## Overview

A [page object](/reference/page) is made up of page properties that contain data about the page.

When you send a request to [Create a page](/reference/post-page), set the page properties in the `properties` object body parameter.

[Retrieve a page](/reference/retrieve-a-page) surfaces the identifier, type, and value of a page’s properties.

[Retrieve a page property item](/reference/retrieve-a-page-property) returns information about a single property ID. Especially for formulas, rollups, and relations, Notion recommends using this API to ensure you get an accurate, up-to-date property value that isn't truncating any results. Refer to [Page property items](/reference/property-item-object) for specific API shape details when using this endpoint.

An [Update page](/reference/patch-page) query modifies the page property values specified in the `properties` object body param.

> **Pages that live in a data source are easier to query and manage**
>
> **Page properties** are most useful when interacting with a page that is an entry in a data source, represented as a row in the Notion app UI.
>
> If a page is not part of a data source, then its only available property is its `title`.

## Attributes

Each page property value object contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` | An underlying identifier for the property. Historically, this may be a UUID, but newer IDs are a short ID that's always URL-encoded in the API and in [integration webhooks](/reference/webhooks).<br/>`id` may be used in place of `name` when creating or updating pages.<br/>`id` remains constant when the property name changes. | `"f%5C%5C%3Ap"` |
| `type` | `string` (enum) | The type of the property in the page object. Possible type values are:<br/>- `checkbox`<br/>- `created_by`<br/>- `created_time`<br/>- `date`<br/>- `email`<br/>- `files`<br/>- `formula`<br/>- `last_edited_by`<br/>- `last_edited_time`<br/>- `multi_select`<br/>- `number`<br/>- `people`<br/>- `phone_number`<br/>- `relation`<br/>- `rollup`<br/>- `rich_text`<br/>- `select`<br/>- `status`<br/>- `title`<br/>- `url`<br/>- `unique_id`<br/>- `verification`<br/>Refer to specific type sections below for details on type-specific values. | `"rich_text"` |
| `checkbox` | `boolean` | Whether the checkbox is checked (`true`) or unchecked (`false`). | `true` |

### Size limits for page property values

For information about size limitations for specific page property objects, refer to the [limits for property values documentation](/reference/request-limits#limits-for-property-values).

When returned from the [Retrieve page property item](/changelog/retrieve-page-property-values) API, there's an additional field, `object`, which is always the string `"property_item"`, as described in [Page property items](/reference/property-item-object).

## Type objects

### Checkbox

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `checkbox` | `boolean` | Whether the checkbox is checked (`true`) or unchecked (`false`). | `true` |

#### Example `properties` body param for a post or patch page request that creates or updates a checkbox page property value

```json
{
  "properties": {
    "checkbox": true
  }
}
```

📘

Size limits for page property values

For information about size limitations for specific page property objects, refer to the [limits for property values documentation](/reference/request-limits#limits-for-property-values).
```

# Properties

## Example checkbox page property value as returned in a GET page request

### JSON

```json
{
  "Task completed": {
    "id": "ZI%40W",
    "type": "checkbox",
    "checkbox": true
  }
}
```

## Created by

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `created_by` | `object` | A [user object](/reference/user) containing information about the user who created the page.<br/><br/>`created_by` can’t be updated. | Refer to the example response objects below. |

### Example `created_by` page property value as returned in a GET page request

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `created_by` | `object` | A [user object](/reference/user) containing information about the user who created the page.<br/><br/>`created_by` can’t be updated. | Refer to the example response objects below. |

## Created time

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `created_time` | `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) | The date and time that the page was created.<br/><br/>The `created_time` value can’t be updated. | `"2022-10-12T16:34:00.000Z"` |

### Example `created_time` page property value as returned in a GET page request

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Created time` | `object` | A string representing the end of a date range.<br/><br/>If the value is `null`, then the date value is not a range. | `"2020-12-08T12:00:00Z"` |

## Date

If the `type` of a page property value is `"date"`, then the property value contains a `"date"` object with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `end` | `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) | (Optional) A string representing the end of a date range.<br/><br/>If the value is `null`, then the date value is not a range. | `"2020-12-08T12:00:00Z"` |
| `start` | `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) | A date, with an optional time.<br/><br/>If the `date` value is a range, then `start` represents the start of the range. | `"2020-12-08T12:00:00Z"` |

### Example `properties` body param for a POST or PATCH page request that creates or updates a date page property value

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Due date` | `object` | An object containing information about the date. | Refer to the example response objects below. |

### Example `date` page property value as returned in a GET page request

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Due date` | `object` | An object containing information about the date. | Refer to the example response objects below. |

## Email

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `email` | `string` | A string describing an email address. | `"[email@example.com]"` |

### Example `properties` body param for a POST or PATCH page request that creates or updates an `email` page property value

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Email` | `object` | An object containing information about the email. | Refer to the example response objects below. |

### Example `email` page property value as returned in a GET page request

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Email` | `object` | An object containing information about the email. | Refer to the example response objects below. |

## Files

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `files` | `array` of [file objects](/reference/file-object) | An array of objects containing information about the files. | Refer to the example response objects below. |

### Example creation or update of `files` property

The following is an example `properties` body parameter for a `POST` or `PATCH` page request that creates or updates a `files` page property value.

When providing an `external` URL, the `name` parameter is required.

When providing a `file_upload`, the `name` is optional and defaults to the `filename` of the original [File Upload](/reference/file-upload).

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Blueprint` | `object` | An object containing information about the files. | Refer to the example response objects below. |

### Example `files` page property value as returned in a GET page request

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `Blueprint` | `object` | An object containing information about the files. | Refer to the example response objects below. |

> ```json
> {
>   "Task completed": {
>     "id": "ZI%40W",
>     "type": "checkbox",
>     "checkbox": true
>   }
> }
> ```
```

# 📘Array parameter overwrites the entire existing value

When updating a `files` page property value, the value is overwritten by the new array of `files` passed.

If you pass a `file` object containing a file hosted by Notion, it remains one of the files. To remove any file, don't pass it in the update request.

## Formula

Formula property value objects represent the result of evaluating a formula described in the [data source's properties](/reference/data-source).

If the `type` of a page property value is `"formula"`, then the property value contains a `"formula"` object with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| boolean || date || number || string | The value of the result of the formula. The value can’t be updated directly via the API. | 42 |
| type | string (enum) | A string indicating the data type of the result of the formula. Possible `type` values are: - `boolean` - `date` - `number` - `string` | `"number"` |

### Example `formula` page property value as returned in a GET page request

```json
{
  "Days until launch": {
    "id": "CSoE",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 56
    }
  }
}
```

> The [Retrieve a page endpoint](/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `formula` property. If a `formula` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](/reference/retrieve-a-page-property) for the specific `formula` property to get its complete list of references.

## Icon

> Page icon and cover are not nested under `properties`.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| icon | an object | Icon object | Refer to the example response objects below. |

### Example emoji `icon` property value as returned in GET page request

```json
{
  "icon": {
    "type": "emoji",
    "emoji": "😀"
  }
}
```

### Example uploaded `icon` page property value as returned in a GET page request

```json
{
  "icon": {
    "type": "file",
    "file": {
      "url": "https://local-files-secure.s3.us-west-2.amazonaws.com/13950b26-c203-4f3b-b97d-93ec06319565/a7084c4c-3e9a-4324-af99-34e0cb7f8fe7/notion.jpg?...",
      "expiry_time": "2024-12-03T19:44:56.932Z"
    }
  }
}
```

### Example updating a page icon to an uploaded file

After uploading an image using the [File Upload API](file-upload#file-types-and-sizes), use the File Upload's ID in the [Create a page](/reference/post-page) or [Update page properties](/reference/patch-page) API to attach it as a page icon. For example:

```json
{
  "icon": {
    "type": "file_upload",
    "file_upload": {
      "id": "43833259-72ae-404e-8441-b6577f3159b4"
    }
  }
}
```

To attach a file upload as a page cover rather than an icon, use the create or update page APIs with the `cover` parameter, nesting a `file_upload` parameter the same way as the `icon` example.

## Last edited by

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| last_edited_by | object | A [user object](/reference/user) containing information about the user who last updated the page. `last_edited_by` can’t be updated. | Refer to the example response objects below. |

### Example `last_edited_by` page property value as returned in a GET page request

```json
{
  "Last edited by column name": {
    "id": "uGNN",
    "type": "last_edited_by",
    "last_edited_by": {
      "object": "user",
      "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf",
      "name": "Test Integration",
      "avatar_url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/3db373fe-18f6-4a3c-a536-0f061cb9627f/leplane.jpeg",
      "type": "bot",
      "bot": {}
    }
  }
}
```

## Last edited time

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| last_edited_time | string ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) | The date and time that the page was last edited. The `last_edited_time` value can’t be updated. | `"2022-10-12T16:34:00.000Z"` |

### Example `last_edited_time` page property value as returned in a GET page request

```json
{
  "Last edited time": {
    "id": "%3Defk",
    "type": "last_edited_time",
    "last_edited_time": "2023-02-24T21:06:00.000Z"
  } 
}
```

## Multi-select

If the `type` of a page property value is `"multi_select"`, then the property value contains a `"multi_select"` array with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| color | string (enum) | Color of the option. Note: the `color` value can’t be updated via the API. Possible `"color"` values are: - `blue` - `brown` - `default`(the default value) - `gray` - `green` - `orange` - `pink` - `purple` - `red` - `yellow` | `"blue"` |

## 📘Array parameter overwrites the entire existing value

When updating a `files` page property value, the value is overwritten by the new array of `files` passed.

If you pass a `file` object containing a file hosted by Notion, it remains one of the files. To remove any file, don't pass it in the update request.

## 📘Formula

Formula property value objects represent the result of evaluating a formula described in the [data source's properties](/reference/data-source).

If the `type` of a page property value is `"formula"`, then the property value contains a `"formula"` object with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| boolean || date || number || string | The value of the result of the formula. The value can’t be updated directly via the API. | 42 |
| type | string (enum) | A string indicating the data type of the result of the formula. Possible `type` values are: - `boolean` - `date` - `number` - `string` | `"number"` |

### Example `formula` page property value as returned in a GET page request

```json
{
  "Days until launch": {
    "id": "CSoE",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 56
    }
  }
}
```

> The [Retrieve a page endpoint](/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `formula` property. If a `formula` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](/reference/retrieve-a-page-property) for the specific `formula` property to get its complete list of references.

## 📘Icon

> Page icon and cover are not nested under `properties`.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| icon | an object | Icon object | Refer to the example response objects below. |

### Example emoji `icon` property value as returned in GET page request

```json
{
  "icon": {
    "type": "emoji",
    "emoji": "😀"
  }
}
```

### Example uploaded `icon` page property value as returned in a GET page request

```json
{
  "icon": {
    "type": "file",
    "file": {
      "url": "https://local-files-secure.s3.us-west-2.amazonaws.com/13950b26-c203-4f3b-b97d-93ec06319565/a7084c4c-3e9a-4324-af99-34e0cb7f8fe7/notion.jpg?...",
      "expiry_time": "2024-12-03T19:44:56.932Z"
    }
  }
}
```

### Example updating a page icon to an uploaded file

After uploading an image using the [File Upload API](file-upload#file-types-and-sizes), use the File Upload's ID in the [Create a page](/reference/post-page) or [Update page properties](/reference/patch-page) API to attach it as a page icon. For example:

```json
{
  "icon": {
    "type": "file_upload",
    "file_upload": {
      "id": "43833259-72ae-404e-8441-b6577f3159b4"
    }
  }
}
```

To attach a file upload as a page cover rather than an icon, use the create or update page APIs with the `cover` parameter, nesting a `file_upload` parameter the same way as the `icon` example.

## 📘Last edited by

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| last_edited_by | object | A [user object](/reference/user) containing information about the user who last updated the page. `last_edited_by` can’t be updated. | Refer to the example response objects below. |

### Example `last_edited_by` page property value as returned in a GET page request

```json
{
  "Last edited by column name": {
    "id": "uGNN",
    "type": "last_edited_by",
    "last_edited_by": {
      "object": "user",
      "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf",
      "name": "Test Integration",
      "avatar_url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/3db373fe-18f6-4a3c-a536-0f061cb9627f/leplane.jpeg",
      "type": "bot",
      "bot": {}
    }
  }
}
```

## 📘Last edited time

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| last_edited_time | string ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) | The date and time that the page was last edited. The `last_edited_time` value can’t be updated. | `"2022-10-12T16:34:00.000Z"` |

### Example `last_edited_time` page property value as returned in a GET page request

```json
{
  "Last edited time": {
    "id": "%3Defk",
    "type": "last_edited_time",
    "last_edited_time": "2023-02-24T21:06:00.000Z"
  } 
}
```

## 📘Multi-select

If the `type` of a page property value is `"multi_select"`, then the property value contains a `"multi_select"` array with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| color | string (enum) | Color of the option. Note: the `color` value can’t be updated via the API. Possible `"color"` values are: - `blue` - `brown` - `default`(the default value) - `gray` - `green` - `orange` - `pink` - `purple` - `red` - `yellow` | `"blue"` |
```

# Properties

## Array of [User Objects](https://www.notion.so/reference/user)

An array of user objects.

Refer to the example response objects below.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `users` | array of [User Objects](https://www.notion.so/reference/user) | An array of user objects. | ```{ "users": [{ "id": "c2f20311-9e54-4d11-8c79-7398424ae41e", "name": "Kimberlee Johnson", "avatar_url": null, "type": "person", "person": { "email": "[email protected]" } } ] }``` |

## Array of [Page References](https://www.notion.so/reference/page-reference)

An array of related page references. A page reference is an object with an `id` key and a string value corresponding to a page ID in another data source.

Refer to the example response objects below.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `pageReferences` | array of [Page Reference](https://www.notion.so/reference/page-reference) | An array of related page references. | ```{ "pageReferences": [{ "id": "c2f20311-9e54-4d11-8c79-7398424ae41e", "name": "Kimberlee Johnson", "avatar_url": null, "type": "person", "person": { "email": "[email protected]" } }, { "id": "c2f20311-9e54-4d11-8c79-7398424ae41e", "name": "Kimberlee Johnson", "avatar_url": null, "type": "person", "person": { "email": "[email protected]" } }] }``` |

## Array of [Multi-Select Options](https://www.notion.so/reference/multi-select-option)

An array of multi-select options.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `options` | array of [Multi-Select Option](https://www.notion.so/reference/multi-select-option) | An array of multi-select options. | ```{ "options": [{ "id": "b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python", "color": "gray" }] }``` |

## Array of [Option Items](https://www.notion.so/reference/option-item)

An array of option items.

| Field | Type | Description | Example Value |
| --- | --- | --- | --- |
| `items` | array of [Option Item](https://www.notion.so/reference/option-item) | An array of option items. | ```{ "items": [{ "id": "tC;=", "name": "TypeScript", "color": "purple" }, { "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb", "name": "JavaScript", "color": "red" }, { "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0", "name": "Python",

# Example

## Example JSON

```json
{
  "Related tasks": {
    "relation": [
      {
        "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
      },
      {
        "id": "0c1f7cb2-8090-4f18-924e-d92965055e32"
      }
    ],
    "has_more": false
  }
}
```

## 📘 To update a `relation` property value via the API, share the related parent database with the integration.

If a `relation` property value is unexpectedly empty, then make sure that you have shared the original source database for the data source that the `relation` points to with the integration.

Ensuring correct permissions is also important for complete results for `rollup` and `formula` properties.

### Rollup

If the `type` of a page property value is `"rollup"`, then the property value contains a `"rollup"` object with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `array` || `date` || `incomplete` || `number` || `unsupported` | Corresponds to the field.<br/>For example, if the field is `number`, then the type of the value is `number`. | The value of the calculated rollup.<br/>The value can't be directly updated via the API. | `1234` |
| `function` | `string` (enum) | The function that is evaluated for every page in the relation of the rollup. Possible `"function"` values are:<br/><br/>- `average`<br/>- `checked`<br/>- `count`<br/>- `count_per_group`<br/>- `count_values`<br/>- `date_range`<br/>- `earliest_date`<br/>- `empty`<br/>- `latest_date`<br/>- `max`<br/>- `median`<br/>- `min`<br/>- `not_empty`<br/>- `percent_checked`<br/>- `percent_empty`<br/>- `percent_not_empty`<br/>- `percent_per_group`<br/>- `percent_unchecked`<br/>- `range`<br/>- `show_original`<br/>- `show_unique`<br/>- `sum`<br/>- `unchecked`<br/>- `unique` | `"sum"` |
| `type` | `array` || `date` || `incomplete` || `number` || `unsupported` | The value type of the calculated rollup. | `number` |

#### Example `rollup` page property value as returned in a GET page request

```json
{
  "Number of units": {
    "id": "hgMz",
    "type": "rollup",
    "rollup": {
      "type": "number",
      "number": 2,
      "function": "count"
    }
  }
}
```

### Rich text

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `rich_text` | an array of [rich text objects](/reference/rich-text) | An array of [rich text objects](/reference/rich-text) | Refer to the example response objects below. |
| `rich_text` | `string` (enum) | An array of [rich text objects](/reference/rich-text) | Refer to the example response objects below. |

#### Example `properties` body param for a POST or PATCH page request that creates or updates a `rich_text` page property value

```json
{
  "properties": {
    "Description": {
      "rich_text": [
        {
          "type": "text",
          "text": {
            "content": "There is some ",
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
          "plain_text": "There is some ",
          "href": null
        },
        {
          "type": "text",
          "text": {
            "content": "text",
            "link": null
          },
          "annotations": {
            "bold": true,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "text",
          "href": null
        },
        {
          "type": "text",
          "text": {
            "content": " in this property!",
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
          "plain_text": " in this property!",
          "href": null
        }
      ]
    }
  }
}
```

#### Example `rich_text` page property value as returned in a GET page request

```json
{
  "Description": {
    "id": "HbZT",
    "type": "rich_text",
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "There is some ",
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
        "plain_text": "There is some ",
        "href": null
      },
      {
        "type": "text",
        "text": {
          "content": "text",
          "link": null
        },
        "annotations": {
          "bold": true,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "text",
        "href": null
      },
      {
        "type": "text",
        "text": {
          "content": " in this property!",
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
        "plain_text": " in this property!",
        "href": null
      }
    ]
  } 
}
```

### 📘

The [Retrieve a page endpoint](/reference/retrieve-a-page) returns a maximum of 25 populated inline page or person references for a `rich_text` property. If a `rich_text` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](/reference/retrieve-a-page-property) for the specific `rich_text` property to get its complete list of references.

### Select

If the type of a page property value is `select`, then the property value contains a `select` object with the following fields:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `color` | `string` (enum) | The color of the option. Possible `"color"` values are:<br/><br/>- `"color"` | `"color"` |
```

# Properties

## Select Property Values

### Example `properties` body param for a POST or PATCH page request that creates or updates a `select` page property value

```json
{
  "properties": {
    "Department": {
      "select": {
        "name": "Marketing"
      }
    }
  }
}
```

### Example select page property value as returned in a GET page request

```json
{
  "Department": {
    "id": "Yc%3FJ",
    "type": "select",
    "select": {
      "id": "ou@_",
      "name": "jQuery",
      "color": "purple"
    }
  }
}
```

## Status

If the type of a page property value is `status`, then the property value contains a `status` object with the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `color` | `string` (enum) | The color of the option. Possible `"color"` values are: - `blue` - `brown` - `default` - `gray` - `green` - `orange` - `pink` - `purple` - `red` - `yellow` Defaults to `default`. The `color` value can’t be updated via the API. | `"red"` |
| `id` | `string` | string | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"` |
| `name` | `string` | The name of the option as it appears in Notion. | `"In progress"` |

### Example `properties` body param for a POST or PATCH page request that creates or updates a `status` page property value

```json
{
  "properties": {
    "Status": {
      "status": {
        "name": "Not started"
      }
    }
  }
}
```

### Example `status` page property value as returned in a GET page request

```json
{
  "Status": {
    "id": "Z%3ClH",
    "type": "status",
    "status": {
      "id": "539f2705-6529-42d8-a215-61a7183a92c0",
      "name": "In progress",
      "color": "blue"
    }
  }
}
```

## Title

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `title` | an array of [rich text objects](/reference/rich-text) | An array of [rich text objects](/reference/rich-text). | Refer to the example response objects below. |
|  | `string` |  |  |
|  | `array of rich text objects` |  |  |

### Example `properties` body param for a POST or PATCH page request that creates or updates a `title` page property value

```json
{
  "properties": {
    "Title": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "A better title for the page",
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
          "plain_text": "This is also not done",
          "href": null
        }
      ]
    }
  }
}
```

### Example `title` page property value as returned in a GET page request

```json
{
  "Title": {
    "id": "title",
    "type": "title",
    "title": [
      {
        "type": "text",
        "text": {
          "content": "A better title for the page",
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
        "plain_text": "This is also not done",
        "href": null
      }
    ]
  }
}
```

> The [Retrieve a page endpoint](/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `title` property. If a `title` property includes more than 25 references, then you can use the [Retrieve a page property item endpoint](/reference/retrieve-a-page-property) for the specific `title` property to get its complete list of references.

## URL

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `url` | `string` | A string that describes a web address. | `"https://developers.notion.com/"` |

### Example `properties` body param for a POST or PATCH page request that creates or updates a `url` page property value

```json
{
  "properties": {
    "Website": {
      "url": "https://developers.notion.com/"
    }
  }
}
```

### Example `url` page property value as returned in a GET page request

```json
{
  "Url": {
    "type": "url",
    "url": "https://developers.notion.com/"
  }
}
```

# Page Property Types

## Overview

This document provides a comprehensive guide to the various page property types available through the Notion API. Each property type serves a specific purpose in representing different aspects of your Notion pages.

## Attributes

### Type objects

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `number` | `number` | The ID count (auto-incrementing). | 3 |
| `prefix` | `string` or `null` | An optional prefix to be applied to the unique ID. | "RL" |

> **Note:** Unique IDs can be read using the API with a [GET page](/reference/retrieve-a-page) request, but they cannot be updated with the API, since they are auto-incrementing.

### Example `url` page property value as returned in a GET page request

```json
{
  "test-ID": {
    "id": "tqqd",
    "type": "unique_id",
    "unique_id": {
      "number": 3,
      "prefix": "RL",
    },
  },
}
```

## Verification

The verification status of a page in a wiki database. Pages can be verified or unverified, and verifications can have an optional expiration date set.

The verification status cannot currently be set or updated via the public API.

> **Note:** The `verification` property is only available for pages that are part of a [wiki database](/docs/working-with-databases#wiki-databases). To learn more about wiki databases and verifying pages, see our [Help Center article](https://www.notion.so/help/wikis-and-verified-pages#verifying-pages).

### Example `verification` page property values as returned in a GET page request

#### Unverified

```json
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: { state: "unverified", verified_by: null, date: null },
  },
}
```

#### Verified with no expiration date set

```json
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: {
      state: "verified",
      verified_by: {
        object: "user",
        id: "01e46064-d5fb-4444-8ecc-ad47d076f804",
        name: "User Name",
        avatar_url: null,
        type: "person",
        person: {},
      },
      date: { start: "2023-08-01T04:00:00.000Z", end: null, time_zone: null },
    },
  },
}
```

#### Verified with 90-day expiration date

```json
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: {
      ...,
      date: {
        start: "2023-08-01T04:00:00.000Z",
        end: "2023-10-30T04:00:00.000Z",
        time_zone: null,
      },
    },
  },
}
```

## Unsupported properties

The Public API supports a subset of property types. Unsupported types will be returned with a `null` value. Exclude these unsupported types when you are updating page properties.

```json
{
	"properties": {
		"Place": {
      "id": "%60%40Gq",
      "type": "place",
      "place": null
    }
	}
}
```

## Paginated page properties

The `title`, `rich_text`, `relation` and `people` page properties are returned as a paginated `list` object of individual `property_item` objects.

An abridged set of the the properties found in the `list` object is below. Refer to the [pagination documentation](/reference/intro#pagination) for additional information.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `object` | `"list"` | Always `"list"`. | `"list"` |
| `type` | `"property_item"` | Always `"property_item"`. | `"property_item"` |
| `results` | `list` | List of `property_item` objects. | `[{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}...]` |
| `property_item` | `object` | A `property_item` object that describes the property. | `{"id": "title", "next_url": null, "type": "title", "title": {}}` |
| `next_url` | `string` or `null` | The URL the user can request to get the next page of results. | `"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"` |

## Table of Contents

- [Overview](#overview)
- [Attributes](#attributes)
- [Type objects](#type-objects)
  - [Checkbox](#checkbox)
  - [Created by](#created-by)
  - [Created time](#created-time)
  - [Date](#date)
  - [Email](#email)
  - [Files](#files)
  - [Formula](#formula)
  - [Icon](#icon)
  - [Last edited by](#last-edited-by)
  - [Last edited time](#last-edited-time)
  - [Multi-select](#multi-select)
  - [Number](#number)
  - [People](#people)
  - [Phone number](#phone-number)
  - [Relation](#relation)
  - [Rollup](#rollup)
  - [Rich text](#rich-text)
  - [Select](#select)
  - [Status](#status)
  - [Title](#title)
  - [URL](#url)
  - [Unique ID](#unique-id)
  - [Verification](#verification)
  - [Unsupported properties](#unsupported-properties)
- [Paginated page properties](#paginated-page-properties)
```