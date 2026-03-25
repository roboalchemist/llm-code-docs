# Source: https://developers-classic.mailerlite.com/reference/groupsby_group_namesubscribers.md

# /groups/group_name/subscribers

Add a new single subscriber to the group with the given name. If the group doesn't exist, it gets created. If multiple groups with the same name exist, the subscriber is added to the oldest group. [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

Response contains [Single Subscriber](https://developers-classic.mailerlite.com/docs/single-subscriber) object.

[block:api-header]
{
  "type": "basic",
  "title": "Double opt-in for API"
}
[/block]

Find out how to enable it [in our help center](https://help.mailerlite.com/article/show/29273-double-opt-in-for-api).

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
    "/groups/group_name/subscribers": {
      "post": {
        "summary": "/groups/group_name/subscribers",
        "description": "Add a new single subscriber to the group with the given name. If the group doesn't exist, it gets created. If multiple groups with the same name exist, the subscriber is added to the oldest group. [Rate limited]",
        "operationId": "groupsby_group_namesubscribers",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "group_name": {
                    "type": "string",
                    "description": "The name of the group to add the subscriber to"
                  },
                  "email": {
                    "type": "string",
                    "description": "email of new subscriber",
                    "default": "null"
                  },
                  "name": {
                    "type": "string"
                  },
                  "fields": {
                    "type": "object",
                    "description": "object that contains your custom fields. i.e. company, city, state, etc.",
                    "properties": {
                      "company": {
                        "type": "string"
                      },
                      "city": {
                        "type": "string"
                      }
                    }
                  },
                  "resubscribe": {
                    "type": "boolean",
                    "description": "reactivate subscriber if value is true",
                    "default": false
                  },
                  "autoresponders": {
                    "type": "boolean",
                    "description": "autoresponders will be sent if value is true",
                    "default": true
                  },
                  "type": {
                    "type": "string",
                    "description": "available values: unsubscribed, active, unconfirmed",
                    "default": "null"
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
                    "value": "{\n  \"id\": 1343965485,\n  \"name\": \"John\",\n  \"email\": \"demo@mailerlite.com\",\n  \"sent\": 0,\n  \"opened\": 0,\n  \"clicked\": 0,\n  \"type\": \"active\",\n  \"fields\": [\n    {\n      \"key\": \"email\",\n      \"value\": \"demo@mailerlite.com\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"name\",\n      \"value\": \"John\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"last_name\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"company\",\n      \"value\": \"MailerLite\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"country\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"city\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"phone\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"state\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    },\n    {\n      \"key\": \"zip\",\n      \"value\": \"\",\n      \"type\": \"TEXT\"\n    }\n  ],\n  \"date_subscribe\": null,\n  \"date_unsubscribe\": null,\n  \"date_created\": \"2016-04-04\"\n}"
                  }
                },
                "schema": {
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/groups/group_name/subscribers \\\n-d '{\"group_name\": \"Demo group\", \"email\":\"demo@mailerlite.com\", \"name\": \"John\", \"fields\": {\"company\": \"MailerLite\"}}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
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
  "_id": "58b53b141065f9c438aa1afe:60cb441c93cb250252acbfd7"
}
```