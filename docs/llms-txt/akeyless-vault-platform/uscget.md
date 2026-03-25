# Source: https://docs.akeyless.io/reference/uscget.md

# /usc-get

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
    "/usc-get": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uscGet",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uscGet"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uscGetResponse"
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
      "uscGetResponse": {
        "description": "uscGetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UscGetSecretOutput"
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
      "UscGetSecretOutput": {
        "type": "object",
        "properties": {
          "binary_value": {
            "type": "boolean",
            "x-go-name": "BinaryValue"
          },
          "encryption_key": {
            "type": "string",
            "x-go-name": "EncryptionKey"
          },
          "id": {
            "type": "string",
            "x-go-name": "Id"
          },
          "metadata": {
            "x-go-name": "Metadata"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "value": {
            "type": "string",
            "x-go-name": "Value"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "uscGet": {
        "description": "uscGet is a command that gets the value and internal details of a secret from a Universal Secrets Connector",
        "type": "object",
        "required": [
          "usc-name",
          "secret-id"
        ],
        "properties": {
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
            "description": "The secret id (or name, for AWS, Azure, K8s or Hashi vault targets) to get from the Universal Secrets Connector",
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
          },
          "version-id": {
            "description": "The version id (if not specified, will retrieve the last version)",
            "type": "string",
            "x-go-name": "VersionId"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```