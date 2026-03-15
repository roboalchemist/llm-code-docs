# Source: https://posthog.com/docs/open-api-spec/environments_persisted_folder_list.md

# environments_persisted_folder_list

## OpenAPI

```json GET /api/environments/{environment_id}/persisted_folder/
{
  "paths": {
    "/api/environments/{environment_id}/persisted_folder/": {
      "get": {
        "operationId": "environments_persisted_folder_list",
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
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
                  "$ref": "#/components/schemas/PaginatedPersistedFolderList"
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
      "PaginatedPersistedFolderList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PersistedFolder"
            }
          }
        }
      },
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
