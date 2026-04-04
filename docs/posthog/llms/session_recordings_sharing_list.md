# Source: https://posthog.com/docs/open-api-spec/session_recordings_sharing_list.md

# session_recordings_sharing_list

## OpenAPI

```json GET /api/projects/{project_id}/session_recordings/{recording_id}/sharing/
{
  "paths": {
    "/api/projects/{project_id}/session_recordings/{recording_id}/sharing/": {
      "get": {
        "operationId": "session_recordings_sharing_list",
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
              "sharing_configuration:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/SharingConfiguration"
                  }
                }
              }
            },
            "description": ""
          }
        },
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
