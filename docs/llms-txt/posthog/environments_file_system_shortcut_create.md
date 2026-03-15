# Source: https://posthog.com/docs/open-api-spec/environments_file_system_shortcut_create.md

# environments_file_system_shortcut_create

## OpenAPI

```json POST /api/environments/{environment_id}/file_system_shortcut/
{
  "paths": {
    "/api/environments/{environment_id}/file_system_shortcut/": {
      "post": {
        "operationId": "environments_file_system_shortcut_create",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "file_system_shortcut"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FileSystemShortcut"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/FileSystemShortcut"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/FileSystemShortcut"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "file_system_shortcut:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FileSystemShortcut"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "FileSystemShortcut": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "path": {
            "type": "string"
          },
          "type": {
            "type": "string",
            "maxLength": 100
          },
          "ref": {
            "type": "string",
            "nullable": true,
            "maxLength": 100
          },
          "href": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "id",
          "path"
        ]
      }
    }
  }
}
```
