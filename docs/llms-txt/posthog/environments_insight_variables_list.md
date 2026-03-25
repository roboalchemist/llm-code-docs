# Source: https://posthog.com/docs/open-api-spec/environments_insight_variables_list.md

# environments_insight_variables_list

## OpenAPI

```json GET /api/environments/{environment_id}/insight_variables/
{
  "paths": {
    "/api/environments/{environment_id}/insight_variables/": {
      "get": {
        "operationId": "environments_insight_variables_list",
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
            "name": "page",
            "required": false,
            "in": "query",
            "description": "A page number within the paginated result set.",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "tags": [
          "insight_variables"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "insight_variable:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedInsightVariableList"
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
      "PaginatedInsightVariableList": {
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
            "example": "http://api.example.org/accounts/?page=4"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?page=2"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/InsightVariable"
            }
          }
        }
      },
      "InsightVariable": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 400
          },
          "type": {
            "$ref": "#/components/schemas/InsightVariableTypeEnum"
          },
          "default_value": {
            "nullable": true
          },
          "created_by": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "code_name": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "values": {
            "nullable": true
          }
        },
        "required": [
          "code_name",
          "created_at",
          "created_by",
          "id",
          "name",
          "type"
        ]
      },
      "InsightVariableTypeEnum": {
        "enum": [
          "String",
          "Number",
          "Boolean",
          "List",
          "Date"
        ],
        "type": "string",
        "description": "* `String` - String\n* `Number` - Number\n* `Boolean` - Boolean\n* `List` - List\n* `Date` - Date"
      }
    }
  }
}
```
