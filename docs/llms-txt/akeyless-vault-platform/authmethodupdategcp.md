# Source: https://docs.akeyless.io/reference/authmethodupdategcp.md

# /auth-method-update-gcp

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
    "/auth-method-update-gcp": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "authMethodUpdateGcp",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/authMethodUpdateGcp"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "201": {
            "$ref": "#/components/responses/authMethodUpdateGcpResponse"
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
      "authMethodUpdateGcpResponse": {
        "description": "authMethodUpdateGcpResponse wraps response body.",
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
      "authMethodUpdateGcp": {
        "description": "authMethodUpdateGcp is a command that updates a new auth method that\nwill be able to authenticate using GCP IAM Service Account credentials\nor GCE instance credentials.",
        "type": "object",
        "required": [
          "name",
          "type",
          "audience"
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
            "description": "The audience to verify in the JWT received by the client",
            "type": "string",
            "default": "akeyless.io",
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
          "bound-labels": {
            "description": "A comma-separated list of GCP labels formatted as \"key:value\" strings that must be set on authorized GCE instances.\nTODO: Because GCP labels are not currently ACL'd ....",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundLabels"
          },
          "bound-projects": {
            "description": "=== Human and Machine authentication section ===\nArray of GCP project IDs. Only entities belonging to any of the provided projects can authenticate.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundProjects"
          },
          "bound-regions": {
            "description": "List of regions that a GCE instance must belong to in order to be authenticated.\nTODO: If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundRegions"
          },
          "bound-service-accounts": {
            "description": "List of service accounts the service account must be part of in order to be authenticated.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundServiceAccounts"
          },
          "bound-zones": {
            "description": "=== Machine authentication section ===\nList of zones that a GCE instance must belong to in order to be authenticated.\nTODO: If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "BoundZones"
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
          "service-account-creds-data": {
            "description": "ServiceAccount credentials data instead of giving a file path, base64 encoded",
            "type": "string",
            "x-go-name": "ServiceAccountCredsFileData"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Type of the GCP Access Rules",
            "type": "string",
            "x-go-name": "Type"
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