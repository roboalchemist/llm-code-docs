# Source: https://developers.notion.com/reference/intro

The reference is your key to a comprehensive understanding of the Notion API.
Integrations use the API to access Notion's pages, databases, and users. Integrations can connect services to Notion and build interactive experiences for users within Notion. Using the navigation on the left, you'll find details for objects and endpoints used in the API.
> ## 📘
> You need an integration token to interact with the Notion API. You can find an integration token after you create an integration on the integration settings page. If this is your first look at the Notion API, we recommend beginning with the [Getting started guide](https://developers.notion.com/docs/getting-started) to learn how to create an integration. 
> If you want to work on a specific integration, but can't access the token, confirm that you are an admin in the associated workspace. You can check inside the Notion UI via `Settings & Members` in the left sidebar. If you're not an admin in any of your workspaces, you can create a personal workspace for free.
## [](https://developers.notion.com/reference/intro#conventions)
The base URL to send all API requests is `https://api.notion.com`. HTTPS is required for all API requests.
The Notion API follows RESTful conventions when possible, with most operations performed via `GET`, `POST`, `PATCH`, and `DELETE` requests on page and database resources. Request and response bodies are encoded as JSON.
### [](https://developers.notion.com/reference/intro#json-conventions)
  * Top-level resources have an `"object"` property. This property can be used to determine the type of the resource (e.g. `"database"`, `"user"`, etc.)
  * Top-level resources are addressable by a UUIDv4 `"id"` property. You may omit dashes from the ID when making requests to the API, e.g. when copying the ID from a Notion URL.
  * Property names are in `snake_case` (not `camelCase` or `kebab-case`).
  * Temporal values (dates and datetimes) are encoded in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) strings. Datetimes will include the time value (`2020-08-12T02:12:33.231Z`) while dates will include only the date (`2020-08-12`)
  * The Notion API does not support empty strings. To unset a string value for properties like a `url` [Property value object](https://developers.notion.com/reference/property-value-object), for example, use an explicit `null` instead of `""`.


## [](https://developers.notion.com/reference/intro#code-samples--sdks)
Samples requests and responses are shown for each endpoint. Requests are shown using the Notion [JavaScript SDK](https://github.com/makenotion/notion-sdk-js), and [cURL](https://curl.se/). These samples make it easy to copy, paste, and modify as you build your integration. 
Notion SDKs are open source projects that you can install to easily start building. You may also choose any other language or library that allows you to make HTTP requests.
## [](https://developers.notion.com/reference/intro#pagination)
Endpoints that return lists of objects support cursor-based pagination requests. By default, Notion returns ten items per API call. If the number of items in a response from a support endpoint exceeds the default, then an integration can use pagination to request a specific set of the results and/or to limit the number of returned items.
### [](https://developers.notion.com/reference/intro#supported-endpoints)
HTTP method | Endpoint  
---|---  
GET | [List all users](https://developers.notion.com/reference/get-users)  
GET | [Retrieve block children](https://developers.notion.com/reference/get-block-children)  
GET | [Retrieve a comment](https://developers.notion.com/reference/retrieve-a-comment)  
GET | [Retrieve a page property item](https://developers.notion.com/reference/retrieve-a-page-property)  
POST | [Query a database](https://developers.notion.com/reference/post-database-query)  
POST | [Search](https://developers.notion.com/reference/post-search)  
### [](https://developers.notion.com/reference/intro#responses)
If an endpoint supports pagination, then the response object contains the below fields. 
Field | Type | Description  
---|---|---  
`has_more` | `boolean` | Whether the response includes the end of the list. `false` if there are no more results. Otherwise, `true`.  
`next_cursor` | `string` | A string that can be used to retrieve the next page of results by passing the value as the `start_cursor` [parameter](https://developers.notion.com/reference/intro#parameters-for-paginated-requests) to the same endpoint.  
  
Only available when `has_more` is true.  
`object` | `"list"` | The constant string `"list"`.  
`results` | `array of objects` | The list, or partial list, of endpoint-specific results. Refer to a [supported endpoint](https://developers.notion.com/reference/intro#supported-endpoints)'s individual documentation for details.  
`type` |  `"block"`  
  
`"comment"`  
  
`"database"`  
  
`"page"`  
  
`"page_or_database"`  
  
`"property_item"`  
  
`"user"` | A constant string that represents the type of the objects in `results`.  
`{type}` | [`paginated list object`](https://developers.notion.com/reference/page-property-values#paginated-page-properties) | An object containing type-specific pagination information. For `property_item`s, the value corresponds to the [paginated page property type](https://developers.notion.com/reference/page-property-values#paginated-page-properties). For all other types, the value is an empty object.  
### [](https://developers.notion.com/reference/intro#parameters-for-paginated-requests)
> ## 🚧
> Parameter location varies by endpoint
> `GET` requests accept parameters in the query string. 
> `POST` requests receive parameters in the request body.
Parameter | Type | Description  
---|---|---  
`page_size` | `number` | The number of items from the full list to include in the response.  
  
**Default** : `100`  
**Maximum** : `100`  
  
The response may contain fewer than the default number of results.  
`start_cursor` | `string` | A `next_cursor` value returned in a previous [response](https://developers.notion.com/reference/intro#responses). Treat this as an opaque value.  
  
Defaults to `undefined`, which returns results from the beginning of the list.  
### [](https://developers.notion.com/reference/intro#how-to-send-a-paginated-request)
  1. Send an initial request to the [supported endpoint](https://dev.notion.so/Review-Pagination-documentation-e48701d7465444c7ad79237914aa47cd).
  2. Retrieve the `next_cursor` value from the response (only available when `has_more` is `true`). 
  3. Send a follow up request to the endpoint that includes the `next_cursor` param in either the query string (for `GET` requests) or in the body params (`POST` requests).


#### [](https://developers.notion.com/reference/intro#example-request-the-next-set-of-query-results-from-a-database)
cURL
```
curl --location --request POST 'https://api.notion.com/v1/databases/<database_id>/query' \
--header 'Authorization: Bearer <secret_bot>' \
--header 'Content-Type: application/json' \
--data '{
    "start_cursor": "33e19cb9-751f-4993-b74d-234d67d0d534"
}'

```

