# Source: https://docs.akeyless.io/reference/exportclassickey.md

# /export-classic-key

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
    "/export-classic-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "ExportClassicKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ExportClassicKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/ExportClassicKeyResponse"
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
      "ExportClassicKeyResponse": {
        "description": "ExportClassicKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ExportClassicKeyOutput"
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
      "ExportClassicKey": {
        "description": "ExportClassicKey is a command that returns the classic key material",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "accessibility": {
            "description": "for personal password manager",
            "type": "string",
            "default": "regular",
            "x-go-name": "ItemAccessibilityString"
          },
          "export-public-key": {
            "description": "Use this option to output only public key",
            "type": "boolean",
            "default": false,
            "x-go-name": "ExportPublicKey"
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
            "x-go-name": "ClassicKeyName"
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
            "description": "Classic key version",
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          },
          "wrapping-key-name": {
            "description": "Classic key name to wrap the key material with",
            "type": "string",
            "x-go-name": "WrappingKeyName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "ExportClassicKeyOutput": {
        "type": "object",
        "properties": {
          "certificatePem": {
            "type": "string",
            "x-go-name": "CertificatePem"
          },
          "key": {
            "type": "string",
            "x-go-name": "Key"
          },
          "ssh": {
            "type": "string",
            "x-go-name": "Ssh"
          },
          "wrapping-iv": {
            "type": "string",
            "x-go-name": "WrappingIV"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
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
      }
    }
  }
}
```