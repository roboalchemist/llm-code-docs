# Source: https://docs.akeyless.io/reference/decrypt.md

# /decrypt

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
    "/decrypt": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "decrypt",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/decrypt"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/decryptResponse"
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
      "decryptResponse": {
        "description": "decryptResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/decryptOutput"
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
      "decrypt": {
        "description": "decrypt is a command that decrypts ciphertext into plaintext by using an AES\nkey.",
        "type": "object",
        "required": [
          "key-name"
        ],
        "properties": {
          "ciphertext": {
            "description": "Ciphertext to be decrypted in base64 encoded format",
            "type": "string",
            "x-go-name": "Ciphertext"
          },
          "display-id": {
            "description": "The display id of the key to use in the decryption process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "encryption-context": {
            "description": "The encryption context. If this was specified in the encrypt command, it\nmust be specified here or the decryption operation will fail",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "EncContext"
          },
          "item-id": {
            "description": "The item id of the key to use in the decryption process",
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
            "description": "The name of the key to use in the decryption process",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "output-format": {
            "description": "If specified, the output will be formatted accordingly. options: [base64]",
            "type": "string",
            "x-go-name": "OutputFormat"
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
      "decryptOutput": {
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