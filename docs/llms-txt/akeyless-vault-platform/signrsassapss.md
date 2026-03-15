# Source: https://docs.akeyless.io/reference/signrsassapss.md

# /sign-rsassa-pss

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
    "/sign-rsassa-pss": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "signRsaSsaPss",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/signRsaSsaPss"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/signRsaSsaPssResponse"
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
      "signRsaSsaPssResponse": {
        "description": "signRsaSsaPssResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/SignRsaSsaPssOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "HashFunction": {
        "description": "HashFunction defines the hash function (e.g. sha-256)",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
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
      "SignRsaSsaPssOutput": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "signRsaSsaPss": {
        "description": "signRsaSsaPss is a command that calculates the signature of a given message using rsassa-pss",
        "type": "object",
        "required": [
          "message"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the RSA key to use in the signing process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "hash-function": {
            "$ref": "#/components/schemas/HashFunction"
          },
          "item-id": {
            "description": "The item id of the RSA key to use in the signing process",
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
            "description": "The name of the RSA key to use in the signing process",
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