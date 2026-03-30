# Source: https://posthog.com/docs/open-api-spec/error_tracking_grouping_rules_retrieve.md

# error_tracking_grouping_rules_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/grouping_rules/{id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/grouping_rules/{id}/": {
      "get": {
        "operationId": "error_tracking_grouping_rules_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this error tracking grouping rule.",
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
                  "$ref": "#/components/schemas/ErrorTrackingGroupingRule"
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
      "ErrorTrackingGroupingRule": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "filters": {},
          "assignee": {
            "type": "string",
            "readOnly": true
          },
          "order_key": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648
          },
          "disabled_data": {
            "nullable": true
          }
        },
        "required": [
          "assignee",
          "filters",
          "id",
          "order_key"
        ]
      }
    }
  }
}
```
