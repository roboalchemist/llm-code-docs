# Source: https://posthog.com/docs/open-api-spec/environments_file_system_destroy.md

# environments_file_system_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/file_system/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/file_system/{id}/": {
      "delete": {
        "operationId": "environments_file_system_destroy",
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
            "description": "A UUID string identifying this file system.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "file_system"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "file_system:write"
            ]
          }
        ],
        "responses": {
          "204": {
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
