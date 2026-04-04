# Source: https://developers.activecampaign.com/reference/getsmscreditdata.md

# Get current sms credit use data

Retrieve the current period's sms credit usage and remaining balance

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
    "/sms/credits": {
      "get": {
        "tags": [
          "Credits"
        ],
        "summary": "Get current sms credit use data",
        "description": "Retrieve the current period's sms credit usage and remaining balance",
        "operationId": "getSmsCreditData",
        "responses": {
          "200": {
            "description": "Sms Credits for this period",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreditsResponse"
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
      "CreditsResponse": {
        "type": "object",
        "properties": {
          "smsCredits": {
            "type": "object",
            "properties": {
              "period": {
                "type": "string",
                "example": "month"
              },
              "nextRefillDate": {
                "type": "string",
                "example": "2026-02-26 15:06:25"
              },
              "includedThisPeriod": {
                "type": "integer",
                "example": 1000
              },
              "usedThisPeriod": {
                "type": "integer",
                "example": 71
              },
              "extra": {
                "type": "integer",
                "example": 9040
              },
              "available": {
                "type": "integer",
                "example": 9969
              }
            }
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