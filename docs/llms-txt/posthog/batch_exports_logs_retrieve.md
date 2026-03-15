# Source: https://posthog.com/docs/open-api-spec/batch_exports_logs_retrieve.md

# batch_exports_logs_retrieve

## OpenAPI

```json GET /api/organizations/{organization_id}/batch_exports/{id}/logs/
{
  "paths": {
    "/api/organizations/{organization_id}/batch_exports/{id}/logs/": {
      "get": {
        "operationId": "batch_exports_logs_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this batch export.",
            "required": true
          },
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "batch_exports",
          "batch_exports"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  }
}
```
