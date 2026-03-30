# Source: https://posthog.com/docs/open-api-spec/environments_exports_list.md

# environments_exports_list

## OpenAPI

```json GET /api/environments/{environment_id}/exports/
{
  "paths": {
    "/api/environments/{environment_id}/exports/": {
      "get": {
        "operationId": "environments_exports_list",
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
                  "$ref": "#/components/schemas/PaginatedExportedAssetList"
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
      "PaginatedExportedAssetList": {
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
              "$ref": "#/components/schemas/ExportedAsset"
            }
          }
        }
      },
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
