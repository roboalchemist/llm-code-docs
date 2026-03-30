# Source: https://posthog.com/docs/open-api-spec/environments_query_log_retrieve.md

# environments_query_log_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/query/{id}/log/
{
  "paths": {
    "/api/environments/{environment_id}/query/{id}/log/": {
      "get": {
        "operationId": "environments_query_log_retrieve",
        "description": "Get query log details from query_log_archive table for a specific query_id, the query must have been issued in last 24 hours.",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true
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
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
