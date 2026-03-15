# Source: https://docs.akeyless.io/reference/kmiprenewclientcertificate.md

# /kmip-renew-client

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
    "/kmip-renew-client": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "kmipRenewClientCertificate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/kmipRenewClientCertificate"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/kmipRenewClientCertificateResponse"
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
      "kmipRenewClientCertificateResponse": {
        "description": "kmipRenewClientCertificateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/kmipRenewClientCertificateOutput"
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
      "kmipRenewClientCertificate": {
        "type": "object",
        "title": "kmipRenewClientCertificate is a command that renews KMIP client certificate.",
        "properties": {
          "client-id": {
            "type": "string",
            "x-go-name": "ClientID"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
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
      "kmipRenewClientCertificateOutput": {
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