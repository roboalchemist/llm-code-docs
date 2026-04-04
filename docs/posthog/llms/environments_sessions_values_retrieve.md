# Source: https://posthog.com/docs/open-api-spec/environments_sessions_values_retrieve.md

# environments_sessions_values_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/sessions/values/
{
  "paths": {
    "/api/environments/{environment_id}/sessions/values/": {
      "get": {
        "operationId": "environments_sessions_values_retrieve",
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
          "sessions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
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
