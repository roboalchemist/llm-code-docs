# Source: https://posthog.com/docs/open-api-spec/experiment_saved_metrics_destroy.md

# experiment_saved_metrics_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/experiment_saved_metrics/{id}/
{
  "paths": {
    "/api/projects/{project_id}/experiment_saved_metrics/{id}/": {
      "delete": {
        "operationId": "experiment_saved_metrics_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this experiment saved metric.",
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
          "experiment_saved_metrics"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "experiment_saved_metric:write"
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
