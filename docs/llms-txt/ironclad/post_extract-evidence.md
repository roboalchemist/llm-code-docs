# Source: https://clickwrap-developer.ironcladapp.com/reference/post_extract-evidence.md

# Create an Export

Creates an export job.

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
      "post": {
        "description": "Creates an export job.",
        "summary": "Create an Export",
        "tags": [
          "Extraction"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "start_date": {
                    "type": "string",
                    "format": "date-time"
                  },
                  "end_date": {
                    "type": "string",
                    "format": "date-time",
                    "description": "If not provided, it defaults to now. Cannot be earlier than \"start_date\". Selected date range cannot exceed maximum allowed days for the site."
                  },
                  "sort": {
                    "type": "string"
                  },
                  "filter": {
                    "type": "object"
                  },
                  "select": {
                    "type": "object",
                    "properties": {
                      "standard": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "connection": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "custom": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "render": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    }
                  },
                  "standard_all": {
                    "type": "boolean",
                    "description": "If provided as true, all standard fields are included in the export file. This will override the \"select.standard\" array."
                  },
                  "connection_all": {
                    "type": "boolean",
                    "description": "If provided as true, all connection fields are included in the export file. This will override the \"select.connection\" array."
                  },
                  "custom_all": {
                    "type": "boolean",
                    "description": "If provided as true, all custom fields are included in the export file. This will override the \"select.custom\" array."
                  },
                  "export_types": {
                    "type": "array",
                    "description": "Array can include: `clickwrap_activities`, `clickwrap_activities_as_pdfs`",
                    "items": {
                      "type": "string"
                    }
                  }
                },
                "type": "object",
                "required": [
                  "start_date"
                ],
                "title": "EvidenceExportRequest"
              },
              "example": {
                "start_date": "2022-10-06T00:00:00.000Z",
                "end_date": "2022-10-06T00:00:00.000Z",
                "sort": "-created_time",
                "select": {
                  "standard": [
                    "uuid",
                    "created_time",
                    "batch",
                    "session",
                    "event_time",
                    "contract",
                    "version"
                  ]
                },
                "filter": {
                  "contract": {
                    "_id": 1
                  },
                  "and": [
                    {
                      "version_number": {
                        "$gt": 1
                      }
                    },
                    {
                      "version_number": {
                        "$lte": 3
                      }
                    }
                  ]
                },
                "connection_all": true,
                "custom_all": true,
                "export_types": [
                  "clickwrap_activities",
                  "clickwrap_activities_as_pdfs"
                ]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created.",
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
                },
                "example": {
                  "status": "pending",
                  "source": "api",
                  "retry_count": 0,
                  "active": true,
                  "job_name": "ExtractEvidenceCSV",
                  "message": "Export job is currently pending.",
                  "created_time": "2023-01-06T17:00:01.901Z",
                  "updated_time": "2023-01-06T17:00:01.901Z",
                  "id": "000000000000000000000000"
                }
              }
            }
          },
          "400": {
            "description": "Bad request."
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