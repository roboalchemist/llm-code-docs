# Source: https://posthog.com/docs/open-api-spec/environments_hog_flows_logs_retrieve.md

# environments_hog_flows_logs_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/hog_flows/{id}/logs/
{
  "paths": {
    "/api/environments/{environment_id}/hog_flows/{id}/logs/": {
      "get": {
        "operationId": "environments_hog_flows_logs_retrieve",
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
            "description": "A UUID string identifying this hog flow.",
            "required": true
          }
        ],
        "tags": [
          "workflows",
          "hog_flows"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "workflows"
        ]
      }
    }
  }
}
```
