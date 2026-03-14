# Source: https://developers.activecampaign.com/reference/list-flow-execution-contact.md

# List Flow Execution Contacts

Lists Flow Execution Contacts.

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
    "/channel/whatsapp/flow-execution-contact": {
      "get": {
        "operationId": "List Flow Execution Contact",
        "description": "Lists Flow Execution Contacts.",
        "summary": "List Flow Execution Contacts",
        "parameters": [
          {
            "in": "query",
            "name": "contact",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Contact Id to filter the Flow Execution Contacts and only get those from that Contact.",
            "examples": {
              "OnlyReturnTheFlowExecutionsContactOfThisContact": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Only return the Flow Executions Contact of this Contact"
              }
            }
          },
          {
            "in": "query",
            "name": "execution_steps__step_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "in": "query",
            "name": "flow",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Flow Id to filter the Flow Execution Contacts and only get those from that Flow.",
            "examples": {
              "OnlyReturnTheFlowExecutionsContactOfThisFlow": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Only return the Flow Executions Contact of this flow"
              }
            }
          },
          {
            "in": "query",
            "name": "flow_execution",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Flow Execution Id to filter the Flow Execution Contacts and only get those from that Flow Execution.",
            "examples": {
              "OnlyReturnTheFlowExecutionsContactOfThisFlowExecution": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Only return the Flow Executions Contact of this Flow Execution"
              }
            }
          },
          {
            "in": "query",
            "name": "flow_version",
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "in": "query",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "in": "query",
            "name": "is_active",
            "schema": {
              "type": "boolean"
            },
            "description": "A boolean param to filter between active/in progress Flow Execution Contacs.\n\n If the parameter is omitted it will respond with Flow Execution Contacts with any `status`.",
            "examples": {
              "OnlyReturnTheFlowExecutionsContactThatAreWithStatus`READY`Or`RUNNING`.": {
                "value": [
                  "true",
                  "any-truthy-value",
                  1
                ],
                "summary": "Only return the Flow Executions Contact that are with status `READY` or `RUNNING`."
              },
              "OnlyReturnTheFlowExecutionsContactThatAreWithStatus`CANCELED`Or`COMPLETED`.": {
                "value": [
                  "false",
                  0
                ],
                "summary": "Only return the Flow Executions Contact that are with status `CANCELED` or `COMPLETED`."
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
            "in": "query",
            "name": "search",
            "schema": {
              "type": "string"
            },
            "description": "You can search with the `contact__phone`, `contact__first_name`, `contact__last_name`, `contact__email` fields.",
            "examples": {
              "ByContactEmail": {
                "value": "erik@hilos.io",
                "summary": "by contact email"
              },
              "ByContactPhone": {
                "value": "+525512345678",
                "summary": "by contact phone"
              },
              "ByContactLastName": {
                "value": "Smith",
                "summary": "by contact last_name"
              },
              "ByContactFirstName": {
                "value": "Jonh",
                "summary": "by contact first_name"
              }
            }
          }
        ],
        "tags": [
          "Flows"
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
                  "$ref": "#/components/schemas/PaginatedFlowExecutionContactListSimpleList"
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
      "ContactReadSimple": {
        "type": "object",
        "properties": {
          "first_name": {
            "type": "string",
            "nullable": true,
            "maxLength": 100
          },
          "last_name": {
            "type": "string",
            "nullable": true,
            "maxLength": 100
          },
          "email": {
            "type": "string",
            "format": "email",
            "nullable": true,
            "maxLength": 254
          },
          "meta": {},
          "canonical_phone": {
            "type": "string",
            "nullable": true,
            "maxLength": 30
          },
          "is_deleted": {
            "type": "boolean"
          },
          "phone": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "last_updated_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "title": "Última actualización el"
          },
          "source": {
            "type": "string",
            "maxLength": 255
          },
          "external_url": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "maxLength": 200
          }
        },
        "required": [
          "id",
          "last_updated_on",
          "phone",
          "source"
        ]
      },
      "FlowExecutionContactListSimple": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "contact": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ContactReadSimple"
              }
            ],
            "description": "The Contact that the Flow Execution Contact is for."
          },
          "status": {
            "$ref": "#/components/schemas/FlowExecutionContactStatusEnum"
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "status_reason": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "is_test": {
            "type": "boolean"
          },
          "flow_version": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "flow": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "flow_name": {
            "type": "string",
            "readOnly": true,
            "description": "The name of the Flow that the Flow Execution Contact is for."
          }
        },
        "required": [
          "contact",
          "flow_name",
          "id",
          "status_reason"
        ]
      },
      "FlowExecutionContactStatusEnum": {
        "enum": [
          "READY",
          "RUNNING",
          "COMPLETED",
          "CANCELED",
          "EXPIRED",
          "FAILED"
        ],
        "type": "string",
        "description": "* `READY` - Ready\n* `RUNNING` - Running\n* `COMPLETED` - Completed\n* `CANCELED` - Canceled\n* `EXPIRED` - Expired\n* `FAILED` - Failed"
      },
      "PaginatedFlowExecutionContactListSimpleList": {
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
              "$ref": "#/components/schemas/FlowExecutionContactListSimple"
            }
          }
        }
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
      "name": "Flows"
    }
  ]
}
```