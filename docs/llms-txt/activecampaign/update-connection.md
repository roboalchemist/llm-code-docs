# Source: https://developers.activecampaign.com/reference/update-connection.md

# Update a connection

Update an existing connection resource.

```json PUT /connections/:id (Example REQUEST)
{
  "connection": {
    "externalid": "johndoe@example.com",
    "name": "Acme, Inc."
  }
}
```

```json PUT /connections/:id (Example RESPONSE)
{
  "connection": {
    "service": "fooCommerce",
    "externalid": "johndoe@example.com",
    "name": "Acme, Inc.",
    "isInternal": "0",
    "status": "1",
    "syncStatus": "0",
    "logoUrl": "http://foocorp.net/i/path3523.png",
    "linkUrl": "http://example.com/",
    "listId": "1",
    "cdate": "2017-02-02T14:56:05-06:00",
    "udate": "2017-02-03T15:54:51-06:00",
    "links": {
      "customers": "/api/3/connections/2/customers"
    },
    "id": "2"
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
      "put": {
        "summary": "Update a connection",
        "description": "Update an existing connection resource.",
        "operationId": "update-connection",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "The id of the connection to update",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
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
                        "description": "The name associated with the account in the external service."
                      },
                      "logoUrl": {
                        "type": "string",
                        "description": "The URL to a logo image for the third-party service."
                      },
                      "linkUrl": {
                        "type": "string",
                        "description": "The link to the third-party integrator's site."
                      },
                      "status": {
                        "type": "integer",
                        "description": "The status of the connection (0 = error; 1 = connected)",
                        "format": "int32"
                      },
                      "syncStatus": {
                        "type": "integer",
                        "description": "The status of a sync triggered on the connection (0 = sync stopped; 1 = sync running).",
                        "format": "int32"
                      }
                    },
                    "required": [],
                    "type": "object"
                  }
                }
              },
              "examples": {
                "JSON": {
                  "value": {
                    "connection": {
                      "externalid": "johndoe@example.com",
                      "name": "Acme, Inc."
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
                    "value": "{\n  \"connection\": {\n    \"service\": \"fooCommerce\",\n    \"externalid\": \"johndoe@example.com\",\n    \"name\": \"Acme, Inc.\",\n    \"isInternal\": \"0\",\n    \"status\": \"1\",\n    \"syncStatus\": \"0\",\n    \"logoUrl\": \"http://foocorp.net/i/path3523.png\",\n    \"linkUrl\": \"http://example.com/\",\n    \"listId\": \"1\",\n    \"cdate\": \"2017-02-02T14:56:05-06:00\",\n    \"udate\": \"2017-02-03T15:54:51-06:00\",\n    \"links\": {\n      \"customers\": \"/api/3/connections/2/customers\"\n    },\n    \"id\": \"2\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "connection": {
                      "type": "object",
                      "properties": {
                        "service": {
                          "type": "string",
                          "example": "fooCommerce"
                        },
                        "externalid": {
                          "type": "string",
                          "example": "johndoe@example.com"
                        },
                        "name": {
                          "type": "string",
                          "example": "Acme, Inc."
                        },
                        "isInternal": {
                          "type": "string",
                          "example": "0"
                        },
                        "status": {
                          "type": "string",
                          "example": "1"
                        },
                        "syncStatus": {
                          "type": "string",
                          "example": "0"
                        },
                        "logoUrl": {
                          "type": "string",
                          "example": "http://foocorp.net/i/path3523.png"
                        },
                        "linkUrl": {
                          "type": "string",
                          "example": "http://example.com/"
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
                          "example": "2017-02-03T15:54:51-06:00"
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "customers": {
                              "type": "string",
                              "example": "/api/3/connections/2/customers"
                            }
                          }
                        },
                        "id": {
                          "type": "string",
                          "example": "2"
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