# Source: https://posthog.com/docs/open-api-spec/visual_review_repos_partial_update.md

# visual_review_repos_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/visual_review/repos/{id}/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/repos/{id}/": {
      "patch": {
        "operationId": "visual_review_repos_partial_update",
        "description": "Update a repo's settings.",
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
                "$ref": "#/components/schemas/PatchedUpdateRepoRequestInput"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedUpdateRepoRequestInput"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedUpdateRepoRequestInput"
              }
            }
          }
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
                  "$ref": "#/components/schemas/Repo"
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
      "PatchedUpdateRepoRequestInput": {
        "type": "object",
        "properties": {
          "baseline_file_paths": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "nullable": true
          }
        }
      },
      "Repo": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "team_id": {
            "type": "integer"
          },
          "repo_external_id": {
            "type": "integer"
          },
          "repo_full_name": {
            "type": "string"
          },
          "baseline_file_paths": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          }
        },
        "required": [
          "baseline_file_paths",
          "created_at",
          "id",
          "repo_external_id",
          "repo_full_name",
          "team_id"
        ]
      }
    }
  }
}
```
