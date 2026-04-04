# Source: https://posthog.com/docs/open-api-spec/environments_persisted_folder_destroy.md

# environments_persisted_folder_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/persisted_folder/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/persisted_folder/{id}/": {
      "delete": {
        "operationId": "environments_persisted_folder_destroy",
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
            "description": "A UUID string identifying this Persisted Folder.",
            "required": true
          }
        ],
        "tags": [
          "persisted_folder"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "persisted_folder:write"
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
