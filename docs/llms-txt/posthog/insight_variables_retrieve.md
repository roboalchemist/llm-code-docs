# Source: https://posthog.com/docs/open-api-spec/insight_variables_retrieve.md

# insight_variables_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/insight_variables/{id}/
{
  "paths": {
    "/api/projects/{project_id}/insight_variables/{id}/": {
      "get": {
        "operationId": "insight_variables_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this insight variable.",
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
                  "$ref": "#/components/schemas/InsightVariable"
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
