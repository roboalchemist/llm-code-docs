# Source: https://posthog.com/docs/open-api-spec/app_metrics_error_details_retrieve.md

# app_metrics_error_details_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/app_metrics/{id}/error_details/
{
  "paths": {
    "/api/projects/{project_id}/app_metrics/{id}/error_details/": {
      "get": {
        "operationId": "app_metrics_error_details_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this plugin config.",
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
