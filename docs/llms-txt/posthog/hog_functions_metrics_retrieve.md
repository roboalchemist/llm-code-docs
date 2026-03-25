# Source: https://posthog.com/docs/open-api-spec/hog_functions_metrics_retrieve.md

# hog_functions_metrics_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/hog_functions/{id}/metrics/
{
  "paths": {
    "/api/projects/{project_id}/hog_functions/{id}/metrics/": {
      "get": {
        "operationId": "hog_functions_metrics_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this hog function.",
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
          "hog_functions",
          "hog_functions"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "hog_functions"
        ]
      }
    }
  }
}
```
