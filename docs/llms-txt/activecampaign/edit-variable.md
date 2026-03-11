# Source: https://developers.activecampaign.com/reference/edit-variable.md

# Edit a Variable

Edit a personalization variable

```json PUT /personalizations/{id} (Example REQUEST)
{
    "personalization": {
        "tag": "brand new tag",
        "name": "changed name",
        "format": "text",
        "content": "Hello World!",
        "listids": "2,3,4,5"
    }
}
```

```json PUT /personalizations/{id} (Example RESPONSE)
{
    "personalization": {
        "userid": "1",
        "tag": "brand-new-tag",
        "name": "changed name",
        "content": "Hello World!",
        "format": "text",
        "created_timestamp": "2024-08-14 12:31:35",
        "updated_timestamp": "2024-08-14 12:31:35",
        "created_by": null,
        "updated_by": null,
        "listids": "2,3,4,5",
        "links": [],
        "id": "8"
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
    "/personalizations/{variableID}": {
      "put": {
        "summary": "Edit a Variable",
        "description": "Edit a personalization variable",
        "operationId": "edit-variable",
        "parameters": [
          {
            "name": "variableID",
            "in": "path",
            "description": "ID (int) of personalization/variable",
            "schema": {
              "type": "integer",
              "format": "int32"
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
                  "personalization": {
                    "properties": {
                      "tag": {
                        "type": "string",
                        "description": "tag name"
                      },
                      "name": {
                        "type": "string",
                        "description": "Tag name"
                      },
                      "format": {
                        "type": "string",
                        "description": "\"html\" or \"text\""
                      },
                      "content": {
                        "type": "string",
                        "description": "Personalization/Variable contents"
                      },
                      "listids": {
                        "type": "string",
                        "description": "Comma-separated list of list ids (string), ie: \"2,3,4,5\""
                      }
                    },
                    "required": [],
                    "type": "object"
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
                    "value": {
                      "personalization": {
                        "userid": "1",
                        "tag": "brand-new-tag",
                        "name": "changed name",
                        "content": "Hello World!",
                        "format": "text",
                        "created_timestamp": "2024-08-14 12:31:35",
                        "updated_timestamp": "2024-08-14 12:31:35",
                        "created_by": null,
                        "updated_by": null,
                        "isLocked": false,
                        "listids": "2,3,4,5",
                        "links": [],
                        "id": "8"
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "personalization": {
                      "type": "object",
                      "properties": {
                        "userid": {
                          "type": "string",
                          "example": "1"
                        },
                        "tag": {
                          "type": "string",
                          "example": "brand-new-tag"
                        },
                        "name": {
                          "type": "string",
                          "example": "changed name"
                        },
                        "content": {
                          "type": "string",
                          "example": "Hello World!"
                        },
                        "format": {
                          "type": "string",
                          "example": "text"
                        },
                        "created_timestamp": {
                          "type": "string",
                          "example": "2024-08-14 12:31:35"
                        },
                        "updated_timestamp": {
                          "type": "string",
                          "example": "2024-08-14 12:31:35"
                        },
                        "created_by": {},
                        "updated_by": {},
                        "listids": {
                          "type": "string",
                          "example": "2,3,4,5"
                        },
                        "links": {
                          "type": "array"
                        },
                        "id": {
                          "type": "string",
                          "example": "8"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"message\": \"No Result found for ActiveCampaign\\\\Hosted\\\\Personalization\\\\Personalization with id 22\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "No Result found for ActiveCampaign\\Hosted\\Personalization\\Personalization with id 22"
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