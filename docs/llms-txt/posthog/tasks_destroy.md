# Source: https://posthog.com/docs/open-api-spec/tasks_destroy.md

# tasks_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/tasks/{id}/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{id}/": {
      "delete": {
        "operationId": "tasks_destroy",
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
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "tasks"
        ]
      }
    }
  }
}
```
