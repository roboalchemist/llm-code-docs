# Source: https://docs.akeyless.io/reference/staticcredsauth.md

# /static-creds-auth

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
    "/static-creds-auth": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "staticCredsAuth",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/staticCredsAuth"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/staticCredsAuthResponse"
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
      "staticCredsAuthResponse": {
        "description": "staticCredsAuthResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/staticCredsAuthOutput"
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
      "staticCredsAuth": {
        "description": "staticCredsAuth is a command that creates a temporary access profile using\nthe provided static credentials.",
        "type": "object",
        "properties": {
          "access-id": {
            "description": "Akeyless JWT token",
            "type": "string",
            "x-go-name": "AccessID"
          },
          "admin-email": {
            "description": "Akeyless JWT token",
            "type": "string",
            "x-go-name": "AdminEmail"
          },
          "creds": {
            "description": "Akeyless JWT token",
            "type": "string",
            "x-go-name": "Creds"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "staticCredsAuthOutput": {
        "type": "object",
        "properties": {
          "token": {
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