# Source: https://docs.akeyless.io/reference/staticsecretdeletesync.md

# /static-secret-delete-sync

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
    "/static-secret-delete-sync": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "staticSecretDeleteSync",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/staticSecretDeleteSync"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/staticSecretDeleteSyncResponse"
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
      "staticSecretDeleteSyncResponse": {
        "description": "staticSecretDeleteSyncResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/StaticSecretDeleteSyncOutput"
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
      "StaticSecretDeleteSyncOutput": {
        "type": "object",
        "properties": {
          "secret-name": {
            "type": "string",
            "x-go-name": "SecretName"
          },
          "usc-name": {
            "type": "string",
            "x-go-name": "USCName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "staticSecretDeleteSync": {
        "type": "object",
        "title": "staticSecretDeleteSync is a command that deletes a static secret sync.",
        "required": [
          "usc-name",
          "name"
        ],
        "properties": {
          "delete-from-usc": {
            "description": "Delete the secret from the remote target USC as well",
            "type": "boolean",
            "default": false,
            "x-go-name": "DeleteRemote"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Static secret name",
            "type": "string",
            "x-go-name": "StaticSecretName"
          },
          "remote-secret-name": {
            "description": "Remote Secret Name to disambiguate when multiple syncs exist under the same USC",
            "type": "string",
            "x-go-name": "RemoteSecretName"
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
          "usc-name": {
            "description": "Universal Secret Connector name",
            "type": "string",
            "x-go-name": "USCName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```