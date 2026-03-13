# Source: https://developers-classic.mailerlite.com/reference/groups.md

# /groups

Get list of groups. [Rate limited]

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
      "get": {
        "summary": "/groups",
        "description": "Get list of groups. [Rate limited]",
        "operationId": "groups",
        "parameters": [
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
            "name": "offset",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "filters",
            "in": "query",
            "schema": {
              "type": "string",
              "default": "null"
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
                    "value": "[\n  {\n    \"id\": 3640549,\n    \"name\": \"Demo API v2 List\",\n    \"total\": 1,\n    \"active\": 1,\n    \"unsubscribed\": 0,\n    \"bounced\": 0,\n    \"unconfirmed\": 0,\n    \"junk\": 0,\n    \"sent\": 0,\n    \"opened\": 0,\n    \"clicked\": 0,\n    \"date_created\": \"2016-04-04 11:02:33\",\n    \"date_updated\": \"2016-04-04 11:02:33\"\n  },\n  {\n    \"id\": 3640743,\n    \"name\": \"Demo Group\",\n    \"total\": 0,\n    \"active\": 0,\n    \"unsubscribed\": 0,\n    \"bounced\": 0,\n    \"unconfirmed\": 0,\n    \"junk\": 0,\n    \"sent\": 0,\n    \"opened\": 0,\n    \"clicked\": 0,\n    \"date_created\": \"2016-04-04 11:14:18\",\n    \"date_updated\": \"2016-04-04 11:14:18\"\n  }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "example": 3640549,
                        "default": 0
                      },
                      "name": {
                        "type": "string",
                        "example": "Demo API v2 List"
                      },
                      "total": {
                        "type": "integer",
                        "example": 1,
                        "default": 0
                      },
                      "active": {
                        "type": "integer",
                        "example": 1,
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
                        "example": "2016-04-04 11:02:33"
                      },
                      "date_updated": {
                        "type": "string",
                        "example": "2016-04-04 11:02:33"
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
              "code": "curl -v https://api.mailerlite.com/api/v2/groups \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$groupsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->groups();\n\n$groups = $groupsApi->get(); // returns array of groups"
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
  "_id": "58b53b141065f9c438aa1afe:56e5b06f9191742000ef2078"
}
```