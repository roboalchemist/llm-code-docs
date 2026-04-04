# Source: https://clickwrap-developer.ironcladapp.com/reference/get_activity-activity-id-record.md

# Retrieve PDF Record by ID

Retrieve a PDF Record of a Clickwrap Action by Action ID

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
    "/activity/{activity_id}/record": {
      "get": {
        "description": "Retrieve a PDF Record of a Clickwrap Action by Action ID",
        "summary": "Retrieve PDF Record by ID",
        "tags": [
          "Activity"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "activity_id",
            "description": "The ID of the Activity.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "filename",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A PDF Record for a Clickwrap Action",
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