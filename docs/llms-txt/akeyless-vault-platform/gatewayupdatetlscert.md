# Source: https://docs.akeyless.io/reference/gatewayupdatetlscert.md

# /gateway-update-tls-cert

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
    "/gateway-update-tls-cert": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "GatewayUpdateTlsCert",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GatewayUpdateTlsCert"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/GatewayUpdateTlsCertResponse"
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
      "GatewayUpdateTlsCertResponse": {
        "description": "GatewayUpdateTlsCertResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GatewayUpdateTlsCertOutput"
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
      "GatewayUpdateTlsCert": {
        "description": "gatewayUpdateTlsCert is a command that updates Gateway TLS certificate",
        "type": "object",
        "properties": {
          "cert-data": {
            "description": "TLS Certificate (base64 encoded)",
            "type": "string",
            "x-go-name": "CertData"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the certificate would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key-data": {
            "description": "TLS Private Key (base64 encoded)",
            "type": "string",
            "x-go-name": "KeyData"
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
      "GatewayUpdateTlsCertOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
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
      }
    }
  }
}
```