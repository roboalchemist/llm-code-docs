# Source: https://docs.akeyless.io/reference/hmac.md

# /hmac

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
    "/hmac": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "hmac",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/hmac"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/hmacResponse"
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
      "hmacResponse": {
        "description": "hmacResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/hmacOutput"
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
      "hmac": {
        "type": "object",
        "title": "hmac is a command that Hash plaintext by using an AES encryption key.",
        "required": [
          "key-name"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the key to use in the encryption process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "hash-function": {
            "description": "Hash function [sha-256,sha-512]",
            "type": "string",
            "default": "sha-256",
            "x-go-name": "HashFunc"
          },
          "input-format": {
            "description": "Select default assumed format for any plaintext input. Currently supported options: [base64]",
            "type": "string",
            "x-go-name": "InputFormat"
          },
          "item-id": {
            "description": "The item id of the key to use in the encryption process",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemId"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-name": {
            "description": "The name of the key to use in the encryption process",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "plaintext": {
            "description": "Data to perform hmac on",
            "type": "string",
            "x-go-name": "Plaintext"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "hmacOutput": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```