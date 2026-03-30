# Source: https://posthog.com/docs/open-api-spec/dashboards_destroy.md

# dashboards_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/dashboards/{id}/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/{id}/": {
      "delete": {
        "operationId": "dashboards_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
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
              "dashboard:write"
            ]
          }
        ],
        "responses": {
          "405": {
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
