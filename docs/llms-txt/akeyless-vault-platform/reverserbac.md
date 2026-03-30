# Source: https://docs.akeyless.io/reference/reverserbac.md

# /reverse-rbac

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
    "/reverse-rbac": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "reverseRBAC",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/reverseRBAC"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/reverseRBACResponse"
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
      "reverseRBACResponse": {
        "description": "reverseRBACResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ReverseRBACOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "AuthMethodRoleAssociation": {
        "description": "AuthMethodRoleAssociation includes details of an association between an auth\nmethod and a role.",
        "type": "object",
        "properties": {
          "allowed_ops": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "AllowedOperations"
          },
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
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
          "is_sub_claims_case_sensitive": {
            "type": "boolean",
            "x-go-name": "IsSubClaimsCaseSensitive"
          },
          "is_subclaims_with_operator": {
            "type": "boolean",
            "x-go-name": "IsSubclaimsWithOperator"
          },
          "role_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "RoleId"
          },
          "role_name": {
            "type": "string",
            "x-go-name": "RoleName"
          },
          "rules": {
            "$ref": "#/components/schemas/Rules"
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
      "PathRule": {
        "type": "object",
        "title": "PathRule is a single rule used in AKEYLESS RBAC.",
        "properties": {
          "assigners": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RuleAssigner"
            },
            "x-go-name": "Assigners"
          },
          "capabilities": {
            "description": "The approved/denied capabilities in the path",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Capabilities"
          },
          "cb": {
            "type": "integer",
            "format": "uint64",
            "x-go-name": "CapabilitiesBitmap"
          },
          "is_limit_access": {
            "description": "flag that indicate that this rule is allowed to be access RemainingAccess of times.",
            "type": "boolean",
            "x-go-name": "IsLimitAccess"
          },
          "item_id": {
            "description": "The item id this rule directly refers to (when applicable)",
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "number_of_access_used": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfAccessUsed"
          },
          "number_of_allowed_access": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "NumberOfAllowedAccess"
          },
          "path": {
            "description": "The path the rule refers to",
            "type": "string",
            "x-go-name": "Path"
          },
          "start_time": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "StartTime"
          },
          "ttl": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TTL"
          },
          "type": {
            "$ref": "#/components/schemas/PathRuleType"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PathRuleType": {
        "type": "string",
        "title": "PathRuleType defines a kind of every PathRule assigned to a Role.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ReverseRBACClient": {
        "type": "object",
        "title": "ReverseRBACClient is a single entity that has access to a given object.",
        "properties": {
          "assocs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AuthMethodRoleAssociation"
            },
            "x-go-name": "Assocs"
          },
          "auth_method_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "AuthMethodId"
          },
          "auth_method_name": {
            "type": "string",
            "x-go-name": "AuthMethodName"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ReverseRBACOutput": {
        "type": "object",
        "title": "ReverseRBACOutput defines output of ReverseRBAC operation.",
        "properties": {
          "clients": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/ReverseRBACClient"
            },
            "x-go-name": "Clients"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "RuleAssigner": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "unique_id": {
            "type": "string",
            "x-go-name": "UniqueId"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "Rules": {
        "type": "object",
        "title": "Rules are a part of AKEYLESS RBAC.",
        "properties": {
          "admin": {
            "description": "Is admin",
            "type": "boolean",
            "x-go-name": "Admin"
          },
          "path_rules": {
            "description": "The path the rules refers to",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PathRule"
            },
            "x-go-name": "PathRules"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "reverseRBAC": {
        "description": "reverseRBAC is a command that shows which auth methods have access to a\nparticular object.",
        "type": "object",
        "required": [
          "path",
          "type"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "path": {
            "description": "Path to an object",
            "type": "string",
            "x-go-name": "Path"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "type": {
            "description": "Type of object (item, am, role)",
            "type": "string",
            "x-go-name": "Type"
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