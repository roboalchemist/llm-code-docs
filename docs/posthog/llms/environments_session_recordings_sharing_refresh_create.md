# Source: https://posthog.com/docs/open-api-spec/environments_session_recordings_sharing_refresh_create.md

# environments_session_recordings_sharing_refresh_create

## OpenAPI

```json POST /api/environments/{environment_id}/session_recordings/{recording_id}/sharing/refresh/
{
  "paths": {
    "/api/environments/{environment_id}/session_recordings/{recording_id}/sharing/refresh/": {
      "post": {
        "operationId": "environments_session_recordings_sharing_refresh_create",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SharingConfiguration"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SharingConfiguration"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SharingConfiguration"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "sharing_configuration:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SharingConfiguration"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "SharingConfiguration": {
        "type": "object",
        "properties": {
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "enabled": {
            "type": "boolean"
          },
          "access_token": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "settings": {
            "nullable": true
          },
          "password_required": {
            "type": "boolean"
          },
          "share_passwords": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "access_token",
          "created_at",
          "share_passwords"
        ]
      }
    }
  }
}
```
