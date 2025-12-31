# Source: https://developers.notion.com/reference/intro.md

# Notion API

## Introduction
[Introduction](https://docs.notion.so/reference/intro)

## Integration capabilities
[Integration capabilities](https://docs.notion.so/reference/capabilities)

## Webhooks
[Webhooks](https://docs.notion.so/reference/webhooks)
- [Event types & delivery](https://docs.notion.so/reference/webhooks-events-delivery)

## Request limits
[Request limits](https://docs.notion.so/reference/request-limits)

## Status codes
[Status codes](https://docs.notion.so/reference/status-codes)

## Versioning
[Versioning](https://docs.notion.so/reference/versioning)
- [Changes by version](https://docs.notion.so/reference/changes-by-version)

## Objects

### Block
[Block](https://docs.notion.so/reference/block)
- [Rich text](https://docs.notion.so/reference/rich-text)

### Page
[Page](https://docs.notion.so/reference/page)
- [Page properties](https://docs.notion.so/reference/page-property-values)
  - [Page property items](https://docs.notion.so/reference/property-item-object)

### Database
[Database](https://docs.notion.so/reference/database)

### Data source
[Data source](https://docs.notion.so/reference/data-source)
- [Data source properties](https://docs.notion.so/reference/property-object)

### Comment
[Comment](https://docs.notion.so/reference/comment-object)
- [Comment attachment](https://docs.notion.so/reference/comment-attachment)
- [Comment display name](https://docs.notion.so/reference/comment-display-name)

### File
[File](https://docs.notion.so/reference/file-object)
- [File Upload](https://docs.notion.so/reference/file-upload)

### User
[User](https://docs.notion.so/reference/user)

### Parent
[Parent](https://docs.notion.so/reference/parent-object)

### Emoji
[Emoji](https://docs.notion.so/reference/emoji-object)

### Unfurl attribute (Link Previews)
[Unfurl attribute (Link Previews)](https://docs.notion.so/reference/unfurl-attribute-object)

## Endpoints

### Authentication
[Authentication](https://docs.notion.so/reference/authentication)
- [Create a token](https://docs.notion.so/reference/create-a-token) (post)
- [Introspect token](https://docs.notion.so/reference/introspect-token) (post)
- [Revoke token](https://docs.notion.so/reference/revoke-token) (post)
- [Refresh a token](https://docs.notion.so/reference/refresh-a-token) (post)

### Blocks
[Blocks](https://docs.notion.so/reference/patch-block-children)
- [Append block children](https://docs.notion.so/reference/patch-block-children) (patch)
- [Retrieve a block](https://docs.notion.so/reference/retrieve-a-block) (get)
- [Retrieve block children](https://docs.notion.so/reference/get-block-children) (get)
- [Update a block](https://docs.notion.so/reference/update-a-block) (patch)
- [Delete a block](https://docs.notion.so/reference/delete-a-block) (del)

### Pages
[Pages](https://docs.notion.so/reference/post-page)
- [Create a page](https://docs.notion.so/reference/post-page) (post)
- [Retrieve a page](https://docs.notion.so/reference/retrieve-a-page) (get)
- [Retrieve a page property item](https://docs.notion.so/reference/retrieve-a-page-property) (get)
- [Update page](https://docs.notion.so/reference/patch-page)
  - [Trash a page](https://docs.notion.so/reference/archive-a-page)

### Databases
[Databases](https://docs.notion.so/reference/database-create)
- [Create a database](https://docs.notion.so/reference/database-create) (post)
- [List databases](https://docs.notion.so/reference/list-databases) (get)
- [Get database properties](https://docs.notion.so/reference/get-database-properties) (get)
- [Update database properties](https://docs.notion.so/reference/update-database-properties) (patch)
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

# Introduction

The reference is your key to a comprehensive understanding of the Notion API.

Integrations use the API to access Notion's pages, databases, and users. Integrations can connect services to Notion and build interactive experiences for users within Notion. Using the navigation on the left, you'll find details for objects and endpoints used in the API.

> 📘
> 
> You need an integration token to interact with the Notion API. You can find an integration token after you create an integration on the integration settings page. If this is your first look at the Notion API, we recommend beginning with the [Getting started guide](/docs/getting-started) to learn how to create an integration.
> 
> If you want to work on a specific integration, but can't access the token, confirm that you are an admin in the associated workspace. You can check inside the Notion UI via `Settings & Members` in the left sidebar. If you're not an admin in any of your workspaces, you can create a personal workspace for free.

## Conventions

The base URL to send all API requests is `https://api.notion.com`. HTTPS is required for all API requests.

The Notion API follows RESTful conventions when possible, with most operations performed via `GET`, `POST`, `PATCH`, and `DELETE` requests on page and database resources. Request and response bodies are encoded as JSON.

### JSON conventions

- Top-level resources have an `"object"` property. This property can be used to determine the type of the resource (e.g., `"database"`, `"user"`, etc.)
- Top-level resources are addressable by a UUIDv4 `"id"` property. You may omit dashes from the ID when making requests to the API, e.g., when copying the ID from a Notion URL.
- Property names are in `snake_case` (not `camelCase` or `kebab-case`).
- Temporal values (dates and datetimes) are encoded in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) strings. Datetimes will include the time value (`2020-08-12T02:12:33.231Z`) while dates will include only the date (`2020-08-12`)
- The Notion API does not support empty strings. To unset a string value for properties like a `url` [Property value object](/reference/property-value-object), for example, use an explicit `null` instead of `""`.

## Code samples & SDKs

Samples requests and responses are shown for each endpoint. Requests are shown using the Notion [JavaScript SDK](https://github.com/makenotion/notion-sdk-js), and [cURL](https://curl.se/). These samples make it easy to copy, paste, and modify as you build your integration.

Notion SDKs are open source projects that you can install to easily start building. You may also choose any other language or library that allows you to make HTTP requests.

## Pagination

Endpoints that return lists of objects support cursor-based pagination requests. By default, Notion returns ten items per API call. If the number of items in a response from a support endpoint exceeds the default, then an integration can use pagination to request a specific set of the results and/or to limit the number of returned items.

### Supported endpoints

| HTTP method | Endpoint |
| --- | --- |
| GET | [List all users](/reference/get-users) |
| GET | [Retrieve block children](/reference/get-block-children) |
| GET | [Retrieve a comment](/reference/retrieve-a-comment) |
| GET | [Retrieve a page property item](/reference/retrieve-a-page-property) |
| POST | [Query a database](/reference/post-database-query) |
| POST | [Search](/reference/post-search) |

### Responses

If an endpoint supports pagination, then the response object contains the below fields.

| Field | Type | Description |
| --- | --- | --- |
| `has_more` | `boolean` | Whether the response includes the end of the list. `false` if there are no more results. Otherwise, `true`. |
| `next_cursor` | `string` | A string that can be used to retrieve the next page of results by passing the value as the `start_cursor` parameter to the same endpoint. Only available when `has_more` is true. |
| `"list"` | `"list"` | The constant string `"list"`. |
| `results` | `array of objects` | The list, or partial list, of endpoint-specific results. Refer to a [supported endpoint](#supported-endpoints)'s individual documentation for details. |
| `"type"` | `"block"`, `"comment"`, `"database"`, `"page"`, `"page_or_database"`, `"property_item"`, `"user"` | A constant string that represents the type of the objects in `results`. |
| `{type}` | [paginated list object](/reference/page-property-values#paginated-page-properties) | An object containing type-specific pagination information. For `property_item`s, the value corresponds to the [paginated page property type](/reference/page-property-values#paginated-page-properties). For all other types, the value is an empty object. |

### Parameters for paginated requests

> 🚧Parameter location varies by endpoint
> 
> `GET` requests accept parameters in the query string.
> 
> `POST` requests receive parameters in the request body.
```

# HTTP Response Headers

When you make a request to a Notion API endpoint, Notion returns some metadata about the result set to your client. This metadata is contained within the headers of the response.

## Conventions

### JSON conventions

Notion uses a specific JSON structure to represent responses from its APIs. For details on this structure, see [HTTP Response Metadata](https://dev.notion.so/API-reference/reply).

## Code samples & SDKs

## Pagination

### Supported endpoints

| Endpoint | Description |
| --- | --- |
| `GET /v1/databases/&lt;database_id&gt;/query` | Returns a list of databases associated with the specified database. The response includes a `next_cursor` field if there are more records. |
| `GET /v1/databases/&lt;database_id&gt;/query?start=33e19cb9-751f-4993-b74d-234d67d0d534` | Returns a subset of the records starting from the record identified by the `start_cursor`. The response includes a `next_cursor` field if there are more records. |

### Responses

| Status code | Response | Description |
| --- | --- | --- |
| 200 | OK | The request was successful. The response includes a `next_cursor` field if there are more records. |
| 400 | Bad Request | The request was not valid. |
| 401 | Unauthorized | The request requires authentication. |
| 403 | Forbidden | The user does not have access to the requested resource. |
| 422 | Unprocessable Entity | The request body was invalid. |

### Parameters for paginated requests

The `next_cursor` parameter can be included in the request body or query string to indicate the position in the list of where the next page of results should start.

#### Example: request the next set of query results from a database

**cURL**

```bash
curl --location --request POST 'https://api.notion.com/v1/databases/<database_id>/query' \
--header 'Authorization: Bearer <secret_bot>' \
--header 'Content-Type: application/json' \
--data '{
    "start_cursor": "33e19cb9-751f-4993-b74d-234d67d0d534"
}'
```

### How to send a paginated request

1. Send an initial request to the [supported endpoint](https://dev.notion.so/Review-Pagination-documentation-e48701d7465444c7ad79237914aa47cd).
2. Retrieve the `next_cursor` value from the response (only available when `has_more` is `true`).
3. Send a follow up request to the endpoint that includes the `next_cursor` param in either the query string (for `GET` requests) or in the body params (`POST` requests).
```