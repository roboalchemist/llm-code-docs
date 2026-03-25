# Source: https://docs.akeyless.io/reference/listacmeaccounts.md

# /list-acme-accounts

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
    "/list-acme-accounts": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "listAcmeAccounts",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/listAcmeAccounts"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/listAcmeAccountsResponse"
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
      "listAcmeAccountsResponse": {
        "description": "listAcmeAccountsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ListAcmeAccountsOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AcmeAccount": {
        "description": "AcmeAccount is copied without the jwk as it seems\nlike it has issues with sdk",
        "type": "object",
        "properties": {
          "account_id": {
            "description": "AccountId is the ACME account id, not Akeyless account id",
            "type": "string",
            "x-go-name": "AccountId"
          },
          "key_digest": {
            "type": "string",
            "x-go-name": "KeyDigest"
          },
          "status": {
            "type": "string",
            "x-go-name": "Status"
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
      },
      "ListAcmeAccountsOutput": {
        "type": "object",
        "properties": {
          "accounts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AcmeAccount"
            },
            "x-go-name": "Accounts"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "listAcmeAccounts": {
        "description": "listAcmeAccounts is a command lists acme external accounts for a cert issuer",
        "type": "object",
        "required": [
          "cert-issuer-name"
        ],
        "properties": {
          "cert-issuer-name": {
            "description": "The name of the PKI certificate issuer",
            "type": "string",
            "x-go-name": "CertIssuerName"
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