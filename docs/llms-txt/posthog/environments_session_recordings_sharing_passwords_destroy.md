# Source: https://posthog.com/docs/open-api-spec/environments_session_recordings_sharing_passwords_destroy.md

# environments_session_recordings_sharing_passwords_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/session_recordings/{recording_id}/sharing/passwords/{password_id}/
{
  "paths": {
    "/api/environments/{environment_id}/session_recordings/{recording_id}/sharing/passwords/{password_id}/": {
      "delete": {
        "operationId": "environments_session_recordings_sharing_passwords_destroy",
        "description": "Delete a password from the sharing configuration.",
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
            "name": "password_id",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "recording_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "session_recordings"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "sharing_configuration:write"
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
          "core"
        ]
      }
    }
  }
}
```
