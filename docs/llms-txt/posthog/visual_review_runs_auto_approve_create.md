# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_auto_approve_create.md

# visual_review_runs_auto_approve_create

## OpenAPI

```json POST /api/projects/{project_id}/visual_review/runs/{id}/auto-approve/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/{id}/auto-approve/": {
      "post": {
        "operationId": "visual_review_runs_auto_approve_create",
        "description": "Auto-approve all changes and return signed baseline YAML.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
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
          "visual_review",
          "visual_review"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "visual_review:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AutoApproveResult"
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
      "AutoApproveResult": {
        "type": "object",
        "properties": {
          "run": {
            "$ref": "#/components/schemas/Run"
          },
          "baseline_content": {
            "type": "string"
          }
        },
        "required": [
          "baseline_content",
          "run"
        ]
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
