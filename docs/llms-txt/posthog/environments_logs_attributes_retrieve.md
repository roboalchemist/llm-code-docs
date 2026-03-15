# Source: https://posthog.com/docs/open-api-spec/environments_logs_attributes_retrieve.md

# environments_logs_attributes_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/logs/attributes/
{
  "paths": {
    "/api/environments/{environment_id}/logs/attributes/": {
      "get": {
        "operationId": "environments_logs_attributes_retrieve",
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
