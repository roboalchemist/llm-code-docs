# Source: https://docs.akeyless.io/reference/gatewaygetallowedaccess.md

# /gateway-get-allowed-access

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
    "/gateway-get-allowed-access": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "gatewayGetAllowedAccess",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/gatewayGetAllowedAccess"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/gatewayGetAllowedAccessResponse"
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
      "gatewayGetAllowedAccessResponse": {
        "description": "gatewayGetAllowedAccessResponse wraps response body.",
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
      "gatewayGetAllowedAccess": {
        "description": "gatewayGetAllowedAccess is a command that gets allowed access from gateway",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
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