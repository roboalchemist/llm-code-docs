# Source: https://posthog.com/docs/open-api-spec/environments_file_system_shortcut_partial_update.md

# environments_file_system_shortcut_partial_update

## OpenAPI

```json PATCH /api/environments/{environment_id}/file_system_shortcut/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/file_system_shortcut/{id}/": {
      "patch": {
        "operationId": "environments_file_system_shortcut_partial_update",
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
            "description": "A UUID string identifying this file system shortcut.",
            "required": true
          }
        ],
        "tags": [
          "file_system_shortcut"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedFileSystemShortcut"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedFileSystemShortcut"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedFileSystemShortcut"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "file_system_shortcut:write"
            ]
          }
        ],
        "responses": {
          "200": {
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
      "PatchedFileSystemShortcut": {
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
        }
      },
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
