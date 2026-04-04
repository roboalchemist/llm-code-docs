# Source: https://posthog.com/docs/open-api-spec/tasks_runs_logs_retrieve.md

# tasks_runs_logs_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/tasks/{task_id}/runs/{id}/logs/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/logs/": {
      "get": {
        "operationId": "tasks_runs_logs_retrieve",
        "description": "Fetch the logs for a task run. Returns JSONL formatted log entries.",
        "summary": "Get task run logs",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this task run.",
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
          },
          {
            "in": "path",
            "name": "task_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "task-runs",
          "tasks"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:read"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "Log content in JSONL format"
          },
          "404": {
            "description": "Task run not found"
          }
        },
        "x-explicit-tags": [
          "task-runs"
        ]
      }
    }
  }
}
```
