# Source: https://posthog.com/docs/open-api-spec/environments_session_recording_playlists_destroy.md

# environments_session_recording_playlists_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/session_recording_playlists/{short_id}/
{
  "paths": {
    "/api/environments/{environment_id}/session_recording_playlists/{short_id}/": {
      "delete": {
        "operationId": "environments_session_recording_playlists_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
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
              "session_recording_playlist:write"
            ]
          }
        ],
        "responses": {
          "405": {
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
