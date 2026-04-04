# Source: https://clickwrap-developer.ironcladapp.com/reference/delete-a-signer-1.md

# Delete a Signer by Signer ID

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
    "/signers/id:{signer_id}": {
      "delete": {
        "summary": "Delete a Signer by Signer ID",
        "description": "",
        "operationId": "delete-a-signer",
        "tags": [
          "Signers"
        ],
        "parameters": [
          {
            "name": "signer_id",
            "in": "path",
            "description": "The Signer ID, URL encoded.",
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
                    "uuid": {
                      "type": "string",
                      "example": "65c2a53d0293acd1651a5a5c"
                    },
                    "signer_id": {
                      "type": "string",
                      "example": "eric@pactsafe.com"
                    }
                  }
                }
              }
            }
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