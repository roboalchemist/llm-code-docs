# Source: https://posthog.com/docs/open-api-spec/conversations_create.md

# conversations_create

## OpenAPI

```json POST /api/environments/{project_id}/conversations/
{
  "paths": {
    "/api/environments/{project_id}/conversations/": {
      "post": {
        "operationId": "conversations_create",
        "description": "Unified endpoint that handles both conversation creation and streaming.\n\n- If message is provided: Start new conversation processing\n- If no message: Stream from existing conversation",
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
          "max",
          "conversations"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Message"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Message"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Message"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "conversation:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Message"
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
      "Message": {
        "type": "object",
        "description": "Serializer for appending a message to an existing conversation without triggering AI processing.",
        "properties": {
          "content": {
            "type": "string",
            "nullable": true,
            "maxLength": 40000
          },
          "conversation": {
            "type": "string",
            "format": "uuid"
          },
          "contextual_tools": {
            "type": "object",
            "additionalProperties": {}
          },
          "ui_context": {},
          "billing_context": {},
          "trace_id": {
            "type": "string",
            "format": "uuid"
          },
          "session_id": {
            "type": "string"
          },
          "agent_mode": {
            "$ref": "#/components/schemas/AgentModeEnum"
          },
          "is_sandbox": {
            "type": "boolean",
            "default": false
          },
          "resume_payload": {
            "nullable": true
          }
        },
        "required": [
          "content",
          "conversation",
          "trace_id"
        ]
      },
      "AgentModeEnum": {
        "enum": [
          "product_analytics",
          "sql",
          "session_replay",
          "error_tracking",
          "plan",
          "execution",
          "survey",
          "onboarding",
          "research",
          "flags",
          "llm_analytics",
          "sandbox"
        ],
        "type": "string",
        "description": "* `product_analytics` - product_analytics\n* `sql` - sql\n* `session_replay` - session_replay\n* `error_tracking` - error_tracking\n* `plan` - plan\n* `execution` - execution\n* `survey` - survey\n* `onboarding` - onboarding\n* `research` - research\n* `flags` - flags\n* `llm_analytics` - llm_analytics\n* `sandbox` - sandbox"
      }
    }
  }
}
```
