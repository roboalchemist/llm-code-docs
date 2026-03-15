# Source: https://docs.akeyless.io/reference/verifydatawithclassickey.md

# /verify-data-with-classic-key

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
    "/verify-data-with-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "verifyDataWithClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/verifyDataWithClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/verifyDataWithClassicKeyResponse"
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
      "verifyDataWithClassicKeyResponse": {
        "description": "verifyDataWithClassicKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/verifyPKICertOutput"
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
      "verifyDataWithClassicKey": {
        "type": "object",
        "title": "verifyDataWithClassicKey is a command that verifies signed data by using a Classic key.",
        "required": [
          "name",
          "version",
          "data",
          "signature"
        ],
        "properties": {
          "data": {
            "description": "Data",
            "type": "string",
            "x-go-name": "Data"
          },
          "display-id": {
            "description": "The display id of the key to use in the verification process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "hashed": {
            "description": "Defines whether the data should be hashed as part of the signing. If true, the data will not be hashed",
            "type": "boolean",
            "default": false,
            "x-go-name": "AlreadyHashed"
          },
          "hashing-method": {
            "description": "HashingMethod",
            "type": "string",
            "default": "SHA256",
            "x-go-name": "HashingMethod"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "The name of the key to use in the verification process",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "signature": {
            "description": "The data's signature in a Base64 format.",
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
            "description": "classic key version",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "verifyPKICertOutput": {
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