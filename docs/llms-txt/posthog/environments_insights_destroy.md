# Source: https://posthog.com/docs/open-api-spec/environments_insights_destroy.md

# environments_insights_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/insights/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/insights/{id}/": {
      "delete": {
        "operationId": "environments_insights_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
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
              "insight:write"
            ]
          }
        ],
        "responses": {
          "405": {
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
