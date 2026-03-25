# Source: https://developers.activecampaign.com/reference/partially-update-a-conversation.md

# Partially Update a Conversation

Partially update a Conversation

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "WhatsApp API",
    "version": "1.0.0",
    "description": "All of the below API endpoints require API key authentication, get your token at https://app.hilos.io/dev/api-keys.\n\nTo use this token, send with every request an `Authorization: Token <your token>` header.\n\nProduction API server is located at api.hilos.io using HTTPS.\n\nNo versioning info is required for now."
  },
  "paths": {
    "/channel/whatsapp/inbox/conversation/{id}/update": {
      "patch": {
        "operationId": "Partially update a Conversation",
        "description": "Partially update a Conversation",
        "summary": "Partially Update a Conversation",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "Conversations"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedConversationEdit"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedConversationEdit"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedConversationEdit"
              }
            }
          }
        },
        "security": [
          {
            "tokenAuth": []
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ConversationEdit"
                }
              }
            },
            "description": ""
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ConversationEdit": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "The UUID of the Conversation."
          },
          "contact": {
            "type": "string",
            "format": "uuid"
          },
          "status": {
            "$ref": "#/components/schemas/ConversationStatusEnum"
          },
          "assigned": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserBasicEdit"
            },
            "description": "The Users assigned to the Conversation."
          },
          "tags": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConversationTag"
            },
            "description": "The Tags assigned to the Conversation."
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "title": "Creado el"
          },
          "source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ConversationSourceEnum"
              }
            ],
            "readOnly": true
          },
          "assigned_team": {
            "type": "integer",
            "description": "The ID of the Team assigned to the Conversation."
          },
          "channel": {
            "type": "integer",
            "nullable": true
          }
        },
        "required": [
          "assigned",
          "contact",
          "created_on",
          "id",
          "source"
        ]
      },
      "ConversationSourceEnum": {
        "enum": [
          "INBOX",
          "AUTO_RESPONSE",
          "API",
          "BROADCAST",
          "FLOW",
          "UNKNOWN"
        ],
        "type": "string",
        "description": "* `INBOX` - Inbox\n* `AUTO_RESPONSE` - Auto Response\n* `API` - Api\n* `BROADCAST` - Broadcast\n* `FLOW` - Flow\n* `UNKNOWN` - Unknown"
      },
      "ConversationStatusEnum": {
        "enum": [
          "CREATED",
          "FLOW",
          "NEW",
          "IN_PROGRESS",
          "RESOLVED",
          "CLOSED"
        ],
        "type": "string",
        "description": "* `CREATED` - Created\n* `FLOW` - Flow\n* `NEW` - New\n* `IN_PROGRESS` - In Progress\n* `RESOLVED` - Resolved\n* `CLOSED` - Closed"
      },
      "ConversationTag": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 100
          }
        },
        "required": [
          "id",
          "name"
        ]
      },
      "PatchedConversationEdit": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "The UUID of the Conversation."
          },
          "contact": {
            "type": "string",
            "format": "uuid"
          },
          "status": {
            "$ref": "#/components/schemas/ConversationStatusEnum"
          },
          "assigned": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserBasicEdit"
            },
            "description": "The Users assigned to the Conversation."
          },
          "tags": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConversationTag"
            },
            "description": "The Tags assigned to the Conversation."
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "title": "Creado el"
          },
          "source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ConversationSourceEnum"
              }
            ],
            "readOnly": true
          },
          "assigned_team": {
            "type": "integer",
            "description": "The ID of the Team assigned to the Conversation."
          },
          "channel": {
            "type": "integer",
            "nullable": true
          }
        }
      },
      "UserBasicEdit": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          }
        },
        "required": [
          "id"
        ]
      }
    },
    "securitySchemes": {
      "tokenAuth": {
        "type": "apiKey",
        "in": "header",
        "name": "Token",
        "description": "Token-based authentication with required prefix \"Token\""
      }
    }
  },
  "x-tagGroups": [
    {
      "name": "Users",
      "tags": [
        "User"
      ]
    },
    {
      "name": "Channels",
      "tags": [
        "WhatsApp",
        "Broadcast"
      ]
    },
    {
      "name": "Flows",
      "tags": [
        "Flow Execution",
        "Flow Execution Contact"
      ]
    },
    {
      "name": "CRM",
      "tags": [
        "Contact",
        "Conversation"
      ]
    },
    {
      "name": "Integrations",
      "tags": [
        "Webhook Subscription"
      ]
    }
  ],
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "description": "Production Server"
    }
  ],
  "tags": [
    {
      "name": "Conversations"
    }
  ]
}
```