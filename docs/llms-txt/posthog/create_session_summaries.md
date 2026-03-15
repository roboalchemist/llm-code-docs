# Source: https://posthog.com/docs/open-api-spec/create_session_summaries.md

# create_session_summaries

## OpenAPI

```json POST /api/environments/{project_id}/session_summaries/create_session_summaries/
{
  "paths": {
    "/api/environments/{project_id}/session_summaries/create_session_summaries/": {
      "post": {
        "operationId": "create_session_summaries",
        "description": "Generate AI summary for a group of session recordings to find patterns and generate a notebook.",
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
          "session_summaries"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SessionSummaries"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/SessionSummaries"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/SessionSummaries"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SessionSummaries"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "SessionSummaries": {
        "type": "object",
        "properties": {
          "session_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of session IDs to summarize (max 300)",
            "maxItems": 300,
            "minItems": 1
          },
          "focus_area": {
            "type": "string",
            "description": "Optional focus area for the summarization",
            "maxLength": 500
          }
        },
        "required": [
          "session_ids"
        ]
      }
    }
  }
}
```
