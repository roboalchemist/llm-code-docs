# Source: https://posthog.com/docs/open-api-spec/environments_dashboards_stream_tiles_retrieve.md

# environments_dashboards_stream_tiles_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/dashboards/{id}/stream_tiles/
{
  "paths": {
    "/api/environments/{environment_id}/dashboards/{id}/stream_tiles/": {
      "get": {
        "operationId": "environments_dashboards_stream_tiles_retrieve",
        "description": "Stream dashboard metadata and tiles via Server-Sent Events. Sends metadata first, then tiles as they are rendered.",
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
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "json",
                "txt"
              ]
            }
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this dashboard.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "dashboards"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
