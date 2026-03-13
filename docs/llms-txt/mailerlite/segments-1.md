# Source: https://developers-classic.mailerlite.com/reference/segments-1.md

# /segments

Returns all stored segments in your account.

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
    "0-0": "**id**",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Description",
    "1-0": "**title**",
    "2-0": "**filter**",
    "3-0": "**total**",
    "4-0": "**sent**",
    "5-0": "**opened**",
    "5-1": "`Integer`",
    "4-1": "`Integer`",
    "3-1": "`Integer`",
    "2-1": "`Object`",
    "1-1": "`String`",
    "0-1": "`Integer`",
    "1-3": "",
    "1-2": "Title of the segment",
    "2-2": "Array of segment rules",
    "4-2": "Total number of sent emails to the segment subscribers",
    "5-2": "Total number of opened emails by segment subscribers",
    "3-2": "Number of subscribers in the filter",
    "0-2": "ID of the segment",
    "6-0": "**clicked**",
    "6-1": "`Integer`",
    "6-2": "Total number or clicked links by segment subscribers"
  },
  "cols": 3,
  "rows": 7
}
[/block]

[block:api-header]
{
  "title": "/segments/count"
}
[/block]

You can retrieve only the number of segments.

[block:api-header]
{
  "type": "basic",
  "title": "Response example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"count\": 3\n}",
      "language": "json",
      "name": "200 OK"
    }
  ]
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
    "/segments": {
      "get": {
        "summary": "/segments",
        "description": "Returns all stored segments in your account.",
        "operationId": "segments-1",
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
            "name": "order",
            "in": "query",
            "description": "ASC or DESC",
            "schema": {
              "type": "string",
              "default": "desc"
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
                    "value": "{\n  \"data\": [\n    {\n      \"id\": 1,\n      \"title\": \"Segment 1\",\n      \"filter\": {\n        \"rules\": [\n          {\n            \"operator\": \"text_field_contains\",\n            \"args\": [\n              \"8\",\n              \"*@mailerlite.com\"\n            ]\n          }\n        ]\n      },\n      \"total\": 0,\n      \"sent\": 0,\n      \"opened\": 0,\n      \"clicked\": 0,\n      \"created_at\": \"2018-06-08 17:30:56\",\n      \"updated_at\": \"2018-06-08 17:30:56\"\n    }\n  ],\n  \"meta\": {\n    \"pagination\": {\n      \"total\": 1,\n      \"count\": 1,\n      \"per_page\": 100,\n      \"current_page\": 1,\n      \"total_pages\": 1,\n      \"links\": [\n        \n      ]\n    }\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "example": 1,
                            "default": 0
                          },
                          "title": {
                            "type": "string",
                            "example": "Segment 1"
                          },
                          "filter": {
                            "type": "object",
                            "properties": {
                              "rules": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "operator": {
                                      "type": "string",
                                      "example": "text_field_contains"
                                    },
                                    "args": {
                                      "type": "array",
                                      "items": {
                                        "type": "string",
                                        "example": "8"
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          },
                          "total": {
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
                          "created_at": {
                            "type": "string",
                            "example": "2018-06-08 17:30:56"
                          },
                          "updated_at": {
                            "type": "string",
                            "example": "2018-06-08 17:30:56"
                          }
                        }
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "pagination": {
                          "type": "object",
                          "properties": {
                            "total": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "count": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "per_page": {
                              "type": "integer",
                              "example": 100,
                              "default": 0
                            },
                            "current_page": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "total_pages": {
                              "type": "integer",
                              "example": 1,
                              "default": 0
                            },
                            "links": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {}
                              }
                            }
                          }
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
              "code": "curl -v https://api.mailerlite.com/api/v2/segments \\\n-H \"X-MailerLite-ApiKey: fc7b8c5b32067bcd47cafb5f475d2fe9\" \\"
            },
            {
              "language": "php",
              "code": "<?php\n$segmentsApi = (new \\MailerLiteApi\\MailerLite('your-api-key'))->segments();\n\n$segments = $segmentsApi->get(); // returns array of segments"
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
  "_id": "58b53b141065f9c438aa1afe:5b1a5ca1feba3f00039d5129"
}
```