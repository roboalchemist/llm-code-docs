# Source: https://posthog.com/docs/open-api-spec/batch_exports_destroy_2.md

# batch_exports_destroy_2

## OpenAPI

```json DELETE /api/projects/{project_id}/batch_exports/{id}/
{
  "paths": {
    "/api/projects/{project_id}/batch_exports/{id}/": {
      "delete": {
        "operationId": "batch_exports_destroy_2",
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
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
