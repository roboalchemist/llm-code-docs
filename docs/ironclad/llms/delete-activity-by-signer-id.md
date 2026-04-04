# Source: https://clickwrap-developer.ironcladapp.com/reference/delete-activity-by-signer-id.md

# Delete activity performed by a signer

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
    "/signers/id:{signer_id}/activity": {
      "delete": {
        "summary": "Delete activity performed by a signer",
        "description": "",
        "operationId": "delete-activity-by-signer-id",
        "tags": [
          "Signers"
        ],
        "parameters": [
          {
            "name": "signer_id",
            "in": "path",
            "description": "The signer ID, URL encoded.",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string",
                          "example": "eric@pactsafe.com"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden."
          },
          "404": {
            "description": "Not found."
          }
        },
        "deprecated": false
      }
    }
  }
}
```