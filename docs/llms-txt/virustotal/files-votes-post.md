# Source: https://virustotal.readme.io/reference/files-votes-post.md

# Add a vote on a file

With this endpoint you can post a vote for a given file. The body for the `POST` request must be the JSON representation of a vote object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new votes.

The verdict attribute must have be either `harmless` or `malicious`.

Returns a [Vote](https://virustotal.readme.io/reference/vote-object) object.

```json
{
  "data": {
    "type": "vote",
    "attributes": {
    	"verdict": "harmless"
    }
  }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/files/{id}/votes": {
      "post": {
        "summary": "Add a vote on a file",
        "description": "",
        "operationId": "files-votes-post",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A vote object",
                    "default": "{\"type\": \"vote\", \"attributes\": {\"verdict\": \"malicious\"}}",
                    "format": "json"
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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
          },
          "409": {
            "description": "409",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"AlreadyExistsError\",\n    \"message\": \"User \\\"username\\\" already voted \\\"malicious\\\" for this file\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "code": {
                          "type": "string",
                          "example": "AlreadyExistsError"
                        },
                        "message": {
                          "type": "string",
                          "example": "User \"username\" already voted \"malicious\" for this file"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```