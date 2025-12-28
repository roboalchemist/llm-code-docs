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

# Request limits

To ensure a consistent developer experience for all API users, the Notion API is rate limited and basic size limits apply to request parameters.

## Rate limits

Rate-limited requests will return a `"rate_limited"` error code (HTTP response status 429). **The rate limit for incoming requests per integration is an average of three requests per second.** Some bursts beyond the average rate are allowed.

Integrations should accommodate variable rate limits by handling HTTP 429 responses and respecting the Retry-After response [header value](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html), which is set as an integer number of seconds (in decimal). Requests made after waiting this minimum amount of time should no longer be rate limited.

Alternatively, rate limits can be accommodated by backing off (or slowing down) the speed of future requests. A common way to implement this is using one or several queues for pending requests, which can be consumed by sending requests as long as Notion does not respond with an HTTP 429.

> 🚧Rate limits may change
>
> In the future, Notion plans to adjust rate limits to balance for demand and reliability. Notion may also introduce distinct rate limits for workspaces in different pricing plans.

## Size limits

Notion limits the size of certain parameters, and the depth of children in requests. A requests that exceeds any of these limits will return `"validation_error"` error code (HTTP response status 400) and contain more specific details in the `"message"` property.

Integrations should avoid sending requests beyond these limits proactively. It may be helpful to use test data in your own test suite which intentionally contains large parameters to verify that the errors are handled appropriately. For example, if the integration reads a URL from an external system to put into a Notion page property, the integration should have a plan to deal with URLs that are beyond the length limit of 2000 characters. The integration might choose to log the error, or send an alert to the user who set up the integration via an email, or some other action.

Note that in addition to the property limits below, payloads have a maximum size of 1000 block elements and 500KB overall.

### Limits for property values

| Property value type | Inner property | Size limit |
| --- | --- | --- |
| [Rich text object](/reference/rich-text) | `text.content` | 2000 characters |
| [Rich text object](/reference/rich-text) | `text.link.url` | 2000 characters |
| [Rich text object](/reference/rich-text) | `equation.expression` | 1000 characters |
| Any array of all [block](/reference/block) types, including [rich text objects](/reference/rich-text) |  | 100 elements |
| Any URL |  | 2000 characters |
| Any email |  | 200 characters |
| Any phone number |  | 200 characters |
| Any multi-select |  | 100 options |
| Any relation |  | 100 related pages |
| Any people |  | 100 users |

> 📘Request size limits
>
> These limits apply to requests sent to Notion's API only. There are different limits on the number of relations and people mentions in responses returned by the API.
```