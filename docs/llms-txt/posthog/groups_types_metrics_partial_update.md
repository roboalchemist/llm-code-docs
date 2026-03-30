# Source: https://posthog.com/docs/open-api-spec/groups_types_metrics_partial_update.md

# groups_types_metrics_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/groups_types/{group_type_index}/metrics/{id}/
{
  "paths": {
    "/api/projects/{project_id}/groups_types/{group_type_index}/metrics/{id}/": {
      "patch": {
        "operationId": "groups_types_metrics_partial_update",
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this group usage metric.",
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
          "groups_types"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedGroupUsageMetric"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedGroupUsageMetric"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedGroupUsageMetric"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "group:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GroupUsageMetric"
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
      "PatchedGroupUsageMetric": {
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
