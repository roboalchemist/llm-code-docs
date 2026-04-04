# Source: https://posthog.com/docs/open-api-spec/session_recording_playlists_recordings_retrieve.md

# session_recording_playlists_recordings_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/
{
  "paths": {
    "/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/": {
      "get": {
        "operationId": "session_recording_playlists_recordings_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  }
}
```
