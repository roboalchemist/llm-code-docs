# Source: https://posthog.com/docs/open-api-spec/environments_events_values_retrieve.md

# environments_events_values_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/events/values/
{
  "paths": {
    "/api/environments/{environment_id}/events/values/": {
      "get": {
        "operationId": "environments_events_values_retrieve",
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
                "csv",
                "json"
              ]
            }
          }
        ],
        "tags": [
          "events"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
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
