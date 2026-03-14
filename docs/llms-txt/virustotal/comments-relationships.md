# Source: https://virustotal.readme.io/reference/comments-relationships.md

# Get objects related to a comment

Comment objects are related to other objects in the VirusTotal dataset. As mentioned in the [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to the relationships endpoint.

All available relationships are documented in the [Comment](https://virustotal.readme.io/reference/comment-object) API object page.

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
    "/comments/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to a comment",
        "description": "",
        "operationId": "comments-relationships",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Comment identifier",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/comments#relationships))",
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