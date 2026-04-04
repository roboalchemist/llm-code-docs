# Source: https://virustotal.readme.io/reference/delete-user-id.md

# Delete a user

This request deletes a given user. A user account can only be deleted by its owner, a 403 error is returned otherwise.

An additional `x-user-password` header is required, which is used as confirmation.

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
    "/users/{id}": {
      "delete": {
        "summary": "Delete a user",
        "description": "",
        "operationId": "delete-user-id",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "User ID or API key",
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
          },
          {
            "name": "x-user-password",
            "in": "header",
            "description": "User password, needed as confirmation.",
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
          "403": {
            "description": "403",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"ForbiddenError\",\n    \"message\": \"You are not authorized to perform the requested operation\"\n  }\n}"
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
                          "example": "ForbiddenError"
                        },
                        "message": {
                          "type": "string",
                          "example": "You are not authorized to perform the requested operation"
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
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```