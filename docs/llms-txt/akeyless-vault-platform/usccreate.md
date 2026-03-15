# Source: https://docs.akeyless.io/reference/usccreate.md

# /usc-create

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
    "/usc-create": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "uscCreate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/uscCreate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/uscCreateResponse"
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
      "uscCreateResponse": {
        "description": "uscCreateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/UscCreateSecretOutput"
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
      "ObjectType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/external-secrets-manager/base"
      },
      "UscCreateSecretOutput": {
        "type": "object",
        "properties": {
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
      "uscCreate": {
        "description": "uscCreate is a command that creates a new secret in a Universal Secrets Connector",
        "type": "object",
        "required": [
          "usc-name",
          "value",
          "secret-name"
        ],
        "properties": {
          "binary-value": {
            "description": "Use this option if the universal secrets value is a base64 encoded binary",
            "type": "boolean",
            "x-go-name": "BinaryValue"
          },
          "description": {
            "description": "Description of the universal secrets",
            "type": "string",
            "x-go-name": "Description"
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
          "object-type": {
            "$ref": "#/components/schemas/ObjectType"
          },
          "pfx-password": {
            "description": "Optional, the passphrase that protects the private key within the pfx certificate (Relevant only for Azure KV certificates)",
            "type": "string",
            "x-go-name": "PfxPassword"
          },
          "region": {
            "description": "Optional, create secret in a specific region (GCP only).\nIf empty, a global secret will be created (provider default).",
            "type": "string",
            "x-go-name": "Region"
          },
          "secret-name": {
            "description": "Name for the new universal secrets",
            "type": "string",
            "x-go-name": "SecretName"
          },
          "tags": {
            "description": "Tags for the universal secrets",
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
          "usc-encryption-key": {
            "description": "Optional, The name of the remote key that used to encrypt the secret value (if empty, the default key will be used)",
            "type": "string",
            "x-go-name": "EncryptionKey"
          },
          "usc-name": {
            "description": "Name of the Universal Secrets Connector item",
            "type": "string",
            "x-go-name": "ExternalSecretManagerName"
          },
          "value": {
            "description": "Value of the universal secrets item, either text or base64 encoded binary",
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