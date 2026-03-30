# Source: https://posthog.com/docs/open-api-spec/tasks_update.md

# tasks_update

## OpenAPI

```json PUT /api/projects/{project_id}/tasks/{id}/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{id}/": {
      "put": {
        "operationId": "tasks_update",
        "description": "API for managing tasks within a project. Tasks represent units of work to be performed by an agent.",
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
                "$ref": "#/components/schemas/Task"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Task"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Task"
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
                  "$ref": "#/components/schemas/Task"
                }
              }
            },
            "description": ""
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
      }
    }
  }
}
```
