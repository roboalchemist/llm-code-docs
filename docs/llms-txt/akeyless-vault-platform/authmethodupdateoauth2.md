# Source: https://docs.akeyless.io/reference/authmethodupdateoauth2.md

# /auth-method-update-oauth2

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
    "/auth-method-update-oauth2": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodUpdateOauth2",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodUpdateOauth2"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/authMethodUpdateOauth2Response"
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
      "authMethodUpdateOauth2Response": {
        "description": "authMethodUpdateOauth2Response wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/authMethodUpdateOutput"
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
      "authMethodUpdateOauth2": {
        "description": "authMethodUpdateOauth2 is a command that updates a new auth method that will\nbe able to authenticate using Oauth2.",
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
          "audience": {
            "description": "The audience in the JWT",
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
          "bound-client-ids": {
            "description": "The clients ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundClientID"
          },
          "bound-ips": {
            "description": "A CIDR whitelist with the IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CIDRWhitelist"
          },
          "cert": {
            "description": "CertificateFile Path to a file that contain the certificate in a PEM format.",
            "type": "string",
            "x-go-name": "CertificateFile"
          },
          "cert-file-data": {
            "description": "CertificateFileData PEM Certificate in a Base64 format.",
            "type": "string",
            "x-go-name": "CertificateFileData"
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
          "gateway-url": {
            "description": "Akeyless Gateway URL (Configuration Management port). Relevant only when the jwks-uri is accessible only from the gateway.",
            "type": "string",
            "x-go-name": "GatewayUrl"
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
          "jwks-json-data": {
            "description": "The JSON Web Key Set (JWKS) that containing the public keys\nthat should be used to verify any JSON Web Token (JWT) issued by the\nauthorization server.\nbase64 encoded string",
            "type": "string",
            "x-go-name": "JWKeySetJsonData"
          },
          "jwks-uri": {
            "description": "The URL to the JSON Web Key Set (JWKS) that containing the public keys\nthat should be used to verify any JSON Web Token (JWT) issued by the\nauthorization server.",
            "type": "string",
            "x-go-name": "JWKeySetURL"
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
            "description": "A unique identifier (ID) value should be configured for OAuth2,\nLDAP and SAML authentication method types and is usually a value such\nas the email, username, or upn for example.\nWhenever a user logs in with a token, these authentication types issue\na \"sub claim\" that contains details uniquely identifying that user.\nThis sub claim includes a key containing the ID value that you\nconfigured, and is used to distinguish between different users from\nwithin the same organization.",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "authMethodUpdateOutput": {
        "type": "object",
        "properties": {
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