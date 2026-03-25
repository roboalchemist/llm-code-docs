# Source: https://posthog.com/docs/open-api-spec/tasks_list.md

# tasks_list

## OpenAPI

```json GET /api/projects/{project_id}/tasks/
{
  "paths": {
    "/api/projects/{project_id}/tasks/": {
      "get": {
        "operationId": "tasks_list",
        "description": "Get a list of tasks for the current project, with optional filtering by origin product, stage, organization, repository, and created_by.",
        "summary": "List tasks",
        "parameters": [
          {
            "in": "query",
            "name": "created_by",
            "schema": {
              "type": "integer"
            },
            "description": "Filter by creator user ID"
          },
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "organization",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Filter by repository organization"
          },
          {
            "in": "query",
            "name": "origin_product",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Filter by origin product"
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
            "in": "query",
            "name": "repository",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Filter by repository name (can include org/repo format)"
          },
          {
            "in": "query",
            "name": "stage",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Filter by task run stage"
          }
        ],
        "tags": [
          "tasks",
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
                  "$ref": "#/components/schemas/PaginatedTaskList"
                }
              }
            },
            "description": "List of tasks"
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
      "PaginatedTaskList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Task"
            }
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
      }
    }
  }
}
```
