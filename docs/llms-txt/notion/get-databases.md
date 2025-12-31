# Source: https://developers.notion.com/reference/get-databases.md

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

# List databases (deprecated)

[post](https://docs.rapidapi.com/reference/get-databases)

## Create databases

[post](https://docs.rapidapi.com/reference/create-a-database)
[patch](https://docs.rapidapi.com/reference/update-a-database)

## Update databases

[patch](https://docs.rapidapi.com/reference/update-a-database)
[get](https://docs.rapidapi.com/reference/retrieve-a-database)

## Filter databases

[post](https://docs.rapidapi.com/reference/post-database-query)
[filter](https://docs.rapidapi.com/reference/post-database-query-filter)

## Sort databases

[post](https://docs.rapidapi.com/reference/post-database-query)
[sort](https://docs.rapidapi.com/reference/post-database-query-sort)

## Retrieve databases

[get](https://docs.rapidapi.com/reference/retrieve-a-database)

## Get databases (deprecated)

[get](https://docs.rapidapi.com/reference/get-databases)
```

# List databases (deprecated)

> ❗️Search pages for more details
>
> This endpoint is deprecated and is only available on API version "2021-08-16" and earlier. Use the [Search API](/reference/post-search) instead. This endpoint will only return explicitly shared databases, while search will also return child pages. This endpoint's results cannot be filtered, while search can be used to match on page title.

List all [Databases](/reference/database) shared with the authenticated integration. The response may contain fewer than `page_size` of results.

> 📘Database access
>
> Integrations can only access databases a user has shared with the integration.

See [Pagination](/reference/pagination) for details about how to use a cursor to iterate through the list.

> 📘Integration capabilities
>
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

## Errors

Returns a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
```