# Source: https://developers-classic.mailerlite.com/reference/groupssearch.md

# /groups/search

Search single group by the name. [Rate limited]

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "MailerLite API v2",
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
        "in": "header",
        "name": "x-mailerlite-apikey",
        "x-default": "fc7b8c5b32067bcd47cafb5f475d2fe9"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/groups/search": {
      "post": {
        "summary": "/groups/search",
        "description": "Search single group by the name. [Rate limited]",
        "operationId": "groupssearch",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "group_name": {
                    "type": "string",
                    "description": "Name of the group to search"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n\"id\": 3640743,\n\"name\": \"Demo Group\",\n\"total\": 0,\n\"active\": 0,\n\"unsubscribed\": 0,\n\"bounced\": 0,\n\"unconfirmed\": 0,\n\"junk\": 0,\n\"sent\": 0,\n\"opened\": 0,\n\"clicked\": 0,\n\"date_created\": null,\n\"date_updated\": null\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "example": 3640743,
                      "default": 0
                    },
                    "name": {
                      "type": "string",
                      "example": "Demo Group"
                    },
                    "total": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "active": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "unsubscribed": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "bounced": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "unconfirmed": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "junk": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "sent": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "opened": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "clicked": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "date_created": {},
                    "date_updated": {}
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/groups/search \\\n-d '{\"group_name\":\"Demo Group\"}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            }
          ],
          "samples-languages": [
            "curl"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true,
  "_id": "58cb994d31c89a0f009602e4:60cb400de84cc200401ab223"
}
```