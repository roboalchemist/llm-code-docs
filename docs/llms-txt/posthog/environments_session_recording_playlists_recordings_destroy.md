# Source: https://posthog.com/docs/open-api-spec/environments_session_recording_playlists_recordings_destroy.md

# environments_session_recording_playlists_recordings_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/
{
  "paths": {
    "/api/environments/{environment_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/": {
      "delete": {
        "operationId": "environments_session_recording_playlists_recordings_destroy",
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
            "name": "session_recording_id",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "short_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "replay",
          "session_recording_playlists"
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
