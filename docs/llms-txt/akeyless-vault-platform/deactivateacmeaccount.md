# Source: https://docs.akeyless.io/reference/deactivateacmeaccount.md

# /deactivate-acme-account

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
    "/deactivate-acme-account": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "deactivateAcmeAccount",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/deactivateAcmeAccount"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/deactivateAcmeAccountResponse"
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
      "deactivateAcmeAccountResponse": {
        "description": "deactivateAcmeAccountResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/DeactivateAcmeAccountOutput"
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
      "DeactivateAcmeAccountOutput": {
        "type": "object",
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
      },
      "deactivateAcmeAccount": {
        "description": "deactivateAcmeAccount is a command that Deactivates \\ Deletes an acme external account",
        "type": "object",
        "required": [
          "cert-issuer-name",
          "acme-account-id"
        ],
        "properties": {
          "acme-account-id": {
            "description": "The acme account id to deactivate",
            "type": "string",
            "x-go-name": "AcmeAccountId"
          },
          "cert-issuer-name": {
            "description": "The name of the PKI certificate issuer",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "delete-account": {
            "description": "Delete the account",
            "type": "boolean",
            "x-go-name": "DeleteAccount"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
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