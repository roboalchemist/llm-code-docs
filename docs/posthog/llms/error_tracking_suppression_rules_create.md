# Source: https://posthog.com/docs/open-api-spec/error_tracking_suppression_rules_create.md

# error_tracking_suppression_rules_create

## OpenAPI

```json POST /api/environments/{project_id}/error_tracking/suppression_rules/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/suppression_rules/": {
      "post": {
        "operationId": "error_tracking_suppression_rules_create",
        "parameters": [
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingSuppressionRule"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingSuppressionRule"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ErrorTrackingSuppressionRule"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "error_tracking:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorTrackingSuppressionRule"
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
