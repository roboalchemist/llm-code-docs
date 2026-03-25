# Source: https://posthog.com/docs/open-api-spec/heatmap_screenshots_content_retrieve.md

# heatmap_screenshots_content_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/heatmap_screenshots/{id}/content/
{
  "paths": {
    "/api/projects/{project_id}/heatmap_screenshots/{id}/content/": {
      "get": {
        "operationId": "heatmap_screenshots_content_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this saved heatmap.",
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
        "x-explicit-tags": []
      }
    }
  }
}
```
