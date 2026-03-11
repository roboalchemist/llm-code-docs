# Source: https://developers.activecampaign.com/reference/duplicate-campaign.md

# Duplicate Campaign

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/campaigns/{id}/copy": {
      "post": {
        "summary": "Duplicate Campaign",
        "description": "",
        "operationId": "duplicate-campaign",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "id of the source campaign",
            "schema": {
              "type": "integer",
              "format": "int32"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n\t\"succeeded\":1,\n  \"message\":\"Campaign draft copied.\",\n  \"newCampaignId\":217\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "succeeded": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "message": {
                      "type": "string",
                      "example": "Campaign draft copied."
                    },
                    "newCampaignId": {
                      "type": "integer",
                      "example": 217,
                      "default": 0
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "'Bad request. You are not allowed to copy this campaign.'"
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```