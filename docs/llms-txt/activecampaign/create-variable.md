# Source: https://developers.activecampaign.com/reference/create-variable.md

# Create a Variable

Create a personalization variable

```json POST /personalizations (Example REQUEST)
{
    "personalization": {
        "tag": "brand new tag",
        "name": "brand new name",
        "format": "text",
        "content": "Hello World!",
        "listids": "2,3,4,5"
    }
}
```

```json POST /personalizations (Example RESPONSE)
{
    "personalization": {
        "tag": "brand-new-tag",
        "name": "brand new name",
        "format": "text",
        "content": "Hello World!",
        "listids": "2,3,4,5",
        "userid": "1",
        "links": [],
        "id": "8"
    }
}
```

> 🚧 Tags with spaces will have `-` added between words.
>
> Creating a variable with the `tag` of `"brand new tag"` will result in a variable being created with the tag `"brand-new-tag"`

> 🚧 Creating variables that have a pre-existing tag will have `_X` appended to the tag name.
>
> If a variable is created with the `tag` set to `"tag-name-example"` but another variable already exists with that same tag, the new variable will still be created, but will be created with and underscore and the next available number appended to the end of the tag, ie: `"tag-name-example_1"`

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
    "/personalizations": {
      "post": {
        "summary": "Create a Variable",
        "description": "Create a personalization variable",
        "operationId": "create-variable",
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
                        "tag": "brand-new-tag",
                        "name": "brand new name",
                        "format": "text",
                        "content": "Hello World!",
                        "listids": "2,3,4,5",
                        "userid": "1",
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
                        "tag": {
                          "type": "string",
                          "example": "brand-new-tag"
                        },
                        "name": {
                          "type": "string",
                          "example": "brand new name"
                        },
                        "format": {
                          "type": "string",
                          "example": "text"
                        },
                        "content": {
                          "type": "string",
                          "example": "Hello World!"
                        },
                        "listids": {
                          "type": "string",
                          "example": "2,3,4,5"
                        },
                        "userid": {
                          "type": "string",
                          "example": "1"
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