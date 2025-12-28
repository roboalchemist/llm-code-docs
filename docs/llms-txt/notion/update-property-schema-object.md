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

# Update a database

[post](/reference/database-update)

## Main Menu

*   [Create a database](/reference/database-create)
    *   [Create a database](/reference/create-a-database)
*   [Update a database](/reference/database-update)
    *   [Update a database](/reference/update-a-database)
        *   [Update database properties](/reference/update-property-schema-object)
*   [Retrieve a database](/reference/database-retrieve)
    *   [Retrieve a database](/reference/retrieve-a-database)

## Data Sources

*   [Create a data source](/reference/create-a-data-source)
*   [Update a data source](/reference/update-a-data-source)
    *   [Update data source properties](/reference/update-data-source-properties)
*   [Retrieve a data source](/reference/retrieve-a-data-source)
*   [Query a data source](/reference/query-a-data-source)
    *   [Filter data source entries](/reference/filter-data-source-entries)
    *   [Sort data source entries](/reference/sort-data-source-entries)
*   [List data source templates](/reference/list-data-source-templates)

## Deprecated Database Operations

*   [Databases (deprecated)](/reference/create-a-database)
    *   [Create a database](/reference/create-a-database)
    *   [Query a database](/reference/post-database-query)
        *   [Filter database entries](/reference/post-database-query-filter)
        *   [Sort database entries](/reference/post-database-query-sort)
    *   [Retrieve a database](/reference/retrieve-a-database)
    *   [Update a database](/reference/update-a-database)
        *   [Update database properties](/reference/update-property-schema-object)
    *   [List databases (deprecated)](/reference/get-databases)

## Comments

*   [Create comment](/reference/create-a-comment)
*   [Retrieve a comment](/reference/retrieve-comment)
*   [List comments](/reference/list-comments)

## File Uploads

*   [Create a file upload](/reference/create-a-file-upload)
*   [Send a file upload](/reference/send-a-file-upload)
*   [Complete a file upload](/reference/complete-a-file-upload)
*   [Retrieve a file upload](/reference/retrieve-a-file-upload)
*   [List file uploads](/reference/list-file-uploads)

## Search

*   [Search](/reference/post-search)
```

# Update database properties

> ❗️Deprecated as of version 2025-09-03
> 
> This page describes the API for versions up to and including `2022-06-28`. In the new `2025-09-03` version, the concepts of databases and data sources were split up, as described in [Upgrading to 2025-09-03](/docs/upgrade-guide-2025-09-03).
> 
> Refer to the new page instead:
> 
> - [Update data source properties](/reference/update-data-source-properties)

The API represents columns of a database in the Notion UI as database **properties**.

To use the API to update a data source's properties, send a [PATCH request](/reference/update-a-database) with a `properties` body param.

## Remove a property

To remove a database property, set the property object to null.

### Removing properties by ID

```json
"properties": {
  "J@cT": null,
}
```

### Removing properties by name

```json
"properties": {
  "propertyToDelete": null
}
```

## Rename a property

To change the name of a database property, indicate the new name in the `name` property object value.

### Renaming properties by ID

```json
"properties": {
	"J@cT": {
		"name": "New Property Name"
  }
}
```

### Renaming properties by name

```json
"properties": {
  "Old Property Name": {
    "name": "New Property Name"
  }
}
```

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of the property as it appears in Notion. |

## Update property type

To update the property type, the property schema object should contain the key of the type. This type contains behavior of this property. Possible values of this key are `"title"`, `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"date"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"formula"`, `"relation"`, `"rollup"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, `"last_edited_by"`. Within this property, the configuration is a [property schema object](/reference/property-schema-object).

> ❗️Limitations
> 
> Note that the property type of the `title` cannot be changed.
> 
> It's not possible to update the `name` or `options` values of a `status` property via the API.

### Select configuration updates

To update an existing select configuration, the property schema object optionally contains the following configuration within the `select` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `options` | optional array of [existing select options](#existing-select-options) and [select option objects](/reference/create-a-database#select-options) | Settings for select properties. If an existing option is omitted, it will be removed from the database property. New options will be added to the database property. |  |

#### Existing select options

Note that the name and color of an existing option cannot be updated.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `name` | optional `string` | Name of the option. | `"Fruit"` |
| `id` | optional `string` | ID of the option. | `"ff8e9269-9579-47f7-8f6e-83a84716863c"` |

### Multi-select configuration updates

To update an existing select configuration, the property schema object optionally contains the following configuration within the `multi_select` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `options` | optional array of [existing select options](#existing-multi-select-options) and [multi-select option objects](/reference/create-a-database#multi-select-options) | Settings for multi select properties. If an existing option is omitted, it will be removed from the database property. New options will be added to the database property. |  |

#### Existing multi-select options

Note that the name and color of an existing option cannot be updated.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `name` | `string` | Name of the option as it appears in Notion. | `"Fruit"` |
| `id` | optional `string` | ID of the option. | `"ff8e9269-9579-47f7-8f6e-83a84716863c"` |

## Limitations

### Formula maximum depth
```

# Properties

## Remove a property

### Description

Removes a property from a database.

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `database_id` | string | Yes | The ID of the database containing the property being removed. |
| `property_name` | string | Yes | The name of the property being removed. |

### Example Request

```http
POST /v1/databases/:database_id/properties.json
Content-Type: application/json

{
  "property_name": "my_property"
}
```

### Example Response

```json
{
  "data": {
    "id": "123456789",
    "name": "my_property",
    "type": "string"
  },
  "error": null
}
```

## Rename a property

### Description

Renames a property within a database.

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `database_id` | string | Yes | The ID of the database where the property is located. |
| `new_name` | string | Yes | The new name for the property. |
| `property_name` | string | Yes | The current name of the property being renamed. |

### Example Request

```http
POST /v1/databases/:database_id/properties/:property_name/rename.json
Content-Type: application/json

{
  "new_name": "my_new_property",
  "property_name": "my_property"
}
```

### Example Response

```json
{
  "data": {
    "id": "123456789",
    "name": "my_new_property",
    "type": "string"
  },
  "error": null
}
```

## Update property type

### Description

Updates the data type of a property within a database.

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `database_id` | string | Yes | The ID of the database where the property is located. |
| `property_name` | string | Yes | The name of the property whose data type is being updated. |
| `property_type` | string | Yes | The new data type for the property. |

### Example Request

```http
POST /v1/databases/:database_id/properties/:property_name/type.json
Content-Type: application/json

{
  "property_type": "integer"
}
```

### Example Response

```json
{
  "data": {
    "id": "123456789",
    "name": "my_property",
    "type": "integer"
  },
  "error": null
}
```

## Limitations

### Formula maximum depth

Formulas in Notion can have high levels of complexity beyond what the API can compute in a single request. For formulas with a maximum depth of _have or exceed_ 10 referenced tables, the API will return a "Formula depth" error as a `validation_error`.

As a workaround, you can retrieve the `formula` property object from the Retrieve a Database endpoint and use the formula expression to compute the value of more complex formulas.

### Unsupported Rollup Aggregations

Due to the encoded cursor nature of computing rollup values, a subset of aggregation types are not supported. Instead the endpoint returns a list of `show_unique` (Show unique values), `unique` (Count unique values) and `median` (Median) property_item objects for the following rollup aggregations:

- `show_unique`
- `unique`
- `median`

### Could not find page/database Error

A page property of type `rollup` and `formula` can involve computing a value based on the properties in another `relation` page. As such the integration needs permissions to the other `relation` page. If the integration doesn't have permissions page needed to compute the property value, the API will return a `object_not_found` error specifying the page the integration lacks permissions to.

### Property value doesn't match UI after pagination

If a property value involves pagination and the underlying properties or pages used to compute the property value change whilst the integration is paginating through results, the final value will be impacted and is not guaranteed to be accurate.
```