# Source: https://posthog.com/docs/open-api-spec/error_tracking_grouping_rules_reorder_partial_update.md

# error_tracking_grouping_rules_reorder_partial_update

## OpenAPI

```json PATCH /api/environments/{project_id}/error_tracking/grouping_rules/reorder/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/grouping_rules/reorder/": {
      "patch": {
        "operationId": "error_tracking_grouping_rules_reorder_partial_update",
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
        "responses": {
          "200": {
            "description": "No response body"
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
      }
    }
  }
}
```
