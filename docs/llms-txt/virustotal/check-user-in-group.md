# Source: https://virustotal.readme.io/reference/check-user-in-group.md

# Check if a user is a group member

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
    "/groups/{id}/relationships/users/{user_id}": {
      "get": {
        "summary": "Check if a user is a group member",
        "description": "",
        "operationId": "check-user-in-group",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Group ID.",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "user_id",
            "in": "path",
            "description": "User to check.",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key.",
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
                    "value": "{\n  \"data\": true\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "boolean",
                      "example": true,
                      "default": true
                    }
                  }
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