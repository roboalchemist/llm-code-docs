# Source: https://developers-classic.mailerlite.com/reference/subscribers.md

# /subscribers

Get account's subscribers [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

The response body contains the array of a subscriber objects which is documented [here](https://developers-classic.mailerlite.com/reference/single-subscriber).

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
    "/subscribers": {
      "get": {
        "summary": "/subscribers",
        "description": "Get account's subscribers [Rate limited]",
        "operationId": "subscribers",
        "parameters": [
          {
            "name": "offset",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "limit",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 100
            }
          },
          {
            "name": "type",
            "in": "query",
            "description": "available values: active, unsubscribed, bounced, junk, unconfirmed",
            "schema": {
              "type": "string"
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
                    "value": "[\n   {\n      \"id\":1343965485,\n      \"name\":\"John\",\n      \"email\":\"demo@mailerlite.com\",\n      \"sent\":0,\n      \"opened\":0,\n      \"clicked\":0,\n      \"type\":\"active\",\n      \"fields\":[\n         {\n            \"key\":\"email\",\n            \"value\":\"demo@mailerlite.com\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"name\",\n            \"value\":\"John\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"last_name\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"company\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"country\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"city\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"phone\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"state\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         },\n         {\n            \"key\":\"zip\",\n            \"value\":\"\",\n            \"type\":\"TEXT\"\n         }\n      ],\n      \"date_subscribe\":null,\n      \"date_unsubscribe\":null,\n      \"date_created\":\"2016-04-04\",\n      \"date_updated\":null\n   }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "example": 1343965485,
                        "default": 0
                      },
                      "name": {
                        "type": "string",
                        "example": "John"
                      },
                      "email": {
                        "type": "string",
                        "example": "demo@mailerlite.com"
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
                      "type": {
                        "type": "string",
                        "example": "active"
                      },
                      "fields": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "key": {
                              "type": "string",
                              "example": "email"
                            },
                            "value": {
                              "type": "string",
                              "example": "demo@mailerlite.com"
                            },
                            "type": {
                              "type": "string",
                              "example": "TEXT"
                            }
                          }
                        }
                      },
                      "date_subscribe": {},
                      "date_unsubscribe": {},
                      "date_created": {
                        "type": "string",
                        "example": "2016-04-04"
                      },
                      "date_updated": {}
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
              "code": "curl -v https://api.mailerlite.com/api/v2/subscribers \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$subscribersApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->subscribers();\n\n$subscriber = $subscribersApi->find(123); // returns object of subscriber by its ID\n\n$subscriber = $subscribersApi->find('johndoe@mailerlite.com'); // returns object of subscriber by its email"
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
  "_id": "58b53b141065f9c438aa1afe:595655415dd8990047c7cf01"
}
```