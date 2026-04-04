# Source: https://developers.activecampaign.com/reference/retrieve-fields.md

# List all custom fields

```json GET /fields (Example RESPONSE)
{
    "fieldOptions": [],
    "fieldRels": [],
    "fields": [
        {
            "title": "Another Test Title",
            "descript": null,
            "type": "",
            "isrequired": "0",
            "perstag": "ANOTHER_TEST_TITLE",
            "defval": null,
            "show_in_list": "0",
            "rows": "0",
            "cols": "0",
            "visible": "1",
            "service": "",
            "ordernum": "2",
            "cdate": "2018-11-15T21:43:38-06:00",
            "udate": "2018-11-15T21:43:38-06:00",
            "options": [],
            "relations": [],
            "links": {
                "options": "https://:account.api-us1.com/api/:version/fields/2/options",
                "relations": "https://:account.api-us1.com/api/:version/fields/2/relations"
            },
            "id": "2"
        },
        {
            "title": "Title",
            "descript": "Field  description",
            "type": "textarea",
            "isrequired": "1",
            "perstag": "PERSONALIZEDTAG",
            "defval": "Defaut Value",
            "show_in_list": "1",
            "rows": "2",
            "cols": "2",
            "visible": "1",
            "service": "google",
            "ordernum": "3",
            "cdate": "2018-11-15T21:42:40-06:00",
            "udate": "2018-11-15T21:49:52-06:00",
            "options": [],
            "relations": [],
            "links": {
                "options": "https://:account.api-us1.com/api/:version/fields/1/options",
                "relations": "https://:account.api-us1.com/api/:version/fields/1/relations"
            },
            "id": "1"
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
    "/fields": {
      "get": {
        "summary": "List all custom fields",
        "description": "",
        "operationId": "retrieve-fields",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "The number of fields returned per request.",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 100
            }
          },
          {
            "name": "filters[perstag]",
            "in": "query",
            "description": "The custom field's persistant tag to filter by (Ex: CUSTOMER_GROUP)",
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
                    "value": "{\n    \"fieldOptions\": [],\n    \"fieldRels\": [],\n    \"fields\": [\n        {\n            \"title\": \"Another Test Title\",\n            \"descript\": null,\n            \"type\": \"\",\n            \"isrequired\": \"0\",\n            \"perstag\": \"ANOTHER_TEST_TITLE\",\n            \"defval\": null,\n            \"show_in_list\": \"0\",\n            \"rows\": \"0\",\n            \"cols\": \"0\",\n            \"visible\": \"1\",\n            \"service\": \"\",\n            \"ordernum\": \"2\",\n            \"cdate\": \"2018-11-15T21:43:38-06:00\",\n            \"udate\": \"2018-11-15T21:43:38-06:00\",\n            \"options\": [],\n            \"relations\": [],\n            \"links\": {\n                \"options\": \"https://:account.api-us1.com/api/:version/fields/2/options\",\n                \"relations\": \"https://:account.api-us1.com/api/:version/fields/2/relations\"\n            },\n            \"id\": \"2\"\n        },\n        {\n            \"title\": \"Title\",\n            \"descript\": \"Field  description\",\n            \"type\": \"textarea\",\n            \"isrequired\": \"1\",\n            \"perstag\": \"PERSONALIZEDTAG\",\n            \"defval\": \"Defaut Value\",\n            \"show_in_list\": \"1\",\n            \"rows\": \"2\",\n            \"cols\": \"2\",\n            \"visible\": \"1\",\n            \"service\": \"google\",\n            \"ordernum\": \"3\",\n            \"cdate\": \"2018-11-15T21:42:40-06:00\",\n            \"udate\": \"2018-11-15T21:49:52-06:00\",\n            \"options\": [],\n            \"relations\": [],\n            \"links\": {\n                \"options\": \"https://:account.api-us1.com/api/:version/fields/1/options\",\n                \"relations\": \"https://:account.api-us1.com/api/:version/fields/1/relations\"\n            },\n            \"id\": \"1\"\n        }\n    ],\n    \"meta\": {\n        \"total\": \"2\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "fieldOptions": {
                      "type": "array"
                    },
                    "fieldRels": {
                      "type": "array"
                    },
                    "fields": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "title": {
                            "type": "string",
                            "example": "Another Test Title"
                          },
                          "descript": {},
                          "type": {
                            "type": "string",
                            "example": ""
                          },
                          "isrequired": {
                            "type": "string",
                            "example": "0"
                          },
                          "perstag": {
                            "type": "string",
                            "example": "ANOTHER_TEST_TITLE"
                          },
                          "defval": {},
                          "show_in_list": {
                            "type": "string",
                            "example": "0"
                          },
                          "rows": {
                            "type": "string",
                            "example": "0"
                          },
                          "cols": {
                            "type": "string",
                            "example": "0"
                          },
                          "visible": {
                            "type": "string",
                            "example": "1"
                          },
                          "service": {
                            "type": "string",
                            "example": ""
                          },
                          "ordernum": {
                            "type": "string",
                            "example": "2"
                          },
                          "cdate": {
                            "type": "string",
                            "example": "2018-11-15T21:43:38-06:00"
                          },
                          "udate": {
                            "type": "string",
                            "example": "2018-11-15T21:43:38-06:00"
                          },
                          "options": {
                            "type": "array"
                          },
                          "relations": {
                            "type": "array"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "options": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/fields/2/options"
                              },
                              "relations": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/:version/fields/2/relations"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "2"
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