# Source: https://posthog.com/docs/open-api-spec/environments_saved_list.md

# environments_saved_list

## OpenAPI

```json GET /api/environments/{environment_id}/saved/
{
  "paths": {
    "/api/environments/{environment_id}/saved/": {
      "get": {
        "operationId": "environments_saved_list",
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
          "saved"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "heatmap:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedHeatmapScreenshotResponseList"
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
      "PaginatedHeatmapScreenshotResponseList": {
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
              "$ref": "#/components/schemas/HeatmapScreenshotResponse"
            }
          }
        }
      },
      "HeatmapScreenshotResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "short_id": {
            "type": "string",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "url": {
            "type": "string",
            "format": "uri",
            "maxLength": 2000
          },
          "data_url": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "description": "URL for fetching heatmap data",
            "maxLength": 2000
          },
          "target_widths": {},
          "type": {
            "$ref": "#/components/schemas/HeatmapScreenshotResponseTypeEnum"
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HeatmapScreenshotResponseStatusEnum"
              }
            ],
            "readOnly": true
          },
          "has_content": {
            "type": "boolean",
            "readOnly": true
          },
          "snapshots": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "deleted": {
            "type": "boolean"
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
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
            "readOnly": true
          },
          "exception": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "exception",
          "has_content",
          "id",
          "short_id",
          "snapshots",
          "status",
          "updated_at",
          "url"
        ]
      },
      "HeatmapScreenshotResponseTypeEnum": {
        "enum": [
          "screenshot",
          "iframe",
          "recording"
        ],
        "type": "string",
        "description": "* `screenshot` - Screenshot\n* `iframe` - Iframe\n* `recording` - Recording"
      },
      "HeatmapScreenshotResponseStatusEnum": {
        "enum": [
          "processing",
          "completed",
          "failed"
        ],
        "type": "string",
        "description": "* `processing` - Processing\n* `completed` - Completed\n* `failed` - Failed"
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
