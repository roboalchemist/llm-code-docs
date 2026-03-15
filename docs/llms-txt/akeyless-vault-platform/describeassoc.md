# Source: https://docs.akeyless.io/reference/describeassoc.md

# /describe-role-am-assoc

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
    "/describe-role-am-assoc": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "describeAssoc",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/describeAssoc"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/describeAssocResponse"
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
      "describeAssocResponse": {
        "description": "describeAssocResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/RoleAssociationDetails"
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
      "RoleAssociationDetails": {
        "description": "RoleAssociationDetails includes details of an association between a role\nand an auth method.",
        "type": "object",
        "properties": {
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
          },
          "auth_method_name": {
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "auth_method_sub_claims": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "x-go-name": "AuthMethodSubClaims"
          },
          "is_subclaims_with_operator": {
            "type": "boolean",
            "x-go-name": "IsSubclaimsWithOperator"
          },
          "role_name": {
            "type": "string",
            "x-go-name": "RoleName"
          },
          "sub_claims_case_sensitive": {
            "type": "boolean",
            "x-go-name": "IsSubClaimsCaseSensitive"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "describeAssoc": {
        "type": "object",
        "title": "describeAssoc is a command that returns role association details.",
        "required": [
          "assoc-id"
        ],
        "properties": {
          "assoc-id": {
            "description": "The association id",
            "type": "string",
            "x-go-name": "AssocId"
          },
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