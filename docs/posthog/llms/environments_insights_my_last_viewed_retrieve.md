# Source: https://posthog.com/docs/open-api-spec/environments_insights_my_last_viewed_retrieve.md

# environments_insights_my_last_viewed_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/insights/my_last_viewed/
{
  "paths": {
    "/api/environments/{environment_id}/insights/my_last_viewed/": {
      "get": {
        "operationId": "environments_insights_my_last_viewed_retrieve",
        "description": "Returns basic details about the last 5 insights viewed by this user. Most recently viewed first.",
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
