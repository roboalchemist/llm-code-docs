# Source: https://docs.akeyless.io/reference/updatezerossltarget.md

# /update-zerossl-target

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
    "/update-zerossl-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateZeroSSLTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateZeroSSLTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateZeroSSLTargetResponse"
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
      "updateZeroSSLTargetResponse": {
        "description": "updateZeroSSLTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateZeroSSLTargetOutput"
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
      "updateZeroSSLTarget": {
        "description": "updateZeroSSLTarget is a command that updates an existing target. [Deprecated: Use target-update-zerossl command]",
        "type": "object",
        "required": [
          "name",
          "imap-username",
          "imap-password",
          "imap-fqdn",
          "api-key"
        ],
        "properties": {
          "api-key": {
            "description": "API Key of the ZeroSSLTarget account",
            "type": "string",
            "x-go-name": "APIKey"
          },
          "comment": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Comment"
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
          "imap-target-email": {
            "description": "ImapValidationEmail to use when asking ZeroSSL to send a validation email, if empty will user imap-username",
            "type": "string",
            "x-go-name": "ImapValidationEmail"
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
          "keep-prev-version": {
            "description": "Whether to keep previous version [true/false]. If not set, use default according to account settings",
            "type": "string",
            "x-go-name": "KeepPrevVersion"
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
          "new-name": {
            "description": "New target name",
            "type": "string",
            "x-go-name": "NewTargetName"
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
          },
          "update-version": {
            "description": "Deprecated",
            "type": "boolean",
            "x-go-name": "CreateNewVersion"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateZeroSSLTargetOutput": {
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