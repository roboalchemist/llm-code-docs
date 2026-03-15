# Source: https://docs.akeyless.io/reference/updateauthmethodldap.md

# /update-auth-method-ldap

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
    "/update-auth-method-ldap": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "updateAuthMethodLDAP",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/updateAuthMethodLDAP"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/updateAuthMethodLDAPResponse"
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
      "updateAuthMethodLDAPResponse": {
        "description": "updateAuthMethodLDAPResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/updateAuthMethodLDAPOutput"
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
      "updateAuthMethodLDAP": {
        "description": "updateAuthMethodLDAP is a command that updates a new auth method that will\nbe able to authenticate using LDAP. [Deprecated: Use auth-method-update-ldap command]",
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
          "gen-key": {
            "description": "Automatically generate key-pair for LDAP configuration. If set to false, a public key needs to be provided [true/false]",
            "type": "string",
            "x-go-name": "GenerateKeyPair"
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
          "new-name": {
            "description": "Auth Method new name",
            "type": "string",
            "x-go-name": "AuthMethodNewName"
          },
          "product-type": {
            "description": "Choose the relevant product type for the auth method [sm, sra, pm, dp, ca]",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ProductTypes"
          },
          "public-key-data": {
            "description": "A public key generated for LDAP authentication method on Akeyless in base64 or PEM format\n[RSA2048]",
            "type": "string",
            "x-go-name": "PublicKeyData"
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
          },
          "unique-identifier": {
            "description": "A unique identifier (ID) value should be configured for OAuth2,\nLDAP and SAML authentication method types and is usually a value such\nas the email, username, or upn for example.\nWhenever a user logs in with a token, these authentication types issue\na \"sub claim\" that contains details uniquely identifying that user.\nThis sub claim includes a key containing the ID value that you\nconfigured, and is used to distinguish between different users from\nwithin the same organization.",
            "type": "string",
            "default": "users",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "updateAuthMethodLDAPOutput": {
        "type": "object",
        "properties": {
          "prv_key": {
            "type": "string",
            "x-go-name": "PrivateKey"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```