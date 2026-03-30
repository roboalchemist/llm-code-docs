# Source: https://posthog.com/docs/open-api-spec/dashboards_sharing_passwords_destroy.md

# dashboards_sharing_passwords_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/dashboards/{dashboard_id}/sharing/passwords/{password_id}/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/{dashboard_id}/sharing/passwords/{password_id}/": {
      "delete": {
        "operationId": "dashboards_sharing_passwords_destroy",
        "description": "Delete a password from the sharing configuration.",
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
            "name": "password_id",
            "schema": {
              "type": "string"
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
          }
        ],
        "tags": [
          "core",
          "dashboards"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "sharing_configuration:write"
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
