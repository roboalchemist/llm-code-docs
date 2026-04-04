# Source: https://posthog.com/docs/open-api-spec/environments_groups_related_retrieve.md

# environments_groups_related_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/groups/related/
{
  "paths": {
    "/api/environments/{environment_id}/groups/related/": {
      "get": {
        "operationId": "environments_groups_related_retrieve",
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
            "name": "group_type_index",
            "schema": {
              "type": "integer"
            },
            "description": "Specify the group type to find",
            "required": true
          },
          {
            "in": "query",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "description": "Specify the id of the user to find groups for",
            "required": true
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
