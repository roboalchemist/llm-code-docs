# Source: https://posthog.com/docs/open-api-spec/persisted_folder_retrieve.md

# persisted_folder_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/persisted_folder/{id}/
{
  "paths": {
    "/api/projects/{project_id}/persisted_folder/{id}/": {
      "get": {
        "operationId": "persisted_folder_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this Persisted Folder.",
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
          "persisted_folder"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "persisted_folder:read"
            ]
          }
        ],
        "responses": {
          "200": {
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
