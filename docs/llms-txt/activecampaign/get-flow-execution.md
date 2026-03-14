# Source: https://developers.activecampaign.com/reference/get-flow-execution.md

# Get Flow Execution

Get Flow Execution by Id.

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
    "/channel/whatsapp/flow-execution/{id}": {
      "get": {
        "operationId": "Get Flow Execution",
        "description": "Get Flow Execution by Id.",
        "summary": "Get Flow Execution",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A Flow Execution Id to retrive.",
            "required": true,
            "examples": {
              "QueryById": {
                "value": "a3ff7ee5-0c11-49e2-a0d6-7e316626f7b1",
                "summary": "Query by Id"
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
                  "$ref": "#/components/schemas/FlowExecutionReadDetail"
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
      "ChannelProviderEnum": {
        "enum": [
          "META_CLOUD_API",
          "TECH_PROVIDER_CLOUD_API",
          "D360_CLOUD_API",
          "360DIALOG"
        ],
        "type": "string",
        "description": "* `META_CLOUD_API` - Meta Cloud Api\n* `TECH_PROVIDER_CLOUD_API` - Tech Provider Cloud Api\n* `D360_CLOUD_API` - D360 Cloud Api\n* `360DIALOG` - Dialog360"
      },
      "ChannelStatusEnum": {
        "enum": [
          "NEW",
          "ACTIVE",
          "INACTIVE"
        ],
        "type": "string",
        "description": "* `NEW` - New\n* `ACTIVE` - Active\n* `INACTIVE` - Inactive"
      },
      "ChannelTypeEnum": {
        "enum": [
          "WHATSAPP",
          "EMAIL",
          "INSTAGRAM",
          "FB_MESSENGER",
          "TELEGRAM",
          "SMS",
          "VOICE"
        ],
        "type": "string",
        "description": "* `WHATSAPP` - Whatsapp\n* `EMAIL` - Email\n* `INSTAGRAM` - Instagram\n* `FB_MESSENGER` - Fb Messenger\n* `TELEGRAM` - Telegram\n* `SMS` - Sms\n* `VOICE` - Voice"
      },
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
      "FlowExecutionExecuteForEnum": {
        "enum": [
          "FILTERS",
          "LIST",
          "ALL"
        ],
        "type": "string",
        "description": "* `FILTERS` - Filters\n* `LIST` - List\n* `ALL` - All"
      },
      "FlowExecutionReadDetail": {
        "type": "object",
        "properties": {
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FlowExecutionStatusEnum"
              }
            ],
            "readOnly": true,
            "description": "The status of the Flow Execution.\n\n* `PROCESSING` - Processing\n* `READY` - Ready\n* `AWAITING_CONFIRMATION` - Awaiting Confirmation\n* `CONFIRMED` - Confirmed\n* `STARTING` - Starting\n* `RUNNING` - Running\n* `COMPLETED` - Completed\n* `CANCELED` - Canceled"
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
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleUser"
              }
            ],
            "readOnly": true
          },
          "status_last_change_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
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
          "contact_filters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FlowExecutionContactFilterEdit"
            },
            "description": "The filters to use to get the Contacts that the Flow Execution will run for. This field isn't required if executing the flow for a Contact List"
          },
          "contact_import": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "flow": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FlowSimpleRead"
              }
            ],
            "description": "The Flow that the Flow Execution is running."
          },
          "flow_version": {
            "allOf": [
              {
                "$ref": "#/components/schemas/FlowVersionSimpleRead"
              }
            ],
            "description": "The Flow Version that the Flow Execution is running."
          },
          "last_run_on": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "The last time that the Flow Execution was run."
          }
        },
        "required": [
          "created_by",
          "execute_for",
          "flow",
          "flow_version",
          "last_run_on",
          "status",
          "status_last_change_on",
          "status_reason",
          "status_triggered_by"
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
      "FlowSimpleRead": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "maxLength": 100
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleUser"
              }
            ],
            "readOnly": true
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "is_active": {
            "type": "boolean"
          },
          "status": {
            "$ref": "#/components/schemas/FlowStatusEnum"
          },
          "is_legacy": {
            "type": "boolean"
          },
          "channel": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleChannel"
              }
            ],
            "readOnly": true
          },
          "flow_execution_variables": {
            "type": "array",
            "items": {
              "type": "string",
              "maxLength": 255
            },
            "nullable": true
          },
          "trigger_type": {
            "$ref": "#/components/schemas/TriggerTypeEnum"
          },
          "trigger_config": {}
        },
        "required": [
          "channel",
          "created_by",
          "id",
          "name",
          "trigger_type"
        ]
      },
      "FlowStatusEnum": {
        "enum": [
          "DRAFT",
          "PUBLISHED"
        ],
        "type": "string",
        "description": "* `DRAFT` - Draft\n* `PUBLISHED` - Published"
      },
      "FlowVersionSimpleRead": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "flow": {
            "$ref": "#/components/schemas/FlowSimpleRead"
          },
          "is_current_version": {
            "type": "boolean",
            "readOnly": true
          },
          "version_name": {
            "type": "string",
            "maxLength": 255
          },
          "version_description": {
            "type": "string",
            "nullable": true
          },
          "published_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SimpleUser"
              }
            ],
            "readOnly": true
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
          "num_contacts": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": 0
          },
          "completed": {
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
          "avg_completion_time": {
            "type": "string"
          }
        },
        "required": [
          "flow",
          "is_current_version",
          "last_updated_on",
          "published_by"
        ]
      },
      "SimpleChannel": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "channel_type": {
            "$ref": "#/components/schemas/ChannelTypeEnum"
          },
          "name": {
            "type": "string",
            "maxLength": 100
          },
          "channel_id": {
            "type": "string",
            "maxLength": 100
          },
          "status": {
            "$ref": "#/components/schemas/ChannelStatusEnum"
          },
          "created_on": {
            "type": "string",
            "format": "date-time",
            "title": "Creado el"
          },
          "channel_provider": {
            "$ref": "#/components/schemas/ChannelProviderEnum"
          },
          "is_sandbox": {
            "type": "boolean"
          }
        },
        "required": [
          "channel_id",
          "id"
        ]
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
      "TriggerTypeEnum": {
        "enum": [
          "INBOUND_ANY_MESSAGE",
          "INBOUND_SPECIFIC_MESSAGE",
          "OUTBOUND_CAMPAIGN_API",
          "OUTBOUND_CAMPAIGN_CSV",
          "OUTBOUND_CAMPAIGN_SEGMENT",
          "OUTBOUND_ANY",
          "META_C2WA",
          "INTEGRATIONS_HUBSPOT",
          "INTEGRATIONS_ZAPIER",
          "FROM_FLOW",
          "CSAT",
          "OTHER"
        ],
        "type": "string",
        "description": "* `INBOUND_ANY_MESSAGE` - Inbound Any Message\n* `INBOUND_SPECIFIC_MESSAGE` - Inbound Specific Message\n* `OUTBOUND_CAMPAIGN_API` - Outbound Campaign Api\n* `OUTBOUND_CAMPAIGN_CSV` - Outbound Campaign Csv\n* `OUTBOUND_CAMPAIGN_SEGMENT` - Outbound Campaign Segment\n* `OUTBOUND_ANY` - Outbound Any\n* `META_C2WA` - Meta C2Wa\n* `INTEGRATIONS_HUBSPOT` - Integrations Hubspot\n* `INTEGRATIONS_ZAPIER` - Integrations Zapier\n* `FROM_FLOW` - From Flow\n* `CSAT` - Csat\n* `OTHER` - Other"
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