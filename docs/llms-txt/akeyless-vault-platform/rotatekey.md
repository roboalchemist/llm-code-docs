# Source: https://docs.akeyless.io/reference/rotatekey.md

# /rotate-key

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
    "/rotate-key": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotateKey",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotateKey"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotateKeyResponse"
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
      "rotateKeyResponse": {
        "description": "rotateKeyResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/RotateKeyOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "ItemType": {
        "type": "string",
        "title": "ItemType defines types supported by AKEYLESS.",
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
      "RotateKeyOutput": {
        "description": "RotateKeyOutput defines output of RotateKey operation",
        "type": "object",
        "properties": {
          "classic_key_gw_url": {
            "type": "string",
            "x-go-name": "ClassicKeyGWUrl"
          },
          "item_type": {
            "$ref": "#/components/schemas/ItemType"
          },
          "new_item_version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "NewKeyVersion"
          },
          "next_rotation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NextRotationDate"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "rotateKey": {
        "description": "of it.",
        "type": "object",
        "title": "rotateKey is a command that rotates an existing key, by creating a new version of the key.",
        "required": [
          "name"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Key name",
            "type": "string",
            "x-go-name": "KeyName"
          },
          "new-cert-pem-data": {
            "description": "The new pem encoded certificate for the classic key.\nrelevant only for keys provided by user ('bring-your-own-key')",
            "type": "string",
            "x-go-name": "NewCertPemData"
          },
          "new-key-data": {
            "description": "The new base64 encoded value for the classic key.\nrelevant only for keys provided by user ('bring-your-own-key')",
            "type": "string",
            "x-go-name": "NewKeyData"
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
      }
    }
  }
}
```