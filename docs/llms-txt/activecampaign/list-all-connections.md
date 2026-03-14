# Source: https://developers.activecampaign.com/reference/list-all-connections.md

# List all connections

List all existing connection resources.

```json GET /connections (Example RESPONSE)
{
  "connections": [
    {
      "service": "shopify",
      "externalid": "foo.myshopify.com",
      "name": "Foo, Inc.",
      "isInternal": "1",
      "status": "1",
      "syncStatus": "0",
      "lastSync": "2017-02-02T13:09:07-06:00",
      "logoUrl": "",
      "linkUrl": "",
      "listId": "0",
      "cdate": "2017-02-02T13:09:07-06:00",
      "udate": "2017-02-02T13:09:12-06:00",
      "links": {
        "customers": "/api/3/connections/1/customers"
      },
      "id": "1"
    },
    {
      "service": "fooCommerce",
      "externalid": "johndoe@example.com",
      "name": "Acme, Inc.",
      "isInternal": "0",
      "status": "1",
      "syncStatus": "0",
      "lastSync": null,
      "logoUrl": "http://example.com/i/foo.png",
      "linkUrl": "http://example.com/foo/",
      "listId": "1",
      "cdate": "2017-02-02T14:56:05-06:00",
      "udate": "2017-02-03T15:54:51-06:00",
      "links": {
        "customers": "/api/3/connections/2/customers"
      },
      "id": "2"
    }
  ],
  "meta": {
    "total": "2"
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
      "get": {
        "summary": "List all connections",
        "description": "List all existing connection resources.",
        "operationId": "list-all-connections",
        "parameters": [
          {
            "name": "filters[service]",
            "in": "query",
            "description": "Filter by the external service name.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[externalid]",
            "in": "query",
            "description": "Filter by the external id associated with a connection.",
            "schema": {
              "type": "string"
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
                    "value": "{\n  \"connections\": [\n    {\n      \"service\": \"shopify\",\n      \"externalid\": \"foo.myshopify.com\",\n      \"name\": \"Foo, Inc.\",\n      \"isInternal\": \"1\",\n      \"status\": \"1\",\n      \"syncStatus\": \"0\",\n      \"lastSync\": \"2017-02-02T13:09:07-06:00\",\n      \"logoUrl\": \"\",\n      \"linkUrl\": \"\",\n      \"listId\": \"0\",\n      \"cdate\": \"2017-02-02T13:09:07-06:00\",\n      \"udate\": \"2017-02-02T13:09:12-06:00\",\n      \"links\": {\n        \"customers\": \"/api/3/connections/1/customers\"\n      },\n      \"id\": \"1\"\n    },\n    {\n      \"service\": \"fooCommerce\",\n      \"externalid\": \"johndoe@example.com\",\n      \"name\": \"Acme, Inc.\",\n      \"isInternal\": \"0\",\n      \"status\": \"1\",\n      \"syncStatus\": \"0\",\n      \"lastSync\": null,\n      \"logoUrl\": \"http://example.com/i/foo.png\",\n      \"linkUrl\": \"http://example.com/foo/\",\n      \"listId\": \"1\",\n      \"cdate\": \"2017-02-02T14:56:05-06:00\",\n      \"udate\": \"2017-02-03T15:54:51-06:00\",\n      \"links\": {\n        \"customers\": \"/api/3/connections/2/customers\"\n      },\n      \"id\": \"2\"\n    }\n  ],\n  \"meta\": {\n    \"total\": \"2\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "connections": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "service": {
                            "type": "string",
                            "example": "shopify"
                          },
                          "externalid": {
                            "type": "string",
                            "example": "foo.myshopify.com"
                          },
                          "name": {
                            "type": "string",
                            "example": "Foo, Inc."
                          },
                          "isInternal": {
                            "type": "string",
                            "example": "1"
                          },
                          "status": {
                            "type": "string",
                            "example": "1"
                          },
                          "syncStatus": {
                            "type": "string",
                            "example": "0"
                          },
                          "lastSync": {
                            "type": "string",
                            "example": "2017-02-02T13:09:07-06:00"
                          },
                          "logoUrl": {
                            "type": "string",
                            "example": ""
                          },
                          "linkUrl": {
                            "type": "string",
                            "example": ""
                          },
                          "listId": {
                            "type": "string",
                            "example": "0"
                          },
                          "cdate": {
                            "type": "string",
                            "example": "2017-02-02T13:09:07-06:00"
                          },
                          "udate": {
                            "type": "string",
                            "example": "2017-02-02T13:09:12-06:00"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "customers": {
                                "type": "string",
                                "example": "/api/3/connections/1/customers"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "1"
                          }
                        }
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "total": {
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