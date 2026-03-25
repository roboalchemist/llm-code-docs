# Source: https://docs.akeyless.io/reference/assoctargetitem.md

# /assoc-target-item

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
    "/assoc-target-item": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "assocTargetItem",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/assocTargetItem"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/assocTargetItemResponse"
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
      "assocTargetItemResponse": {
        "description": "assocTargetItemResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/CreateTargetItemAssocOutput"
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
      "CreateTargetItemAssocOutput": {
        "description": "CreateTargetItemAssocOutput defines output of CreateTargetItemAssoc\noperation.",
        "type": "object",
        "properties": {
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "assocTargetItem": {
        "description": "assocTargetItem is a command that creates an association between target\nand item.",
        "type": "object",
        "required": [
          "target-name",
          "name"
        ],
        "properties": {
          "certificate-path": {
            "description": "A path on the target to store the certificate pem file (relevant only for certificate provisioning)",
            "type": "string",
            "x-go-name": "CertificatePath"
          },
          "chain-path": {
            "description": "A path on the target to store the full chain pem file (relevant only for certificate provisioning)",
            "type": "string",
            "x-go-name": "ChainPath"
          },
          "disable-previous-key-version": {
            "description": "Automatically disable previous key version (required for azure targets)",
            "type": "boolean",
            "default": false,
            "x-go-name": "AutoDisablePreviousKeyVersion"
          },
          "external-key-name": {
            "description": "The external key name to associate with the classic key (Relevant only for Classic Key AWS/Azure/GCP targets)",
            "type": "string",
            "x-go-name": "ExternalKeyName"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-operations": {
            "description": "A list of allowed operations for the key (required for azure targets)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "KeyOperations"
          },
          "keyring-name": {
            "description": "Keyring name of the GCP KMS (required for gcp targets)",
            "type": "string",
            "x-go-name": "KeyringName"
          },
          "kms-algorithm": {
            "description": "Algorithm of the key in GCP KMS (required for gcp targets)",
            "type": "string",
            "x-go-name": "KMSAlgorithm"
          },
          "location-id": {
            "description": "Location id of the GCP KMS (required for gcp targets)",
            "type": "string",
            "x-go-name": "LocationId"
          },
          "multi-region": {
            "description": "Set to 'true' to create a multi-region managed key. (Relevant only for Classic Key AWS targets)",
            "type": "string",
            "default": "false",
            "x-go-name": "MultiRegion"
          },
          "name": {
            "description": "The item to associate",
            "type": "string",
            "x-go-name": "ItemName"
          },
          "post-provision-command": {
            "description": "A custom command to run on the remote target after successful provisioning (relevant only for certificate provisioning)",
            "type": "string",
            "x-go-name": "PostProvisionCommand"
          },
          "private-key-path": {
            "description": "A path on the target to store the private key (relevant only for certificate provisioning)",
            "type": "string",
            "x-go-name": "PrivateKeyPath"
          },
          "project-id": {
            "description": "Project id of the GCP KMS (required for gcp targets)",
            "type": "string",
            "x-go-name": "ProjectId"
          },
          "protection-level": {
            "description": "Protection level of the key [software/hardware] (relevant for gcp targets)",
            "type": "string",
            "default": "software",
            "x-go-name": "ProtectionLevel"
          },
          "purpose": {
            "description": "Purpose of the key in GCP KMS (required for gcp targets)",
            "type": "string",
            "x-go-name": "Purpose"
          },
          "regions": {
            "description": "The list of regions to create a copy of the key in (relevant for aws targets)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Regions"
          },
          "sra-association": {
            "description": "Is the target to associate is for sra, relevant only for linked target association for ldap rotated secret",
            "type": "boolean",
            "default": false,
            "x-go-name": "IsSraAssociation"
          },
          "target-name": {
            "description": "The target to associate",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "tenant-secret-type": {
            "description": "The tenant secret type [Data/SearchIndex/Analytics] (required for salesforce targets)",
            "type": "string",
            "x-go-name": "TenantSecretType"
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
          "vault-name": {
            "description": "Name of the vault used (required for azure targets)",
            "type": "string",
            "x-go-name": "VaultName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```