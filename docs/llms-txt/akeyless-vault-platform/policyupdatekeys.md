# Source: https://docs.akeyless.io/reference/policyupdatekeys.md

# /policy-update-keys

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
    "/policy-update-keys": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "policyUpdateKeys",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/policyUpdateKeys"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/policyUpdateKeysResponse"
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
      "policyUpdateKeysResponse": {
        "description": "",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/policiesUpdateOutput"
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
      "policiesUpdateOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "policyUpdateKeys": {
        "type": "object",
        "required": [
          "id"
        ],
        "properties": {
          "allowed-algorithms": {
            "description": "Specify allowed key algorithms (e.g., [RSA2048,AES128GCM])",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedAlgorithms"
          },
          "allowed-key-names": {
            "description": "Specify allowed protection key names. To enforce using the account's default protection key, use 'default-account-key'",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedKeyNames"
          },
          "allowed-key-types": {
            "description": "Specify allowed key protection types (dfc, classic-key)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedKeyTypes"
          },
          "id": {
            "description": "Policy id",
            "type": "string",
            "x-go-name": "PolicyID"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "max-rotation-interval-days": {
            "description": "Set the maximum rotation interval for automatic key rotation.",
            "type": "integer",
            "format": "int32",
            "x-go-name": "MaxRotationIntervalDays"
          },
          "object-types": {
            "description": "The object type this policy will apply to (items, targets)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ObjectTypes"
          },
          "path": {
            "description": "The path the policy refers to",
            "type": "string",
            "x-go-name": "Path"
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