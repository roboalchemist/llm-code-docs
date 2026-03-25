# Source: https://posthog.com/docs/open-api-spec/insights_activity_retrieve.md

# insights_activity_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/insights/activity/
{
  "paths": {
    "/api/projects/{project_id}/insights/activity/": {
      "get": {
        "operationId": "insights_activity_retrieve",
        "parameters": [
          {
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "json"
              ]
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
          "insights"
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
        "x-explicit-tags": []
      }
    }
  }
}
```
