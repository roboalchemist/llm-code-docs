# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_approve_create.md

# visual_review_runs_approve_create

## OpenAPI

```json POST /api/projects/{project_id}/visual_review/runs/{id}/approve/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/{id}/approve/": {
      "post": {
        "operationId": "visual_review_runs_approve_create",
        "description": "Approve visual changes for snapshots in this run.",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ApproveRunRequestInput"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ApproveRunRequestInput"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ApproveRunRequestInput"
              }
            }
          },
          "required": true
        },
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
                  "$ref": "#/components/schemas/Run"
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
      "ApproveRunRequestInput": {
        "type": "object",
        "properties": {
          "snapshots": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ApproveSnapshotInput"
            }
          },
          "commit_to_github": {
            "type": "boolean"
          }
        },
        "required": [
          "snapshots"
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
      "ApproveSnapshotInput": {
        "type": "object",
        "properties": {
          "identifier": {
            "type": "string"
          },
          "new_hash": {
            "type": "string"
          }
        },
        "required": [
          "identifier",
          "new_hash"
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
