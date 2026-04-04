# Source: https://posthog.com/docs/open-api-spec/persisted_folder_create.md

# persisted_folder_create

## OpenAPI

```json POST /api/projects/{project_id}/persisted_folder/
{
  "paths": {
    "/api/projects/{project_id}/persisted_folder/": {
      "post": {
        "operationId": "persisted_folder_create",
        "parameters": [
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
          "persisted_folder"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PersistedFolder"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PersistedFolder"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PersistedFolder"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "persisted_folder:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PersistedFolder"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "PersistedFolder": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "type": {
            "$ref": "#/components/schemas/PersistedFolderTypeEnum"
          },
          "protocol": {
            "type": "string",
            "maxLength": 64
          },
          "path": {
            "type": "string"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "id",
          "type",
          "updated_at"
        ]
      },
      "PersistedFolderTypeEnum": {
        "enum": [
          "home",
          "pinned",
          "custom_products"
        ],
        "type": "string",
        "description": "* `home` - Home\n* `pinned` - Pinned\n* `custom_products` - Custom Products"
      }
    }
  }
}
```
