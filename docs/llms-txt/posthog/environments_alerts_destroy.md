# Source: https://posthog.com/docs/open-api-spec/environments_alerts_destroy.md

# environments_alerts_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/alerts/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/alerts/{id}/": {
      "delete": {
        "operationId": "environments_alerts_destroy",
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
            "description": "A UUID string identifying this alert configuration.",
            "required": true
          }
        ],
        "tags": [
          "alerts"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "alert:write"
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
