# Source: https://help.cloudsmith.io/reference/status_check_basic.md

# Endpoint to check basic API connectivity.

Endpoint to check basic API connectivity.

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
    "/status/check/basic/": {
      "get": {
        "operationId": "status_check_basic",
        "summary": "Endpoint to check basic API connectivity.",
        "description": "Endpoint to check basic API connectivity.",
        "responses": {
          "200": {
            "description": "Status check was successful",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StatusBasic"
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
          "status"
        ],
        "security": []
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
      "StatusBasic": {
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "The message describing the state of the API.",
            "type": "string",
            "readOnly": true,
            "default": "Cloudsmith API is operational.",
            "minLength": 1
          },
          "version": {
            "title": "Version",
            "description": "The current version for the Cloudsmith service.",
            "type": "string",
            "readOnly": true,
            "default": "1.0",
            "minLength": 1
          }
        }
      }
    }
  }
}
```