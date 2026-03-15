# Source: https://docs.akeyless.io/reference/createauthmethod.md

# /create-auth-method

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
    "/create-auth-method": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createAuthMethod",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createAuthMethod"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createAuthMethodResponse"
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
      "createAuthMethodResponse": {
        "description": "createAuthMethodResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createAuthMethodOutput"
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
      "createAuthMethod": {
        "description": "createAuthMethod is a command that creates a new auth method. [Deprecated: Use auth-method-create-api-key command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "access-expires": {
            "description": "Access expiration date in Unix timestamp (select 0 for access without\nexpiry date)",
            "type": "integer",
            "format": "int64",
            "default": 0,
            "x-go-name": "AccessExpires"
          },
          "allowed-client-type": {
            "description": "limit the auth method usage for specific client types [cli,ui,gateway-admin,sdk,mobile,extension]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedClientTypes"
          },
          "audit-logs-claims": {
            "description": "Subclaims to include in audit logs, e.g \"--audit-logs-claims email --audit-logs-claims username\"",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AuditLogsClaims"
          },
          "bound-ips": {
            "description": "A CIDR whitelist with the IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CIDRWhitelist"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Auth Method description",
            "type": "string",
            "x-go-name": "Description"
          },
          "expiration-event-in": {
            "description": "How many days before the expiration of the auth method would you like to be notified.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ExpirationEventsInDays"
          },
          "force-sub-claims": {
            "description": "if true: enforce role-association must include sub claims",
            "type": "boolean",
            "x-go-name": "ForceSubClaims"
          },
          "gw-bound-ips": {
            "description": "A CIDR whitelist with the GW IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "GWCIDRWhitelist"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "jwt-ttl": {
            "description": "Jwt TTL",
            "type": "integer",
            "format": "int64",
            "default": 0,
            "x-go-name": "JwtTtl"
          },
          "name": {
            "description": "Auth Method name",
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "product-type": {
            "description": "Choose the relevant product type for the auth method [sm, sra, pm, dp, ca]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ProductTypes"
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
      "createAuthMethodOutput": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access_key": {
            "type": "string",
            "x-go-name": "AccessKey"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```