# Source: https://docs.akeyless.io/reference/uscdelete.md

# /usc-delete

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
    "/usc-delete": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uscDelete",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uscDelete"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "202": {
            "$ref": "#/components/responses/uscDeleteResponse"
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
      "uscDeleteResponse": {
        "description": "uscDeleteResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UscDeleteSecretOutput"
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
      "UscDeleteSecretOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "uscDelete": {
        "description": "uscDelete is a command that deletes a secret from a Universal Secrets Connector",
        "type": "object",
        "required": [
          "usc-name",
          "secret-id"
        ],
        "properties": {
          "force-delete": {
            "description": "Force delete objects that are soft deleted by default (relavent only for Azure target)",
            "type": "boolean",
            "x-go-name": "ForceDelete"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "namespace": {
            "description": "The namespace (relevant for Hashi vault target)",
            "type": "string",
            "x-go-name": "Namespace"
          },
          "secret-id": {
            "description": "The universal secrets id (or name, for AWS, Azure, K8s or Hashi vault targets) to delete",
            "type": "string",
            "x-go-name": "SecretId"
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
            "description": "Name of the Universal Secrets Connector item",
            "type": "string",
            "x-go-name": "ExternalSecretManagerName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```