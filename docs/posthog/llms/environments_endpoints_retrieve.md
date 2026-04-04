# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_retrieve.md

# environments_endpoints_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/endpoints/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/": {
      "get": {
        "operationId": "environments_endpoints_retrieve",
        "description": "List all endpoints for the team.",
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
          "endpoints",
          "endpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "endpoints"
        ]
      }
    }
  }
}
```
