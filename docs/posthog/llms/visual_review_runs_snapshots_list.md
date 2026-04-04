# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_snapshots_list.md

# visual_review_runs_snapshots_list

## OpenAPI

```json GET /api/projects/{project_id}/visual_review/runs/{id}/snapshots/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/{id}/snapshots/": {
      "get": {
        "operationId": "visual_review_runs_snapshots_list",
        "description": "Get all snapshots for a run with diff results.",
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
                  "$ref": "#/components/schemas/PaginatedSnapshotList"
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
      "PaginatedSnapshotList": {
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
              "$ref": "#/components/schemas/Snapshot"
            }
          }
        }
      },
      "Snapshot": {
        "type": "object",
        "properties": {
          "current_artifact": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Artifact"
              }
            ],
            "nullable": true
          },
          "baseline_artifact": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Artifact"
              }
            ],
            "nullable": true
          },
          "diff_artifact": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Artifact"
              }
            ],
            "nullable": true
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "identifier": {
            "type": "string"
          },
          "result": {
            "type": "string"
          },
          "diff_percentage": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "diff_pixel_count": {
            "type": "integer",
            "nullable": true
          },
          "review_state": {
            "type": "string"
          },
          "reviewed_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "approved_hash": {
            "type": "string"
          },
          "metadata": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "approved_hash",
          "diff_percentage",
          "diff_pixel_count",
          "id",
          "identifier",
          "result",
          "review_state",
          "reviewed_at"
        ]
      },
      "Artifact": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "content_hash": {
            "type": "string"
          },
          "width": {
            "type": "integer",
            "nullable": true
          },
          "height": {
            "type": "integer",
            "nullable": true
          },
          "download_url": {
            "type": "string",
            "nullable": true
          }
        },
        "required": [
          "content_hash",
          "download_url",
          "height",
          "id",
          "width"
        ]
      }
    }
  }
}
```
