# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_counts_retrieve.md

# visual_review_runs_counts_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/visual_review/runs/counts/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/counts/": {
      "get": {
        "operationId": "visual_review_runs_counts_retrieve",
        "description": "Review state counts for the runs list.",
        "parameters": [
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
                  "$ref": "#/components/schemas/ReviewStateCounts"
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
      "ReviewStateCounts": {
        "type": "object",
        "properties": {
          "needs_review": {
            "type": "integer"
          },
          "clean": {
            "type": "integer"
          },
          "processing": {
            "type": "integer"
          },
          "stale": {
            "type": "integer"
          }
        },
        "required": [
          "clean",
          "needs_review",
          "processing",
          "stale"
        ]
      }
    }
  }
}
```
