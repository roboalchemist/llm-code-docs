# Source: https://posthog.com/docs/open-api-spec/environments_exports_content_retrieve.md

# environments_exports_content_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/exports/{id}/content/
{
  "paths": {
    "/api/environments/{environment_id}/exports/{id}/content/": {
      "get": {
        "operationId": "environments_exports_content_retrieve",
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
              "type": "integer"
            },
            "description": "A unique integer value identifying this exported asset.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "exports"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "export:read"
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
          "core"
        ]
      }
    }
  }
}
```
