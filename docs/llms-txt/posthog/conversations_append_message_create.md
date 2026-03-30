# Source: https://posthog.com/docs/open-api-spec/conversations_append_message_create.md

# conversations_append_message_create

## OpenAPI

```json POST /api/environments/{project_id}/conversations/{conversation}/append_message/
{
  "paths": {
    "/api/environments/{project_id}/conversations/{conversation}/append_message/": {
      "post": {
        "operationId": "conversations_append_message_create",
        "description": "Appends a message to an existing conversation without triggering AI processing.\nThis is used for client-side generated messages that need to be persisted\n(e.g., support ticket confirmation messages).",
        "parameters": [
          {
            "in": "path",
            "name": "conversation",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this conversation.",
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
          "max",
          "conversations"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MessageMinimal"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/MessageMinimal"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/MessageMinimal"
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
                  "$ref": "#/components/schemas/MessageMinimal"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "max"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "MessageMinimal": {
        "type": "object",
        "description": "Serializer for appending a message to an existing conversation without triggering AI processing.",
        "properties": {
          "content": {
            "type": "string",
            "maxLength": 10000
          }
        },
        "required": [
          "content"
        ]
      }
    }
  }
}
```
