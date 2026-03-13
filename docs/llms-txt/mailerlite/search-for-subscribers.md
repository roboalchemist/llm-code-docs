# Source: https://developers-classic.mailerlite.com/reference/search-for-subscribers.md

# /subscribers/search

Search for subscribers [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

Response contains [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) objects.

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
    "/subscribers/search": {
      "get": {
        "summary": "/subscribers/search",
        "description": "Search for subscribers [Rate limited]",
        "operationId": "search-for-subscribers",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "schema": {
              "type": "string",
              "default": "null"
            }
          },
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
            "name": "minimized",
            "in": "query",
            "description": "returns minimized response with: id, email, type",
            "schema": {
              "type": "boolean",
              "default": false
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
                    "value": "[\n    {\n    \"id\": 1343965485,\n    \"email\": \"demo@mailerlite.com\",\n    \"sent\": 0,\n    \"opened\": 0,\n    \"clicked\": 0,\n    \"type\": \"active\",\n    \"fields\": [\n      {\n        \"key\": \"email\",\n        \"value\": \"demo@mailerlite.com\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"name\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"last_name\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"company\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"country\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"city\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"phone\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"state\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      },\n      {\n        \"key\": \"zip\",\n        \"value\": \"\",\n        \"type\": \"TEXT\"\n      }\n    ],\n    \"date_subscribe\": null,\n    \"date_unsubscribe\": null,\n    \"date_created\": \"2016-04-04\"\n  }\n]"
                  },
                  "OK minimized response": {
                    "value": "[\n  {\n    \"id\": 1343965485,\n    \"email\": \"demo@mailerlite.com\",\n    \"type\": \"active\"\n  }\n]"
                  },
                  "OK with no results": {
                    "value": "[]"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "example": 1343965485,
                            "default": 0
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
                          }
                        }
                      }
                    },
                    {
                      "title": "OK minimized response",
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "example": 1343965485,
                            "default": 0
                          },
                          "email": {
                            "type": "string",
                            "example": "demo@mailerlite.com"
                          },
                          "type": {
                            "type": "string",
                            "example": "active"
                          }
                        }
                      }
                    },
                    {
                      "title": "OK with no results",
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {}
                      }
                    }
                  ]
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
              "code": "curl -v https://api.mailerlite.com/api/v2/subscribers/search?query=demo@mailerlite.com \\\n-H \"X-MailerLite-ApiKey: 12a1b1234abcd123123a1231234a1ab2\""
            },
            {
              "language": "php",
              "code": "<?php\n$subscribersApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->subscribers();\n\n$query = 'demo@mailerlite.com';\n\n$subscribers = $subscribersApi->search($query); // returns array of subscriber objects that match query"
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
  "_id": "58b53b141065f9c438aa1afe:56e5b06f9191742000ef207b"
}
```