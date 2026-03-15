# Source: https://posthog.com/docs/open-api-spec/environments_file_system_log_view_retrieve.md

# environments_file_system_log_view_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/file_system/log_view/
{
  "paths": {
    "/api/environments/{environment_id}/file_system/log_view/": {
      "get": {
        "operationId": "environments_file_system_log_view_retrieve",
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
          "core",
          "file_system"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
