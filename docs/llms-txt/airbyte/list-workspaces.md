# Source: https://docs.airbyte.com/ai-agents/api/api-reference/list-workspaces.md

# List Workspaces

```
GET 
/api/v1/workspaces
```

List external users for the authenticated organization with cursor-based pagination.

* **name\_contains**: Optional filter by external user name (case-insensitive partial match)
* **status**: Optional filter by external user status (active or inactive). If not specified, returns all external users.
* **limit**: Maximum number of external users to return (default: 20, max: 100)
* **cursor**: Pagination cursor from previous response's `next` URL
* **next**: URL for next page (null if no more results)

## Request[​](#request "Direct link to request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 403
* 422
* 500

Successful Response

Bad request

Forbidden

Unprocessable entity

Internal server error
