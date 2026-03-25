# Source: https://posthog.com/docs/open-api-spec/tasks_runs_connection_token_retrieve.md

# tasks_runs_connection_token_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/tasks/{task_id}/runs/{id}/connection_token/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/connection_token/": {
      "get": {
        "operationId": "tasks_runs_connection_token_retrieve",
        "description": "Generate a JWT token for direct connection to the sandbox. Valid for 24 hours.",
        "summary": "Get sandbox connection token",
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
                  "$ref": "#/components/schemas/ConnectionTokenResponse"
                }
              }
            },
            "description": "Connection token for direct sandbox connection"
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
  },
  "components": {
    "schemas": {
      "ConnectionTokenResponse": {
        "type": "object",
        "description": "Response containing a JWT token for direct sandbox connection",
        "properties": {
          "token": {
            "type": "string",
            "description": "JWT token for authenticating with the sandbox"
          }
        },
        "required": [
          "token"
        ]
      }
    }
  }
}
```
