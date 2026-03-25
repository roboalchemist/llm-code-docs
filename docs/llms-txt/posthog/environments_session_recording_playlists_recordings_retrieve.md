# Source: https://posthog.com/docs/open-api-spec/environments_session_recording_playlists_recordings_retrieve.md

# environments_session_recording_playlists_recordings_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/session_recording_playlists/{short_id}/recordings/
{
  "paths": {
    "/api/environments/{environment_id}/session_recording_playlists/{short_id}/recordings/": {
      "get": {
        "operationId": "environments_session_recording_playlists_recordings_retrieve",
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "session_recording_playlist:read"
            ]
          }
        ],
        "responses": {
          "200": {
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
