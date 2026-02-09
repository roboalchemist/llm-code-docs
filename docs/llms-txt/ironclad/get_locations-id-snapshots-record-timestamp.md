# Source: https://clickwrap-developer.ironcladapp.com/reference/get_locations-id-snapshots-record-timestamp.md

# Get a Snapshot record for a timestamp.

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
  "tags": [
    {
      "name": "Snapshots"
    }
  ],
  "paths": {
    "/locations/{id}/snapshots/record/{timestamp}": {
      "get": {
        "tags": [
          "Snapshots"
        ],
        "summary": "Get a Snapshot record for a timestamp.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "timestamp",
            "required": true,
            "description": "ISO 8601 formatted.",
            "example": "2022-04-01T00:00:00+00:00",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/pdf": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            },
            "description": "A Snapshot PDF record."
          },
          "400": {
            "description": "Bad request."
          },
          "401": {
            "description": "The requester is unauthorized."
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