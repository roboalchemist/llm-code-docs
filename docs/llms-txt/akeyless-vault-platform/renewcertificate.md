# Source: https://docs.akeyless.io/reference/renewcertificate.md

# /renew-certificate

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
    "/renew-certificate": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "RenewCertificate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RenewCertificate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/renewCertificateResponse"
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
      "renewCertificateResponse": {
        "description": "renewCertificateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/RenewCertificateOutput"
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
      "RenewCertificate": {
        "type": "object",
        "title": "RenewCertificate is a command that renews a PKI certificate.",
        "properties": {
          "cert-issuer-name": {
            "description": "The name of the PKI certificate issuer",
            "type": "string",
            "x-go-name": "CertIssuerName"
          },
          "generate-key": {
            "description": "Generate a new key as part of the certificate renewal",
            "type": "boolean",
            "x-go-name": "GenerateKey"
          },
          "item-id": {
            "description": "Certificate item id",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemId"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Certificate name",
            "type": "string",
            "x-go-name": "CertName"
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
      "RenewCertificateOutput": {
        "type": "object",
        "properties": {
          "cert": {
            "type": "string",
            "x-go-name": "Cert"
          },
          "cert_display_id": {
            "type": "string",
            "x-go-name": "CertDisplayID"
          },
          "item_id": {
            "type": "string",
            "x-go-name": "ItemID"
          },
          "parent_cert": {
            "type": "string",
            "x-go-name": "ParentCert"
          },
          "private_key": {
            "type": "string",
            "x-go-name": "PrivateKey"
          },
          "reading_token": {
            "type": "string",
            "x-go-name": "IssuanceToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```