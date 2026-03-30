# Source: https://posthog.com/docs/open-api-spec/environments_batch_exports_test_retrieve.md

# environments_batch_exports_test_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/batch_exports/test/
{
  "paths": {
    "/api/environments/{environment_id}/batch_exports/test/": {
      "get": {
        "operationId": "environments_batch_exports_test_retrieve",
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
          "batch_exports",
          "batch_exports"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "INTERNAL"
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
          "batch_exports"
        ]
      }
    }
  }
}
```
