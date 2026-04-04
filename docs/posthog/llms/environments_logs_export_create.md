# Source: https://posthog.com/docs/open-api-spec/environments_logs_export_create.md

# environments_logs_export_create

## OpenAPI

```json POST /api/environments/{environment_id}/logs/export/
{
  "paths": {
    "/api/environments/{environment_id}/logs/export/": {
      "post": {
        "operationId": "environments_logs_export_create",
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
          "logs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "logs:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "logs"
        ]
      }
    }
  }
}
```
