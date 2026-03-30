# Source: https://posthog.com/docs/open-api-spec/destroy_3.md

# destroy_3

## OpenAPI

```json DELETE /api/projects/{project_id}/environments/{id}/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/": {
      "delete": {
        "operationId": "destroy_3",
        "description": "Deprecated: use /api/environments/{id}/ instead.",
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:write"
            ]
          }
        ],
        "deprecated": true,
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
