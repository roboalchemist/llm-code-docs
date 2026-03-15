# Source: https://posthog.com/docs/open-api-spec/experiments_timeseries_results_retrieve.md

# experiments_timeseries_results_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/experiments/{id}/timeseries_results/
{
  "paths": {
    "/api/projects/{project_id}/experiments/{id}/timeseries_results/": {
      "get": {
        "operationId": "experiments_timeseries_results_retrieve",
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
