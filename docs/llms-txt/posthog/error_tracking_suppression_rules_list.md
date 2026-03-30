# Source: https://posthog.com/docs/open-api-spec/error_tracking_suppression_rules_list.md

# error_tracking_suppression_rules_list

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/suppression_rules/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/suppression_rules/": {
      "get": {
        "operationId": "error_tracking_suppression_rules_list",
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
          "error_tracking"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "error_tracking:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedErrorTrackingSuppressionRuleList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "error_tracking"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedErrorTrackingSuppressionRuleList": {
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
              "$ref": "#/components/schemas/ErrorTrackingSuppressionRule"
            }
          }
        }
      },
      "ErrorTrackingSuppressionRule": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "filters": {},
          "order_key": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648
          }
        },
        "required": [
          "filters",
          "id",
          "order_key"
        ]
      }
    }
  }
}
```
