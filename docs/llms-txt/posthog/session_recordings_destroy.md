# Source: https://posthog.com/docs/open-api-spec/session_recordings_destroy.md

# session_recordings_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/session_recordings/{id}/
{
  "paths": {
    "/api/projects/{project_id}/session_recordings/{id}/": {
      "delete": {
        "operationId": "session_recordings_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this session recording.",
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
          "replay",
          "session_recordings"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "session_recording:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  }
}
```
