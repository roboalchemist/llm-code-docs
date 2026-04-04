# Source: https://posthog.com/docs/open-api-spec/environments_insights_trending_retrieve.md

# environments_insights_trending_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/insights/trending/
{
  "paths": {
    "/api/environments/{environment_id}/insights/trending/": {
      "get": {
        "operationId": "environments_insights_trending_retrieve",
        "description": "Returns trending insights based on view count in the last N days (default 7).\nDefaults to returning top 10 insights.",
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
