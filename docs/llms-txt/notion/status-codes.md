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

# Status codes

Responses from the API use HTTP response codes to indicate general classes of success and error.

## Success codes

| HTTP status code | Description |
| --- | --- |
| 200 | Notion successfully processed the request. |

## Error codes

Error responses contain more detail about the error in the response body, in the `"code"` and `"message"` properties.

| HTTP status code | `"code"` | Description | `"message"` example |
| --- | --- | --- | --- |
| 400 | `"invalid_json"` | The request body could not be decoded as JSON. | `"Error parsing JSON body."` |
| 400 | `"invalid_request_url"` | The request URL is not valid. | `"Invalid request URL"` |
| 400 | `"invalid_request"` | This request is not supported. | `"Unsupported request: <request name>."` |
| 400 | `"invalid_grant"` | The provided authorization grant (e.g., authorization code, resource owner credentials) or refresh token is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client. See [OAuth 2.0 documentation](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2) for more information. | `"Invalid code: this code has been revoked."` |
| 400 | `"validation_error"` | The request body does not match the schema for the expected parameters. Check the `"message"` property for more details. | `"body failed validation: body.properties should be defined, instead was undefined."` |
| 400 | `"missing_version"` | The request is missing the required `Notion-Version` header. See [Versioning](/reference/versioning). | `"Notion-Version header failed validation: Notion-Version header should be defined, instead was undefined."` |
| 401 | `"unauthorized"` | The bearer token is not valid. | `"API token is invalid."` |
| 403 | `"restricted_resource"` | Given the bearer token used, the client doesn't have permission to perform this operation. | `"API token does not have access to this resource."` |
| 404 | `"object_not_found"` | Given the bearer token used, the resource does not exist. This error can also indicate that the resource has not been shared with owner of the bearer token. | `"Could not find database with ID: be907abe-510e-4116-a3d1-7ea71018c06f. Make sure the relevant pages and databases are shared with your integration."` |
| 409 | `"conflict_error"` | The transaction could not be completed, potentially due to a data collision. Make sure the parameters are up to date and try again.<br/><br/>We also use this HTTP status code in rare cases when our [File Upload](/reference/file-upload) third-party data storage provider has downtime and sending file contents failed. In this case, please retry the request later. | `"Conflict occurred while saving. Please try again."` |
| 429 | `"rate_limited"` | This request exceeds the number of requests allowed. Slow down and try again. [More details on rate limits](/reference/request-limits). | `"You have been rate limited. Please try again in a few minutes."` |
| 500 | `"internal_server_error"` | An unexpected error occurred. Reach out to [Notion support](https://www.notion.so/help). | `"Unexpected error occurred."` |
| 502 | `"bad_gateway"` | Notion encountered an issue while attempting to complete this request (e.g., failed to establish a connection with an upstream server). Please try again. | `"Bad Gateway"` |
| 503 | `"service_unavailable"` | Notion is unavailable. This can occur when the time to respond to a request takes longer than 60 seconds, the maximum request timeout. Please try again later. | `"Notion is unavailable, please try again later."` |
| 503 | `"database_connection_unavailable"` | Notion's database is unavailable or is not in a state that can be queried. Please try again later. | `"Notion is unavailable, please try again later."` |
| 504 | `"gateway_timeout"` | Notion timed out while attempting to complete this request. Please try again later. | `"Gateway Timeout"` |
```