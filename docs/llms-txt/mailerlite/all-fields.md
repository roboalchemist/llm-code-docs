# Source: https://developers-classic.mailerlite.com/reference/all-fields.md

# /fields

Get subscriber fields of account

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "2-0": "`key`",
    "3-0": "`type`",
    "4-0": "`date_updated`",
    "5-0": "`date_created`",
    "0-1": "*integer*",
    "2-1": "*string*",
    "3-1": "*string*",
    "4-1": "*string*",
    "5-1": "*string*",
    "4-2": "Date & time.\n\nDefault: `null`",
    "5-2": "Date & time.\n\nDefault: `null`",
    "3-2": "**Possible values:**\n\n- `TEXT`\n- `NUMBER`\n- `DATE`",
    "2-2": "Key of field which is generated automatically",
    "1-0": "`title`",
    "1-1": "*string*",
    "1-2": "Title of field",
    "0-2": "ID of field"
  },
  "cols": 3,
  "rows": 6
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
    "/fields": {
      "get": {
        "summary": "/fields",
        "description": "Get subscriber fields of account",
        "operationId": "all-fields",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  {\n    \"id\": 6,\n    \"title\": \"Name\",\n    \"key\": \"name\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 8,\n    \"title\": \"Email\",\n    \"key\": \"email\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 12,\n    \"title\": \"Company\",\n    \"key\": \"company\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 14,\n    \"title\": \"Country\",\n    \"key\": \"country\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 16,\n    \"title\": \"City\",\n    \"key\": \"city\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 18,\n    \"title\": \"Phone\",\n    \"key\": \"phone\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 20,\n    \"title\": \"State\",\n    \"key\": \"state\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 22,\n    \"title\": \"ZIP\",\n    \"key\": \"zip\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 24,\n    \"title\": \"Last name\",\n    \"key\": \"last_name\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"\",\n    \"date_created\": \"\"\n  },\n  {\n    \"id\": 28349,\n    \"title\": \"Favourite Color\",\n    \"key\": \"favourite_color\",\n    \"type\": \"TEXT\",\n    \"date_updated\": \"2016-03-30 21:08:59\",\n    \"date_created\": \"2016-03-30 21:08:59\"\n  }\n]"
                  }
                },
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "example": 6,
                        "default": 0
                      },
                      "title": {
                        "type": "string",
                        "example": "Name"
                      },
                      "key": {
                        "type": "string",
                        "example": "name"
                      },
                      "type": {
                        "type": "string",
                        "example": "TEXT"
                      },
                      "date_updated": {
                        "type": "string",
                        "example": ""
                      },
                      "date_created": {
                        "type": "string",
                        "example": ""
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
              "code": "curl -v https://api.mailerlite.com/api/v2/fields \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$fieldsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->fields();\n\n$fields = $fieldsApi->get(); // returns array of field objects"
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
  "_id": "58b53b141065f9c438aa1afe:5702850e18ad001700a2944b"
}
```