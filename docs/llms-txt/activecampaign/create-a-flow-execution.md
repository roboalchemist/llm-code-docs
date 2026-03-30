# Source: https://developers.activecampaign.com/reference/create-a-flow-execution.md

# Create a Flow Execution

Create a Flow Execution of a Flow.

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
    "/channel/whatsapp/flow/{id}/run": {
      "post": {
        "operationId": "Create a Flow Execution",
        "description": "Create a Flow Execution of a Flow.",
        "summary": "Create a Flow Execution",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Flow Id to create a Flow Execution.",
            "required": true,
            "examples": {
              "CreateByFlowId": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Create by Flow Id"
              }
            }
          }
        ],
        "tags": [
          "Flows"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FlowExecutionCreateRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/FlowExecutionCreateRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/FlowExecutionCreateRequest"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "tokenAuth": []
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FlowExecutionEdit"
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
      "ComparisonEnum": {
        "enum": [
          "exact",
          "!exact",
          "gte",
          "gt",
          "lte",
          "lt",
          "isnull",
          "!isnull",
          "icontains",
          "!icontains"
        ],
        "type": "string",
        "description": "* `exact` - Exact\n* `!exact` - Different\n* `gte` - Gte\n* `gt` - Gt\n* `lte` - Lte\n* `lt` - Lt\n* `isnull` - Is Null\n* `!isnull` - Not Null\n* `icontains` - Contains\n* `!icontains` - Not Contains"
      },
      "ContactNote": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "notes": {
            "type": "string"
          },
          "contact": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "title": "Creado el"
          },
          "created_by": {
            "$ref": "#/components/schemas/SimpleUser"
          }
        },
        "required": [
          "contact",
          "created_on",
          "id",
          "notes"
        ]
      },
      "ContactTag": {
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
      "FlowExecutionContactFilterEdit": {
        "type": "object",
        "properties": {
          "field": {
            "type": "string"
          },
          "comparison": {
            "$ref": "#/components/schemas/ComparisonEnum"
          },
          "value": {
            "type": "string"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          }
        },
        "required": [
          "comparison",
          "field",
          "value"
        ]
      },
      "FlowExecutionCreateRequest": {
        "type": "object",
        "properties": {
          "execute_for": {
            "$ref": "#/components/schemas/FlowExecutionCreateRequestExecuteForEnum"
          },
          "has_priority": {
            "type": "boolean",
            "default": false,
            "description": "Specify as True if you want this execution to                 close any other running flows or conversations."
          },
          "contact_list": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PatchedContactEdit"
            }
          }
        },
        "required": [
          "contact_list",
          "execute_for"
        ]
      },
      "FlowExecutionCreateRequestExecuteForEnum": {
        "enum": [
          "LIST"
        ],
        "type": "string",
        "description": "* `LIST` - LIST"
      },
      "FlowExecutionEdit": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string",
            "readOnly": true,
            "description": "The status of the Flow Execution."
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
            "readOnly": true,
            "nullable": true
          },
          "status_triggered_by": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "status_last_change_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "contact_filters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FlowExecutionContactFilterEdit"
            },
            "description": "The filters to use to get the Contacts that the Flow Execution will run for."
          },
          "contact_list": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PatchedContactEdit"
            },
            "description": "The list of Contacts that the Flow Execution will run for."
          },
          "source": {
            "$ref": "#/components/schemas/FlowExecutionEditSourceEnum"
          },
          "is_hidden": {
            "type": "boolean"
          }
        },
        "required": [
          "execute_for",
          "status",
          "status_last_change_on",
          "status_reason",
          "status_triggered_by"
        ]
      },
      "FlowExecutionEditSourceEnum": {
        "enum": [
          "HUBSPOT",
          "API",
          "FRONTEND"
        ],
        "type": "string",
        "description": "* `HUBSPOT` - Hubspot\n* `API` - Api\n* `FRONTEND` - Frontend"
      },
      "FlowExecutionExecuteForEnum": {
        "enum": [
          "FILTERS",
          "LIST",
          "ALL"
        ],
        "type": "string",
        "description": "* `FILTERS` - Filters\n* `LIST` - List\n* `ALL` - All"
      },
      "PatchedContactEdit": {
        "type": "object",
        "properties": {
          "phone": {
            "type": "string",
            "maxLength": 30
          },
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
          "external_url": {
            "type": "string",
            "format": "uri",
            "nullable": true,
            "maxLength": 200
          },
          "is_deleted": {
            "type": "boolean"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "source": {
            "type": "string",
            "default": "website"
          },
          "notes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ContactNote"
            },
            "readOnly": true
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "tags": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ContactTag"
            }
          },
          "external_id": {
            "type": "string",
            "nullable": true
          },
          "native_id": {
            "type": "string",
            "nullable": true
          },
          "default_assignees": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "contact_import": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "default_channel": {
            "type": "integer",
            "nullable": true
          },
          "wa_id": {
            "type": "string",
            "nullable": true
          },
          "overwrite_tags": {
            "type": "boolean",
            "default": false,
            "description": "If true, the `tags` will be overwritten with the new value. If false, the new value will be merged with the existing value. Default is false."
          },
          "overwrite_default_assignees": {
            "type": "boolean",
            "default": false,
            "description": "If true, the `default_assignees` will be overwritten with the new value. If false, the new value will be merged with the existing value. Default is false."
          },
          "overwrite_meta": {
            "type": "boolean",
            "default": false,
            "description": "If true, the `meta` field will be overwritten with the new value. If false, the new value will be merged with the existing value. Default is false."
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