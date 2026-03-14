# Source: https://virustotal.readme.io/reference/collections-comments-create.md

# Add a comment to a collection

With this endpoint you can post a comment for a given collection. The body for the `POST` request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments.

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

```json Example response
{
  "data": {
    "type": "comment",
    "id": "<comment's ID>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/comments/<comment's ID>"
    },
    "attributes": {
      "date": 1521725475,
      "tags": ["ipsum"],
      "html": "Lorem #ipsum dolor sit ...",
      "text": "Lorem #ipsum dolor sit ...",
      "votes": {
        "abuse": 0,
        "negative": 0,
        "positive": 0
      }
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
    "/collections/{id}/comments": {
      "post": {
        "summary": "Add a comment to a collection",
        "description": "",
        "operationId": "collections-comments-create",
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
            "description": "Collection's ID",
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
                    "description": "A comment object",
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