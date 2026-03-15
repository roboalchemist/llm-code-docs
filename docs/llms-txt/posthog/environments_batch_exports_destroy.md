# Source: https://posthog.com/docs/open-api-spec/environments_batch_exports_destroy.md

# environments_batch_exports_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/batch_exports/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/batch_exports/{id}/": {
      "delete": {
        "operationId": "environments_batch_exports_destroy",
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
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this batch export.",
            "required": true
          }
        ],
        "tags": [
          "batch_exports",
          "batch_exports"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "batch_export:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  }
}
```
