# Source: https://posthog.com/docs/open-api-spec/object_media_previews_partial_update.md

# object_media_previews_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/object_media_previews/{id}/
{
  "paths": {
    "/api/projects/{project_id}/object_media_previews/{id}/": {
      "patch": {
        "operationId": "object_media_previews_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this object media preview.",
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
          "object_media_previews"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedObjectMediaPreview"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedObjectMediaPreview"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedObjectMediaPreview"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ObjectMediaPreview"
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
      "PatchedObjectMediaPreview": {
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
