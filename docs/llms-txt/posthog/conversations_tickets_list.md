# Source: https://posthog.com/docs/open-api-spec/conversations_tickets_list.md

# conversations_tickets_list

## OpenAPI

```json GET /api/projects/{project_id}/conversations/tickets/
{
  "paths": {
    "/api/projects/{project_id}/conversations/tickets/": {
      "get": {
        "operationId": "conversations_tickets_list",
        "description": "List tickets with person data attached.",
        "parameters": [
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "ticket:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedTicketList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "conversations"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedTicketList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Ticket"
            }
          }
        }
      },
      "Ticket": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "ticket_number": {
            "type": "integer",
            "readOnly": true
          },
          "channel_source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ChannelSourceEnum"
              }
            ],
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "readOnly": true
          },
          "status": {
            "$ref": "#/components/schemas/TicketStatusEnum"
          },
          "priority": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/PriorityEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "assignee": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TicketAssignment"
              }
            ],
            "readOnly": true
          },
          "anonymous_traits": {},
          "ai_resolved": {
            "type": "boolean"
          },
          "escalation_reason": {
            "type": "string",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "message_count": {
            "type": "integer",
            "readOnly": true
          },
          "last_message_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_message_text": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "unread_team_count": {
            "type": "integer",
            "readOnly": true
          },
          "unread_customer_count": {
            "type": "integer",
            "readOnly": true
          },
          "session_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "session_context": {
            "readOnly": true
          },
          "sla_due_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "slack_channel_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "slack_thread_ts": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "slack_team_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "person": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TicketPerson"
              }
            ],
            "readOnly": true,
            "nullable": true
          },
          "tags": {
            "type": "array",
            "items": {}
          }
        },
        "required": [
          "assignee",
          "channel_source",
          "created_at",
          "distinct_id",
          "id",
          "last_message_at",
          "last_message_text",
          "message_count",
          "person",
          "session_context",
          "session_id",
          "slack_channel_id",
          "slack_team_id",
          "slack_thread_ts",
          "ticket_number",
          "unread_customer_count",
          "unread_team_count",
          "updated_at"
        ]
      },
      "ChannelSourceEnum": {
        "enum": [
          "widget",
          "email",
          "slack"
        ],
        "type": "string",
        "description": "* `widget` - Widget\n* `email` - Email\n* `slack` - Slack"
      },
      "TicketStatusEnum": {
        "enum": [
          "new",
          "open",
          "pending",
          "on_hold",
          "resolved"
        ],
        "type": "string",
        "description": "* `new` - New\n* `open` - Open\n* `pending` - Pending\n* `on_hold` - On hold\n* `resolved` - Resolved"
      },
      "PriorityEnum": {
        "enum": [
          "low",
          "medium",
          "high"
        ],
        "type": "string",
        "description": "* `low` - Low\n* `medium` - Medium\n* `high` - High"
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
      },
      "TicketAssignment": {
        "type": "object",
        "description": "Serializer for ticket assignment (user or role).",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "type": {
            "type": "string",
            "readOnly": true
          },
          "user": {
            "type": "string",
            "readOnly": true
          },
          "role": {
            "type": "string",
            "readOnly": true
          }
        },
        "required": [
          "id",
          "role",
          "type",
          "user"
        ]
      },
      "TicketPerson": {
        "type": "object",
        "description": "Minimal person serializer for embedding in ticket responses.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "distinct_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "readOnly": true
          },
          "properties": {
            "type": "object",
            "additionalProperties": {},
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "is_identified": {
            "type": "boolean",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "distinct_ids",
          "id",
          "is_identified",
          "name",
          "properties"
        ]
      }
    }
  }
}
```
