# Source: https://docs.akeyless.io/reference/gatewaycreateallowedaccess.md

# /gateway-create-allowed-access

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
    "/gateway-create-allowed-access": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayCreateAllowedAccess",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayCreateAllowedAccess"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayCreateAllowedAccessResponse"
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
      "gatewayCreateAllowedAccessResponse": {
        "description": "gatewayCreateAllowedAccessResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AllowedAccess"
            }
          }
        }
      }
    },
    "schemas": {
      "AccessPermission": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
      },
      "AllowedAccess": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access_type": {
            "type": "string",
            "x-go-name": "AccessType"
          },
          "cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ClusterID"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreatedAt"
          },
          "description": {
            "type": "string",
            "x-go-name": "Description"
          },
          "editable": {
            "type": "boolean",
            "x-go-name": "Editable"
          },
          "error": {
            "type": "string",
            "x-go-name": "Error"
          },
          "id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ID"
          },
          "is_valid": {
            "type": "boolean",
            "x-go-name": "IsValid"
          },
          "name": {
            "type": "string",
            "x-go-name": "Name"
          },
          "permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AccessPermission"
            },
            "x-go-name": "Permissions"
          },
          "sub_claims": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "SubClaims"
          },
          "sub_claims_case_insensitive": {
            "type": "boolean",
            "x-go-name": "SubClaimsCaseInsensitive"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "UpdatedAt"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/gator"
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
      "gatewayCreateAllowedAccess": {
        "description": "gatewayCreateAllowedAccess is a command that creates allowed access in Gator",
        "type": "object",
        "required": [
          "name",
          "access-id"
        ],
        "properties": {
          "SubClaimsCaseInsensitive": {
            "type": "boolean"
          },
          "access-id": {
            "description": "Access ID\nThe access id to be attached to this allowed access. Auth method with this access id should already exist.",
            "type": "string",
            "x-go-name": "AccessID"
          },
          "case-sensitive": {
            "description": "Treat sub claims as case-sensitive [true/false]",
            "type": "string",
            "default": "true",
            "x-go-name": "IsSubClaimsCaseSensitive"
          },
          "description": {
            "description": "Allowed access description",
            "type": "string",
            "x-go-name": "Description"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Allowed access name",
            "type": "string",
            "x-go-name": "Name"
          },
          "permissions": {
            "description": "Permissions\n\nComma-seperated list of permissions for this allowed access.\nAvailable permissions: [defaults,targets,classic_keys,automatic_migration,ldap_auth,dynamic_secret,k8s_auth,log_forwarding,zero_knowledge_encryption,rotated_secret,caching,event_forwarding,admin,kmip,general,rotate_secret_value]",
            "type": "string",
            "x-go-name": "Permissions"
          },
          "sub-claims": {
            "description": "Sub claims\nkey/val of sub claims, e.g group=admins,developers",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "SubClaims"
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