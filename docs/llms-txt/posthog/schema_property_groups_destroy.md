# Source: https://posthog.com/docs/open-api-spec/schema_property_groups_destroy.md

# schema_property_groups_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/schema_property_groups/{id}/
{
  "paths": {
    "/api/projects/{project_id}/schema_property_groups/{id}/": {
      "delete": {
        "operationId": "schema_property_groups_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this schema property group.",
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
          "schema_property_groups"
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
