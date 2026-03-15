# Source: https://docs.akeyless.io/reference/verifypkicertwithclassickey.md

# /verify-pki-cert-with-classic-key

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
    "/verify-pki-cert-with-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "verifyPKICertWithClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/verifyPKICertWithClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/verifyPKICertWithClassicKeyResponse"
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
      "verifyPKICertWithClassicKeyResponse": {
        "description": "verifyPKICertWithClassicKeyResponse wraps response body.",
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
      "verifyPKICertOutput": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "x-go-name": "Result"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "verifyPKICertWithClassicKey": {
        "type": "object",
        "title": "verifyPKICertWithClassicKey is a command that verifys PKICert by using an Classic key.",
        "required": [
          "display-id",
          "version",
          "pki-cert"
        ],
        "properties": {
          "display-id": {
            "description": "The name of the key to use in the verify PKICert process",
            "type": "string",
            "x-go-name": "DisplayId"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "pki-cert": {
            "description": "PkiCert",
            "type": "string",
            "x-go-name": "PkiCert"
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
      }
    }
  }
}
```