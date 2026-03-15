# Source: https://docs.akeyless.io/reference/createusc.md

# /create-usc

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
    "/create-usc": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "CreateUSC",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateUSC"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/CreateUniversalSecretsConnectorResponse"
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
      "CreateUniversalSecretsConnectorResponse": {
        "description": "CreateUniversalSecretsConnectorResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateUSCOutput"
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
      "CreateUSC": {
        "description": "CreateUSC is a command that creates a Universal Secrets Connector",
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
            "description": "Description of the Universal Secrets Connector",
            "type": "string",
            "x-go-name": "Description"
          },
          "environment-names": {
            "description": "The environments in repo-name/environment-name format, comma-separated (only relevant for: github-scope=repository-environment)",
            "type": "string",
            "x-go-name": "GithubEnvironmentsNames"
          },
          "gcp-project-id": {
            "description": "GCP Project ID (Relevant only for GCP targets)",
            "type": "string",
            "x-go-name": "GcpProjectId"
          },
          "gcp-sm-regions": {
            "description": "GCP Secret Manager regions to query for regional secrets (comma-separated, e.g., us-east1,us-west1). Max 12 regions.\nRequired when listing with object-type=regional-secrets.",
            "type": "string",
            "x-go-name": "GcpSmRegions"
          },
          "github-scope": {
            "description": "The scope where secrets will be created, available options: [repository, organization, repository-environment]",
            "type": "string",
            "default": "repository",
            "x-go-name": "GithubScope"
          },
          "item-custom-fields": {
            "description": "Additional custom fields to associate with the item",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "ItemCustomFields"
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
            "description": "Universal Secrets Connector name",
            "type": "string",
            "x-go-name": "ESMName"
          },
          "organization-name": {
            "description": "The organization name to create the secret in (only relevant for: github-scope=organization)",
            "type": "string",
            "x-go-name": "GithubOrganizationName"
          },
          "repository-access": {
            "type": "string",
            "default": "public",
            "x-go-name": "GithubRepositoryAccess"
          },
          "repository-names": {
            "description": "The repository names, comma-separated (only relevant for: github-scope=repository)",
            "type": "string",
            "x-go-name": "GithubRepositoriesNames"
          },
          "tags": {
            "description": "List of the tags attached to this Universal Secrets Connector",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "target-to-associate": {
            "description": "Target Universal Secrets Connector to connect",
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
          },
          "usc-prefix": {
            "description": "Prefix for all secrets created in AWS Secrets Manager",
            "type": "string",
            "x-go-name": "USCPrefix"
          },
          "use-prefix-as-filter": {
            "description": "Whether to filter the USC secret list using the specified usc-prefix [true/false]",
            "type": "string",
            "default": "false",
            "x-go-name": "UsePrefixAsFilterStr"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "CreateUSCOutput": {
        "type": "object",
        "properties": {
          "universal_secrets_connector_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ESMId"
          },
          "universal_secrets_connector_name": {
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