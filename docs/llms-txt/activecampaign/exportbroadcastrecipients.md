# Source: https://developers.activecampaign.com/reference/exportbroadcastrecipients.md

# Export broadcast recipients

Export recipient data as CSV including full contact records

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
    "/sms/broadcasts/{broadcastId}/recipients/export": {
      "post": {
        "tags": [
          "Recipients",
          "Exports",
          "Broadcasts",
          "Metrics"
        ],
        "summary": "Export broadcast recipients",
        "description": "Export recipient data as CSV including full contact records",
        "operationId": "exportBroadcastRecipients",
        "parameters": [
          {
            "name": "broadcastId",
            "in": "path",
            "required": true,
            "description": "Broadcast ID",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "string",
                    "format": "date"
                  },
                  "end_date": {
                    "type": "string",
                    "format": "date"
                  },
                  "engagement": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "deliverability": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "search": {
                    "type": "string"
                  },
                  "order": {
                    "type": "object"
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