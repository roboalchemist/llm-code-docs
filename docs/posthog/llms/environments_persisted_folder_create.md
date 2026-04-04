# Source: https://posthog.com/docs/open-api-spec/environments_persisted_folder_create.md

# environments_persisted_folder_create

## OpenAPI

```json POST /api/environments/{environment_id}/persisted_folder/
{
  "paths": {
    "/api/environments/{environment_id}/persisted_folder/": {
      "post": {
        "operationId": "environments_persisted_folder_create",
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
        "deprecated": true,
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
