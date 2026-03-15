# Source: https://posthog.com/docs/open-api-spec/event_definitions_golang_retrieve.md

# event_definitions_golang_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/event_definitions/golang/
{
  "paths": {
    "/api/projects/{project_id}/event_definitions/golang/": {
      "get": {
        "operationId": "event_definitions_golang_retrieve",
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
          "core",
          "event_definitions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:read"
            ]
          }
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
