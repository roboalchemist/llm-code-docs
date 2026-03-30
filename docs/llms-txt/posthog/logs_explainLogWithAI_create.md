# Source: https://posthog.com/docs/open-api-spec/logs_explainLogWithAI_create.md

# logs_explainLogWithAI_create

## OpenAPI

```json POST /api/environments/{project_id}/logs/explainLogWithAI/
{
  "paths": {
    "/api/environments/{project_id}/logs/explainLogWithAI/": {
      "post": {
        "operationId": "logs_explainLogWithAI_create",
        "description": "Explain a log entry using AI.\n\nPOST /api/environments/:id/logs/explainLogWithAI/",
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
          "logs"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ExplainRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ExplainRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ExplainRequest"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "logs:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ExplainRequest"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "logs"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "ExplainRequest": {
        "type": "object",
        "properties": {
          "uuid": {
            "type": "string",
            "description": "UUID of the log entry to explain"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp of the log entry (used for efficient lookup)"
          },
          "force_refresh": {
            "type": "boolean",
            "default": false,
            "description": "Force regenerate explanation, bypassing cache"
          }
        },
        "required": [
          "timestamp",
          "uuid"
        ]
      }
    }
  }
}
```
