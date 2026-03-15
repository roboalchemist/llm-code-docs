# Source: https://posthog.com/docs/open-api-spec/environments_app_metrics_historical_exports_retrieve_2.md

# environments_app_metrics_historical_exports_retrieve_2

## OpenAPI

```json GET /api/environments/{environment_id}/app_metrics/{plugin_config_id}/historical_exports/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/app_metrics/{plugin_config_id}/historical_exports/{id}/": {
      "get": {
        "operationId": "environments_app_metrics_historical_exports_retrieve_2",
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
              "type": "string"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "plugin_config_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "app_metrics"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "plugin:read"
            ]
          }
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
