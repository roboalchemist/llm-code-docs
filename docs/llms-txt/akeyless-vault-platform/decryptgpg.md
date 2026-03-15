# Source: https://docs.akeyless.io/reference/decryptgpg.md

# /decrypt-gpg

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
    "/decrypt-gpg": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "decryptGPG",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/decryptGPG"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/decryptGPGResponse"
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
      "decryptGPGResponse": {
        "description": "decryptGPGResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/decryptGPGOutput"
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
      "decryptGPG": {
        "type": "object",
        "title": "decryptGPG is a command that decrypts GPG cipher text based on RSA key.",
        "required": [
          "key-name",
          "ciphertext"
        ],
        "properties": {
          "ciphertext": {
            "description": "Ciphertext to be decrypted",
            "type": "string",
            "x-go-name": "Ciphertext"
          },
          "display-id": {
            "description": "The display id of the key to use in the decryption process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "input-format": {
            "description": "Select default assumed format for the ciphertext. Currently supported options: [base64,raw]",
            "type": "string",
            "default": "base64",
            "x-go-name": "InputFormat"
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
          "passphrase": {
            "description": "Passphrase that was used to generate the key",
            "type": "string",
            "x-go-name": "Passphrase"
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
      "decryptGPGOutput": {
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