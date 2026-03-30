# Source: https://docs.akeyless.io/reference/uidrotatetoken.md

# /uid-rotate-token

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
    "/uid-rotate-token": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uidRotateToken",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uidRotateToken"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uidRotateTokenResponse"
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
      "uidRotateTokenResponse": {
        "description": "uidRotateTokenResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/uidRotateTokenOutput"
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
      "uidRotateToken": {
        "description": "uidRotateToken is a command that rotates an Akeyless Universal Identity\ntoken.",
        "type": "object",
        "properties": {
          "fork": {
            "description": "Create a new child token with default parameters",
            "type": "boolean",
            "x-go-name": "Fork"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "send-manual-ack-token": {
            "description": "The new rotated token to send manual ack for (with\nuid-token=the-orig-token)",
            "type": "string",
            "x-go-name": "SendManualAckToken"
          },
          "uid-token": {
            "description": "The Universal identity token",
            "type": "string",
            "x-go-name": "UIDToken"
          },
          "with-manual-ack": {
            "description": "Disable automatic ack",
            "type": "boolean",
            "x-go-name": "WithManualAck"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "uidRotateTokenOutput": {
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