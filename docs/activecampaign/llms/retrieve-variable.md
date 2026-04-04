# Source: https://developers.activecampaign.com/reference/retrieve-variable.md

# Retrieve a Variable

Retrieve an individual personalization variable

```json GET /personalizations/{id} (Example RESPONSE)
{
    "personalization": {
        "name": "brand new name",
        "tag": "brand-new-tag",
        "format": "text",
        "content": "Hello World!",
        "listIds": "2,3,5,4",
        "listNames": "Another List,League Players,real,Test Segmentation",
	      "listsCount": "4",
				"isLocked": false,
        "links": [],
        "id": "8"
    }
}
```

```json 404 - Not Found
{
    "message": "No Result found for Personalization with id 15"
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
      "get": {
        "summary": "Retrieve a Variable",
        "description": "Retrieve an individual personalization variable",
        "operationId": "retrieve-variable",
        "parameters": [
          {
            "name": "variableID",
            "in": "path",
            "description": "ID (int) of variable",
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
                    "value": {
                      "personalization": {
                        "name": "brand new name",
                        "tag": "brand-new-tag",
                        "format": "text",
                        "content": "Hello World!",
                        "listIds": "2,3,5,4",
                        "listNames": "Another List,League Players,real,Test Segmentation",
                        "listsCount": "4",
                        "isLocked": false,
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
                        "name": {
                          "type": "string",
                          "example": "brand new name"
                        },
                        "tag": {
                          "type": "string",
                          "example": "brand-new-tag"
                        },
                        "format": {
                          "type": "string",
                          "example": "text"
                        },
                        "content": {
                          "type": "string",
                          "example": "Hello World!"
                        },
                        "listIds": {
                          "type": "string",
                          "example": "2,3,5,4"
                        },
                        "listNames": {
                          "type": "string",
                          "example": "Another List,League Players,real,Test Segmentation"
                        },
                        "listsCount": {
                          "type": "string",
                          "example": "4"
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
                    "value": "{\n    \"message\": \"No Result found for Personalization with id 22\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "No Result found for Personalization with id 22"
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