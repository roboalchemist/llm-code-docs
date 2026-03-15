# Source: https://docs.akeyless.io/reference/authmethodupdatecert.md

# /auth-method-update-cert

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
    "/auth-method-update-cert": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodUpdateCert",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodUpdateCert"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/authMethodUpdateCertResponse"
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
      "authMethodUpdateCertResponse": {
        "description": "authMethodUpdateCertResponse wraps response body.",
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
      "authMethodUpdateCert": {
        "description": "authMethodUpdateCert is a command that updates a new auth method that\nwill be able to authenticate using a client certificate",
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
          "allowed-cors": {
            "description": "Comma separated list of allowed CORS domains to be validated as part of the authentication flow.",
            "type": "string",
            "x-go-name": "AllowedCors"
          },
          "audit-logs-claims": {
            "description": "Subclaims to include in audit logs, e.g \"--audit-logs-claims email --audit-logs-claims username\"",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AuditLogsClaims"
          },
          "bound-common-names": {
            "description": "A list of names. At least one must exist in the Common Name. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundCommonNames"
          },
          "bound-dns-sans": {
            "description": "A list of DNS names. At least one must exist in the SANs. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundDnsSans"
          },
          "bound-email-sans": {
            "description": "A list of Email Addresses. At least one must exist in the SANs. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundEmailSans"
          },
          "bound-extensions": {
            "description": "A list of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values much match. Supports globbing on \"value\".",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundExtensions"
          },
          "bound-ips": {
            "description": "A CIDR whitelist with the IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CIDRWhitelist"
          },
          "bound-organizational-units": {
            "description": "A list of Organizational Units names. At least one must exist in the OU field.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundOrganizationalUnits"
          },
          "bound-uri-sans": {
            "description": "A list of URIs. At least one must exist in the SANs. Supports globbing.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundUriSans"
          },
          "certificate-data": {
            "description": "The certificate data in base64, if no file was provided",
            "type": "string",
            "x-go-name": "CertificateData"
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
          "require-crl-dp": {
            "description": "Require certificate CRL distribution points (CDP) and enforce CRL validation during authentication.",
            "type": "boolean",
            "x-go-name": "RequireCrlDp"
          },
          "revoked-cert-ids": {
            "description": "A list of revoked cert ids",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "RevokedCertIds"
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
            "description": "A unique identifier (ID) value should be configured, such as common_name or organizational_unit\nWhenever a user logs in with a token, these authentication types issue\na \"sub claim\" that contains details uniquely identifying that user.\nThis sub claim includes a key containing the ID value that you\nconfigured, and is used to distinguish between different users from\nwithin the same organization.",
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