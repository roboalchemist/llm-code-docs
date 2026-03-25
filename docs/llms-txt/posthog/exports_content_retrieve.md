# Source: https://posthog.com/docs/open-api-spec/exports_content_retrieve.md

# exports_content_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/exports/{id}/content/
{
  "paths": {
    "/api/projects/{project_id}/exports/{id}/content/": {
      "get": {
        "operationId": "exports_content_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this exported asset.",
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
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
