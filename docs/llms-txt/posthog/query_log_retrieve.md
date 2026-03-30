# Source: https://posthog.com/docs/open-api-spec/query_log_retrieve.md

# query_log_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/query/{id}/log/
{
  "paths": {
    "/api/projects/{project_id}/query/{id}/log/": {
      "get": {
        "operationId": "query_log_retrieve",
        "description": "Get query log details from query_log_archive table for a specific query_id, the query must have been issued in last 24 hours.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true
          },
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
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {},
                  "description": "Unspecified response body"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
