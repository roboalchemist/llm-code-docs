# Source: https://posthog.com/docs/open-api-spec/environments_app_metrics_error_details_retrieve.md

# environments_app_metrics_error_details_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/app_metrics/{id}/error_details/
{
  "paths": {
    "/api/environments/{environment_id}/app_metrics/{id}/error_details/": {
      "get": {
        "operationId": "environments_app_metrics_error_details_retrieve",
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
            "description": "A unique integer value identifying this plugin config.",
            "required": true
          }
        ],
        "tags": [
          "app_metrics"
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
