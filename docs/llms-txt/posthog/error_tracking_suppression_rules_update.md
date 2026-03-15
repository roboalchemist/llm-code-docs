# Source: https://posthog.com/docs/open-api-spec/error_tracking_suppression_rules_update.md

# error_tracking_suppression_rules_update

## OpenAPI

```json PUT /api/environments/{project_id}/error_tracking/suppression_rules/{id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/suppression_rules/{id}/": {
      "put": {
        "operationId": "error_tracking_suppression_rules_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this error tracking suppression rule.",
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
          "200": {
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
        "x-explicit-tags": []
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
