# Source: https://docs.akeyless.io/reference/gatewaygettmpusers.md

# /gateway-get-producer-tmp-creds

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
    "/gateway-get-producer-tmp-creds": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetTmpUsers",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetTmpUsers"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayGetTmpUsersResponse"
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
      "gatewayGetTmpUsersResponse": {
        "description": "gatewayGetTmpUsersResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/TmpUserData"
              }
            }
          }
        }
      }
    },
    "schemas": {
      "DynamicSecretType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer"
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
      "TmpUserData": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "custom_ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CustomTtl"
          },
          "dynamic_secret_type": {
            "$ref": "#/components/schemas/DynamicSecretType"
          },
          "encrypted_secret": {
            "type": "string",
            "x-go-name": "EncryptedSecret"
          },
          "host": {
            "type": "string",
            "x-go-name": "Host"
          },
          "id": {
            "type": "string",
            "x-go-name": "ID"
          },
          "sub_claims": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "SubClaims"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/producer/dynamicsecret/base"
      },
      "gatewayGetTmpUsers": {
        "description": "gatewayGetTmpUsers is a command that returns gateway configuration [Deprecated: Use dynamic-secret-tmp-creds-get command]",
        "type": "object",
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
            "description": "Dynamic secret name",
            "type": "string",
            "x-go-name": "DSName"
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