# Source: https://posthog.com/docs/open-api-spec/tasks_runs_artifacts_create.md

# tasks_runs_artifacts_create

## OpenAPI

```json POST /api/projects/{project_id}/tasks/{task_id}/runs/{id}/artifacts/
{
  "paths": {
    "/api/projects/{project_id}/tasks/{task_id}/runs/{id}/artifacts/": {
      "post": {
        "operationId": "tasks_runs_artifacts_create",
        "description": "Persist task artifacts to S3 and attach them to the run manifest.",
        "summary": "Upload artifacts for a task run",
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
                "$ref": "#/components/schemas/TaskRunArtifactsUploadRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunArtifactsUploadRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/TaskRunArtifactsUploadRequest"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "task:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TaskRunArtifactsUploadResponse"
                }
              }
            },
            "description": "Run with updated artifact manifest"
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            },
            "description": "Invalid artifact payload"
          },
          "404": {
            "description": "Run not found"
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
      "TaskRunArtifactsUploadRequest": {
        "type": "object",
        "properties": {
          "artifacts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TaskRunArtifactUpload"
            },
            "description": "Array of artifacts to upload"
          }
        },
        "required": [
          "artifacts"
        ]
      },
      "TaskRunArtifactsUploadResponse": {
        "type": "object",
        "properties": {
          "artifacts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TaskRunArtifactResponse"
            },
            "description": "Updated list of artifacts on the run"
          }
        },
        "required": [
          "artifacts"
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
      },
      "TaskRunArtifactUpload": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "File name to associate with the artifact",
            "maxLength": 255
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TaskRunArtifactUploadTypeEnum"
              }
            ],
            "description": "Classification for the artifact\n\n* `plan` - plan\n* `context` - context\n* `reference` - reference\n* `output` - output\n* `artifact` - artifact"
          },
          "content": {
            "type": "string",
            "description": "Raw file contents (UTF-8 string or base64 data)"
          },
          "content_type": {
            "type": "string",
            "description": "Optional MIME type for the artifact",
            "maxLength": 255
          }
        },
        "required": [
          "content",
          "name",
          "type"
        ]
      },
      "TaskRunArtifactResponse": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Artifact file name"
          },
          "type": {
            "type": "string",
            "description": "Artifact classification (plan, context, etc.)"
          },
          "size": {
            "type": "integer",
            "description": "Artifact size in bytes"
          },
          "content_type": {
            "type": "string",
            "description": "Optional MIME type"
          },
          "storage_path": {
            "type": "string",
            "description": "S3 object key for the artifact"
          },
          "uploaded_at": {
            "type": "string",
            "description": "Timestamp when the artifact was uploaded"
          }
        },
        "required": [
          "name",
          "storage_path",
          "type",
          "uploaded_at"
        ]
      },
      "TaskRunArtifactUploadTypeEnum": {
        "enum": [
          "plan",
          "context",
          "reference",
          "output",
          "artifact"
        ],
        "type": "string",
        "description": "* `plan` - plan\n* `context` - context\n* `reference` - reference\n* `output` - output\n* `artifact` - artifact"
      }
    }
  }
}
```
