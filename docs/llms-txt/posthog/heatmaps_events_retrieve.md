# Source: https://posthog.com/docs/open-api-spec/heatmaps_events_retrieve.md

# heatmaps_events_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/heatmaps/events/
{
  "paths": {
    "/api/projects/{project_id}/heatmaps/events/": {
      "get": {
        "operationId": "heatmaps_events_retrieve",
        "parameters": [
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
          "heatmaps"
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
