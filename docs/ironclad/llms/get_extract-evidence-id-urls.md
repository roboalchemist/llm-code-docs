# Source: https://clickwrap-developer.ironcladapp.com/reference/get_extract-evidence-id-urls.md

# Retrieve Export Job URLs

Retrieve the presigned urls of an export job if it is complete

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
    "/extract/evidence/{id}/urls": {
      "get": {
        "description": "Retrieve the presigned urls of an export job if it is complete",
        "summary": "Retrieve Export Job URLs",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "tags": [
          "Extraction"
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "presignedUrls": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "error": {
                      "type": "string",
                      "description": "The potential error message"
                    }
                  }
                },
                "examples": {
                  "Success": {
                    "value": {
                      "clickwrap_activities": [
                        "https://storage.googleapis.com/**"
                      ]
                    }
                  },
                  "Failure": {
                    "value": {
                      "error": "Fail to fetch to presigned url."
                    }
                  }
                }
              }
            },
            "description": "An array of presigned urls."
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