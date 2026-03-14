# Source: https://virustotal.readme.io/reference/domains-comments-post.md

# Add a comment to a domain

With this endpoint you can post a comment for a given domain. The body for the POST request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments.

Any word starting with # in your comment's text will be considered a tag, and added to the comment's tag attribute.

```json Example request
{
  "data": {
    "type": "comment",
    "attributes": {
    	"text": "Lorem #ipsum dolor sit ..."
    }
  }
}
```

Returns a [Comment](https://virustotal.readme.io/reference/comments) object.

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
    "/domains/{domain}/comments": {
      "post": {
        "summary": "Add a comment to a domain",
        "description": "",
        "operationId": "domains-comments-post",
        "parameters": [
          {
            "name": "domain",
            "in": "path",
            "description": "Domain name",
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
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A comment object",
                    "default": "{\"type\": \"comment\", \"attributes\": {\"text\": \"Lorem ipsum dolor sit ...\"}}",
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