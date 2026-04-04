# Source: https://clickwrap-developer.ironcladapp.com/reference/get_extract-evidence.md

# List all Export Jobs

Get all export jobs.

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
    "/extract/evidence": {
      "get": {
        "description": "Get all export jobs.",
        "summary": "List all Export Jobs",
        "tags": [
          "Extraction"
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "allOf": [
                    {
                      "properties": {
                        "count": {
                          "type": "integer"
                        },
                        "has_more": {
                          "type": "boolean"
                        },
                        "page": {
                          "type": "integer"
                        },
                        "per_page": {
                          "type": "integer"
                        },
                        "total_count": {
                          "type": "integer"
                        }
                      },
                      "title": "Collection",
                      "type": "object"
                    },
                    {
                      "properties": {
                        "data": {
                          "type": "array",
                          "items": {
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
                      }
                    }
                  ]
                }
              }
            },
            "description": "An array of scheduled export jobs."
          },
          "400": {
            "description": "Bad request."
          },
          "401": {
            "description": "The requester is unauthorized."
          },
          "403": {
            "description": "Forbidden."
          }
        }
      }
    }
  }
}
```