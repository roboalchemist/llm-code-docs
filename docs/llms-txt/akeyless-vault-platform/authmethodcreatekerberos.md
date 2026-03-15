# Source: https://docs.akeyless.io/reference/authmethodcreatekerberos.md

# /auth-method-create-kerberos

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
    "/auth-method-create-kerberos": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodCreateKerberos",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodCreateKerberos"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/authMethodCreateUniversalIdentityResponse"
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
      "authMethodCreateUniversalIdentityResponse": {
        "description": "",
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
      "authMethodCreateKerberos": {
        "description": "authMethodCreateKerberos is a command that creates a new auth\nmethod that will be able to authenticate using Kerberos",
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
          "bind-dn": {
            "type": "string",
            "x-go-name": "BindDn"
          },
          "bind-dn-password": {
            "type": "string",
            "x-go-name": "BindDnPassword"
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
          "group-attr": {
            "type": "string",
            "x-go-name": "GroupAttr"
          },
          "group-dn": {
            "type": "string",
            "x-go-name": "GroupDn"
          },
          "group-filter": {
            "type": "string",
            "x-go-name": "GroupFilter"
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
          "keytab-file-data": {
            "type": "string",
            "x-go-name": "KeytabData"
          },
          "keytab-file-path": {
            "type": "string",
            "x-go-name": "KeytabPath"
          },
          "krb5-conf-data": {
            "type": "string",
            "x-go-name": "Krb5ConfData"
          },
          "krb5-conf-path": {
            "type": "string",
            "x-go-name": "Krb5ConfPath"
          },
          "ldap-anonymous-search": {
            "type": "boolean",
            "x-go-name": "LdapAnonymousSearch"
          },
          "ldap-ca-cert": {
            "type": "string",
            "x-go-name": "LdapCACert"
          },
          "ldap-url": {
            "type": "string",
            "x-go-name": "LdapUrlAddress"
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
            "description": "A unique identifier (ID) value which is a \"sub claim\" name that contains details uniquely identifying that resource. This \"sub claim\" is used to distinguish between different identities.",
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          },
          "user-attribute": {
            "type": "string",
            "x-go-name": "UserAttribute"
          },
          "user-dn": {
            "type": "string",
            "x-go-name": "UserDn"
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