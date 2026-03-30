# Source: https://virustotal.readme.io/reference/domain-votes-post.md

# Add a vote to a domain

With this endpoint you can post a vote for a given file. The body for the POST request must be the JSON representation of a [vote object](https://virustotal.readme.io/reference/vote-object). Note however that you don't need to provide an ID for the object, as they are automatically generated for new votes.

The verdict attribute must have be either harmless or malicious.

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

Returns a [votes](https://virustotal.readme.io/reference/vote-object) object.

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
    "/domains/{domain}/votes": {
      "post": {
        "summary": "Add a vote to a domain",
        "description": "",
        "operationId": "domain-votes-post",
        "parameters": [
          {
            "name": "domain",
            "in": "path",
            "description": "hostname or domain name",
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
                    "description": "Vote object",
                    "default": "{\"type\": \"vote\", \"attributes\": {\"verdict\": \"harmless\"}}",
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
                    "value": "{\n  \"error\": {\n    \"code\": \"AlreadyExistsError\",\n    \"message\": \"User \\\"username\\\" already voted \\\"harmless\\\" for this domain\"\n  }\n}"
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
                          "example": "User \"username\" already voted \"harmless\" for this domain"
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