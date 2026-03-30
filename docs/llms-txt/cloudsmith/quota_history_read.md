# Source: https://help.cloudsmith.io/reference/quota_history_read.md

# Quota history for a given namespace.

Quota history for a given namespace.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/quota/history/{owner}/": {
      "get": {
        "operationId": "quota_history_read",
        "summary": "Quota history for a given namespace.",
        "description": "Quota history for a given namespace.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/QuotaHistory"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "quota"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "Usage": {
        "type": "object",
        "properties": {
          "limit": {
            "title": "Limit",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          },
          "percentage": {
            "title": "Percentage",
            "type": "string",
            "maxLength": 10,
            "minLength": 1
          },
          "used": {
            "title": "Used",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          }
        }
      },
      "StorageUsage": {
        "type": "object",
        "properties": {
          "limit": {
            "title": "Limit",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          },
          "peak": {
            "title": "Peak",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          },
          "percentage": {
            "title": "Percentage",
            "type": "string",
            "maxLength": 10,
            "minLength": 1
          },
          "used": {
            "title": "Used",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          }
        }
      },
      "HistoryFieldset": {
        "required": [
          "downloaded",
          "storage_used",
          "uploaded"
        ],
        "type": "object",
        "properties": {
          "downloaded": {
            "$ref": "#/components/schemas/Usage"
          },
          "storage_used": {
            "$ref": "#/components/schemas/StorageUsage"
          },
          "uploaded": {
            "$ref": "#/components/schemas/Usage"
          }
        }
      },
      "UsageRaw": {
        "type": "object",
        "properties": {
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "percentage": {
            "title": "Percentage",
            "type": "string",
            "format": "decimal"
          },
          "used": {
            "title": "Used",
            "type": "integer"
          }
        }
      },
      "StorageUsageRaw": {
        "type": "object",
        "properties": {
          "limit": {
            "title": "Limit",
            "type": "integer"
          },
          "peak": {
            "title": "Peak",
            "type": "integer"
          },
          "percentage": {
            "title": "Percentage",
            "type": "string",
            "format": "decimal"
          },
          "used": {
            "title": "Used",
            "type": "integer"
          }
        }
      },
      "HistoryFieldsetRaw": {
        "required": [
          "downloaded",
          "storage_used",
          "uploaded"
        ],
        "type": "object",
        "properties": {
          "downloaded": {
            "$ref": "#/components/schemas/UsageRaw"
          },
          "storage_used": {
            "$ref": "#/components/schemas/StorageUsageRaw"
          },
          "uploaded": {
            "$ref": "#/components/schemas/UsageRaw"
          }
        }
      },
      "History": {
        "required": [
          "display",
          "end",
          "plan",
          "raw",
          "start"
        ],
        "type": "object",
        "properties": {
          "days": {
            "title": "Days",
            "type": "integer",
            "default": 0
          },
          "display": {
            "$ref": "#/components/schemas/HistoryFieldset"
          },
          "end": {
            "title": "End",
            "type": "string",
            "format": "date-time"
          },
          "plan": {
            "title": "Plan",
            "type": "string",
            "maxLength": 64,
            "minLength": 1
          },
          "raw": {
            "$ref": "#/components/schemas/HistoryFieldsetRaw"
          },
          "start": {
            "title": "Start",
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "QuotaHistory": {
        "required": [
          "history"
        ],
        "type": "object",
        "properties": {
          "history": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/History"
            }
          }
        }
      }
    }
  }
}
```