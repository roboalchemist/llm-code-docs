# Source: https://docs.akeyless.io/reference/signecdsa.md

# /sign-ecdsa

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
    "/sign-ecdsa": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "signEcDsa",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/signEcDsa"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/signEcDsaResponse"
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
      "signEcDsaResponse": {
        "description": "signEcDsaResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/SignEcDsaOutput"
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
      "SignEcDsaOutput": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "signEcDsa": {
        "description": "signEcDsa Calculates the signature of a given message using ECDSA\nand a sha hash algorithm matching the key size",
        "type": "object",
        "required": [
          "message"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "display-id": {
            "description": "The display id of the EC key to use for the signing process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "item-id": {
            "description": "The item id of the EC key to use for the signing process",
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
            "description": "The name of the EC key to use for the signing process",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "message": {
            "description": "The input message to sign in a base64 format",
            "type": "string",
            "x-go-name": "Message"
          },
          "prehashed": {
            "description": "Markes that the message is already hashed",
            "type": "boolean",
            "x-go-name": "Prehashed"
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
            "description": "The version of the key to use for signing",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```