# Source: https://developers.notion.com/reference/update-property-schema-object

> ##
>
> Deprecated as of version 2025-09-03
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
```
"properties": {
  "J@cT": null,
}
```
```
"properties": {
  "propertyToDelete": null
}
```
## Rename a property
To change the name of a database property, indicate the new name in the `name` property object value.
```
"properties": {
    "J@cT": {
        "name": "New Property Name"
  }
}
```
```
"properties": {
  "Old Property Name": {
    "name": "New Property Name
  }
}
```
| Property | Type     | Description                                       |
|----------|----------|---------------------------------------------------|
| `name`   | `string` | The name of the property as it appears in Notion. |
## Update property type
To update the property type, the property schema object should contain the key of the type. This type contains behavior of this property. Possible values of this key are `"title"`, `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"date"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"formula"`, `"relation"`, `"rollup"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, `"last_edited_by"`. Within this property, the configuration is a [property schema object](/reference/property-schema-object).
> ##
>
> Limitations
>
> Note that the property type of the `title` cannot be changed.
>
> It's not possible to update the `name` or `options` values of a `status` property via the API.
### Select configuration updates
To update an existing select configuration, the property schema object optionally contains the following configuration within the `select` property:
| Property | Type | Description | Example value |
|----|----|----|----|
| `options` | optional array of [existing select options](#existing-select-options) and [select option objects](/reference/create-a-database#select-options) | Settings for select properties. If an existing option is omitted, it will be removed from the database property. New options will be added to the database property. |  |
#### Existing select options
Note that the name and color of an existing option cannot be updated.
| Property | Type | Description | Example value |
|----|----|----|----|
| `name` | optional `string` | Name of the option. | `"Fruit"` |
| `id` | optional `string` | ID of the option. | `"ff8e9269-9579-47f7-8f6e-83a84716863c" ` |
### Multi-select configuration updates
To update an existing select configuration, the property schema object optionally contains the following configuration within the `multi_select` property:
| Property | Type | Description | Example value |
|----|----|----|----|
| `options` | optional array of [existing select options](#existing-multi-select-options) and [multi-select option objects](/reference/create-a-database#multi-select-options) | Settings for multi select properties. If an existing option is omitted, it will be removed from the database property. New options will be added to the database property. |  |
#### Existing multi-select options
Note that the name and color of an existing option cannot be updated.
| Property | Type | Description | Example value |
|----|----|----|----|
| `name` | `string` | Name of the option as it appears in Notion. | `"Fruit"` |
| `id` | optional `string` | ID of the option. | `"ff8e9269-9579-47f7-8f6e-83a84716863c" ` |
## Limitations
### Formula maximum depth
Formulas in Notion can have high levels of complexity beyond what the API can compute in a single request. For `formula` property values that exceed *have or exceed depth of 10* referenced tables, the API will return a "Formula depth" error as a [`"validation_error"`](/reference/errors)
As a workaround, you can retrieve the `formula` property object from the Retrieve a Database endpoint and use the formula expression to compute the value of more complex formulas.
### Unsupported Rollup Aggregations
Due to the encoded cursor nature of computing rollup values, a subset of aggregation types are not supported. Instead the endpoint returns a list of *all* property_item objects for the following rollup aggregations:
- `show_unique` (Show unique values)
- `unique` (Count unique values)
- `median` (Median)
### `Could not find page/database` Error
A page property of type `rollup` and `formula` can involve computing a value based on the properties in another `relation` page. As such the integration needs permissions to the other `relation` page. If the integration doesn't have permissions page needed to compute the property value, the API will return a [`"object_not_found"`](/reference/errors) error specifying the page the integration lacks permissions to.
### Property value doesn't match UI after pagination
If a property value involves [pagination](/reference/pagination) and the underlying properties or pages used to compute the property value change whilst the integration is paginating through results, the final value will impacted and is not guaranteed to be accurate.