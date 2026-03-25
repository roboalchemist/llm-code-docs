# Source: https://posthog.com/docs/open-api-spec/batch_exports_destroy.md

# batch_exports_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/batch_exports/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/batch_exports/{id}/": {
      "delete": {
        "operationId": "batch_exports_destroy",
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
        "x-explicit-tags": [
          "batch_exports"
        ]
      }
    }
  }
}
```
