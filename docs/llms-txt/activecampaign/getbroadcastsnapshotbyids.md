# Source: https://developers.activecampaign.com/reference/getbroadcastsnapshotbyids.md

# Get broadcast snapshot

Returns snapshot for specified broadcast IDs

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
    "/sms/broadcasts/metrics/snapshot": {
      "post": {
        "tags": [
          "Metrics",
          "Snapshots",
          "Broadcasts"
        ],
        "summary": "Get broadcast snapshot",
        "description": "Returns snapshot for specified broadcast IDs",
        "operationId": "getBroadcastSnapshotByIds",
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
            "description": "Snapshot retrieved successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SnapshotResponse"
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
      "SnapshotResponse": {
        "type": "object",
        "properties": {
          "snapshot": {
            "type": "object",
            "properties": {
              "campaigns": {
                "type": "integer"
              },
              "sends": {
                "type": "integer"
              },
              "deliveries": {
                "type": "integer"
              },
              "clicks": {
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