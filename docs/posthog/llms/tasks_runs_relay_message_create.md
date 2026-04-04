# Source: https://posthog.com/docs/open-api-spec/tasks_runs_relay_message_create.md

# tasks_runs_relay_message_create

## OpenAPI

```json POST /api/projects/{project_id}/tasks/{task_id}/runs/{id}/relay_message/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/relay_message/": {
      "post": {
        "operationId": "tasks_runs_relay_message_create",
        "description": "Queue a Slack relay workflow to post a run message into the mapped Slack thread.",
        "summary": "Relay run message to Slack",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunRelayMessageRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunRelayMessageRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunRelayMessageRequest"
              }
            }
          },
          "required": true
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
                  "$ref": "#/components/schemas/TaskRunRelayMessageResponse"
                }
              }
            },
            "description": "Relay accepted"
          },
          "404": {
            "description": "Run not found"
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
      "TaskRunRelayMessageRequest": {
        "type": "object",
        "properties": {
          "text": {
            "type": "string",
            "maxLength": 10000
          }
        },
        "required": [
          "text"
        ]
      },
      "TaskRunRelayMessageResponse": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string",
            "description": "Relay status: 'accepted' or 'skipped'"
          },
          "relay_id": {
            "type": "string",
            "description": "Relay workflow ID when accepted"
          }
        },
        "required": [
          "status"
        ]
      }
    }
  }
}
```
