# Source: https://posthog.com/docs/open-api-spec/environments_hog_functions_metrics_retrieve.md

# environments_hog_functions_metrics_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/hog_functions/{id}/metrics/
{
  "paths": {
    "/api/environments/{environment_id}/hog_functions/{id}/metrics/": {
      "get": {
        "operationId": "environments_hog_functions_metrics_retrieve",
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
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this hog function.",
            "required": true
          }
        ],
        "tags": [
          "hog_functions",
          "hog_functions"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "hog_functions"
        ]
      }
    }
  }
}
```
