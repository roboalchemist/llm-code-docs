# Source: https://posthog.com/docs/open-api-spec/cohorts_persons_retrieve.md

# cohorts_persons_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/cohorts/{id}/persons/
{
  "paths": {
    "/api/projects/{project_id}/cohorts/{id}/persons/": {
      "get": {
        "operationId": "cohorts_persons_retrieve",
        "parameters": [
          {
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "json"
              ]
            }
          },
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
              "cohort:read",
              "person:read"
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
