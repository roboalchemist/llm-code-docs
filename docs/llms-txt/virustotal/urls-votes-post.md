# Source: https://virustotal.readme.io/reference/urls-votes-post.md

# Add a vote on a URL

> 📘
>
> See [URL identifiers](https://virustotal.readme.io/reference/url#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

With this endpoint you can post a vote for a given URL. The body for the `POST` request must be the JSON representation of a vote object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new votes.

The verdict attribute must have be either `harmless` or `malicious`.

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

Returns a [Vote](https://virustotal.readme.io/reference/vote-object) object.

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
    "/urls/{id}/votes": {
      "post": {
        "summary": "Add a vote on a URL",
        "description": "",
        "operationId": "urls-votes-post",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "URL identifier",
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
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "Vote object",
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
                    "value": "{\n  \"error\": {\n    \"code\": \"AlreadyExistsError\",\n    \"message\": \"User \\\"username\\\" already voted \\\"malicious\\\" for this url\"\n  }\n}"
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
                          "example": "User \"username\" already voted \"malicious\" for this url"
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