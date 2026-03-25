# Source: https://posthog.com/docs/open-api-spec/object_media_previews_preferred_for_event_retrieve.md

# object_media_previews_preferred_for_event_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/object_media_previews/preferred_for_event/
{
  "paths": {
    "/api/projects/{project_id}/object_media_previews/preferred_for_event/": {
      "get": {
        "operationId": "object_media_previews_preferred_for_event_retrieve",
        "description": "Get the preferred media preview for an event definition.\nMost recent user-uploaded, then most recent exported asset.\nRequires event_definition (query param).",
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
          "object_media_previews"
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
