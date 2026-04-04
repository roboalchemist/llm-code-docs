# Source: https://posthog.com/docs/open-api-spec/environments_query_check_auth_for_async_create.md

# environments_query_check_auth_for_async_create

## OpenAPI

```json POST /api/environments/{environment_id}/query/check_auth_for_async/
{
  "paths": {
    "/api/environments/{environment_id}/query/check_auth_for_async/": {
      "post": {
        "operationId": "environments_query_check_auth_for_async_create",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "query"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
