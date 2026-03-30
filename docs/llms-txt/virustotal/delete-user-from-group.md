# Source: https://virustotal.readme.io/reference/delete-user-from-group.md

# Remove a user from a group

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
      "delete": {
        "summary": "Remove a user from a group",
        "description": "",
        "operationId": "delete-user-from-group",
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
            "description": "User to remove.",
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
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": ""
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