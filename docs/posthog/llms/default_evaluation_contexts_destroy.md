# Source: https://posthog.com/docs/open-api-spec/default_evaluation_contexts_destroy.md

# default_evaluation_contexts_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/environments/{id}/default_evaluation_contexts/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/default_evaluation_contexts/": {
      "delete": {
        "operationId": "default_evaluation_contexts_destroy",
        "description": "Manage default evaluation contexts for a team.",
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
