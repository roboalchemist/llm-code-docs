# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_run_retrieve.md

# environments_endpoints_run_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/endpoints/{name}/run/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/run/": {
      "get": {
        "operationId": "environments_endpoints_run_retrieve",
        "description": "Execute endpoint with optional materialization. Supports version parameter, runs latest version if not set.",
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
            "name": "name",
            "schema": {
              "type": "string",
              "description": "URL-safe name for the endpoint"
            },
            "required": true
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
