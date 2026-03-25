# Source: https://developers-classic.mailerlite.com/reference/create-a-webhook.md

# /webhooks

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
    "/webhooks": {
      "post": {
        "summary": "/webhooks",
        "description": "",
        "operationId": "create-a-webhook",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "url",
                  "event"
                ],
                "properties": {
                  "url": {
                    "type": "string",
                    "description": "Your URL where callbacks are sent"
                  },
                  "event": {
                    "type": "string",
                    "description": "Subscribed event"
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
                    "value": "{\n  \"id\": 7,\n  \"event\": \"subscriber.create\",\n  \"url\": \"https://requestb.in/1dt2ugd1\",\n  \"created_at\": {\n    \"date\": \"2017-05-25 13:49:28.000000\",\n    \"timezone_type\": 3,\n    \"timezone\": \"UTC\"\n  },\n  \"updated_at\": {\n    \"date\": \"2017-05-25 13:49:28.000000\",\n    \"timezone_type\": 3,\n    \"timezone\": \"UTC\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "example": 7,
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
                          "example": "2017-05-25 13:49:28.000000"
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
                          "example": "2017-05-25 13:49:28.000000"
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
                    "value": "{\n  \"error\": {\n    \"code\": 400,\n    \"message\": \"Url must be an active domain, Event contains invalid value\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "integer",
                          "example": 400,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Url must be an active domain, Event contains invalid value"
                        }
                      }
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/webhooks \\\n-d '{\n\t\"url\": \"https://yoursite/script-is-here\",\n\t\"event\": \"subscriber.create\"\n}'\n-H 'Content-Type: application/json' \\\n-H 'X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9' \\"
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
  "_id": "58b53b141065f9c438aa1afe:5926e03ec385770f00113ab2"
}
```