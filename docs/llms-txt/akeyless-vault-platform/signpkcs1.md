# Source: https://docs.akeyless.io/reference/signpkcs1.md

# /sign-pkcs1

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
    "/sign-pkcs1": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "signPKCS1",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/signPKCS1"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/signPKCS1Response"
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
      "signPKCS1Response": {
        "description": "signPKCS1Response wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/SignPKCS1Output"
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
      "SignPKCS1Output": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "signPKCS1": {
        "description": "signPKCS1 is a command that calculates the signature of hashed data using\nRSASSA-PKCS1-V1_5-SIGN from RSA PKCS#1 v1.5.",
        "type": "object",
        "required": [
          "message"
        ],
        "properties": {
          "display-id": {
            "description": "The display id of the key to use in the signing process",
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
            "description": "The item id of the key to use in the signing process",
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
            "description": "The message to be signed",
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