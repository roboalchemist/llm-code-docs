# Source: https://posthog.com/docs/open-api-spec/environments_session_recordings_destroy.md

# environments_session_recordings_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/session_recordings/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/session_recordings/{id}/": {
      "delete": {
        "operationId": "environments_session_recordings_destroy",
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
            "description": "A UUID string identifying this session recording.",
            "required": true
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
        "deprecated": true,
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  }
}
```
