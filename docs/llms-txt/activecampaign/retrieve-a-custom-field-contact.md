# Source: https://developers.activecampaign.com/reference/retrieve-a-custom-field-contact.md

# Get a custom field by ID

```json GET /fields/:id (Example RESPONSE)
{
    "fieldOptions": [],
    "fieldRels": [
        {
            "field": "1",
            "relid": "0",
            "dorder": "0",
            "cdate": "2018-08-17T11:09:43-05:00",
            "links": [],
            "id": "1"
        }
    ],
    "field": {
        "title": "test",
        "descript": "",
        "type": "text",
        "isrequired": "0",
        "perstag": "TEST",
        "defval": "",
        "show_in_list": "0",
        "rows": "0",
        "cols": "0",
        "visible": "1",
        "service": "",
        "ordernum": "1",
        "cdate": "2018-08-17T11:09:43-05:00",
        "udate": "2018-08-17T11:09:43-05:00",
        "options": [],
        "relations": [
            "1"
        ],
        "links": {
            "options": "https://:account.api-us1.com/api/3/fields/1/options",
            "relations": "https://:account.api-us1.com/api/3/fields/1/relations"
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
    "/fields/{id}": {
      "get": {
        "summary": "Get a custom field by ID",
        "description": "",
        "operationId": "retrieve-a-custom-field-contact",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of the field to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32"
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
                    "value": "{\n    \"fieldOptions\": [],\n    \"fieldRels\": [\n        {\n            \"field\": \"1\",\n            \"relid\": \"0\",\n            \"dorder\": \"0\",\n            \"cdate\": \"2018-08-17T11:09:43-05:00\",\n            \"links\": [],\n            \"id\": \"1\"\n        }\n    ],\n    \"field\": {\n        \"title\": \"test\",\n        \"descript\": \"\",\n        \"type\": \"text\",\n        \"isrequired\": \"0\",\n        \"perstag\": \"TEST\",\n        \"defval\": \"\",\n        \"show_in_list\": \"0\",\n        \"rows\": \"0\",\n        \"cols\": \"0\",\n        \"visible\": \"1\",\n        \"service\": \"\",\n        \"ordernum\": \"1\",\n        \"cdate\": \"2018-08-17T11:09:43-05:00\",\n        \"udate\": \"2018-08-17T11:09:43-05:00\",\n        \"options\": [],\n        \"relations\": [\n            \"1\"\n        ],\n        \"links\": {\n            \"options\": \"https://:account.api-us1.com/api/3/fields/1/options\",\n            \"relations\": \"https://:account.api-us1.com/api/3/fields/1/relations\"\n        },\n        \"id\": \"1\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "fieldOptions": {
                      "type": "array"
                    },
                    "fieldRels": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "field": {
                            "type": "string",
                            "example": "1"
                          },
                          "relid": {
                            "type": "string",
                            "example": "0"
                          },
                          "dorder": {
                            "type": "string",
                            "example": "0"
                          },
                          "cdate": {
                            "type": "string",
                            "example": "2018-08-17T11:09:43-05:00"
                          },
                          "links": {
                            "type": "array"
                          },
                          "id": {
                            "type": "string",
                            "example": "1"
                          }
                        }
                      }
                    },
                    "field": {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "string",
                          "example": "test"
                        },
                        "descript": {
                          "type": "string",
                          "example": ""
                        },
                        "type": {
                          "type": "string",
                          "example": "text"
                        },
                        "isrequired": {
                          "type": "string",
                          "example": "0"
                        },
                        "perstag": {
                          "type": "string",
                          "example": "TEST"
                        },
                        "defval": {
                          "type": "string",
                          "example": ""
                        },
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
                          "example": "1"
                        },
                        "cdate": {
                          "type": "string",
                          "example": "2018-08-17T11:09:43-05:00"
                        },
                        "udate": {
                          "type": "string",
                          "example": "2018-08-17T11:09:43-05:00"
                        },
                        "options": {
                          "type": "array"
                        },
                        "relations": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "1"
                          }
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "options": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/fields/1/options"
                            },
                            "relations": {
                              "type": "string",
                              "example": "https://:account.api-us1.com/api/3/fields/1/relations"
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