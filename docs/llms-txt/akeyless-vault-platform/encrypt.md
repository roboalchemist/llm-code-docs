# Source: https://docs.akeyless.io/reference/encrypt.md

# /encrypt

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
    "/encrypt": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "encrypt",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/encrypt"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/encryptResponse"
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
      "encryptResponse": {
        "description": "encryptResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/encryptOutput"
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
      "encrypt": {
        "type": "object",
        "title": "encrypt is a command that encrypts plaintext into ciphertext by using an AES key.",
        "required": [
          "key-name"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the key to use in the encryption process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "encryption-context": {
            "description": "name-value pair that specifies the encryption context to be used for\nauthenticated encryption. If used here, the same value must be supplied\nto the decrypt command or decryption will fail",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "EncContext"
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
          },
          "version": {
            "description": "key version (relevant only for classic key)",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "encryptOutput": {
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