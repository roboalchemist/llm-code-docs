# Source: https://posthog.com/docs/open-api-spec/surveys_activity_retrieve.md

# surveys_activity_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/surveys/activity/
{
  "paths": {
    "/api/projects/{project_id}/surveys/activity/": {
      "get": {
        "operationId": "surveys_activity_retrieve",
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
          "surveys",
          "surveys"
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
          "surveys"
        ]
      }
    }
  }
}
```
