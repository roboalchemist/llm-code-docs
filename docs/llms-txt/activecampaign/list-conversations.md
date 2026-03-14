# Source: https://developers.activecampaign.com/reference/list-conversations.md

# List Conversations

Lists Conversations. 

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
    "/channel/whatsapp/inbox/conversation": {
      "get": {
        "operationId": "List Conversations",
        "description": "Lists Conversations. ",
        "summary": "List Conversations",
        "parameters": [
          {
            "in": "query",
            "name": "contact",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Contact Id to filter the Conversations and only get those from that Contact.",
            "examples": {
              "OnlyReturnTheConversationsOfThisContact": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Only return the Conversations of this Contact"
              }
            }
          },
          {
            "name": "page",
            "required": false,
            "in": "query",
            "description": "A page number within the paginated result set.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "page_size",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "search",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "tags": [
          "Conversations"
        ],
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
                  "$ref": "#/components/schemas/PaginatedConversationReadSimpleList"
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
      "ConversationReadSimple": {
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
            "allOf": [
              {
                "$ref": "#/components/schemas/ConversationStatusEnum"
              }
            ],
            "readOnly": true
          },
          "first_message": {
            "allOf": [
              {
                "$ref": "#/components/schemas/WhatsAppMessageSimple"
              }
            ],
            "description": "The first Message of the Conversation."
          },
          "assigned": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserSimple"
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
          "first_message",
          "id",
          "source",
          "status"
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
      "MessageSourceEnum": {
        "enum": [
          "INBOUND",
          "INBOX",
          "AUTO_RESPONSE",
          "API",
          "BROADCAST",
          "FLOW"
        ],
        "type": "string",
        "description": "* `INBOUND` - Inbound\n* `INBOX` - Inbox\n* `AUTO_RESPONSE` - Auto Response\n* `API` - Api\n* `BROADCAST` - Broadcast\n* `FLOW` - Flow"
      },
      "MessageStatusEnum": {
        "enum": [
          "new",
          "retry",
          "accepted",
          "sending",
          "sent",
          "receiving",
          "received",
          "delivered",
          "undelivered",
          "failed",
          "read",
          "deleted"
        ],
        "type": "string",
        "description": "* `new` - New\n* `retry` - Retry\n* `accepted` - Accepted\n* `sending` - Sending\n* `sent` - Sent\n* `receiving` - Receiving\n* `received` - Received\n* `delivered` - Delivered\n* `undelivered` - Undelivered\n* `failed` - Failed\n* `read` - Read\n* `deleted` - Deleted"
      },
      "MessageTypeEnum": {
        "enum": [
          "audio",
          "voice",
          "button",
          "document",
          "text",
          "image",
          "interactive",
          "order",
          "sticker",
          "system",
          "unknown",
          "video",
          "unsupported",
          "location",
          "contacts",
          "template",
          "reaction",
          "ephemeral",
          "request_welcome"
        ],
        "type": "string",
        "description": "* `audio` - Audio\n* `voice` - Voice\n* `button` - Button\n* `document` - Document\n* `text` - Text\n* `image` - Image\n* `interactive` - Interactive\n* `order` - Order\n* `sticker` - Sticker\n* `system` - System\n* `unknown` - Unknown\n* `video` - Video\n* `unsupported` - Unsupported\n* `location` - Location\n* `contacts` - Contacts\n* `template` - Template\n* `reaction` - Reaction\n* `ephemeral` - Ephemeral\n* `request_welcome` - Request Welcome"
      },
      "PaginatedConversationReadSimpleList": {
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
            "example": "http://api.example.org/accounts/?page=4"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?page=2"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConversationReadSimple"
            }
          }
        }
      },
      "SimpleUser": {
        "type": "object",
        "properties": {
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
            "maxLength": 254
          },
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "profile_image": {
            "type": "string",
            "format": "uri",
            "nullable": true
          },
          "role": {
            "type": "integer",
            "nullable": true
          }
        },
        "required": [
          "email",
          "id"
        ]
      },
      "UserSimple": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "first_name": {
            "type": "string",
            "readOnly": true
          },
          "last_name": {
            "type": "string",
            "readOnly": true
          },
          "email": {
            "type": "string",
            "format": "email",
            "readOnly": true
          },
          "account": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "profile_image": {
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "date_joined": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "account",
          "date_joined",
          "email",
          "first_name",
          "id",
          "last_name",
          "profile_image"
        ]
      },
      "WhatsAppMessageSimple": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "to_number": {
            "type": "string",
            "readOnly": true
          },
          "from_number": {
            "type": "string",
            "readOnly": true
          },
          "body": {
            "type": "string",
            "nullable": true
          },
          "direction": {
            "type": "string"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "contact": {
            "type": "string"
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MessageStatusEnum"
              }
            ],
            "readOnly": true
          },
          "queued_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "accepted_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "sent_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "delivered_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "read_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "failed_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "provider_id": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "provider_error_code": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "provider_error_message": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "sent_by": {
            "$ref": "#/components/schemas/SimpleUser"
          },
          "is_deleted": {
            "type": "boolean",
            "readOnly": true
          },
          "content": {
            "readOnly": true,
            "nullable": true
          },
          "whatsapp_template": {
            "type": "string",
            "format": "uuid",
            "readOnly": true,
            "nullable": true
          },
          "content_type": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "content_url": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "maxLength": 2000
          },
          "msg_type": {
            "$ref": "#/components/schemas/MessageTypeEnum"
          },
          "failed_attempts": {
            "type": "integer",
            "readOnly": true
          },
          "source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MessageSourceEnum"
              }
            ],
            "readOnly": true
          }
        },
        "required": [
          "accepted_on",
          "contact",
          "content",
          "content_type",
          "delivered_on",
          "direction",
          "failed_attempts",
          "failed_on",
          "from_number",
          "id",
          "is_deleted",
          "provider_error_code",
          "provider_error_message",
          "provider_id",
          "queued_on",
          "read_on",
          "sent_by",
          "sent_on",
          "source",
          "status",
          "timestamp",
          "to_number",
          "whatsapp_template"
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