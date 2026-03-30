# Source: https://posthog.com/docs/open-api-spec/groups_types_metrics_list.md

# groups_types_metrics_list

## OpenAPI

```json GET /api/projects/{project_id}/groups_types/{group_type_index}/metrics/
{
  "paths": {
    "/api/projects/{project_id}/groups_types/{group_type_index}/metrics/": {
      "get": {
        "operationId": "groups_types_metrics_list",
        "parameters": [
          {
            "in": "path",
            "name": "group_type_index",
            "schema": {
              "type": "integer",
              "maximum": 2147483647,
              "minimum": -2147483648
            },
            "required": true
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
          "groups_types"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "group:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedGroupUsageMetricList"
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
      "PaginatedGroupUsageMetricList": {
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
              "$ref": "#/components/schemas/GroupUsageMetric"
            }
          }
        }
      },
      "GroupUsageMetric": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 255
          },
          "format": {
            "$ref": "#/components/schemas/GroupUsageMetricFormatEnum"
          },
          "interval": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648,
            "description": "In days"
          },
          "display": {
            "$ref": "#/components/schemas/DisplayEnum"
          },
          "filters": {}
        },
        "required": [
          "filters",
          "id",
          "name"
        ]
      },
      "GroupUsageMetricFormatEnum": {
        "enum": [
          "numeric",
          "currency"
        ],
        "type": "string",
        "description": "* `numeric` - numeric\n* `currency` - currency"
      },
      "DisplayEnum": {
        "enum": [
          "number",
          "sparkline"
        ],
        "type": "string",
        "description": "* `number` - number\n* `sparkline` - sparkline"
      }
    }
  }
}
```
