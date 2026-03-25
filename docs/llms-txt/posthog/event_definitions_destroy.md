# Source: https://posthog.com/docs/open-api-spec/event_definitions_destroy.md

# event_definitions_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/event_definitions/{id}/
{
  "paths": {
    "/api/projects/{project_id}/event_definitions/{id}/": {
      "delete": {
        "operationId": "event_definitions_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this event definition.",
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
          "event_definitions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:write"
            ]
          }
        ],
        "responses": {
          "204": {
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
