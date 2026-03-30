# Source: https://posthog.com/docs/open-api-spec/persisted_folder_destroy.md

# persisted_folder_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/persisted_folder/{id}/
{
  "paths": {
    "/api/projects/{project_id}/persisted_folder/{id}/": {
      "delete": {
        "operationId": "persisted_folder_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this Persisted Folder.",
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
        "x-explicit-tags": []
      }
    }
  }
}
```
