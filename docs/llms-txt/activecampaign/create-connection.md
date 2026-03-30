# Source: https://developers.activecampaign.com/reference/create-connection.md

# Create a connection

Create a new connection resource.

```json POST /connections (Example REQUEST)
{
  "connection": {
    "service": "fooCommerce",
    "externalid": "toystore123",
    "name": "Toystore, Inc.",
    "logoUrl": "http://example.com/i/foo.png",
    "linkUrl": "http://example.com/foo/",
    "listId": "1"
  }
}
```

```json POST /connections (Example RESPONSE)
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
    "/connections": {
      "post": {
        "summary": "Create a connection",
        "description": "Create a new connection resource.",
        "operationId": "create-connection",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "connection": {
                    "properties": {
                      "service": {
                        "type": "string",
                        "description": "The name of the service."
                      },
                      "externalid": {
                        "type": "string",
                        "description": "The id of the account in the external service."
                      },
                      "name": {
                        "type": "string",
                        "description": "The name associated with the account in the external service. Often this will be a company name (e.g., 'My Toystore, Inc.')."
                      },
                      "logoUrl": {
                        "type": "string",
                        "description": "The URL to a logo image for the external service."
                      },
                      "linkUrl": {
                        "type": "string",
                        "description": "The URL to a page where the integration with the external service can be managed in the third-party's website."
                      },
                      "listId": {
                        "type": "string",
                        "description": "The ID of list where new contacts from connection will be synced"
                      }
                    },
                    "required": [
                      "service",
                      "externalid",
                      "name",
                      "logoUrl",
                      "linkUrl"
                    ],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "JSON": {
                  "value": {
                    "connection": {
                      "service": "fooCommerce",
                      "externalid": "toystore123",
                      "name": "Toystore, Inc.",
                      "logoUrl": "http://example.com/i/foo.png",
                      "linkUrl": "http://example.com/foo/",
                      "listId": "1"
                    }
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
                    "value": "{\n  \"connection\": {\n    \"isInternal\": 0,\n    \"service\": \"fooCommerce\",\n    \"externalid\": \"toystore123\",\n    \"name\": \"Toystore, Inc.\",\n    \"logoUrl\": \"http://example.com/i/foo.png\",\n    \"linkUrl\": \"http://example.com/foo/\",\n\t\t\"listId\": \"1\",\n    \"cdate\": \"2017-02-02T14:56:05-06:00\",\n    \"udate\": \"2017-02-02T14:56:05-06:00\",\n    \"links\": {\n      \"customers\": \"/connections/1/customers\"\n    },\n    \"id\": \"1\"\n  }\n}"
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