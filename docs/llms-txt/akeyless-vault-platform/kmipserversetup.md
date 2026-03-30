# Source: https://docs.akeyless.io/reference/kmipserversetup.md

# /kmip-create-environment

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
    "/kmip-create-environment": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "kmipServerSetup",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/kmipServerSetup"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/kmipServerSetupResponse"
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
      "kmipServerSetupResponse": {
        "description": "kmipServerSetupResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/KMIPEnvironmentCreateResponse"
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
      "KMIPEnvironmentCreateResponse": {
        "type": "object",
        "properties": {
          "ca_cert": {
            "type": "array",
            "items": {
              "type": "integer",
              "format": "uint8"
            },
            "x-go-name": "CACert"
          },
          "root": {
            "type": "string",
            "x-go-name": "Root"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/gateway/config"
      },
      "kmipServerSetup": {
        "type": "object",
        "title": "kmipServerSetup is a command that creates a new KMIP environment.",
        "required": [
          "hostname",
          "root"
        ],
        "properties": {
          "certificate-ttl": {
            "description": "Server certificate TTL in days",
            "type": "integer",
            "format": "int64",
            "default": 90,
            "x-go-name": "CertificateTTL"
          },
          "hostname": {
            "description": "Hostname",
            "type": "string",
            "x-go-name": "Hostname"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "root": {
            "description": "Root path of KMIP Resources",
            "type": "string",
            "x-go-name": "Root"
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