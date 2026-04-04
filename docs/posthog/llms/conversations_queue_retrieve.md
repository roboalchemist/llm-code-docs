# Source: https://posthog.com/docs/open-api-spec/conversations_queue_retrieve.md

# conversations_queue_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/conversations/{conversation}/queue/
{
  "paths": {
    "/api/environments/{project_id}/conversations/{conversation}/queue/": {
      "get": {
        "operationId": "conversations_queue_retrieve",
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
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Conversation"
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
      "Conversation": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ConversationStatusEnum"
              }
            ],
            "readOnly": true
          },
          "title": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "description": "Title of the conversation."
          },
          "user": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ConversationTypeEnum"
              }
            ],
            "readOnly": true
          },
          "is_internal": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true,
            "description": "Whether this conversation was created during an impersonated session (e.g., by support agents). Internal conversations are hidden from customers."
          },
          "slack_thread_key": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "description": "Unique key for Slack thread: '{workspace_id}:{channel}:{thread_ts}'"
          },
          "slack_workspace_domain": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "description": "Slack workspace subdomain (e.g. 'posthog' for posthog.slack.com)"
          },
          "messages": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "readOnly": true
          },
          "has_unsupported_content": {
            "type": "boolean",
            "readOnly": true
          },
          "agent_mode": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "is_sandbox": {
            "type": "boolean",
            "readOnly": true
          },
          "pending_approvals": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "description": "Return pending approval cards as structured data.\n\nCombines metadata from conversation.approval_decisions with payload from checkpoint\ninterrupts (single source of truth for payload data).",
            "readOnly": true
          }
        },
        "required": [
          "agent_mode",
          "created_at",
          "has_unsupported_content",
          "id",
          "is_internal",
          "is_sandbox",
          "messages",
          "pending_approvals",
          "slack_thread_key",
          "slack_workspace_domain",
          "status",
          "title",
          "type",
          "updated_at",
          "user"
        ]
      },
      "ConversationStatusEnum": {
        "enum": [
          "idle",
          "in_progress",
          "canceling"
        ],
        "type": "string",
        "description": "* `idle` - Idle\n* `in_progress` - In progress\n* `canceling` - Canceling"
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "ConversationTypeEnum": {
        "enum": [
          "assistant",
          "tool_call",
          "deep_research",
          "slack"
        ],
        "type": "string",
        "description": "* `assistant` - Assistant\n* `tool_call` - Tool call\n* `deep_research` - Deep research\n* `slack` - Slack"
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
