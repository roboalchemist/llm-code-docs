# Source: https://docs.akeyless.io/reference/esmdelete.md

# /esm-delete

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
    "/esm-delete": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "esmDelete",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/esmDelete"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "202": {
            "$ref": "#/components/responses/esmDeleteResponse"
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
      "esmDeleteResponse": {
        "description": "esmDeleteResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/EsmDeleteSecretOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "EsmDeleteSecretOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
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
      },
      "esmDelete": {
        "description": "esmDelete is a command that deletes a secret from an External Secrets Manager",
        "type": "object",
        "required": [
          "esm-name",
          "secret-id"
        ],
        "properties": {
          "esm-name": {
            "description": "Name of the External Secrets Manager item",
            "type": "string",
            "x-go-name": "ExternalSecretManagerName"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "secret-id": {
            "description": "The external secret id (or name, for AWS, Azure or K8s targets) to delete",
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
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```