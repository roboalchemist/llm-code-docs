# Source: https://posthog.com/docs/open-api-spec/batch_exports_test_retrieve.md

# batch_exports_test_retrieve

## OpenAPI

```json GET /api/organizations/{organization_id}/batch_exports/test/
{
  "paths": {
    "/api/organizations/{organization_id}/batch_exports/test/": {
      "get": {
        "operationId": "batch_exports_test_retrieve",
        "parameters": [
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
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  }
}
```
