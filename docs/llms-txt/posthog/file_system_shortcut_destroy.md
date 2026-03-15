# Source: https://posthog.com/docs/open-api-spec/file_system_shortcut_destroy.md

# file_system_shortcut_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/file_system_shortcut/{id}/
{
  "paths": {
    "/api/projects/{project_id}/file_system_shortcut/{id}/": {
      "delete": {
        "operationId": "file_system_shortcut_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this file system shortcut.",
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
        "x-explicit-tags": []
      }
    }
  }
}
```
