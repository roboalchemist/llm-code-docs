# Source: https://posthog.com/docs/open-api-spec/environments_groups_property_definitions_retrieve.md

# environments_groups_property_definitions_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/groups/property_definitions/
{
  "paths": {
    "/api/environments/{environment_id}/groups/property_definitions/": {
      "get": {
        "operationId": "environments_groups_property_definitions_retrieve",
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
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
