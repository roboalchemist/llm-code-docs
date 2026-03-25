# Source: https://pipedream.com/docs/rest-api/overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Use the REST API to create workflows, manage event sources, handle subscriptions, and more.

<Note>
  Looking for the Pipedream Connect API? [Go here](/connect/api-reference/introduction).
</Note>

## Base URL

All API requests should be made to:

```
https://api.pipedream.com/v1
```

## Authentication

All requests to the Pipedream API must be authenticated. Read more about [authentication here](/rest-api/auth).

## Required Headers

All API requests must include:

* **Authorization**: Bearer token (required on all endpoints)
* **Content-Type**: `application/json` (required for POST and PUT requests with JSON payloads)

Example:

```bash  theme={null}
curl https://api.pipedream.com/v1/users/me \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json"
```

## Common Parameters

The following parameters are available on many endpoints:

* **`include`**: Specify fields to include in the response
* **`exclude`**: Specify fields to exclude from the response
* **`org_id`**: Workspace ID (required only when using User API keys to specify which workspace to operate in; not needed with OAuth tokens)

## Pagination

List endpoints return paginated results with a default page size of 10 items.

### Parameters

* **`limit`**: Number of items per page (1-100, default: 10)
* **`after`**: Cursor for next page
* **`before`**: Cursor for previous page

### Example Response

```json  theme={null}
{
  "page_info": {
    "total_count": 100,
    "count": 10,
    "start_cursor": "ZXhhbXBsZSBjdXJzb3I",
    "end_cursor": "ZXhhbXBsZSBjdXJzb3I"
  },
  "data": [...]
}
```

## Errors

The API uses standard HTTP response codes:

* **2xx**: Success
* **4xx**: Client error (bad request, unauthorized, not found, etc.)
* **5xx**: Server error

Error responses include a JSON body with details about what went wrong.

Built with [Mintlify](https://mintlify.com).
