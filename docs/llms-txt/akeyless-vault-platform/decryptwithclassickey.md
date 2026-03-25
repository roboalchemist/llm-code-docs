# Source: https://docs.akeyless.io/reference/decryptwithclassickey.md

# /decrypt-with-classic-key

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
    "/decrypt-with-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "decryptWithClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/decryptWithClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/decryptWithClassicKeyResponse"
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
      "decryptWithClassicKeyResponse": {
        "description": "decryptWithClassicKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/decryptWithClassicKeyOutput"
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
      "decryptWithClassicKey": {
        "type": "object",
        "title": "decryptWithClassicKey is a command that decryptWithClassicKeys ciphertext into plaintext by using a classic key.",
        "required": [
          "display-id",
          "version",
          "ciphertext"
        ],
        "properties": {
          "ciphertext": {
            "description": "Ciphertext to be decrypted in base64 encoded format",
            "type": "string",
            "x-go-name": "Ciphertext"
          },
          "display-id": {
            "description": "The name of the key to use in the encryption process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "ignore-cache": {
            "description": "Retrieve the Secret value without checking the Gateway's cache [true/false]. This flag is only relevant when using the RestAPI",
            "type": "string",
            "default": "false",
            "x-go-name": "IgnoreCache"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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
            "description": "classic key version",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "decryptWithClassicKeyOutput": {
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