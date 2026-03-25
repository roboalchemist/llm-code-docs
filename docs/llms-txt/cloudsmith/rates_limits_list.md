# Source: https://help.cloudsmith.io/reference/rates_limits_list.md

# Endpoint to check rate limits for current user.

Endpoint to check rate limits for current user.

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
    "/rates/limits/": {
      "get": {
        "operationId": "rates_limits_list",
        "summary": "Endpoint to check rate limits for current user.",
        "description": "Endpoint to check rate limits for current user.",
        "responses": {
          "200": {
            "description": "Rate check was successful",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ResourcesRateCheck"
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
          "rates"
        ]
      },
      "parameters": []
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
      "RateCheck": {
        "type": "object",
        "properties": {
          "interval": {
            "title": "Interval",
            "description": "The time in seconds that you are suggested to wait until the next request in order to avoid consuming too much within the rate limit window.",
            "type": "number",
            "readOnly": true
          },
          "limit": {
            "title": "Limit",
            "description": "The maximum number of requests that you are permitted to send per hour",
            "type": "integer",
            "readOnly": true
          },
          "remaining": {
            "title": "Remaining",
            "description": "The number of requests that are remaining in the current rate limit window",
            "type": "integer",
            "readOnly": true
          },
          "reset": {
            "title": "Reset",
            "description": "The UTC epoch timestamp at which the current rate limit window will reset",
            "type": "integer",
            "readOnly": true
          },
          "reset_iso_8601": {
            "title": "Reset iso 8601",
            "description": "The ISO 8601 datetime at which the current rate limit window will reset",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "throttled": {
            "title": "Throttled",
            "description": "If true, throttling is currently being enforced.",
            "type": "boolean",
            "readOnly": true
          }
        }
      },
      "ResourcesRateCheck": {
        "type": "object",
        "properties": {
          "resources": {
            "title": "Resources",
            "description": "Rate limit values per resource",
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/RateCheck"
            },
            "readOnly": true
          }
        }
      }
    }
  }
}
```