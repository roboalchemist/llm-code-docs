# Source: https://docs.akeyless.io/reference/targetcreategodaddy.md

# /target-create-godaddy

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
    "/target-create-godaddy": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "targetCreateGodaddy",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/targetCreateGodaddy"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/targetCreateGodaddyResponse"
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
      "targetCreateGodaddyResponse": {
        "description": "targetCreateGodaddyResponse wraps response body.",
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
      "targetCreateGodaddy": {
        "type": "object",
        "title": "targetCreateGodaddy is a command that creates a new Godaddy target.",
        "required": [
          "imap-username",
          "imap-password",
          "imap-fqdn",
          "api-key",
          "secret",
          "name"
        ],
        "properties": {
          "api-key": {
            "description": "Key of the api credentials to the Godaddy account",
            "type": "string",
            "x-go-name": "Key"
          },
          "customer_id": {
            "description": "Customer ID (ShopperId) required for renewal of imported certificates",
            "type": "string",
            "x-go-name": "CustomerID"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "imap-fqdn": {
            "description": "ImapFQDN of the IMAP service, FQDN or IPv4 address. Must be FQDN if the IMAP is using TLS",
            "type": "string",
            "x-go-name": "ImapFQDN"
          },
          "imap-password": {
            "description": "ImapPassword to access the IMAP service",
            "type": "string",
            "x-go-name": "ImapPassword"
          },
          "imap-port": {
            "description": "ImapPort of the IMAP service",
            "type": "string",
            "default": "993",
            "x-go-name": "ImapPort"
          },
          "imap-username": {
            "description": "ImapUsername to access the IMAP service",
            "type": "string",
            "x-go-name": "ImapUsername"
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
          "secret": {
            "description": "Secret of the api credentials to the Godaddy account",
            "type": "string",
            "x-go-name": "Secret"
          },
          "timeout": {
            "description": "Timeout waiting for certificate validation in Duration format (1h - 1 Hour, 20m - 20 Minutes, 33m3s - 33 Minutes and 3 Seconds), maximum 1h.",
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