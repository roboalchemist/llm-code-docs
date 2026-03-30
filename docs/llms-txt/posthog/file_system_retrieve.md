# Source: https://posthog.com/docs/open-api-spec/file_system_retrieve.md

# file_system_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/file_system/{id}/
{
  "paths": {
    "/api/projects/{project_id}/file_system/{id}/": {
      "get": {
        "operationId": "file_system_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this file system.",
            "required": true
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          }
        ],
        "tags": [
          "core",
          "file_system"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "file_system:read"
            ]
          }
        ],
        "responses": {
          "200": {
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
