# Source: https://posthog.com/docs/open-api-spec/cohorts_activity_retrieve.md

# cohorts_activity_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/cohorts/activity/
{
  "paths": {
    "/api/projects/{project_id}/cohorts/activity/": {
      "get": {
        "operationId": "cohorts_activity_retrieve",
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
          "core",
          "cohorts"
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
          "core"
        ]
      }
    }
  }
}
```
