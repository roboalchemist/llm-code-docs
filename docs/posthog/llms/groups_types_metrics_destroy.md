# Source: https://posthog.com/docs/open-api-spec/groups_types_metrics_destroy.md

# groups_types_metrics_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/groups_types/{group_type_index}/metrics/{id}/
{
  "paths": {
    "/api/projects/{project_id}/groups_types/{group_type_index}/metrics/{id}/": {
      "delete": {
        "operationId": "groups_types_metrics_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "group_type_index",
            "schema": {
              "type": "integer",
              "maximum": 2147483647,
              "minimum": -2147483648
            },
            "required": true
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this group usage metric.",
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
          "groups_types"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "group:write"
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
