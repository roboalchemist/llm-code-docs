# Source: https://docs.akeyless.io/reference/listgateways.md

# /list-gateways

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
    "/list-gateways": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "listGateways",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/listGateways"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/listGatewaysResponse"
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
      "listGatewaysResponse": {
        "description": "listGatewaysResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GatewaysListResponse"
            }
          }
        }
      }
    },
    "schemas": {
      "CfInfo": {
        "type": "object",
        "properties": {
          "cf_name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "description": {
            "type": "string",
            "x-go-name": "Description"
          },
          "hash": {
            "type": "string",
            "x-go-name": "Hash"
          },
          "id": {
            "type": "string",
            "x-go-name": "Id"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GWClusterStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GatewaysListResponse": {
        "description": "GatewaysListResponse Gateway cluster identity list",
        "type": "object",
        "properties": {
          "clusters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/GwClusterIdentity"
            },
            "x-go-name": "GwClusterList"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "GwClusterIdentity": {
        "type": "object",
        "properties": {
          "action_allowed": {
            "type": "boolean",
            "x-go-name": "ActionAllowed"
          },
          "allowed": {
            "type": "boolean",
            "x-go-name": "Allowed"
          },
          "allowed_access_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedAccessIDs"
          },
          "cluster_name": {
            "type": "string",
            "x-go-name": "ClusterName"
          },
          "cluster_url": {
            "type": "string",
            "x-go-name": "ClusterUrl"
          },
          "current_gw": {
            "type": "boolean",
            "x-go-name": "CurrentGW"
          },
          "customer_fragment_ids": {
            "description": "Deprecated - use CustomerFragments instead",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "CustomerFragmentIDs"
          },
          "customer_fragments": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CfInfo"
            },
            "x-go-name": "CustomerFragments"
          },
          "default_protection_key_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DefProtectionKeyID"
          },
          "default_secret_location": {
            "type": "string",
            "x-go-name": "DefSecretLocation"
          },
          "display_name": {
            "type": "string",
            "x-go-name": "DisplayName"
          },
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Id"
          },
          "is_kerberos_auth_enabled": {
            "type": "boolean",
            "x-go-name": "IsKerberosAuthEnabled"
          },
          "is_ldap_auth_enabled": {
            "type": "boolean",
            "x-go-name": "IsLdapAuthEnabled"
          },
          "serverless_type": {
            "type": "string",
            "x-go-name": "ServerlessType"
          },
          "status": {
            "$ref": "#/components/schemas/GWClusterStatus"
          },
          "status_description": {
            "type": "string",
            "x-go-name": "StatusDescription"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
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
      "listGateways": {
        "type": "object",
        "title": "listGateways is a command that returns a list of gateways.",
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