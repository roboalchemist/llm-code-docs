# Source: https://developers-classic.mailerlite.com/reference/get-webhooks-list.md

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
      "get": {
        "summary": "/webhooks",
        "description": "",
        "operationId": "get-webhooks-list",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"webhooks\": [\n    {\n      \"id\": 1,\n      \"event\": \"subscriber.create\",\n      \"url\": \"https://requestb.in/1dt2ugd1\",\n      \"created_at\": {\n        \"date\": \"2017-05-08 12:13:35.000000\",\n        \"timezone_type\": 3,\n        \"timezone\": \"UTC\"\n      },\n      \"updated_at\": {\n        \"date\": \"2017-05-25 12:39:16.000000\",\n        \"timezone_type\": 3,\n        \"timezone\": \"UTC\"\n      }\n    },\n    {\n      \"id\": 2,\n      \"event\": \"subscriber.update\",\n      \"url\": \"http://requestb.in/1k7uz6o1\",\n      \"created_at\": {\n        \"date\": \"2017-05-08 13:57:18.000000\",\n        \"timezone_type\": 3,\n        \"timezone\": \"UTC\"\n      },\n      \"updated_at\": {\n        \"date\": \"2017-05-08 13:57:18.000000\",\n        \"timezone_type\": 3,\n        \"timezone\": \"UTC\"\n      }\n    }\n  ],\n  \"count\": 2,\n  \"start\": 0,\n  \"limit\": 100\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "webhooks": {
                      "type": "array",
                      "items": {
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
                    },
                    "count": {
                      "type": "integer",
                      "example": 2,
                      "default": 0
                    },
                    "start": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "limit": {
                      "type": "integer",
                      "example": 100,
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
              "code": "curl -v https://api.mailerlite.com/api/v2/webhooks \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
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
  "_id": "58b53b141065f9c438aa1afe:5926dfb621e2930f001c1e67"
}
```