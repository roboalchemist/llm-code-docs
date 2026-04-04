# Source: https://posthog.com/docs/open-api-spec/insights_trending_retrieve.md

# insights_trending_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/insights/trending/
{
  "paths": {
    "/api/projects/{project_id}/insights/trending/": {
      "get": {
        "operationId": "insights_trending_retrieve",
        "description": "Returns trending insights based on view count in the last N days (default 7).\nDefaults to returning top 10 insights.",
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
