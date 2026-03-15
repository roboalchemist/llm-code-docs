# Source: https://docs.akeyless.io/reference/verifypkcs1.md

# /verify-pkcs1

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
    "/verify-pkcs1": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "verifyPKCS1",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/verifyPKCS1"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/verifyPKCS1Response"
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
      "verifyPKCS1Response": {
        "description": "verifyPKCS1Response wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/verifyPKCS1Output"
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
      "verifyPKCS1": {
        "type": "object",
        "title": "verifyPKCS1 is a command that verifies an RSA PKCS#1 v1.5 signature.",
        "required": [
          "key-name",
          "message",
          "signature"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the key to use in the verification process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "hash-function": {
            "$ref": "#/components/schemas/HashFunction"
          },
          "input-format": {
            "description": "Select default assumed format for the plaintext message. Currently supported options: [base64]",
            "type": "string",
            "x-go-name": "InputFormat"
          },
          "item-id": {
            "description": "The item id of the key to use in the verification process",
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
            "description": "The name of the RSA key to use in the verification process",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "message": {
            "description": "The message to be verified",
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
      "verifyPKCS1Output": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```