# Source: https://posthog.com/docs/open-api-spec/app_metrics_historical_exports_retrieve.md

# app_metrics_historical_exports_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/app_metrics/{plugin_config_id}/historical_exports/
{
  "paths": {
    "/api/projects/{project_id}/app_metrics/{plugin_config_id}/historical_exports/": {
      "get": {
        "operationId": "app_metrics_historical_exports_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "plugin_config_id",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
        "x-explicit-tags": []
      }
    }
  }
}
```
