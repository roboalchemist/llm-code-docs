# Source: https://docs.akeyless.io/reference/encryptgpg.md

# /encrypt-gpg

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
    "/encrypt-gpg": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "encryptGPG",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/encryptGPG"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/encryptGPGResponse"
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
      "encryptGPGResponse": {
        "description": "encryptGPGResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/encryptGPGOutput"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
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
      "encryptGPG": {
        "type": "object",
        "title": "encryptGPG is a command that encrypts plaintext using GPG based on RSA key.",
        "required": [
          "key-name",
          "plaintext"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the key to use in the encryption process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "input-format": {
            "description": "If specified, the plaintext input is assumed to be formatted accordingly. Current supported options: [base64]",
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
            "description": "Data to be encrypted",
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
      "encryptGPGOutput": {
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