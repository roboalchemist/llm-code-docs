# Source: https://posthog.com/docs/open-api-spec/environments_file_system_shortcut_destroy.md

# environments_file_system_shortcut_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/file_system_shortcut/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/file_system_shortcut/{id}/": {
      "delete": {
        "operationId": "environments_file_system_shortcut_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this file system shortcut.",
            "required": true
          }
        ],
        "tags": [
          "file_system_shortcut"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "file_system_shortcut:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
