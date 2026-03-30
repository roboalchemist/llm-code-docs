# Source: https://developers.activecampaign.com/reference/get-connection.md

# Retrieve a connection

Retrieve an existing connection resource.

```json GET /connections/:id (Example RESPONSE)
{
  "connection": {
    "isInternal": 0,
    "service": "fooCommerce",
    "externalid": "toystore123",
    "name": "Toystore, Inc.",
    "logoUrl": "http://example.com/i/foo.png",
    "linkUrl": "http://example.com/foo/",
    "listId": "1",
    "cdate": "2017-02-02T14:56:05-06:00",
    "udate": "2017-02-02T14:56:05-06:00",
    "links": {
      "customers": "/connections/1/customers"
    },
    "id": "1"
  }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/connections/{id}": {
      "get": {
        "summary": "Retrieve a connection",
        "description": "Retrieve an existing connection resource.",
        "operationId": "get-connection",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The id of the connection to retrieve",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"connection\": {\n    \"isInternal\": 0,\n    \"service\": \"fooCommerce\",\n    \"externalid\": \"toystore123\",\n    \"name\": \"Toystore, Inc.\",\n    \"logoUrl\": \"http://example.com/i/foo.png\",\n    \"linkUrl\": \"http://example.com/foo/\",\n    \"listId\": \"1\",  \n    \"cdate\": \"2017-02-02T14:56:05-06:00\",\n    \"udate\": \"2017-02-02T14:56:05-06:00\",\n    \"links\": {\n      \"customers\": \"/connections/1/customers\"\n    },\n    \"id\": \"1\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "connection": {
                      "type": "object",
                      "properties": {
                        "isInternal": {
                          "type": "integer",
                          "example": 0,
                          "default": 0
                        },
                        "service": {
                          "type": "string",
                          "example": "fooCommerce"
                        },
                        "externalid": {
                          "type": "string",
                          "example": "toystore123"
                        },
                        "name": {
                          "type": "string",
                          "example": "Toystore, Inc."
                        },
                        "logoUrl": {
                          "type": "string",
                          "example": "http://example.com/i/foo.png"
                        },
                        "linkUrl": {
                          "type": "string",
                          "example": "http://example.com/foo/"
                        },
                        "listId": {
                          "type": "string",
                          "example": "1"
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2017-02-02T14:56:05-06:00"
                        },
                        "udate": {
                          "type": "string",
                          "example": "2017-02-02T14:56:05-06:00"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "customers": {
                              "type": "string",
                              "example": "/connections/1/customers"
                            }
                          }
                        },
                        "id": {
                          "type": "string",
                          "example": "1"
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
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```