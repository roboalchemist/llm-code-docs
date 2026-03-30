# Source: https://posthog.com/docs/open-api-spec/environments_dashboards_destroy.md

# environments_dashboards_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/dashboards/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/dashboards/{id}/": {
      "delete": {
        "operationId": "environments_dashboards_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
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
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "json",
                "txt"
              ]
            }
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this dashboard.",
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
              "dashboard:write"
            ]
          }
        ],
        "responses": {
          "405": {
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
