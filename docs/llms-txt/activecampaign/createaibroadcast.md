# Source: https://developers.activecampaign.com/reference/createaibroadcast.md

# Create AI-generated broadcast

Creates a broadcast using AI based on prompt and tone

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
      "post": {
        "tags": [
          "AI",
          "Broadcasts"
        ],
        "summary": "Create AI-generated broadcast",
        "description": "Creates a broadcast using AI based on prompt and tone",
        "operationId": "createAIBroadcast",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AIBroadcastRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "AI broadcast request initiated",
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
      "AIBroadcastRequest": {
        "type": "object",
        "required": [
          "source",
          "prompt",
          "tone"
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
            "type": "string",
            "description": "User prompt for AI generation"
          },
          "tone": {
            "type": "string",
            "description": "Desired tone for the message"
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