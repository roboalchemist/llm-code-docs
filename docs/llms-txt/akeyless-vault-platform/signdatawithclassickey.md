# Source: https://docs.akeyless.io/reference/signdatawithclassickey.md

# /sign-data-with-classic-key

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
    "/sign-data-with-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "signDataWithClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/signDataWithClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/signDataWithClassicKeyResponse"
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
      "signDataWithClassicKeyResponse": {
        "description": "signDataWithClassicKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/signOutput"
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
      "signDataWithClassicKey": {
        "type": "object",
        "title": "signDataWithClassicKey is a command that signs data by using a Classic key.",
        "required": [
          "name",
          "display-id",
          "version",
          "data"
        ],
        "properties": {
          "data": {
            "description": "Data",
            "type": "string",
            "x-go-name": "Data"
          },
          "display-id": {
            "description": "The name of the key to use in the sign data process",
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
          "name": {
            "description": "ClassicKey name",
            "type": "string",
            "x-go-name": "KeyName"
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
      "signOutput": {
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