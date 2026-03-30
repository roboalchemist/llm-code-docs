# Source: https://posthog.com/docs/open-api-spec/conversations_tickets_suggest_reply_create.md

# conversations_tickets_suggest_reply_create

## OpenAPI

```json POST /api/projects/{project_id}/conversations/tickets/{id}/suggest_reply/
{
  "paths": {
    "/api/projects/{project_id}/conversations/tickets/{id}/suggest_reply/": {
      "post": {
        "operationId": "conversations_tickets_suggest_reply_create",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this ticket.",
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
          "conversations"
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuggestReplyResponse"
                }
              }
            },
            "description": ""
          },
          "400": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuggestReplyError"
                }
              }
            },
            "description": ""
          },
          "403": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuggestReplyError"
                }
              }
            },
            "description": ""
          },
          "500": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuggestReplyError"
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
      "SuggestReplyResponse": {
        "type": "object",
        "properties": {
          "suggestion": {
            "type": "string"
          }
        },
        "required": [
          "suggestion"
        ]
      },
      "SuggestReplyError": {
        "type": "object",
        "properties": {
          "detail": {
            "type": "string"
          },
          "error_type": {
            "type": "string"
          }
        },
        "required": [
          "detail"
        ]
      }
    }
  }
}
```
