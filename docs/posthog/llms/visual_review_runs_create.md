# Source: https://posthog.com/docs/open-api-spec/visual_review_runs_create.md

# visual_review_runs_create

## OpenAPI

```json POST /api/projects/{project_id}/visual_review/runs/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/runs/": {
      "post": {
        "operationId": "visual_review_runs_create",
        "description": "Create a new run from a CI manifest.",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateRunInput"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/CreateRunInput"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/CreateRunInput"
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
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateRunResult"
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
      "CreateRunInput": {
        "type": "object",
        "properties": {
          "repo_id": {
            "type": "string",
            "format": "uuid"
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
          "snapshots": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SnapshotManifestItem"
            }
          },
          "pr_number": {
            "type": "integer",
            "nullable": true
          },
          "baseline_hashes": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "metadata": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "branch",
          "commit_sha",
          "repo_id",
          "run_type",
          "snapshots"
        ]
      },
      "CreateRunResult": {
        "type": "object",
        "properties": {
          "run_id": {
            "type": "string",
            "format": "uuid"
          },
          "uploads": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UploadTarget"
            }
          }
        },
        "required": [
          "run_id",
          "uploads"
        ]
      },
      "SnapshotManifestItem": {
        "type": "object",
        "properties": {
          "identifier": {
            "type": "string"
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
          "metadata": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "content_hash",
          "identifier"
        ]
      },
      "UploadTarget": {
        "type": "object",
        "properties": {
          "content_hash": {
            "type": "string"
          },
          "url": {
            "type": "string"
          },
          "fields": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          }
        },
        "required": [
          "content_hash",
          "fields",
          "url"
        ]
      }
    }
  }
}
```
