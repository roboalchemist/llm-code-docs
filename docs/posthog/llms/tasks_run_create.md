# Source: https://posthog.com/docs/open-api-spec/tasks_run_create.md

# tasks_run_create

## OpenAPI

```json POST /api/projects/{project_id}/tasks/{id}/run/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{id}/run/": {
      "post": {
        "operationId": "tasks_run_create",
        "description": "Create a new task run and kick off the workflow.",
        "summary": "Run task",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this task.",
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
          "tasks",
          "tasks"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunCreateRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunCreateRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunCreateRequest"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Task"
                }
              }
            },
            "description": "Task with updated latest run"
          },
          "404": {
            "description": "Task not found"
          }
        },
        "x-explicit-tags": [
          "tasks"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "TaskRunCreateRequest": {
        "type": "object",
        "description": "Request body for creating a new task run",
        "properties": {
          "mode": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TaskRunCreateRequestModeEnum"
              }
            ],
            "default": "background",
            "description": "Execution mode: 'interactive' for user-connected runs, 'background' for autonomous runs\n\n* `interactive` - interactive\n* `background` - background"
          },
          "branch": {
            "type": "string",
            "nullable": true,
            "description": "Git branch to checkout in the sandbox",
            "maxLength": 255
          },
          "resume_from_run_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of a previous run to resume from. Must belong to the same task."
          },
          "pending_user_message": {
            "type": "string",
            "description": "Follow-up user message to include in the resumed run's prompt."
          }
        }
      },
      "Task": {
        "type": "object",
        "description": "Serializer for extracted tasks",
        "properties": {
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "assignee": {
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "title"
        ]
      },
      "TaskRunCreateRequestModeEnum": {
        "enum": [
          "interactive",
          "background"
        ],
        "type": "string",
        "description": "* `interactive` - interactive\n* `background` - background"
      }
    }
  }
}
```
