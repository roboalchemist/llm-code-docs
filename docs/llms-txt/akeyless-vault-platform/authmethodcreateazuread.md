# Source: https://docs.akeyless.io/reference/authmethodcreateazuread.md

# /auth-method-create-azure-ad

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
    "/auth-method-create-azure-ad": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodCreateAzureAD",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodCreateAzureAD"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/authMethodCreateAzureADResponse"
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
      "authMethodCreateAzureADResponse": {
        "description": "authMethodCreateAzureADResponse wraps response body.",
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
      "authMethodCreateAzureAD": {
        "description": "authMethodCreateAzureAD is a command that creates a new auth method that\nwill be able to authenticate using Azure Active Directory credentials.",
        "type": "object",
        "required": [
          "name",
          "bound-tenant-id"
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
            "description": "Deprecated\n(Deprecated) The audience in the JWT",
            "type": "string",
            "default": "https://management.azure.com/",
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
          "bound-group-id": {
            "description": "A list of group ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundGroupIDs"
          },
          "bound-ips": {
            "description": "A CIDR whitelist with the IPs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CIDRWhitelist"
          },
          "bound-providers": {
            "description": "A list of resource providers that the access is restricted to (e.g,\nMicrosoft.Compute, Microsoft.ManagedIdentity, etc)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceProviders"
          },
          "bound-resource-id": {
            "description": "A list of full resource ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceIds"
          },
          "bound-resource-names": {
            "description": "A list of resource names that the access is restricted to (e.g, a\nvirtual machine name, scale set name, etc).",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceNames"
          },
          "bound-resource-types": {
            "description": "A list of resource types that the access is restricted to (e.g,\nvirtualMachines, userAssignedIdentities, etc)",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceTypes"
          },
          "bound-rg-id": {
            "description": "A list of resource groups that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundResourceGroups"
          },
          "bound-spid": {
            "description": "A list of service principal IDs that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundServicePrincipalIDs"
          },
          "bound-sub-id": {
            "description": "A list of subscription ids that the access is restricted to",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundSubscriptionsIDs"
          },
          "bound-tenant-id": {
            "description": "The Azure tenant id that the access is restricted to",
            "type": "string",
            "x-go-name": "BoundTenantID"
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
            "default": "https://sts.windows.net/---bound_tenant_id---",
            "x-go-name": "Issuer"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "jwks-uri": {
            "description": "The URL to the JSON Web Key Set (JWKS) that containing the public keys\nthat should be used to verify any JSON Web Token (JWT) issued by the\nauthorization server.",
            "type": "string",
            "default": "https://login.microsoftonline.com/common/discovery/keys",
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
          },
          "unique-identifier": {
            "description": "A unique identifier (ID) value which is a \"sub claim\" name that contains details uniquely identifying that resource. This \"sub claim\" is used to distinguish between different identities.",
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