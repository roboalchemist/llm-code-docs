# Source: https://developers.activecampaign.com/reference/listbroadcastlists.md

# Get all broadcast lists

Gets a paged list of all broadcast lists (SMS channel)

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
    "/sms/lists": {
      "get": {
        "tags": [
          "Broadcasts"
        ],
        "summary": "Get all broadcast lists",
        "description": "Gets a paged list of all broadcast lists (SMS channel)",
        "operationId": "listBroadcastLists",
        "parameters": [
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
          },
          {
            "name": "filters[name]",
            "in": "query",
            "description": "Filter by list name",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BroadcastListsResponse"
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
      "BroadcastList": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "subscriber_count": {
            "type": "integer"
          }
        }
      },
      "BroadcastListsResponse": {
        "type": "object",
        "properties": {
          "lists": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BroadcastList"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "total": {
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