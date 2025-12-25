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

```

# RESTful API Reference

## Database Operations

- [Create a database](https://docs.apimatic.io/reference/database-create)
- [Update a database](https://docs.apimatic.io/reference/database-update)
- [Retrieve a database](https://docs.apimatic.io/reference/database-retrieve)

## Data Sources

### Create a Data Source

- [Create a data source](https://docs.apimatic.io/reference/create-a-data-source)
- [Update a data source](https://docs.apimatic.io/reference/update-a-data-source)
  - [Update data source properties](https://docs.apimatic.io/reference/update-data-source-properties)
- [Retrieve a data source](https://docs.apimatic.io/reference/retrieve-a-data-source)
- [Query a data source](https://docs.apimatic.io/reference/query-a-data-source)
  - [Filter data source entries](https://docs.apimatic.io/reference/filter-data-source-entries)
  - [Sort data source entries](https://docs.apimatic.io/reference/sort-data-source-entries)
- [List data source templates](https://docs.apimatic.io/reference/list-data-source-templates)

### Databases (deprecated)

#### Create a Database

- [Create a database](https://docs.apimatic.io/reference/create-a-database)
- [Query a database](https://docs.apimatic.io/reference/post-database-query)
  - [Filter database entries](https://docs.apimatic.io/reference/post-database-query-filter)
  - [Sort database entries](https://docs.apimatic.io/reference/post-database-query-sort)
- [Retrieve a database](https://docs.apimatic.io/reference/retrieve-a-database)
- [Update a database](https://docs.apimatic.io/reference/update-a-database)
  - [Update database properties](https://docs.apimatic.io/reference/update-property-schema-object)
- [List databases (deprecated)](https://docs.apimatic.io/reference/get-databases)

### Comments

- [Create comment](https://docs.apimatic.io/reference/create-a-comment)
- [Retrieve a comment](https://docs.apimatic.io/reference/retrieve-comment)
- [List comments](https://docs.apimatic.io/reference/list-comments)

### File Uploads

- [Create a file upload](https://docs.apimatic.io/reference/create-a-file-upload)
- [Send a file upload](https://docs.apimatic.io/reference/send-a-file-upload)
- [Complete a file upload](https://docs.apimatic.io/reference/complete-a-file-upload)
- [Retrieve a file upload](https://docs.apimatic.io/reference/retrieve-a-file-upload)
- [List file uploads](https://docs.apimatic.io/reference/list-file-uploads)

### Search

- [Search](https://docs.apimatic.io/reference/post-search)
```

# Retrieve a page property item

Retrieves a `property_item` object for a given `page_id` and `property_id`. Depending on the property type, the object returned will either be a value or a [paginated](/reference/pagination) list of property item values. See [Property item objects](/reference/property-item-object) for specifics.

To obtain `property_id`'s, use the [Retrieve a database](/reference/retrieve-a-database) endpoint.

In cases where a property item has more than 25 references, this endpoint should be used, rather than [Retrieve a page](/reference/retrieve-a-page). ([Retrieve a page](/reference/retrieve-a-page) will not return a complete list when the list exceeds 25 references.)

## Property Item Objects

For more detailed information refer to the [Property item object documentation](/reference/property-item-object).

### Simple Properties

Each individual `property_item` properties will have a `type` and under the the key with the value for `type`, an object that identifies the property value, documented under [Property value objects](/reference/page#property-value-object).

### Paginated Properties

Property types that return a paginated list of property item objects are:

- `title`
- `rich_text`
- `relation`
- `people`

Look for the `next_url` value in the response object for these property items to view paginated results. Refer to [paginated page properties](/reference/page-property-values#paginated-page-properties) for a full description of the response object for these properties.

Refer to the [pagination reference](/reference/pagination) for details on how to iterate through a results list.

### Rollup Properties

> 👍 Learn more about rollup properties on the [Page properties page](/reference/page-property-values#rollup) or in Notion’s [Help Center](https://www.notion.so/help/relations-and-rollups).

For regular "Show original" rollups, the endpoint returns a flattened list of all the property items in the rollup.

For rollups with an aggregation, the API returns a [rollup property value](/reference/page#rollup-property-values) under the `rollup` key and the list of relations.

In order to avoid timeouts, if the rollup has a large number of aggregations or properties, the endpoint returns a `next_cursor` value that is used to determine the aggregation value _so far_ for the subset of relations that have been paginated through.

Once `has_more` is `false`, then the final rollup value is returned. Refer to the [Pagination documentation](/reference/pagination) for more information on pagination in the Notion API.

Computing the values of following aggregations are _not_ supported. Instead the endpoint returns a list of `property_item` objects for the rollup:

- `show_unique` (Show unique values)
- `unique` (Count unique values)
- `median`(Median)

> 📘 Integration capabilities
> 
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

### Errors

Returns a 404 HTTP response if the page or property doesn't exist, or if the integration doesn't have access to the page.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
```