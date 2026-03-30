# Source: https://docs.akeyless.io/reference/gatewayrevoketmpusers.md

# /gateway-revoke-producer-tmp-creds

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
    "/gateway-revoke-producer-tmp-creds": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayRevokeTmpUsers",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayRevokeTmpUsers"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayRevokeTmpUsersResponse"
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
      "gatewayRevokeTmpUsersResponse": {
        "description": "gatewayRevokeTmpUsersResponse wraps response body."
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
      "gatewayRevokeTmpUsers": {
        "description": "gatewayRevokeTmpUsers is a command that revoke producer tmp user [Deprecated: Use dynamic-secret-tmp-creds-delete command]",
        "type": "object",
        "required": [
          "name"
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
          "revoke-all": {
            "description": "Revoke All Temp Creds",
            "type": "boolean",
            "x-go-name": "RevokeAll"
          },
          "soft-delete": {
            "description": "Soft Delete",
            "type": "boolean",
            "x-go-name": "SoftDelete"
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