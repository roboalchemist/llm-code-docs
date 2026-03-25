# Source: https://posthog.com/docs/open-api-spec/web_experiments_destroy.md

# web_experiments_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/web_experiments/{id}/
{
  "paths": {
    "/api/projects/{project_id}/web_experiments/{id}/": {
      "delete": {
        "operationId": "web_experiments_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this web experiment.",
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
          "web_experiments"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment:write"
            ]
          }
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
