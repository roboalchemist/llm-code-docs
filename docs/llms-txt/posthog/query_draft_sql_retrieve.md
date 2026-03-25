# Source: https://posthog.com/docs/open-api-spec/query_draft_sql_retrieve.md

# query_draft_sql_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/query/draft_sql/
{
  "paths": {
    "/api/projects/{project_id}/query/draft_sql/": {
      "get": {
        "operationId": "query_draft_sql_retrieve",
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
