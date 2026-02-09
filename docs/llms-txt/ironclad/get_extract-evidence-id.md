# Source: https://clickwrap-developer.ironcladapp.com/reference/get_extract-evidence-id.md

# Get an Export Job by ID

Get an export job by id.

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
    "/extract/evidence/{id}": {
      "get": {
        "description": "Get an export job by id.",
        "summary": "Get an Export Job by ID",
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
                  "properties": {
                    "job_name": {
                      "type": "string"
                    },
                    "status": {
                      "enum": [
                        "pending",
                        "scheduled",
                        "started",
                        "success",
                        "failed"
                      ],
                      "title": "Status",
                      "type": "string"
                    },
                    "source": {
                      "enum": [
                        "manual",
                        "cron",
                        "api"
                      ],
                      "title": "Source",
                      "type": "string"
                    },
                    "account": {
                      "readOnly": true,
                      "type": "integer"
                    },
                    "site": {
                      "readOnly": true,
                      "type": "integer"
                    },
                    "created_by": {
                      "readOnly": true,
                      "type": "integer"
                    },
                    "active": {
                      "type": "boolean"
                    },
                    "message": {
                      "type": "string"
                    },
                    "created_time": {
                      "type": "string",
                      "description": "ISO 8601 formatted."
                    },
                    "updated_time": {
                      "type": "string",
                      "description": "ISO 8601 formatted."
                    },
                    "data": {
                      "type": "object"
                    },
                    "retry_count": {
                      "type": "integer"
                    }
                  },
                  "title": "ScheduledJobResponse",
                  "type": "object"
                }
              }
            },
            "description": "A scheduled job object."
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