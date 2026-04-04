# Source: https://posthog.com/docs/open-api-spec/cohorts_calculation_history_retrieve.md

# cohorts_calculation_history_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/cohorts/{id}/calculation_history/
{
  "paths": {
    "/api/projects/{project_id}/cohorts/{id}/calculation_history/": {
      "get": {
        "operationId": "cohorts_calculation_history_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this cohort.",
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
          "cohorts"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "cohort:read"
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
