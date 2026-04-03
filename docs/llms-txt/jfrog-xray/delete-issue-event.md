# Source: https://docs.jfrog.com/security/reference/delete-issue-event.md

# Delete Issue Event

Deletes a custom issue

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Xray REST APIs",
    "description": "Combined JFrog Xray REST API specification (all endpoints).",
    "version": "3.140"
  },
  "servers": [
    {
      "url": "https://jf.example.com/xray",
      "description": "JFrog Platform (Xray)"
    }
  ],
  "security": [
    {
      "basicAuth": []
    }
  ],
  "paths": {
    "/api/v1/events/{id}": {
      "delete": {
        "operationId": "delete-issue-event",
        "summary": "Delete Issue Event",
        "description": "Deletes a custom issue",
        "tags": [
          "Custom Issues V1"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Resource identifier",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "info": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "info"
                  ]
                },
                "example": {
                  "info": "Vulnerability with id <id> has been successfully deleted"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication using username/password or API key"
      }
    }
  },
  "tags": [
    {
      "name": "Custom Issues V1",
      "description": "APIs from Custom Issues V1"
    }
  ]
}
```