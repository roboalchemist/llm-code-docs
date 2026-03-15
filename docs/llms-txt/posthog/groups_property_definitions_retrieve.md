# Source: https://posthog.com/docs/open-api-spec/groups_property_definitions_retrieve.md

# groups_property_definitions_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/groups/property_definitions/
{
  "paths": {
    "/api/projects/{project_id}/groups/property_definitions/": {
      "get": {
        "operationId": "groups_property_definitions_retrieve",
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
          "groups"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "group:read"
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
