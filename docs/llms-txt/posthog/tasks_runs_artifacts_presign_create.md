# Source: https://posthog.com/docs/open-api-spec/tasks_runs_artifacts_presign_create.md

# tasks_runs_artifacts_presign_create

## OpenAPI

```json POST /api/projects/{project_id}/tasks/{task_id}/runs/{id}/artifacts/presign/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/artifacts/presign/": {
      "post": {
        "operationId": "tasks_runs_artifacts_presign_create",
        "description": "Returns a temporary, signed URL that can be used to download a specific artifact.",
        "summary": "Generate presigned URL for an artifact",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this task run.",
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
          },
          {
            "in": "path",
            "name": "task_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "task-runs",
          "tasks"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunArtifactPresignRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunArtifactPresignRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunArtifactPresignRequest"
              }
            }
          },
          "required": true
        },
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
                  "$ref": "#/components/schemas/TaskRunArtifactPresignResponse"
                }
              }
            },
            "description": "Presigned URL for the requested artifact"
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            },
            "description": "Invalid request"
          },
          "404": {
            "description": "Artifact not found"
          }
        },
        "x-explicit-tags": [
          "task-runs"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "TaskRunArtifactPresignRequest": {
        "type": "object",
        "properties": {
          "storage_path": {
            "type": "string",
            "description": "S3 storage path returned in the artifact manifest",
            "maxLength": 500
          }
        },
        "required": [
          "storage_path"
        ]
      },
      "TaskRunArtifactPresignResponse": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "format": "uri",
            "description": "Presigned URL for downloading the artifact"
          },
          "expires_in": {
            "type": "integer",
            "description": "URL expiry in seconds"
          }
        },
        "required": [
          "expires_in",
          "url"
        ]
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Error message"
          }
        },
        "required": [
          "error"
        ]
      }
    }
  }
}
```
