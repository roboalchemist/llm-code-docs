# Source: https://docs.akeyless.io/reference/targetcreatesalesforce.md

# /target-create-salesforce

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
    "/target-create-salesforce": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetCreateSalesforce",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetCreateSalesforce"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetCreateSalesforceResponse"
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
      "targetCreateSalesforceResponse": {
        "description": "targetCreateSalesforceResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/targetCreateOutput"
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
      "targetCreateOutput": {
        "type": "object",
        "properties": {
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "targetCreateSalesforce": {
        "description": "targetCreateSalesforce is a command that creates a new Salesforce target",
        "type": "object",
        "required": [
          "tenant-url",
          "client-id",
          "email",
          "auth-flow",
          "name"
        ],
        "properties": {
          "app-private-key-data": {
            "description": "Base64 encoded PEM of the connected app private key (relevant for JWT auth only)",
            "type": "string",
            "x-go-name": "AppPrivateKeyData"
          },
          "auth-flow": {
            "description": "type of the auth flow ('jwt' / 'user-password')",
            "type": "string",
            "x-go-name": "AuthFlowType"
          },
          "ca-cert-data": {
            "description": "Base64 encoded PEM cert to use when uploading a new key to Salesforce",
            "type": "string",
            "x-go-name": "CACertData"
          },
          "ca-cert-name": {
            "description": "name of the certificate in Salesforce tenant to use when uploading new key",
            "type": "string",
            "x-go-name": "CACertName"
          },
          "client-id": {
            "description": "Client ID of the oauth2 app to use for connecting to Salesforce",
            "type": "string",
            "x-go-name": "ClientId"
          },
          "client-secret": {
            "description": "Client secret of the oauth2 app to use for connecting to Salesforce (required for password flow)",
            "type": "string",
            "x-go-name": "ClientSecret"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "email": {
            "description": "The email of the user attached to the oauth2 app used for connecting to Salesforce",
            "type": "string",
            "x-go-name": "Email"
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
          "password": {
            "description": "The password of the user attached to the oauth2 app used for connecting to Salesforce (required for user-password flow)",
            "type": "string",
            "x-go-name": "Password"
          },
          "security-token": {
            "description": "The security token of the user attached to the oauth2 app used for connecting to Salesforce  (required for user-password flow)",
            "type": "string",
            "x-go-name": "SecurityToken"
          },
          "tenant-url": {
            "description": "Url of the Salesforce tenant",
            "type": "string",
            "x-go-name": "TenantUrl"
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