# Source: https://developers-classic.mailerlite.com/reference/stats.md

# /stats

Get basic stats for of account, such as subscribers, open/click rates and so on.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "V2 production",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.mailerlite.com/api/v2"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "X-MailerLite-ApiKey",
        "in": "header",
        "x-default": "your api key"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/stats": {
      "get": {
        "summary": "/stats",
        "description": "Get basic stats for of account, such as subscribers, open/click rates and so on.",
        "operationId": "stats",
        "parameters": [
          {
            "name": "timestamp",
            "in": "query",
            "description": "Specify UNIX timestamp if you want to receive stats values at the specific point in the past.",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"subscribed\": 10187,\n    \"unsubscribed\": 1,\n    \"campaigns\": 4,\n    \"sent_emails\": 2,\n    \"open_rate\": 0.1,\n    \"click_rate\": 0.05,\n    \"bounce_rate\": 0.05\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "subscribed": {
                      "type": "integer",
                      "example": 10187,
                      "default": 0
                    },
                    "unsubscribed": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "campaigns": {
                      "type": "integer",
                      "example": 4,
                      "default": 0
                    },
                    "sent_emails": {
                      "type": "integer",
                      "example": 2,
                      "default": 0
                    },
                    "open_rate": {
                      "type": "number",
                      "example": 0.1,
                      "default": 0
                    },
                    "click_rate": {
                      "type": "number",
                      "example": 0.05,
                      "default": 0
                    },
                    "bounce_rate": {
                      "type": "number",
                      "example": 0.05,
                      "default": 0
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl -v https://api.mailerlite.com/api/v2/stats \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$statsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->stats();\n\n$stats = $statsApi->get();\n\n// specify a unix timestamp in the past\n$statsInThePast = $statsApi->getHistorical(1483228800);"
            }
          ],
          "samples-languages": [
            "curl",
            "php"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [
      {
        "key": "X-MailerLite-ApiDocs",
        "value": "true"
      }
    ],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true,
  "_id": "58b53b141065f9c438aa1afe:589b4abafce0af0f00acdf13"
}
```