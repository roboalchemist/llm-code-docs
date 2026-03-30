# Source: https://developers-classic.mailerlite.com/reference/create-field.md

# /fields

Create new custom field in account

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
      "post": {
        "summary": "/fields",
        "description": "Create new custom field in account",
        "operationId": "create-field",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "string",
                    "description": "Title of field"
                  },
                  "type": {
                    "type": "string",
                    "description": "Type of field. Available values: TEXT, NUMBER, DATE",
                    "default": "TEXT"
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
                    "value": "{\n  \"id\": 28353,\n  \"title\": \"Favourite Color\",\n  \"key\": \"favourite_color\",\n  \"type\": \"TEXT\",\n  \"date_updated\": \"2016-04-04 15:46:15\",\n  \"date_created\": \"2016-04-04 15:46:15\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer",
                      "example": 28353,
                      "default": 0
                    },
                    "title": {
                      "type": "string",
                      "example": "Favourite Color"
                    },
                    "key": {
                      "type": "string",
                      "example": "favourite_color"
                    },
                    "type": {
                      "type": "string",
                      "example": "TEXT"
                    },
                    "date_updated": {
                      "type": "string",
                      "example": "2016-04-04 15:46:15"
                    },
                    "date_created": {
                      "type": "string",
                      "example": "2016-04-04 15:46:15"
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
                  "Title Not Provided": {
                    "value": "{\n  \"error\": {\n    \"code\": 123,\n    \"message\": \"You must provide field title\"\n  }\n}"
                  },
                  "All Fields Are Used": {
                    "value": "{\n  \"error\": {\n    \"code\": 123,\n    \"message\": \"You used all available fields\"\n  }\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "title": "Title Not Provided",
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
                              "example": "You must provide field title"
                            }
                          }
                        }
                      }
                    },
                    {
                      "title": "All Fields Are Used",
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
                              "example": "You used all available fields"
                            }
                          }
                        }
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
              "code": "curl -X POST https://api.mailerlite.com/api/v2/fields \\\n-d '{\"title\": \"Favourite Color\"}' \\\n-H \"Content-Type: application/json\" \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\""
            },
            {
              "language": "php",
              "code": "<?php\n$fieldsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->fields();\n\n$fieldData = [\n  'title' => 'Eye Color',\n  'type' => 'TEXT'\n];\n\n$addedField = $fieldsApi->create($fieldData); // returns created field object"
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
  "_id": "58b53b141065f9c438aa1afe:5703a0748ed24e0e006894ce"
}
```