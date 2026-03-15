# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_list.md

# visual_review_runs_list

## OpenAPI

```json GET /api/projects/{project_id}/visual_review/runs/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/": {
      "get": {
        "operationId": "visual_review_runs_list",
        "description": "List runs for the team, optionally filtered by review state.",
        "parameters": [
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
            "name": "review_state",
            "schema": {
              "type": "string"
            },
            "description": "Filter by review state"
          }
        ],
        "tags": [
          "visual_review",
          "visual_review"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "visual_review:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedRunList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "visual_review"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedRunList": {
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
              "$ref": "#/components/schemas/Run"
            }
          }
        }
      },
      "Run": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "repo_id": {
            "type": "string",
            "format": "uuid"
          },
          "status": {
            "type": "string"
          },
          "run_type": {
            "type": "string"
          },
          "commit_sha": {
            "type": "string"
          },
          "branch": {
            "type": "string"
          },
          "pr_number": {
            "type": "integer",
            "nullable": true
          },
          "approved": {
            "type": "boolean"
          },
          "approved_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "summary": {
            "$ref": "#/components/schemas/RunSummary"
          },
          "error_message": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "completed_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "is_stale": {
            "type": "boolean"
          },
          "metadata": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "approved",
          "approved_at",
          "branch",
          "commit_sha",
          "completed_at",
          "created_at",
          "error_message",
          "id",
          "pr_number",
          "repo_id",
          "run_type",
          "status",
          "summary"
        ]
      },
      "RunSummary": {
        "type": "object",
        "properties": {
          "total": {
            "type": "integer"
          },
          "changed": {
            "type": "integer"
          },
          "new": {
            "type": "integer"
          },
          "removed": {
            "type": "integer"
          },
          "unchanged": {
            "type": "integer"
          }
        },
        "required": [
          "changed",
          "new",
          "removed",
          "total",
          "unchanged"
        ]
      }
    }
  }
}
```
