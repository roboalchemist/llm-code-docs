# Source: https://developers-classic.mailerlite.com/reference/update-a-webhook.md

# /webhooks/:id

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "API Settings",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.mailerlite.com/api/master"
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "x-default": "",
        "type": "apiKey",
        "name": "X-MailerLite-ApiKey"
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
      "put": {
        "summary": "/webhooks/:id",
        "description": "",
        "operationId": "update-a-webhook",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
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
                    "value": "{\n  \"id\": 1,\n  \"event\": \"subscriber.update\",\n  \"url\": \"https://requestb.in/1dt2ugd1\",\n  \"created_at\": {\n    \"date\": \"2017-05-08 12:13:35.000000\",\n    \"timezone_type\": 3,\n    \"timezone\": \"UTC\"\n  },\n  \"updated_at\": {\n    \"date\": \"2017-05-25 13:51:27.000000\",\n    \"timezone_type\": 3,\n    \"timezone\": \"UTC\"\n  }\n}"
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
                      "example": "subscriber.update"
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
                          "example": "2017-05-25 13:51:27.000000"
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
              "code": "curl -X PUT https://api.mailerlite.com/api/v2/webhooks/1 \\\n-d '{\"url\": \"http://newurl/script\"}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
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
  "_id": "58b53b141065f9c438aa1afd:5926dfe021e2930f001c1e69"
}
```