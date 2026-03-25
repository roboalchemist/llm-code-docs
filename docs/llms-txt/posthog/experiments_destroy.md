# Source: https://posthog.com/docs/open-api-spec/experiments_destroy.md

# experiments_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/experiments/{id}/
{
  "paths": {
    "/api/projects/{project_id}/experiments/{id}/": {
      "delete": {
        "operationId": "experiments_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this experiment.",
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
          "experiments",
          "experiments"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment:write"
            ]
          }
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "experiments"
        ]
      }
    }
  }
}
```
