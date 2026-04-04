# Source: https://posthog.com/docs/open-api-spec/batch_exports_test_retrieve_2.md

# batch_exports_test_retrieve_2

## OpenAPI

```json GET /api/projects/{project_id}/batch_exports/test/
{
  "paths": {
    "/api/projects/{project_id}/batch_exports/test/": {
      "get": {
        "operationId": "batch_exports_test_retrieve_2",
        "parameters": [
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
