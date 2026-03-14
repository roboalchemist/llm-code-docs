# Source: https://developers.activecampaign.com/reference/getbroadcastmetrics.md

# Get all broadcast metrics

Returns metrics for specified broadcast IDs

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
    "/sms/broadcasts/metrics": {
      "post": {
        "tags": [
          "Metrics",
          "Broadcasts"
        ],
        "summary": "Get all broadcast metrics",
        "description": "Returns metrics for specified broadcast IDs",
        "operationId": "getBroadcastMetrics",
        "parameters": [
          {
            "name": "start_date",
            "in": "query",
            "description": "Start date for metrics (YYYY-MM-DD)",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "End date for metrics (YYYY-MM-DD)",
            "schema": {
              "type": "string",
              "format": "date"
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
            "description": "Metrics retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BroadcastMetricsResponse"
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
      "BroadcastMetrics": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "sends": {
            "type": "integer"
          },
          "deliveries": {
            "type": "integer"
          },
          "replies": {
            "type": "integer"
          },
          "failures": {
            "type": "integer"
          },
          "optOuts": {
            "type": "integer"
          },
          "clicks": {
            "type": "integer"
          }
        }
      },
      "BroadcastMetricsResponse": {
        "type": "object",
        "properties": {
          "metrics": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BroadcastMetrics"
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