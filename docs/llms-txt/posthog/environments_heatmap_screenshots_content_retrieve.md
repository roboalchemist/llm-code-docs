# Source: https://posthog.com/docs/open-api-spec/environments_heatmap_screenshots_content_retrieve.md

# environments_heatmap_screenshots_content_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/heatmap_screenshots/{id}/content/
{
  "paths": {
    "/api/environments/{environment_id}/heatmap_screenshots/{id}/content/": {
      "get": {
        "operationId": "environments_heatmap_screenshots_content_retrieve",
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
            "description": "A UUID string identifying this saved heatmap.",
            "required": true
          }
        ],
        "tags": [
          "heatmap_screenshots"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "heatmap:read"
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
