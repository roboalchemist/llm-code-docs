# Source: https://docs.akeyless.io/reference/provisioncertificate.md

# /provision-certificate

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
    "/provision-certificate": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "provisionCertificate",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/provisionCertificate"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/provisionCertificateResponse"
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
      "provisionCertificateResponse": {
        "description": "provisionCertificateResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ProvisionCertificateOutput"
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
      "ProvisionCertificateOutput": {
        "type": "object",
        "properties": {
          "FailMessage": {
            "type": "string"
          },
          "SuccessMessage": {
            "type": "string"
          },
          "host_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "HostNames"
          },
          "provisioned_at": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ProvisionedAt"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "provisionCertificate": {
        "description": "provisionCertificate is a command that provisions a certificate content to a target",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "display-id": {
            "description": "Certificate display ID",
            "type": "string",
            "x-go-name": "CertificateDisplayID"
          },
          "item-id": {
            "description": "Certificate item ID",
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertificateItemId"
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
            "x-go-name": "CertificateName"
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