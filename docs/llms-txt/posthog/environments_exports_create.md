# Source: https://posthog.com/docs/open-api-spec/environments_exports_create.md

# environments_exports_create

## OpenAPI

```json POST /api/environments/{environment_id}/exports/
{
  "paths": {
    "/api/environments/{environment_id}/exports/": {
      "post": {
        "operationId": "environments_exports_create",
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
          "exports"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ExportedAsset"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ExportedAsset"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ExportedAsset"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "export:write"
            ]
          }
        ],
        "responses": {
          "201": {
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
        "deprecated": true,
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
