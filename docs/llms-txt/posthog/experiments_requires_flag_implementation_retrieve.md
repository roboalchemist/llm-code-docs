# Source: https://posthog.com/docs/open-api-spec/experiments_requires_flag_implementation_retrieve.md

# experiments_requires_flag_implementation_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/experiments/requires_flag_implementation/
{
  "paths": {
    "/api/projects/{project_id}/experiments/requires_flag_implementation/": {
      "get": {
        "operationId": "experiments_requires_flag_implementation_retrieve",
        "parameters": [
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
              "experiment:read"
            ]
          }
        ],
        "responses": {
          "200": {
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
