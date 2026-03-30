# Source: https://posthog.com/docs/open-api-spec/evaluation_runs_create.md

# evaluation_runs_create

## OpenAPI

```json POST /api/environments/{project_id}/evaluation_runs/
{
  "paths": {
    "/api/environments/{project_id}/evaluation_runs/": {
      "post": {
        "operationId": "evaluation_runs_create",
        "description": "Create a new evaluation run.\n\nThis endpoint validates the request and enqueues a Temporal workflow\nto asynchronously execute the evaluation.",
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
          "evaluation_runs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "evaluation:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "llm_analytics"
        ]
      }
    }
  }
}
```
