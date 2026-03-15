# Source: https://docs.akeyless.io/reference/verifyecdsa.md

# /verify-ecdsa

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
    "/verify-ecdsa": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "verifyEcDsa",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/verifyEcDsa"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/verifyEcDsaResponse"
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
      "verifyEcDsaResponse": {
        "description": "verifyEcDsaResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/verifyEcDsaOutput"
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
      "verifyEcDsa": {
        "description": "verifyEcDsa is a command that verifies an ECDSA signature\nusing a sha hash algorithm matching the key size",
        "type": "object",
        "required": [
          "message",
          "signature"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the EC key to use for the verification process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "item-id": {
            "description": "The item id of the EC key to use for the verification process",
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
            "description": "The name of the EC key to use for the verification process",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "message": {
            "description": "The message to be verified in a base64 format",
            "type": "string",
            "x-go-name": "Message"
          },
          "prehashed": {
            "description": "Markes that the message is already hashed",
            "type": "boolean",
            "x-go-name": "Prehashed"
          },
          "signature": {
            "description": "The message's signature",
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
          },
          "version": {
            "description": "The version of the key to use for verification",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "verifyEcDsaOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```