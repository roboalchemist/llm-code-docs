# Source: https://clickwrap-developer.ironcladapp.com/reference/post_locations-id-snapshots-snapshotid-archive.md

# Archives a Snapshot.

Requires **manage** permissions for Snapshots.

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
    "/locations/{id}/snapshots/{snapshotId}/archive": {
      "post": {
        "tags": [
          "Snapshots"
        ],
        "summary": "Archives a Snapshot.",
        "description": "Requires **manage** permissions for Snapshots.",
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
            "name": "snapshotId",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "archived_reason": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success.",
            "content": {
              "application/json": {
                "schema": {
                  "properties": {
                    "data": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        }
                      }
                    }
                  },
                  "type": "object"
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