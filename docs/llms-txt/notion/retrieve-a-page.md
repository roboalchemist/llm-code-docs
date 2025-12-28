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
- [Update page](/reference/update-page) (PATCH)
  - [Trash a page](/reference/trash-a-page)

### Databases
- [Create a database](/reference/create-database) (POST)
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

# Retrieve a page

> 🚧This endpoint will not accurately return properties that exceed 25 references
>
> Do **not** use this endpoint if a page property includes more than 25 references to receive the full list of references. Instead, use the [Retrieve a page property endpoint](/reference/retrieve-a-page-property) for the specific property to get its complete reference list.

Retrieves a [Page object](/reference/page) using the ID specified.

Responses contain page **properties**, not page content. To fetch page content, use the [Retrieve block children](/reference/get-block-children) endpoint.

Page properties are limited to up to **25 references** per page property. To retrieve data related to properties that have more than 25 references, use the [Retrieve a page property](/reference/retrieve-a-page-property#rollup-properties) endpoint. (See [Limits](/reference/retrieve-a-page#limits) below for additional information.)

## Parent objects: Pages vs. databases

If a page’s [Parent object](/reference/parent-object) is a database, then the property values will conform to the [database property schema](/reference/property-object).

If a page object is not part of a database, then the only property value available for that page is its `title`.

## Limits

The endpoint returns a maximum of 25 page or person references per [page property](/reference/property-value-object). If a page property includes more than 25 references, then the 26th reference and beyond might be returned as `Untitled`, `Anonymous`, or not be returned at all.

This limit affects the following properties:

-   [`people`](/reference/property-value-object#people-property-values): response object can’t be guaranteed to return more than 25 people.
-   [`relation`](/reference/property-value-object#relation-property-values): the `has_more` value of the `relation` in the response object is `true` if a `relation` contains more than 25 related pages. Otherwise, `has_more` is false.
-   [`rich_text`](/reference/property-value-object#rich-text-property-values): response object includes a maximum of 25 populated inline page or person mentions.
-   [`title`](/reference/property-value-object#title-property-values): response object includes a maximum of 25 inline page or person mentions.

> 📘Integration capabilities
>
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

## Errors

Returns a 404 HTTP response if the page doesn't exist, or if the integration doesn't have access to the page.

Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
```