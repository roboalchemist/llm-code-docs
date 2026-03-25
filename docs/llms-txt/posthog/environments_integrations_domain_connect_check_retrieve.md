# Source: https://posthog.com/docs/open-api-spec/environments_integrations_domain_connect_check_retrieve.md

# environments_integrations_domain_connect_check_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/integrations/domain-connect/check/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/domain-connect/check/": {
      "get": {
        "operationId": "environments_integrations_domain_connect_check_retrieve",
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
