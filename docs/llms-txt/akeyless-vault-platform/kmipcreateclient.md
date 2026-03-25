# Source: https://docs.akeyless.io/reference/kmipcreateclient.md

# /kmip-create-client

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
    "/kmip-create-client": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "kmipCreateClient",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/kmipCreateClient"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/kmipCreateClientResponse"
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
      "kmipCreateClientResponse": {
        "description": "kmipCreateClientResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/kmipCreateClientOutput"
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
      "kmipCreateClient": {
        "type": "object",
        "title": "kmipCreateClient is a command that creates a new KMIP client.",
        "required": [
          "name"
        ],
        "properties": {
          "activate-keys-on-creation": {
            "description": "If set to 'true', newly created keys on the client will be set to an 'active' state",
            "type": "string",
            "default": "false",
            "x-go-name": "ActivateKeysOnCreation"
          },
          "certificate-ttl": {
            "description": "Client certificate TTL in days",
            "type": "integer",
            "format": "int64",
            "default": 90,
            "x-go-name": "CertificateTTL"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Client name",
            "type": "string",
            "x-go-name": "ClientName"
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
      "kmipCreateClientOutput": {
        "type": "object",
        "properties": {
          "certificate": {
            "type": "string",
            "x-go-name": "Certificate"
          },
          "id": {
            "type": "string",
            "x-go-name": "ID"
          },
          "key": {
            "type": "string",
            "x-go-name": "Key"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```