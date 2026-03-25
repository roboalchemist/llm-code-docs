# Source: https://posthog.com/docs/open-api-spec/environments_heatmaps_events_retrieve.md

# environments_heatmaps_events_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/heatmaps/events/
{
  "paths": {
    "/api/environments/{environment_id}/heatmaps/events/": {
      "get": {
        "operationId": "environments_heatmaps_events_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
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
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
