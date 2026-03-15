# Source: https://posthog.com/docs/open-api-spec/environments_file_system_create.md

# environments_file_system_create

## OpenAPI

```json POST /api/environments/{environment_id}/file_system/
{
  "paths": {
    "/api/environments/{environment_id}/file_system/": {
      "post": {
        "operationId": "environments_file_system_create",
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
          "core",
          "file_system"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FileSystem"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/FileSystem"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/FileSystem"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "file_system:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FileSystem"
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
      "FileSystem": {
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
          "depth": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
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
          "meta": {
            "nullable": true
          },
          "shortcut": {
            "type": "boolean",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "last_viewed_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "depth",
          "id",
          "last_viewed_at",
          "path"
        ]
      }
    }
  }
}
```
