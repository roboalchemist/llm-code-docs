# Source: https://virustotal.readme.io/reference/users-relationships.md

# Get objects related to a user

Retrieve related objects IDs to an User

Users are related to other objects in our dataset. As mentioned in the [Relationships](https://virustotal.readme.io/reference/relationships) section, those related objects can be retrieved by sending `GET` requests to this API endpoint.

Some relationships are only accessible to their account's owners and their group's admins.

The supported relationships are documented in the [User](https://virustotal.readme.io/reference/user-object#relationships) API object page.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/users/{id}/{relationship}": {
      "get": {
        "summary": "Get objects related to a user",
        "description": "Retrieve related objects IDs to an User",
        "operationId": "users-relationships",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Username or API key",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://virustotal.readme.io/reference/user-object#relationships))",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of related objects to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
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
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```