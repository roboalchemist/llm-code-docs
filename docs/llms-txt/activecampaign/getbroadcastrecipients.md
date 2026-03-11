# Source: https://developers.activecampaign.com/reference/getbroadcastrecipients.md

# Get broadcast recipients

Fetch all contacts who were sent a specific broadcast

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
    "/sms/broadcasts/{broadcastId}/recipients": {
      "get": {
        "tags": [
          "Recipients",
          "Broadcasts"
        ],
        "summary": "Get broadcast recipients",
        "description": "Fetch all contacts who were sent a specific broadcast",
        "operationId": "getBroadcastRecipients",
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
          },
          {
            "name": "filters[deliverability][]",
            "in": "query",
            "description": "Filter by deliverability status",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "deliveries",
                  "failures"
                ]
              }
            }
          },
          {
            "name": "filters[engagement][]",
            "in": "query",
            "description": "Filter by engagement type",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "clicks",
                  "replies",
                  "optOuts"
                ]
              }
            }
          },
          {
            "name": "search",
            "in": "query",
            "description": "Search contacts by name or phone",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order[field]",
            "in": "query",
            "description": "Order by field",
            "schema": {
              "type": "string",
              "enum": [
                "name",
                "phone",
                "sentDate",
                "clicks",
                "deliverability",
                "optOut",
                "replies"
              ]
            }
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Offset for pagination",
            "schema": {
              "type": "integer",
              "default": 0
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Number of items to return",
            "schema": {
              "type": "integer",
              "default": 20
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Recipients retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RecipientsResponse"
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
      "Recipient": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Contact ID"
          },
          "name": {
            "type": "string"
          },
          "phoneNumber": {
            "type": "string"
          },
          "sentDate": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in CST"
          },
          "clicks": {
            "type": "integer"
          },
          "deliverability": {
            "type": "string",
            "enum": [
              "delivered",
              "failed"
            ]
          },
          "replies": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "message": {
                  "type": "string"
                },
                "date": {
                  "type": "string",
                  "format": "date-time",
                  "description": "Timestamp in CST"
                }
              }
            }
          },
          "optOut": {
            "type": "string",
            "enum": [
              "yes",
              "no"
            ]
          },
          "details": {
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
              }
            }
          }
        }
      },
      "RecipientsResponse": {
        "type": "object",
        "properties": {
          "recipients": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Recipient"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "total": {
                "type": "integer"
              },
              "limit": {
                "type": "integer"
              },
              "offset": {
                "type": "integer"
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