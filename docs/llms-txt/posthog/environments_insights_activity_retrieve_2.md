# Source: https://posthog.com/docs/open-api-spec/environments_insights_activity_retrieve_2.md

# environments_insights_activity_retrieve_2

## OpenAPI

```json GET /api/environments/{environment_id}/insights/{id}/activity/
{
  "paths": {
    "/api/environments/{environment_id}/insights/{id}/activity/": {
      "get": {
        "operationId": "environments_insights_activity_retrieve_2",
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
