# Source: https://posthog.com/docs/open-api-spec/tasks_runs_session_logs_retrieve.md

# tasks_runs_session_logs_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/tasks/{task_id}/runs/{id}/session_logs/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/session_logs/": {
      "get": {
        "operationId": "tasks_runs_session_logs_retrieve",
        "description": "Fetch session log entries for a task run with optional filtering by timestamp, event type, and limit.",
        "summary": "Get filtered task run session logs",
        "parameters": [
          {
            "in": "query",
            "name": "after",
            "schema": {
              "type": "string",
              "format": "date-time"
            },
            "description": "Only return events after this ISO8601 timestamp"
          },
          {
            "in": "query",
            "name": "event_types",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Comma-separated list of event types to include"
          },
          {
            "in": "query",
            "name": "exclude_types",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Comma-separated list of event types to exclude"
          },
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
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "maximum": 5000,
              "minimum": 1,
              "default": 1000
            },
            "description": "Maximum number of entries to return (default 1000, max 5000)"
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
            "description": "Filtered log events as JSON array"
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
