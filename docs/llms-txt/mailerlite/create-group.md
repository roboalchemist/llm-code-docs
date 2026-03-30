# Source: https://developers-classic.mailerlite.com/reference/create-group.md

# /groups

Create new group. [Rate limited]

[block:api-header]
{
  "type": "basic",
  "title": "Response Body Parameters"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "1-0": "`name`",
    "0-1": "*integer*",
    "1-1": "*string*",
    "2-0": "`total`",
    "2-1": "*integer*",
    "3-0": "`active`",
    "3-1": "*integer*",
    "4-0": "`unsubscribed`",
    "4-1": "*integer*",
    "5-0": "`bounced`",
    "5-1": "*integer*",
    "6-0": "`unconfirmed`",
    "6-1": "*integer*",
    "7-0": "`junk`",
    "7-1": "*integer*",
    "8-0": "`sent`",
    "8-1": "*integer*",
    "9-0": "`opened`",
    "10-0": "`clicked`",
    "9-1": "*integer*",
    "10-1": "*integer*",
    "0-2": "ID of group",
    "1-2": "Title of group",
    "2-2": "Total count of people in group",
    "3-2": "Total count of active people in group",
    "4-2": "Total count of unsubscribed people in group",
    "5-2": "Total count of bounced people in group",
    "6-2": "Total count of unconfirmed people in group",
    "7-2": "Total count of junk people in group",
    "8-2": "Total count of sent emails in a group",
    "9-2": "Total count of opens in a group",
    "10-2": "Total count of clicks in a group",
    "12-0": "`date_updated`",
    "11-0": "`date_created`",
    "12-1": "*string*",
    "11-1": "*string*",
    "12-2": "Date & time when group is updated",
    "11-2": "Date & time when group is created"
  },
  "cols": 3,
  "rows": 13
}
[/block]

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
    "/groups": {
      "post": {
        "summary": "/groups",
        "description": "Create new group. [Rate limited]",
        "operationId": "create-group",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of your group",
                    "default": "Group name"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "201",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"id\": 3640743,\n  \"name\": \"Demo Group\",\n  \"total\": 0,\n  \"active\": 0,\n  \"unsubscribed\": 0,\n  \"bounced\": 0,\n  \"unconfirmed\": 0,\n  \"junk\": 0,\n  \"sent\": 0,\n  \"opened\": 0,\n  \"clicked\": 0,\n  \"date_created\": null,\n  \"date_updated\": null\n}"
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
                    "value": "{\n  \"error\": {\n    \"code\": 123,\n    \"message\": \"Group name must be provided\"\n  }\n}"
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
                          "example": 123,
                          "default": 0
                        },
                        "message": {
                          "type": "string",
                          "example": "Group name must be provided"
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/groups \\\n-d '{\"name\":\"Demo Group\"}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$groupData = ['name' => 'New Group'];\n$groups = $groupsApi->create($groupData); // returns created group object"
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
  "_id": "58b53b141065f9c438aa1afe:56fd1e294388650e00eb4705"
}
```