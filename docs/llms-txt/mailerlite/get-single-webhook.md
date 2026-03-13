# Source: https://developers-classic.mailerlite.com/reference/get-single-webhook.md

# /webhooks/:id

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
    "/webhooks/{id}": {
      "get": {
        "summary": "/webhooks/:id",
        "description": "",
        "operationId": "get-single-webhook",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of a webhook",
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
                    "value": "{\n  \"id\": 1,\n  \"event\": \"subscriber.create\",\n  \"url\": \"https://requestb.in/1dt2ugd1\",\n  \"created_at\": {\n    \"date\": \"2017-05-08 12:13:35.000000\",\n    \"timezone_type\": 3,\n    \"timezone\": \"UTC\"\n  },\n  \"updated_at\": {\n    \"date\": \"2017-05-25 12:39:16.000000\",\n    \"timezone_type\": 3,\n    \"timezone\": \"UTC\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "example": 1,
                      "default": 0
                    },
                    "event": {
                      "type": "string",
                      "example": "subscriber.create"
                    },
                    "url": {
                      "type": "string",
                      "example": "https://requestb.in/1dt2ugd1"
                    },
                    "created_at": {
                      "type": "object",
                      "properties": {
                        "date": {
                          "type": "string",
                          "example": "2017-05-08 12:13:35.000000"
                        },
                        "timezone_type": {
                          "type": "integer",
                          "example": 3,
                          "default": 0
                        },
                        "timezone": {
                          "type": "string",
                          "example": "UTC"
                        }
                      }
                    },
                    "updated_at": {
                      "type": "object",
                      "properties": {
                        "date": {
                          "type": "string",
                          "example": "2017-05-25 12:39:16.000000"
                        },
                        "timezone_type": {
                          "type": "integer",
                          "example": 3,
                          "default": 0
                        },
                        "timezone": {
                          "type": "string",
                          "example": "UTC"
                        }
                      }
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
              "code": "curl -v https://api.mailerlite.com/api/v2/webhooks/1 \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
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
  "_id": "58b53b141065f9c438aa1afe:5926dfc96c729e0f00595f72"
}
```