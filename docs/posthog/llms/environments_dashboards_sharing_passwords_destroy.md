# Source: https://posthog.com/docs/open-api-spec/environments_dashboards_sharing_passwords_destroy.md

# environments_dashboards_sharing_passwords_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/dashboards/{dashboard_id}/sharing/passwords/{password_id}/
{
  "paths": {
    "/api/environments/{environment_id}/dashboards/{dashboard_id}/sharing/passwords/{password_id}/": {
      "delete": {
        "operationId": "environments_dashboards_sharing_passwords_destroy",
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
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "password_id",
            "schema": {
              "type": "string"
            },
            "required": true
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
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
