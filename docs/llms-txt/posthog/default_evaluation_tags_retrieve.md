# Source: https://posthog.com/docs/open-api-spec/default_evaluation_tags_retrieve.md

# default_evaluation_tags_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/environments/{id}/default_evaluation_tags/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/default_evaluation_tags/": {
      "get": {
        "operationId": "default_evaluation_tags_retrieve",
        "description": "Manage default evaluation tags for a team",
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
