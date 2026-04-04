# Source: https://posthog.com/docs/open-api-spec/event_ingestion_restrictions_retrieve.md

# event_ingestion_restrictions_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/environments/{id}/event_ingestion_restrictions/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/event_ingestion_restrictions/": {
      "get": {
        "operationId": "event_ingestion_restrictions_retrieve",
        "description": "Deprecated: use /api/environments/{id}/ instead.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this environment (aka team).",
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
          "environments"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:read"
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
