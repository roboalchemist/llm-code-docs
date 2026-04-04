# Source: https://posthog.com/docs/open-api-spec/environments_query_draft_sql_retrieve.md

# environments_query_draft_sql_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/query/draft_sql/
{
  "paths": {
    "/api/environments/{environment_id}/query/draft_sql/": {
      "get": {
        "operationId": "environments_query_draft_sql_retrieve",
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
