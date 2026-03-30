# Source: https://docs.akeyless.io/reference/validatecertificatechallenge.md

# /validate-certificate-challenge

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
    "/validate-certificate-challenge": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "ValidateCertificateChallenge",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ValidateCertificateChallenge"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/validateCertificateChallengeResponse"
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
      "validateCertificateChallengeResponse": {
        "description": "validateCertificateChallengeResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ValidateCertificateChallengeOutput"
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
      "ValidateCertificateChallenge": {
        "description": "ValidateCertificateChallenge validates HTTP-01 challenge and finalizes certificate issuance (Phase 2)",
        "type": "object",
        "properties": {
          "Result": {
            "$ref": "#/components/schemas/ValidateCertificateChallengeOutput"
          },
          "cert-display-id": {
            "description": "Certificate display ID from Phase 1",
            "type": "string",
            "x-go-name": "CertDisplayID"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Certificate name (alternative to cert-display-id)",
            "type": "string",
            "x-go-name": "CertName"
          },
          "timeout": {
            "description": "Validation timeout in seconds",
            "type": "integer",
            "format": "int64",
            "default": 120,
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
      "ValidateCertificateChallengeOutput": {
        "description": "ValidateCertificateChallengeOutput defines output for HTTP-01 challenge validation",
        "type": "object",
        "properties": {
          "cert": {
            "type": "string",
            "x-go-name": "CertBytes"
          },
          "cert_display_id": {
            "type": "string",
            "x-go-name": "CertDisplayID"
          },
          "cert_item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "CertItemID"
          },
          "status": {
            "type": "string",
            "x-go-name": "Status"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      }
    }
  }
}
```