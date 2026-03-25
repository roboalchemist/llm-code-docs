# Source: https://posthog.com/docs/open-api-spec/query_check_auth_for_async_create.md

# query_check_auth_for_async_create

## OpenAPI

```json POST /api/projects/{project_id}/query/check_auth_for_async/
{
  "paths": {
    "/api/projects/{project_id}/query/check_auth_for_async/": {
      "post": {
        "operationId": "query_check_auth_for_async_create",
        "parameters": [
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
        "x-explicit-tags": []
      }
    }
  }
}
```
