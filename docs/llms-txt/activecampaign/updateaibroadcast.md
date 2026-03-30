# Source: https://developers.activecampaign.com/reference/updateaibroadcast.md

# Update broadcast with AI

Updates an existing broadcast using AI

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
    "/sms/broadcasts/ai": {
      "put": {
        "summary": "Update broadcast with AI",
        "description": "Updates an existing broadcast using AI",
        "operationId": "updateAIBroadcast",
        "tags": [
          "AI",
          "Broadcasts"
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AIBroadcastUpdateRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "AI broadcast update request initiated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AIBroadcastResponse"
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
      "AIBroadcastUpdateRequest": {
        "type": "object",
        "required": [
          "source",
          "prompt",
          "tone",
          "broadcastId"
        ],
        "properties": {
          "source": {
            "type": "string",
            "enum": [
              "ai_index",
              "sms_index",
              "ai_builder"
            ]
          },
          "prompt": {
            "type": "string"
          },
          "tone": {
            "type": "string"
          },
          "broadcastId": {
            "type": "integer"
          }
        }
      },
      "AIBroadcastResponse": {
        "type": "object",
        "properties": {
          "requestId": {
            "type": "string",
            "description": "External identifier to track the request"
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