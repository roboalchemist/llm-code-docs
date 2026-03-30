# Source: https://posthog.com/docs/open-api-spec/environments_integrations_destroy.md

# environments_integrations_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/integrations/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/{id}/": {
      "delete": {
        "operationId": "environments_integrations_destroy",
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
              "type": "integer"
            },
            "description": "A unique integer value identifying this integration.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "integrations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "integration:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
