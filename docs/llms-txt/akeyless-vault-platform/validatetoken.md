# Source: https://docs.akeyless.io/reference/validatetoken.md

# /validate-token

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/validate-token": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "validateToken",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/validateToken"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/validateTokenResponse"
          },
          "401": {
            "$ref": "#/components/responses/errorResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "validateTokenResponse": {
        "description": "validateTokenResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ValidateTokenOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "ValidateTokenOutput": {
        "type": "object",
        "properties": {
          "expiration": {
            "type": "string",
            "x-go-name": "ExpirationTime"
          },
          "is_valid": {
            "type": "boolean",
            "x-go-name": "IsValid"
          },
          "last_rotate": {
            "type": "string",
            "x-go-name": "LastRotate"
          },
          "reason": {
            "type": "string",
            "x-go-name": "Reason"
          },
          "ttl": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "TTL"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "validateToken": {
        "description": "validate-token is a command that validaties token",
        "type": "object",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "token": {
            "description": "Token",
            "type": "string",
            "x-go-name": "Token"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```