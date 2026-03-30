# Source: https://posthog.com/docs/open-api-spec/environments_insight_variables_destroy.md

# environments_insight_variables_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/insight_variables/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/insight_variables/{id}/": {
      "delete": {
        "operationId": "environments_insight_variables_destroy",
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this insight variable.",
            "required": true
          }
        ],
        "tags": [
          "insight_variables"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "insight_variable:write"
            ]
          }
        ],
        "responses": {
          "204": {
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
