# Source: https://posthog.com/docs/open-api-spec/event_schemas_destroy.md

# event_schemas_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/event_schemas/{id}/
{
  "paths": {
    "/api/projects/{project_id}/event_schemas/{id}/": {
      "delete": {
        "operationId": "event_schemas_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this event schema.",
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
          "event_schemas"
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
        "x-explicit-tags": []
      }
    }
  }
}
```
