# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_snapshot_history_list.md

# visual_review_runs_snapshot_history_list

## OpenAPI

```json GET /api/projects/{project_id}/visual_review/runs/{id}/snapshot-history/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/{id}/snapshot-history/": {
      "get": {
        "operationId": "visual_review_runs_snapshot_history_list",
        "description": "Recent change history for a snapshot identifier across runs.",
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
            "in": "query",
            "name": "identifier",
            "schema": {
              "type": "string"
            },
            "description": "Snapshot identifier",
            "required": true
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
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedSnapshotHistoryEntryList"
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
      "PaginatedSnapshotHistoryEntryList": {
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
              "$ref": "#/components/schemas/SnapshotHistoryEntry"
            }
          }
        }
      },
      "SnapshotHistoryEntry": {
        "type": "object",
        "properties": {
          "run_id": {
            "type": "string",
            "format": "uuid"
          },
          "result": {
            "type": "string"
          },
          "branch": {
            "type": "string"
          },
          "commit_sha": {
            "type": "string"
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          }
        },
        "required": [
          "branch",
          "commit_sha",
          "created_at",
          "result",
          "run_id"
        ]
      }
    }
  }
}
```
