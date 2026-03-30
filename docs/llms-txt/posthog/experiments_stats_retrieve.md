# Source: https://posthog.com/docs/open-api-spec/experiments_stats_retrieve.md

# experiments_stats_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/experiments/stats/
{
  "paths": {
    "/api/projects/{project_id}/experiments/stats/": {
      "get": {
        "operationId": "experiments_stats_retrieve",
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
