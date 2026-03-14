# Source: https://developers.activecampaign.com/reference/getaibroadcaststatus.md

# Get AI broadcast request status

Returns the current status of the AI process execution

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "SMS Broadcast API",
    "description": "API for managing SMS broadcasts, lists, metrics, and AI-powered content generation in ActiveCampaign",
    "version": "3.0.0",
    "contact": {
      "name": "ActiveCampaign Support",
      "url": "https://www.activecampaign.com"
    }
  },
  "servers": [
    {
      "url": "https://{yourAccountName}.api-us1.com/api/3",
      "description": "US-based Users",
      "variables": {
        "yourAccountName": {
          "default": "yourAccountName"
        }
      }
    }
  ],
  "paths": {
    "/sms/broadcasts/ai/{Id}": {
      "get": {
        "tags": [
          "AI",
          "Broadcasts"
        ],
        "summary": "Get AI broadcast request status",
        "description": "Returns the current status of the AI process execution",
        "operationId": "getAIBroadcastStatus",
        "parameters": [
          {
            "name": "Id",
            "in": "path",
            "required": true,
            "description": "Request ID from AI broadcast creation",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Status retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AIBroadcastStatus"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "AIBroadcastStatus": {
        "type": "object",
        "properties": {
          "source": {
            "type": "string",
            "enum": [
              "ai_index",
              "sms_index",
              "ai_builder"
            ]
          },
          "status": {
            "type": "string",
            "enum": [
              "in_progress",
              "error",
              "success"
            ]
          },
          "broadcastId": {
            "type": "integer",
            "nullable": true
          }
        }
      }
    },
    "securitySchemes": {
      "ApiToken": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "description": "Your ActiveCampaign API token"
      }
    }
  },
  "security": [
    {
      "ApiToken": []
    }
  ]
}
```