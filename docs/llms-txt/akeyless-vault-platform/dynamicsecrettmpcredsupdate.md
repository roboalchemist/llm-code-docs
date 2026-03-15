# Source: https://docs.akeyless.io/reference/dynamicsecrettmpcredsupdate.md

# /dynamic-secret-tmp-creds-update

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
    "/dynamic-secret-tmp-creds-update": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "dynamicSecretTmpCredsUpdate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/dynamicSecretTmpCredsUpdate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/dynamicSecretTmpCredsUpdateResponse"
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
      "dynamicSecretTmpCredsUpdateResponse": {
        "description": "dynamicSecretTmpCredsUpdateResponse wraps response body."
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
      "dynamicSecretTmpCredsUpdate": {
        "description": "dynamicSecretTmpCredsUpdate is a command that updates dynamic secret temp creds",
        "type": "object",
        "required": [
          "name",
          "tmp-creds-id",
          "new-ttl-min",
          "host"
        ],
        "properties": {
          "host": {
            "description": "Host",
            "type": "string",
            "x-go-name": "Host"
          },
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
          "new-ttl-min": {
            "description": "New TTL in Minutes",
            "type": "integer",
            "format": "int64",
            "x-go-name": "NewTTL"
          },
          "tmp-creds-id": {
            "description": "Tmp Creds ID",
            "type": "string",
            "x-go-name": "TmpCredsID"
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