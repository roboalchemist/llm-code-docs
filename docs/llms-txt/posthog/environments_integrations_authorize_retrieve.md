# Source: https://posthog.com/docs/open-api-spec/environments_integrations_authorize_retrieve.md

# environments_integrations_authorize_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/integrations/authorize/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/authorize/": {
      "get": {
        "operationId": "environments_integrations_authorize_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "core",
          "integrations"
        ],
        "responses": {
          "200": {
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
