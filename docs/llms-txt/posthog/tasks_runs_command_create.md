# Source: https://posthog.com/docs/open-api-spec/tasks_runs_command_create.md

# tasks_runs_command_create

## OpenAPI

```json POST /api/projects/{project_id}/tasks/{task_id}/runs/{id}/command/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/command/": {
      "post": {
        "operationId": "tasks_runs_command_create",
        "description": "Forward a JSON-RPC command to the agent server running in the sandbox. Supports user_message, cancel, and close commands.",
        "summary": "Send command to agent server",
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
                "$ref": "#/components/schemas/TaskRunCommandRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunCommandRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunCommandRequest"
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
                  "$ref": "#/components/schemas/TaskRunCommandResponse"
                }
              }
            },
            "description": "Agent server response"
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            },
            "description": "Invalid command or no active sandbox"
          },
          "404": {
            "description": "Task run not found"
          },
          "502": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            },
            "description": "Agent server unreachable"
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
      "TaskRunCommandRequest": {
        "type": "object",
        "description": "JSON-RPC request to send a command to the agent server in the sandbox.",
        "properties": {
          "jsonrpc": {
            "allOf": [
              {
                "$ref": "#/components/schemas/JsonrpcEnum"
              }
            ],
            "description": "JSON-RPC version, must be '2.0'\n\n* `2.0` - 2.0"
          },
          "method": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MethodEnum"
              }
            ],
            "description": "Command method to execute on the agent server\n\n* `user_message` - user_message\n* `cancel` - cancel\n* `close` - close"
          },
          "params": {
            "type": "object",
            "additionalProperties": {},
            "description": "Parameters for the command"
          },
          "id": {
            "description": "Optional JSON-RPC request ID (string or number)"
          }
        },
        "required": [
          "jsonrpc",
          "method"
        ]
      },
      "TaskRunCommandResponse": {
        "type": "object",
        "description": "Response from the agent server command endpoint.",
        "properties": {
          "jsonrpc": {
            "type": "string",
            "description": "JSON-RPC version"
          },
          "id": {
            "description": "Request ID echoed back (string or number)"
          },
          "result": {
            "type": "object",
            "additionalProperties": {},
            "description": "Command result on success"
          },
          "error": {
            "type": "object",
            "additionalProperties": {},
            "description": "Error details on failure"
          }
        },
        "required": [
          "jsonrpc"
        ]
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Error message"
          }
        },
        "required": [
          "error"
        ]
      },
      "JsonrpcEnum": {
        "enum": [
          "2.0"
        ],
        "type": "string",
        "description": "* `2.0` - 2.0"
      },
      "MethodEnum": {
        "enum": [
          "user_message",
          "cancel",
          "close"
        ],
        "type": "string",
        "description": "* `user_message` - user_message\n* `cancel` - cancel\n* `close` - close"
      }
    }
  }
}
```
