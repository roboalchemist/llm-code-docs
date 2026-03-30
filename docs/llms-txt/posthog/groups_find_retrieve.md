# Source: https://posthog.com/docs/open-api-spec/groups_find_retrieve.md

# groups_find_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/groups/find/
{
  "paths": {
    "/api/projects/{project_id}/groups/find/": {
      "get": {
        "operationId": "groups_find_retrieve",
        "parameters": [
          {
            "in": "query",
            "name": "group_key",
            "schema": {
              "type": "string"
            },
            "description": "Specify the key of the group to find",
            "required": true
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
