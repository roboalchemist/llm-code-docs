# Source: https://posthog.com/docs/open-api-spec/file_system_log_view_retrieve.md

# file_system_log_view_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/file_system/log_view/
{
  "paths": {
    "/api/projects/{project_id}/file_system/log_view/": {
      "get": {
        "operationId": "file_system_log_view_retrieve",
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
