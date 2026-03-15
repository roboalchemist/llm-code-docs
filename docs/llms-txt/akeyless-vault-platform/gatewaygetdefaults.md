# Source: https://docs.akeyless.io/reference/gatewaygetdefaults.md

# /gateway-get-defaults

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
    "/gateway-get-defaults": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetDefaults",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetDefaults"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayGetDefaultsResponse"
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
      "gatewayGetDefaultsResponse": {
        "description": "gatewayGetDefaultsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GatewayGetDefaultsOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GatewayGetDefaultsOutput": {
        "type": "object",
        "properties": {
          "certificate_access_id": {
            "type": "string",
            "x-go-name": "CertAccessId"
          },
          "default_protection_key_id": {
            "type": "string",
            "x-go-name": "ProtectionKey"
          },
          "hvp_route_version": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "HvpRouteVersion"
          },
          "notify_on_status_change": {
            "type": "boolean",
            "x-go-name": "NotifyOnStatusChange"
          },
          "oidc_access_id": {
            "type": "string",
            "x-go-name": "OidcAccessId"
          },
          "saml_access_id": {
            "type": "string",
            "x-go-name": "SamlAccessId"
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
      "gatewayGetDefaults": {
        "description": "gatewayGetDefaults is a command that get defaults settings",
        "type": "object",
        "properties": {
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