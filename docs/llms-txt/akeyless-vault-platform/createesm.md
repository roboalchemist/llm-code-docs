# Source: https://docs.akeyless.io/reference/createesm.md

# /create-esm

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
    "/create-esm": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "CreateESM",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateESM"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/CreateExternalSecretsManagerResponse"
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
      "CreateExternalSecretsManagerResponse": {
        "description": "CreateExternalSecretsManagerResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateESMOutput"
            }
          }
        }
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
      "CreateESM": {
        "description": "CreateESM is a command that creates an External Secrets Manager. [Deprecated: Use command create-usc]",
        "type": "object",
        "required": [
          "name",
          "target-to-associate"
        ],
        "properties": {
          "azure-kv-name": {
            "description": "Azure Key Vault name (Relevant only for Azure targets)",
            "type": "string",
            "x-go-name": "AzureVault"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the External Secrets Manager",
            "type": "string",
            "x-go-name": "Description"
          },
          "gcp-project-id": {
            "description": "GCP Project ID (Relevant only for GCP targets)",
            "type": "string",
            "x-go-name": "GcpProjectId"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "k8s-namespace": {
            "description": "K8s namespace (Relevant to Kubernetes targets)",
            "type": "string",
            "x-go-name": "K8sNamespace"
          },
          "name": {
            "description": "External Secrets Manager name",
            "type": "string",
            "x-go-name": "ESMName"
          },
          "tags": {
            "description": "List of the tags attached to this External Secrets Manager",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "target-to-associate": {
            "description": "Target External Secrets Manager to connect",
            "type": "string",
            "x-go-name": "TargetToAssociate"
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
      },
      "CreateESMOutput": {
        "type": "object",
        "properties": {
          "external_secret_manager_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ESMId"
          },
          "external_secret_manager_name": {
            "type": "string",
            "x-go-name": "ESMName"
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
      }
    }
  }
}
```