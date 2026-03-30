# Source: https://posthog.com/docs/open-api-spec/environments_insights_activity_retrieve.md

# environments_insights_activity_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/insights/activity/
{
  "paths": {
    "/api/environments/{environment_id}/insights/activity/": {
      "get": {
        "operationId": "environments_insights_activity_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
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
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
