# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_materialization_status_retrieve.md

# environments_endpoints_materialization_status_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/endpoints/{name}/materialization_status/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/materialization_status/": {
      "get": {
        "operationId": "environments_endpoints_materialization_status_retrieve",
        "description": "Get materialization status for an endpoint. Supports ?version=N query param.",
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
