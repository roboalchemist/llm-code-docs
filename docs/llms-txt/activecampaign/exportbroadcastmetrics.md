# Source: https://developers.activecampaign.com/reference/exportbroadcastmetrics.md

# Export broadcast metrics

Export broadcast performance metrics as CSV

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
    "/sms/broadcasts/export": {
      "post": {
        "tags": [
          "Metrics",
          "Exports",
          "Broadcasts"
        ],
        "summary": "Export broadcast metrics",
        "description": "Export broadcast performance metrics as CSV",
        "operationId": "exportBroadcastMetrics",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "ids": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Export generated successfully",
            "content": {
              "text/csv": {
                "schema": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
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