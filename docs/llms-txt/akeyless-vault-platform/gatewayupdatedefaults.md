# Source: https://docs.akeyless.io/reference/gatewayupdatedefaults.md

# /gateway-update-defaults

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
    "/gateway-update-defaults": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayUpdateDefaults",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayUpdateDefaults"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/gatewayUpdateDefaultsResponse"
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
      "gatewayUpdateDefaultsResponse": {
        "description": "gatewayUpdateDefaultsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/gatewayUpdateOutput"
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
      "gatewayUpdateDefaults": {
        "description": "gatewayUpdateDefaults is a command that updates defaults settings",
        "type": "object",
        "properties": {
          "cert-access-id": {
            "description": "Default Certificate access id for UI login",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "CertAccessId"
          },
          "event-on-status-change": {
            "description": "Trigger an event when Gateway status is changed [true/false]",
            "type": "string",
            "x-go-name": "NotifyOnStatusChange"
          },
          "hvp-route-version": {
            "description": "Hvp route version to use [1/2]",
            "type": "integer",
            "format": "int64",
            "x-go-name": "HvpRouteVersion"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "key": {
            "description": "The name of the gateway default encryption key",
            "type": "string",
            "default": "Default",
            "x-go-name": "EncryptionKey"
          },
          "oidc-access-id": {
            "description": "Default OIDC access id for UI login",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "OidcAccessId"
          },
          "saml-access-id": {
            "description": "Default SAML access id for UI login",
            "type": "string",
            "default": "use-existing",
            "x-go-name": "SamlAccessId"
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
      "gatewayUpdateOutput": {
        "type": "object",
        "properties": {
          "updated": {
            "type": "boolean",
            "x-go-name": "Updated"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```