# Source: https://posthog.com/docs/open-api-spec/default_release_conditions_retrieve.md

# default_release_conditions_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/environments/{id}/default_release_conditions/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/default_release_conditions/": {
      "get": {
        "operationId": "default_release_conditions_retrieve",
        "description": "Manage default release conditions for new feature flags in this team.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this environment (aka team).",
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
          "environments"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
