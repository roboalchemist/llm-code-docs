# Source: https://clickwrap-developer.ironcladapp.com/reference/get_activity-record-session-session-id.md

# Retrieve PDF Record by Session ID

Retrieve a PDF of a Clickwrap Request or Signer Record by Session ID

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "contact": {
      "email": "support@ironcladapp.com",
      "name": "Ironclad Support"
    },
    "title": "REST API",
    "version": "v1.1"
  },
  "security": [
    {
      "Bearer": []
    }
  ],
  "servers": [
    {
      "description": "Ironclad Clickwrap REST API",
      "url": "https://api.pactsafe.com/v1.1"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "scheme": "bearer",
        "type": "http"
      }
    }
  },
  "paths": {
    "/activity/record/session:{session_id}": {
      "get": {
        "description": "Retrieve a PDF of a Clickwrap Request or Signer Record by Session ID",
        "summary": "Retrieve PDF Record by Session ID",
        "tags": [
          "Activity"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "session_id",
            "required": true,
            "description": "The unique session ID used when capturing the activity event(s). This route can be used to consolidate the activity of the session into a single PDF file.\n",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "signer_id",
            "required": true,
            "description": "URL encoded Signer ID.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A PDF Record for a Clickwrap Request or Signer Summary",
            "content": {
              "application/pdf": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "400": {
            "description": "Bad request."
          },
          "401": {
            "description": "The requester is unauthorized."
          },
          "403": {
            "description": "Forbidden."
          },
          "404": {
            "description": "Not found."
          }
        }
      }
    }
  }
}
```