# Source: https://developers-classic.mailerlite.com/reference/batch-api-requests.md

# /batch

[block:api-header]
{
  "title": "Important notes"
}
[/block]

* There is a limit of maximum 50 requests per single batch.
* The order of response objects are the same as requests which were sent.
* `requests` parameter should not be empty

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
    "/batch": {
      "post": {
        "summary": "/batch",
        "description": "",
        "operationId": "batch-api-requests",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "requests"
                ],
                "properties": {
                  "requests": {
                    "type": "string",
                    "description": "Array of request objects containg method, path and body (optional).",
                    "format": "json"
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
                    "value": "[\n  {\n    \"body\": [\n      {\n        \"id\": 1,\n        \"name\": \"Test Group\",\n        \"total\": 19,\n        \"active\": 19,\n        \"unsubscribed\": 0,\n        \"bounced\": 0,\n        \"unconfirmed\": 0,\n        \"junk\": 0,\n        \"sent\": 0,\n        \"opened\": 0,\n        \"clicked\": 0,\n        \"date_created\": \"2017-05-01 09:24:36\",\n        \"date_updated\": \"2017-05-01 12:16:09\"\n      },\n      {\n        \"id\": 2,\n        \"name\": \"Another one\",\n        \"total\": 5,\n        \"active\": 5,\n        \"unsubscribed\": 0,\n        \"bounced\": 0,\n        \"unconfirmed\": 0,\n        \"junk\": 0,\n        \"sent\": 0,\n        \"opened\": 0,\n        \"clicked\": 0,\n        \"date_created\": \"2017-06-01 13:20:17\",\n        \"date_updated\": \"2017-06-01 13:23:20\"\n       }\n    ],\n    \"status\": 200\n  },\n  {\n    \"body\": {\n      \"id\": 3,\n      \"name\": \"New group\",\n      \"total\": 0,\n      \"active\": 0,\n      \"unsubscribed\": 0,\n      \"bounced\": 0,\n      \"unconfirmed\": 0,\n      \"junk\": 0,\n      \"sent\": 0,\n      \"opened\": 0,\n      \"clicked\": 0,\n      \"date_created\": null,\n      \"date_updated\": null\n    },\n    \"status\": 201\n  }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "body": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "name": {
                              "type": "string",
                              "example": "Test Group"
                            },
                            "total": {
                              "type": "integer",
                              "example": 19,
                              "default": 0
                            },
                            "active": {
                              "type": "integer",
                              "example": 19,
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
                            "date_created": {
                              "type": "string",
                              "example": "2017-05-01 09:24:36"
                            },
                            "date_updated": {
                              "type": "string",
                              "example": "2017-05-01 12:16:09"
                            }
                          }
                        }
                      },
                      "status": {
                        "type": "integer",
                        "example": 200,
                        "default": 0
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
                    "value": "{\n  \"error\": {\n    \"code\": 400,\n    \"message\": \"Every request in a query must have method and path parameters\"\n  }\n}"
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
                          "example": "Every request in a query must have method and path parameters"
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/batch \\\n-d '{\n\t\"requests\": [\n\t\t{\n    \t\"method\":\"GET\",\n      \"path\": \"/api/v2/groups\"\n    },\n\t\t{\n    \t\"method\":\"POST\",\n      \"path\": \"/api/v2/groups\",\n      \"body\": {\n      \t\"name\": \"New group\"\n       }\n     }\n   ]\n}' \\\n-H 'Content-Type: application/json' \\\n-H 'X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9'"
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
  "_id": "58b53b141065f9c438aa1afe:5a0be1e0ada585001eb0bfd0"
}
```