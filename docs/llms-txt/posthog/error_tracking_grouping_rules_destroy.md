# Source: https://posthog.com/docs/open-api-spec/error_tracking_grouping_rules_destroy.md

# error_tracking_grouping_rules_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/error_tracking/grouping_rules/{id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/grouping_rules/{id}/": {
      "delete": {
        "operationId": "error_tracking_grouping_rules_destroy",
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
              "error_tracking:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
