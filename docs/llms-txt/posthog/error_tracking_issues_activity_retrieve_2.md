# Source: https://posthog.com/docs/open-api-spec/error_tracking_issues_activity_retrieve_2.md

# error_tracking_issues_activity_retrieve_2

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/issues/{id}/activity/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/issues/{id}/activity/": {
      "get": {
        "operationId": "error_tracking_issues_activity_retrieve_2",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this error tracking issue.",
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
          "error_tracking",
          "error_tracking"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "activity_log:read"
            ]
          }
        ],
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
  }
}
```
