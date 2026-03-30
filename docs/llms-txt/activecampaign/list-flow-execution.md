# Source: https://developers.activecampaign.com/reference/list-flow-execution.md

# List Flow Executions

Lists Flow Executions. 

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
    "/channel/whatsapp/flow-execution": {
      "get": {
        "operationId": "List Flow Execution",
        "description": "Lists Flow Executions. ",
        "summary": "List Flow Executions",
        "parameters": [
          {
            "in": "query",
            "name": "flow",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Flow Id to filter the Flow Executions and only get those from that Flow.",
            "examples": {
              "OnlyReturnTheFlowExecutionsOfThisFlow": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Only return the Flow Executions of this Flow"
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
            "name": "page",
            "required": false,
            "in": "query",
            "description": "A page number within the paginated result set.",
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
            "description": "You can search with the `status`, `created_by__email` fields.",
            "examples": {
              "CreatedByEmail": {
                "value": "erik@hilos.io",
                "summary": "created by email"
              },
              "With`PROCESSING`Status": {
                "value": "Processing",
                "summary": "with `PROCESSING` status"
              },
              "With`READY`Status": {
                "value": "Ready",
                "summary": "with `READY` status"
              },
              "With`AWAITINGCONFIRMATION`Status": {
                "value": "Awaiting Confirmation",
                "summary": "with `AWAITING_CONFIRMATION` status"
              },
              "With`CONFIRMED`Status": {
                "value": "Confirmed",
                "summary": "with `CONFIRMED` status"
              },
              "With`STARTING`Status": {
                "value": "Starting",
                "summary": "with `STARTING` status"
              },
              "With`RUNNING`Status": {
                "value": "Running",
                "summary": "with `RUNNING` status"
              },
              "With`COMPLETED`Status": {
                "value": "Completed",
                "summary": "with `COMPLETED` status"
              },
              "With`CANCELED`Status": {
                "value": "Canceled",
                "summary": "with `CANCELED` status"
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
                  "$ref": "#/components/schemas/PaginatedFlowExecutionListList"
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
      "FlowExecutionExecuteForEnum": {
        "enum": [
          "FILTERS",
          "LIST",
          "ALL"
        ],
        "type": "string",
        "description": "* `FILTERS` - Filters\n* `LIST` - List\n* `ALL` - All"
      },
      "FlowExecutionList": {
        "type": "object",
        "properties": {
          "status": {
            "$ref": "#/components/schemas/FlowExecutionStatusEnum"
          },
          "execute_for": {
            "$ref": "#/components/schemas/FlowExecutionExecuteForEnum"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "has_priority": {
            "type": "boolean"
          },
          "flow_execution_variables": {},
          "start_on": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "num_contacts": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "expired": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "running": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "completed": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "canceled": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "failed": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "avg_completion_time": {
            "type": "string"
          },
          "status_reason": {
            "type": "string",
            "nullable": true
          },
          "status_triggered_by": {
            "type": "integer",
            "nullable": true
          },
          "status_last_change_on": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleUser"
              }
            ],
            "description": "The User that created the Flow Execution."
          },
          "flow_version": {
            "type": "string",
            "format": "uuid"
          }
        },
        "required": [
          "created_by",
          "execute_for",
          "flow_version"
        ]
      },
      "FlowExecutionStatusEnum": {
        "enum": [
          "PROCESSING",
          "READY",
          "AWAITING_CONFIRMATION",
          "CONFIRMED",
          "STARTING",
          "RUNNING",
          "COMPLETED",
          "CANCELED"
        ],
        "type": "string",
        "description": "* `PROCESSING` - Processing\n* `READY` - Ready\n* `AWAITING_CONFIRMATION` - Awaiting Confirmation\n* `CONFIRMED` - Confirmed\n* `STARTING` - Starting\n* `RUNNING` - Running\n* `COMPLETED` - Completed\n* `CANCELED` - Canceled"
      },
      "PaginatedFlowExecutionListList": {
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
              "$ref": "#/components/schemas/FlowExecutionList"
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