# Source: https://docs.akeyless.io/reference/verifygpg.md

# /verify-gpg

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
    "/verify-gpg": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "verifyGPG",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/verifyGPG"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/verifyGPGResponse"
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
      "verifyGPGResponse": {
        "description": "verifyGPGResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/verifyGPGOutput"
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
      "verifyGPG": {
        "type": "object",
        "title": "verifyGPG is a command that verifies a GPG signature based on RSA key.",
        "required": [
          "key-name",
          "signature"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the key to use in the encryption process",
            "type": "string",
            "x-go-name": "DisplayId"
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
          "passphrase": {
            "description": "Passphrase that was used to generate the key",
            "type": "string",
            "x-go-name": "Passphrase"
          },
          "signature": {
            "description": "The signature to be verified in base64 format",
            "type": "string",
            "x-go-name": "Signature"
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
      "verifyGPGOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```