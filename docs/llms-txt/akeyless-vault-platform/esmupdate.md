# Source: https://docs.akeyless.io/reference/esmupdate.md

# /esm-update

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
    "/esm-update": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "esmUpdate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/esmUpdate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/esmUpdateResponse"
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
      "esmUpdateResponse": {
        "description": "esmUpdateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/EsmUpdateSecretOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "EsmUpdateSecretOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "secret_id": {
            "type": "string",
            "x-go-name": "SecretId"
          },
          "version_id": {
            "type": "string",
            "x-go-name": "VersionId"
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
      "esmUpdate": {
        "description": "esmUpdate is a command that updates a secret in an External Secrets Manager",
        "type": "object",
        "required": [
          "esm-name",
          "secret-id",
          "value"
        ],
        "properties": {
          "binary-value": {
            "description": "Use this option if the external secret value is a base64 encoded binary",
            "type": "boolean",
            "x-go-name": "BinaryValue"
          },
          "description": {
            "description": "Description of the external secret",
            "type": "string",
            "x-go-name": "Description"
          },
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
            "description": "The external secret id (or name, for AWS, Azure or K8s targets) to update",
            "type": "string",
            "x-go-name": "SecretId"
          },
          "tags": {
            "description": "Tags for the external secret",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Tags"
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
          "value": {
            "description": "Value of the external secret item, either text or base64 encoded binary",
            "type": "string",
            "x-go-name": "Value"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```