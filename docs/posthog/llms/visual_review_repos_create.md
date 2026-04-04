# Source: https://posthog.com/docs/open-api-spec/visual_review_repos_create.md

# visual_review_repos_create

## OpenAPI

```json POST /api/projects/{project_id}/visual_review/repos/
{
  "paths": {
    "/api/projects/{project_id}/visual_review/repos/": {
      "post": {
        "operationId": "visual_review_repos_create",
        "description": "Create a new repo.",
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
                "$ref": "#/components/schemas/CreateRepoInput"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/CreateRepoInput"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/CreateRepoInput"
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
      "CreateRepoInput": {
        "type": "object",
        "properties": {
          "repo_full_name": {
            "type": "string"
          },
          "repo_external_id": {
            "type": "integer",
            "nullable": true
          }
        },
        "required": [
          "repo_full_name"
        ]
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
