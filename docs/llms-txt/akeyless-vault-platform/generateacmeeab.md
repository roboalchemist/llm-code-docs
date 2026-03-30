# Source: https://docs.akeyless.io/reference/generateacmeeab.md

# /generate-acme-eab

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
    "/generate-acme-eab": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "generateAcmeEab",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/generateAcmeEab"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/generateAcmeEabResponse"
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
      "generateAcmeEabResponse": {
        "description": "generateAcmeEabResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GenerateAcmeEabOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GenerateAcmeEabOutput": {
        "type": "object",
        "properties": {
          "expires_at": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ExpiresAt"
          },
          "kid": {
            "type": "string",
            "x-go-name": "Kid"
          },
          "mac_key": {
            "type": "string",
            "x-go-name": "MacKey"
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
      "generateAcmeEab": {
        "type": "object",
        "title": "generateAcmeEab is a command that generates a an external account binding for a cert issuer.",
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