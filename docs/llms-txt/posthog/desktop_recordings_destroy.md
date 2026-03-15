# Source: https://posthog.com/docs/open-api-spec/desktop_recordings_destroy.md

# desktop_recordings_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/desktop_recordings/{id}/
{
  "paths": {
    "/api/environments/{project_id}/desktop_recordings/{id}/": {
      "delete": {
        "operationId": "desktop_recordings_destroy",
        "description": "RESTful API for managing desktop meeting recordings.\n\nStandard CRUD operations plus transcript management as a subresource.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this desktop recording.",
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
          "desktop_recordings",
          "desktop_recordings"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "desktop_recording:write"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "desktop_recording:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "desktop_recordings"
        ]
      }
    }
  }
}
```
