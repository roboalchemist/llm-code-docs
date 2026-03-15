# Source: https://posthog.com/docs/open-api-spec/tasks_runs_stream_retrieve.md

# tasks_runs_stream_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/tasks/{task_id}/runs/{id}/stream/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/stream/": {
      "get": {
        "operationId": "tasks_runs_stream_retrieve",
        "description": "API for managing task runs. Each run represents an execution of a task.",
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
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TaskRunDetail"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "task-runs"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "TaskRunDetail": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "task": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "stage": {
            "type": "string",
            "nullable": true,
            "description": "Current stage for this run (e.g., 'research', 'plan', 'build')",
            "maxLength": 100
          },
          "branch": {
            "type": "string",
            "nullable": true,
            "description": "Branch name for the run",
            "maxLength": 255
          },
          "status": {
            "$ref": "#/components/schemas/TaskRunDetailStatusEnum"
          },
          "environment": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EnvironmentEnum"
              }
            ],
            "description": "Execution environment\n\n* `local` - Local\n* `cloud` - Cloud"
          },
          "log_url": {
            "type": "string",
            "nullable": true,
            "description": "Presigned S3 URL for log access (valid for 1 hour).",
            "readOnly": true
          },
          "error_message": {
            "type": "string",
            "nullable": true,
            "description": "Error message if execution failed"
          },
          "output": {
            "nullable": true,
            "description": "Run output data (e.g., PR URL, commit SHA, etc.)"
          },
          "state": {
            "description": "Run state data for resuming or tracking execution state"
          },
          "artifacts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TaskRunArtifactResponse"
            },
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "completed_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "artifacts",
          "completed_at",
          "created_at",
          "id",
          "log_url",
          "task",
          "updated_at"
        ]
      },
      "TaskRunDetailStatusEnum": {
        "enum": [
          "not_started",
          "queued",
          "in_progress",
          "completed",
          "failed",
          "cancelled"
        ],
        "type": "string",
        "description": "* `not_started` - Not Started\n* `queued` - Queued\n* `in_progress` - In Progress\n* `completed` - Completed\n* `failed` - Failed\n* `cancelled` - Cancelled"
      },
      "EnvironmentEnum": {
        "enum": [
          "local",
          "cloud"
        ],
        "type": "string",
        "description": "* `local` - Local\n* `cloud` - Cloud"
      },
      "TaskRunArtifactResponse": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Artifact file name"
          },
          "type": {
            "type": "string",
            "description": "Artifact classification (plan, context, etc.)"
          },
          "size": {
            "type": "integer",
            "description": "Artifact size in bytes"
          },
          "content_type": {
            "type": "string",
            "description": "Optional MIME type"
          },
          "storage_path": {
            "type": "string",
            "description": "S3 object key for the artifact"
          },
          "uploaded_at": {
            "type": "string",
            "description": "Timestamp when the artifact was uploaded"
          }
        },
        "required": [
          "name",
          "storage_path",
          "type",
          "uploaded_at"
        ]
      }
    }
  }
}
```
