# Source: https://posthog.com/docs/open-api-spec/environments_insights_analyze_retrieve.md

# environments_insights_analyze_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/insights/{id}/analyze/
{
  "paths": {
    "/api/environments/{environment_id}/insights/{id}/analyze/": {
      "get": {
        "operationId": "environments_insights_analyze_retrieve",
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
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this insight.",
            "required": true
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
