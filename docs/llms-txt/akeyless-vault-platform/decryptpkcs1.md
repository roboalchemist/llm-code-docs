# Source: https://docs.akeyless.io/reference/decryptpkcs1.md

# /decrypt-pkcs1

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
    "/decrypt-pkcs1": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "decryptPKCS1",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/decryptPKCS1"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/decryptPKCS1Response"
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
      "decryptPKCS1Response": {
        "description": "decryptPKCS1Response wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/decryptPKCS1Output"
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
      "decryptPKCS1": {
        "type": "object",
        "title": "decryptPKCS1 is a command that decrypts plaintext using RSA and the padding scheme from PKCS#1 v1.5.",
        "required": [
          "key-name",
          "ciphertext"
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
      "decryptPKCS1Output": {
        "type": "object",
        "properties": {
          "plaintext": {
            "type": "string",
            "x-go-name": "Plaintext"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```