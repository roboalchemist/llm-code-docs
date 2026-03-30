# Source: https://posthog.com/docs/open-api-spec/error_tracking_grouping_rules_partial_update.md

# error_tracking_grouping_rules_partial_update

## OpenAPI

```json PATCH /api/environments/{project_id}/error_tracking/grouping_rules/{id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/grouping_rules/{id}/": {
      "patch": {
        "operationId": "error_tracking_grouping_rules_partial_update",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedErrorTrackingGroupingRule"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedErrorTrackingGroupingRule"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedErrorTrackingGroupingRule"
              }
            }
          }
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
      "PatchedErrorTrackingGroupingRule": {
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
        }
      },
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
