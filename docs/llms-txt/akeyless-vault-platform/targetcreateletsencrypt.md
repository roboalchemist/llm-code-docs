# Source: https://docs.akeyless.io/reference/targetcreateletsencrypt.md

# /target-create-lets-encrypt

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
    "/target-create-lets-encrypt": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetCreateLetsEncrypt",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetCreateLetsEncrypt"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetCreateLetsEncryptResponse"
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
      "targetCreateLetsEncryptResponse": {
        "description": "targetCreateLetsEncryptResponse wraps response body.",
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
      "targetCreateLetsEncrypt": {
        "description": "targetCreateLetsEncrypt is a command that creates a new Let's Encrypt target",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "acme-challenge": {
            "type": "string",
            "default": "http",
            "x-go-name": "ChallengeType"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "dns-target-creds": {
            "description": "Name of existing cloud target for DNS credentials. Required when acme-challenge=dns. Supported: AWS, Azure, GCP targets",
            "type": "string",
            "x-go-name": "DNSTargetName"
          },
          "email": {
            "description": "Email address for ACME account registration",
            "type": "string",
            "x-go-name": "Email"
          },
          "gcp-project": {
            "description": "GCP Cloud DNS: Project ID. Optional - can be derived from service account",
            "type": "string",
            "x-go-name": "GCPProject"
          },
          "hosted-zone": {
            "description": "AWS Route53 hosted zone ID. Required when dns-target-creds points to AWS target",
            "type": "string",
            "x-go-name": "HostedZone"
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
          "lets-encrypt-url": {
            "type": "string",
            "default": "production",
            "x-go-name": "Environment"
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
          "resource-group": {
            "description": "Azure resource group name. Required when dns-target-creds points to Azure target",
            "type": "string",
            "x-go-name": "ResourceGroup"
          },
          "timeout": {
            "type": "string",
            "default": "5m",
            "x-go-name": "Timeout"
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
      }
    }
  }
}
```