# Source: https://posthog.com/docs/open-api-spec/dashboards_collaborators_destroy_2.md

# dashboards_collaborators_destroy_2

## OpenAPI

```json DELETE /api/projects/{project_id}/dashboards/{dashboard_id}/collaborators/{user__uuid}/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/{dashboard_id}/collaborators/{user__uuid}/": {
      "delete": {
        "operationId": "dashboards_collaborators_destroy_2",
        "parameters": [
          {
            "in": "path",
            "name": "dashboard_id",
            "schema": {
              "type": "integer"
            },
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
          },
          {
            "in": "path",
            "name": "user__uuid",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "dashboards"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "dashboard:write"
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
