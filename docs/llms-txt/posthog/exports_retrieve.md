# Source: https://posthog.com/docs/open-api-spec/exports_retrieve.md

# exports_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/exports/{id}/
{
  "paths": {
    "/api/projects/{project_id}/exports/{id}/": {
      "get": {
        "operationId": "exports_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this exported asset.",
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
          "exports"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "export:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ExportedAsset"
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
      "ExportedAsset": {
        "type": "object",
        "description": "Standard ExportedAsset serializer that doesn't return content.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "dashboard": {
            "type": "integer",
            "nullable": true
          },
          "insight": {
            "type": "integer",
            "nullable": true
          },
          "export_format": {
            "$ref": "#/components/schemas/ExportFormatEnum"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "has_content": {
            "type": "string",
            "readOnly": true
          },
          "export_context": {
            "nullable": true
          },
          "filename": {
            "type": "string",
            "readOnly": true
          },
          "expires_after": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "exception": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "exception",
          "expires_after",
          "export_format",
          "filename",
          "has_content",
          "id"
        ]
      },
      "ExportFormatEnum": {
        "enum": [
          "image/png",
          "application/pdf",
          "text/csv",
          "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          "video/webm",
          "video/mp4",
          "image/gif",
          "application/json"
        ],
        "type": "string",
        "description": "* `image/png` - image/png\n* `application/pdf` - application/pdf\n* `text/csv` - text/csv\n* `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\n* `video/webm` - video/webm\n* `video/mp4` - video/mp4\n* `image/gif` - image/gif\n* `application/json` - application/json"
      }
    }
  }
}
```
