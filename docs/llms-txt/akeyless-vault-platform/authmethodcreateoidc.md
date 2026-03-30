# Source: https://docs.akeyless.io/reference/authmethodcreateoidc.md

# /auth-method-create-oidc

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
    "/auth-method-create-oidc": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodCreateOIDC",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodCreateOIDC"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/authMethodCreateOIDCResponse"
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
      "authMethodCreateOIDCResponse": {
        "description": "authMethodCreateOIDCResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/authMethodCreateOutput"
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
      "authMethodCreateOIDC": {
        "description": "authMethodCreateOIDC is a command that creates a new auth method that will\nbe available to authenticate using OIDC.",
        "type": "object",
        "required": [
          "name",
          "unique-identifier"
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
          "allowed-redirect-uri": {
            "description": "Allowed redirect URIs after the authentication",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedRedirectURIs"
          },
          "audience": {
            "description": "Audience claim to be used as part of the authentication flow. In case set, it must match the one configured on the Identity Provider's Application",
            "type": "string",
            "x-go-name": "Audience"
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
          "client-id": {
            "description": "Client ID",
            "type": "string",
            "x-go-name": "ClientID"
          },
          "client-secret": {
            "description": "Client Secret",
            "type": "string",
            "x-go-name": "ClientSecret"
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
          "issuer": {
            "description": "Issuer URL",
            "type": "string",
            "x-go-name": "Issuer"
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
          "required-scopes": {
            "description": "RequiredScopes is a list of required scopes that the oidc method will request from the oidc provider and the user must approve",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RequiredScopes"
          },
          "required-scopes-prefix": {
            "description": "RequiredScopesPrefix is a a prefix to add to all required-scopes when requesting them from the oidc server (for example, azures' Application ID URI)",
            "type": "string",
            "x-go-name": "RequiredScopesPrefix"
          },
          "subclaims-delimiters": {
            "description": "A list of additional sub claims delimiters (relevant only for SAML, OIDC, OAuth2/JWT)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "SubClaimsDelimiters"
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
            "description": "A unique identifier (ID) value should be configured for OIDC, OAuth2,\nLDAP and SAML authentication method types and is usually a value such\nas the email, username, or upn for example.\nWhenever a user logs in with a token, these authentication types issue\na \"sub claim\" that contains details uniquely identifying that user.\nThis sub claim includes a key containing the ID value that you\nconfigured, and is used to distinguish between different users from\nwithin the same organization.",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "authMethodCreateOutput": {
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
          },
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