# Source: https://posthog.com/docs/open-api-spec/environments_query_destroy.md

# environments_query_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/query/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/query/{id}/": {
      "delete": {
        "operationId": "environments_query_destroy",
        "description": "(Experimental)",
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "Query cancelled"
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
