# Source: https://posthog.com/docs/open-api-spec/session_recording_playlists_recordings_destroy.md

# session_recording_playlists_recordings_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/
{
  "paths": {
    "/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/": {
      "delete": {
        "operationId": "session_recording_playlists_recordings_destroy",
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
        "x-explicit-tags": [
          "replay"
        ]
      }
    }
  }
}
```
