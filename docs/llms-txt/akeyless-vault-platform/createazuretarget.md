# Source: https://docs.akeyless.io/reference/createazuretarget.md

# /create-azure-target

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
    "/create-azure-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createAzureTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createAzureTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createAzureTargetResponse"
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
      "createAzureTargetResponse": {
        "description": "createAzureTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createAzureTargetOutput"
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
      "createAzureTarget": {
        "description": "createAzureTarget is a command that creates a new target. [Deprecated: Use target-create-azure command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "azure-cloud": {
            "description": "Azure cloud environment to use. Values: AzureCloud (default), AzureUSGovernment, AzureChinaCloud.",
            "type": "string",
            "default": "AzureCloud",
            "x-go-name": "AzureCloud"
          },
          "client-id": {
            "description": "Azure client/application id",
            "type": "string",
            "x-go-name": "AzureClientID"
          },
          "client-secret": {
            "description": "Azure client secret",
            "type": "string",
            "x-go-name": "AzureClientSecret"
          },
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
          },
          "connection-type": {
            "description": "Type of connection [credentials/cloud-identity]",
            "type": "string",
            "default": "credentials",
            "x-go-name": "ConnectionType"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key": {
            "description": "The name of a key that used to encrypt the target secret value (if empty, the account default protectionKey key will be used)",
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "max-versions": {
            "description": "Set the maximum number of versions, limited by the account settings defaults.",
            "type": "string",
            "x-go-name": "MaxVersions"
          },
          "name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "resource-group-name": {
            "description": "The Resource Group name in your Azure subscription",
            "type": "string",
            "x-go-name": "AzureResourceGroupName"
          },
          "resource-name": {
            "description": "The name of the relevant Resource",
            "type": "string",
            "x-go-name": "AzureResourceName"
          },
          "subscription-id": {
            "description": "Azure Subscription Id",
            "type": "string",
            "x-go-name": "AzureSubscriptionID"
          },
          "tenant-id": {
            "description": "Azure tenant id",
            "type": "string",
            "x-go-name": "AzureTenantID"
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
          "use-gw-cloud-identity": {
            "description": "Use the GW's Cloud IAM [Deprecated: Use connection-type=cloud-identity]",
            "type": "boolean",
            "x-go-name": "AzureUseDefaultIdentity"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "createAzureTargetOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```