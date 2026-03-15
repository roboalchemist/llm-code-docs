# Source: https://docs.akeyless.io/reference/rotatedsecretsync.md

# /rotated-secret-sync

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
    "/rotated-secret-sync": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rotatedSecretSync",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rotatedSecretSync"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rotatedSecretSyncResponse"
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
      "rotatedSecretSyncResponse": {
        "description": "rotatedSecretSyncResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/rotatedSecretSyncOutput"
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
      "rotatedSecretSync": {
        "type": "object",
        "title": "rotatedSecretSync is a command that sync rotated secret value.",
        "required": [
          "name"
        ],
        "properties": {
          "DeleteRemote": {
            "description": "Delete the secret from remote secret manager (for association create/update)",
            "type": "boolean"
          },
          "filter-secret-value": {
            "description": "JQ expression to filter or transform the secret value",
            "type": "string",
            "x-go-name": "FilterSecretValue"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Rotated secret name",
            "type": "string",
            "x-go-name": "RsName"
          },
          "namespace": {
            "description": "Vault namespace, releavnt only for Hashicorp Vault Target",
            "type": "string",
            "x-go-name": "Namespace"
          },
          "remote-secret-name": {
            "description": "Remote Secret Name that will be synced on the remote endpoint",
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
            "description": "Universal Secret Connector name, If not provided all attached USC's will be synced",
            "type": "string",
            "x-go-name": "USCName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "rotatedSecretSyncOutput": {
        "type": "object",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```