# Source: https://posthog.com/docs/open-api-spec/object_media_previews_list.md

# object_media_previews_list

## OpenAPI

```json GET /api/projects/{project_id}/object_media_previews/
{
  "paths": {
    "/api/projects/{project_id}/object_media_previews/": {
      "get": {
        "operationId": "object_media_previews_list",
        "parameters": [
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
          "object_media_previews"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedObjectMediaPreviewList"
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
      "PaginatedObjectMediaPreviewList": {
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
              "$ref": "#/components/schemas/ObjectMediaPreview"
            }
          }
        }
      },
      "ObjectMediaPreview": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "media_url": {
            "type": "string",
            "readOnly": true
          },
          "media_type": {
            "type": "string",
            "description": "Return 'uploaded' or 'exported' based on which media is set",
            "readOnly": true
          },
          "metadata": {},
          "uploaded_media_id": {
            "type": "string",
            "format": "uuid",
            "writeOnly": true,
            "nullable": true
          },
          "exported_asset_id": {
            "type": "string",
            "format": "uuid",
            "writeOnly": true,
            "nullable": true
          },
          "event_definition_id": {
            "type": "string",
            "format": "uuid",
            "writeOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "id",
          "media_type",
          "media_url",
          "updated_at"
        ]
      }
    }
  }
}
```
