# Source: https://posthog.com/docs/open-api-spec/dashboards_stream_tiles_retrieve.md

# dashboards_stream_tiles_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/dashboards/{id}/stream_tiles/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/{id}/stream_tiles/": {
      "get": {
        "operationId": "dashboards_stream_tiles_retrieve",
        "description": "Stream dashboard metadata and tiles via Server-Sent Events. Sends metadata first, then tiles as they are rendered.",
        "parameters": [
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
          "core",
          "dashboards"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
