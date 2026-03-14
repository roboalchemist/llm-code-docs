# Source: https://developers.activecampaign.com/reference/getbroadcastfailures.md

# Get broadcast failure details

Returns grouping and counts of failures for the broadcast

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
    "/sms/broadcasts/metrics/{broadcastId}/failures": {
      "get": {
        "tags": [
          "Failures",
          "Broadcasts",
          "Metrics"
        ],
        "summary": "Get broadcast failure details",
        "description": "Returns grouping and counts of failures for the broadcast",
        "operationId": "getBroadcastFailures",
        "parameters": [
          {
            "name": "broadcastId",
            "in": "path",
            "required": true,
            "description": "Broadcast ID",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "start_date",
            "in": "query",
            "description": "Start date (YYYY-MM-DD)",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "End date (YYYY-MM-DD)",
            "schema": {
              "type": "string",
              "format": "date"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Failure details retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FailureDetailsResponse"
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
      "FailureDetail": {
        "type": "object",
        "properties": {
          "errorCode": {
            "type": "string"
          },
          "errorSource": {
            "type": "string",
            "enum": [
              "ac",
              "twilio"
            ]
          },
          "count": {
            "type": "integer"
          }
        }
      },
      "FailureDetailsResponse": {
        "type": "object",
        "properties": {
          "failures": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FailureDetail"
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