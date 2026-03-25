# Source: https://posthog.com/docs/open-api-spec/file_system_unfiled_retrieve.md

# file_system_unfiled_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/file_system/unfiled/
{
  "paths": {
    "/api/projects/{project_id}/file_system/unfiled/": {
      "get": {
        "operationId": "file_system_unfiled_retrieve",
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
          "core",
          "file_system"
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
