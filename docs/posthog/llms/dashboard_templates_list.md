# Source: https://posthog.com/docs/open-api-spec/dashboard_templates_list.md

# dashboard_templates_list

## OpenAPI

```json GET /api/projects/{project_id}/dashboard_templates/
{
  "paths": {
    "/api/projects/{project_id}/dashboard_templates/": {
      "get": {
        "operationId": "dashboard_templates_list",
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
          "core",
          "dashboard_templates"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "dashboard_template:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedDashboardTemplateList"
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
      "PaginatedDashboardTemplateList": {
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
              "$ref": "#/components/schemas/DashboardTemplate"
            }
          }
        }
      },
      "DashboardTemplate": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "template_name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "dashboard_description": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "dashboard_filters": {
            "nullable": true
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 255
            },
            "nullable": true
          },
          "tiles": {
            "nullable": true
          },
          "variables": {
            "nullable": true
          },
          "deleted": {
            "type": "boolean",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "created_by": {
            "type": "integer",
            "nullable": true
          },
          "image_url": {
            "type": "string",
            "nullable": true,
            "maxLength": 8201
          },
          "team_id": {
            "type": "integer",
            "nullable": true,
            "readOnly": true
          },
          "scope": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/DashboardTemplateScopeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "availability_contexts": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 255
            },
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "id",
          "team_id"
        ]
      },
      "DashboardTemplateScopeEnum": {
        "enum": [
          "team",
          "global",
          "feature_flag"
        ],
        "type": "string",
        "description": "* `team` - Only team\n* `global` - Global\n* `feature_flag` - Feature Flag"
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
