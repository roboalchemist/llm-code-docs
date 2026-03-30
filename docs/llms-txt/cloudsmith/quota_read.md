# Source: https://help.cloudsmith.io/reference/quota_read.md

# Quota usage for a given namespace.

Quota usage for a given namespace.

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
    "/quota/{owner}/": {
      "get": {
        "operationId": "quota_read",
        "summary": "Quota usage for a given namespace.",
        "description": "Quota usage for a given namespace.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Quota"
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
      "AllocatedLimit": {
        "type": "object",
        "properties": {
          "configured": {
            "title": "Configured",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          },
          "percentage_used": {
            "title": "Percentage used",
            "type": "string",
            "maxLength": 10,
            "minLength": 1
          },
          "plan_limit": {
            "title": "Plan limit",
            "type": "string",
            "maxLength": 32,
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
      "StorageAllocatedLimit": {
        "type": "object",
        "properties": {
          "configured": {
            "title": "Configured",
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
          "percentage_used": {
            "title": "Percentage used",
            "type": "string",
            "maxLength": 10,
            "minLength": 1
          },
          "plan_limit": {
            "title": "Plan limit",
            "type": "string",
            "maxLength": 32,
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
      "UsageLimits": {
        "required": [
          "bandwidth",
          "storage"
        ],
        "type": "object",
        "properties": {
          "bandwidth": {
            "$ref": "#/components/schemas/AllocatedLimit"
          },
          "storage": {
            "$ref": "#/components/schemas/StorageAllocatedLimit"
          }
        }
      },
      "AllocatedLimitRaw": {
        "type": "object",
        "properties": {
          "configured": {
            "title": "Configured",
            "type": "integer"
          },
          "percentage_used": {
            "title": "Percentage used",
            "type": "string",
            "format": "decimal"
          },
          "plan_limit": {
            "title": "Plan limit",
            "type": "integer"
          },
          "used": {
            "title": "Used",
            "type": "integer"
          }
        }
      },
      "StorageAllocatedLimitRaw": {
        "type": "object",
        "properties": {
          "configured": {
            "title": "Configured",
            "type": "integer"
          },
          "peak": {
            "title": "Peak",
            "type": "integer"
          },
          "percentage_used": {
            "title": "Percentage used",
            "type": "string",
            "format": "decimal"
          },
          "plan_limit": {
            "title": "Plan limit",
            "type": "integer"
          },
          "used": {
            "title": "Used",
            "type": "integer"
          }
        }
      },
      "UsageLimitsRaw": {
        "required": [
          "bandwidth",
          "storage"
        ],
        "type": "object",
        "properties": {
          "bandwidth": {
            "$ref": "#/components/schemas/AllocatedLimitRaw"
          },
          "storage": {
            "$ref": "#/components/schemas/StorageAllocatedLimitRaw"
          }
        }
      },
      "UsageFieldset": {
        "required": [
          "display",
          "raw"
        ],
        "type": "object",
        "properties": {
          "display": {
            "$ref": "#/components/schemas/UsageLimits"
          },
          "raw": {
            "$ref": "#/components/schemas/UsageLimitsRaw"
          }
        }
      },
      "Quota": {
        "required": [
          "usage"
        ],
        "type": "object",
        "properties": {
          "usage": {
            "$ref": "#/components/schemas/UsageFieldset"
          }
        }
      }
    }
  }
}
```